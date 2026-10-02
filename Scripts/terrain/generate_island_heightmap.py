#!/usr/bin/env python3
"""Deterministic macro heightmap generator for Ilha Tropical.

Outputs a little-endian unsigned 16-bit RAW (.r16) heightmap compatible with
Unreal Landscape import. This is intentionally a macro base: Landmass,
Landscape Sculpt and manual level-design passes must refine it.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

try:
    import numpy as np
except ImportError as exc:
    raise SystemExit(
        "numpy is required. Install it with: python -m pip install numpy"
    ) from exc

DEFAULT_RESOLUTION = 4033
DEFAULT_WIDTH_M = 4472.14
DEFAULT_Z_SCALE = 500.0
ALGORITHM_VERSION = 2


def smoothstep(edge0: float, edge1: float, x):
    t = np.clip((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def angular_bump(theta, center: float, width: float, amplitude: float):
    delta = np.arctan2(np.sin(theta - center), np.cos(theta - center))
    return amplitude * np.exp(-((delta / width) ** 2))


def gaussian_hill(x, y, cx: float, cy: float, sx: float, sy: float, amplitude: float, power: float = 2.0):
    radial = ((x - cx) / sx) ** 2 + ((y - cy) / sy) ** 2
    return amplitude * np.exp(-(radial ** (power / 2.0)))


def gaussian_ridge(x, y, angle_rad: float, width: float, length: float, amplitude: float, offset_x: float, offset_y: float):
    xx = x - offset_x
    yy = y - offset_y
    ca = math.cos(angle_rad)
    sa = math.sin(angle_rad)
    along = xx * ca + yy * sa
    across = -xx * sa + yy * ca
    return amplitude * np.exp(-((across / width) ** 2 + (along / length) ** 4))


def carve_polyline_channel(height, x, y, points, width: float, depth: float):
    min_distance_sq = np.full_like(x, np.inf)

    for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
        vx = x1 - x0
        vy = y1 - y0
        denom = vx * vx + vy * vy
        t = np.clip(((x - x0) * vx + (y - y0) * vy) / denom, 0.0, 1.0)
        px = x0 + t * vx
        py = y0 + t * vy
        distance_sq = (x - px) ** 2 + (y - py) ** 2
        min_distance_sq = np.minimum(min_distance_sq, distance_sq)

    height -= depth * np.exp(-min_distance_sq / (width * width))


def build_heightfield(resolution: int, seed: int):
    rng = np.random.default_rng(seed)
    axis = np.linspace(-1.0, 1.0, resolution, dtype=np.float32)
    x, y = np.meshgrid(axis, axis)

    # Offset and stretch the radial field so the island never reads as a circle.
    ex = x + 0.015
    ey = (y - 0.01) / 1.05
    radius = np.sqrt(ex * ex + ey * ey)
    theta = np.arctan2(ey, ex)

    # Multi-frequency coastline plus explicit peninsulas and bays.
    coast = (
        0.77
        + 0.075 * np.sin(2.0 * theta + 0.6)
        + 0.045 * np.sin(3.0 * theta - 0.9)
        + 0.035 * np.cos(5.0 * theta + 0.2)
        + 0.022 * np.sin(8.0 * theta - 0.5)
        + 0.012 * np.cos(13.0 * theta)
    )
    coast += angular_bump(theta, -0.10, 0.35, 0.13)  # east peninsula
    coast += angular_bump(theta, 2.45, 0.42, 0.10)   # northwest lobe
    coast += angular_bump(theta, -2.45, 0.32, 0.07)  # southwest lobe
    coast -= angular_bump(theta, -1.52, 0.38, 0.13)  # south bay
    coast -= angular_bump(theta, 1.15, 0.30, 0.065)  # north inlet

    signed_inside = coast - radius
    island_mask = smoothstep(-0.025, 0.055, signed_inside)
    inland = np.clip(1.0 - radius / np.maximum(coast, 0.1), 0.0, 1.0)

    # Coastal shelves and rolling lowlands.
    base = 7.0 + 85.0 * (inland ** 1.25)

    # Asymmetric multi-peak central massif. The peak remains below the RAW
    # ceiling so the generated summit does not become a clipped plateau.
    massif = (
        gaussian_hill(x, y, -0.10, 0.03, 0.33, 0.39, 520.0, 1.7)
        + gaussian_hill(x, y, 0.12, 0.01, 0.24, 0.29, 330.0, 1.8)
        + gaussian_hill(x, y, -0.01, 0.20, 0.20, 0.22, 220.0, 1.9)
        + gaussian_hill(x, y, -0.17, -0.10, 0.19, 0.25, 180.0, 1.8)
    )

    ridges = (
        gaussian_ridge(x, y, math.radians(18), 0.075, 0.72, 80.0, -0.04, 0.04)
        + gaussian_ridge(x, y, math.radians(128), 0.085, 0.65, 70.0, -0.08, 0.03)
        + gaussian_ridge(x, y, math.radians(225), 0.070, 0.55, 60.0, -0.06, 0.00)
    )

    # Secondary hills break the broad slopes into multiple regional silhouettes.
    hills = np.zeros_like(x)
    for _ in range(10):
        angle = rng.uniform(-math.pi, math.pi)
        radial_position = rng.uniform(0.38, 0.68)
        cx = radial_position * math.cos(angle)
        cy = radial_position * math.sin(angle)
        hills += gaussian_hill(
            x,
            y,
            cx,
            cy,
            rng.uniform(0.08, 0.16),
            rng.uniform(0.08, 0.19),
            rng.uniform(45.0, 125.0),
            2.0,
        )

    north_relief = 80.0 * smoothstep(0.25, 0.82, y) * (inland ** 0.75)

    # Broad southern valley supports the initial traversal without becoming flat.
    south_valley = 90.0 * np.exp(-((x + 0.06) / 0.20) ** 2) * smoothstep(-0.72, 0.10, -y)

    # Deterministic medium-frequency relief. Fine detail remains a UE sculpt/material job.
    noise = np.zeros_like(x)
    for _ in range(14):
        fx = rng.uniform(2.0, 16.0)
        fy = rng.uniform(2.0, 16.0)
        phase = rng.uniform(-math.pi, math.pi)
        amplitude = rng.uniform(1.5, 7.0)
        noise += amplitude * np.sin(fx * x + fy * y + phase)
    noise *= np.clip(inland * 1.6, 0.0, 1.0)

    height = (base + massif + ridges + hills + north_relief + noise - south_valley) * island_mask

    # Three curved drainage corridors. Water splines in UE will refine them.
    carve_polyline_channel(
        height, x, y,
        [(-0.04, 0.05), (-0.02, -0.18), (0.02, -0.38), (-0.01, -0.60), (0.04, -0.84)],
        0.022, 34.0,
    )
    carve_polyline_channel(
        height, x, y,
        [(0.07, 0.07), (0.25, 0.00), (0.44, -0.08), (0.62, -0.14), (0.82, -0.20)],
        0.020, 28.0,
    )
    carve_polyline_channel(
        height, x, y,
        [(-0.11, 0.08), (-0.30, 0.16), (-0.43, 0.26), (-0.58, 0.29), (-0.78, 0.36)],
        0.020, 27.0,
    )

    # A wider southern coastal shelf keeps the first beach usable.
    south_beach = np.exp(-((x + 0.04) / 0.38) ** 2) * np.exp(-((y + 0.77) / 0.15) ** 2)
    height *= 1.0 - 0.28 * south_beach

    # Ocean base.
    height = np.where(island_mask < 0.08, -18.0, height)

    # Defensive clamp only; algorithm v2 should naturally stay below the upper cap.
    return np.clip(height, -120.0, 1200.0).astype(np.float32)


def meters_to_u16(height_m, z_scale: float):
    meters_per_raw = (256.0 * (z_scale / 100.0)) / 32768.0
    raw = np.rint(height_m / meters_per_raw + 32768.0)
    return np.clip(raw, 0, 65535).astype("<u2")


def write_r16(path: Path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw.tofile(path)


def write_preview_pgm(path: Path, height):
    normalized = (height - height.min()) / max(float(height.max() - height.min()), 1e-6)
    image = np.rint(normalized * 65535.0).astype(">u2")
    with path.open("wb") as fp:
        fp.write(f"P5\n{height.shape[1]} {height.shape[0]}\n65535\n".encode("ascii"))
        fp.write(image.tobytes())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--resolution", type=int, default=DEFAULT_RESOLUTION)
    parser.add_argument("--seed", type=int, default=583)
    parser.add_argument("--z-scale", type=float, default=DEFAULT_Z_SCALE)
    parser.add_argument("--out", type=Path, default=Path("Generated/Terrain/island_v1.r16"))
    parser.add_argument("--metadata", type=Path, default=Path("Generated/Terrain/island_v1.meta.json"))
    parser.add_argument("--preview", type=Path, default=Path("Generated/Terrain/island_v1_preview.pgm"))
    args = parser.parse_args()

    if args.resolution < 257 or args.resolution % 2 == 0:
        raise SystemExit("Use an odd resolution, default 4033.")

    height = build_heightfield(args.resolution, args.seed)
    raw = meters_to_u16(height, args.z_scale)
    write_r16(args.out, raw)
    write_preview_pgm(args.preview, height)

    metadata = {
        "engine_target": "5.8.3",
        "algorithm_version": ALGORITHM_VERSION,
        "resolution": args.resolution,
        "seed": args.seed,
        "nominal_width_m": DEFAULT_WIDTH_M,
        "xy_scale_cm_for_4033": round(DEFAULT_WIDTH_M * 100.0 / (DEFAULT_RESOLUTION - 1), 3),
        "z_scale": args.z_scale,
        "min_height_m": float(height.min()),
        "max_height_m": float(height.max()),
        "mean_height_m": float(height.mean()),
        "r16": str(args.out),
        "preview_pgm": str(args.preview),
        "notes": [
            "Macro-terrain only; manual Landmass/Landscape pass is required.",
            "Set WaterBodyOcean around 0m.",
            "Algorithm v2 uses asymmetric coastline, multi-peak massif and curved drainage.",
            "Do not commit Generated/ unless intentionally preserving generated assets."
        ],
    }
    args.metadata.parent.mkdir(parents=True, exist_ok=True)
    args.metadata.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(metadata, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
