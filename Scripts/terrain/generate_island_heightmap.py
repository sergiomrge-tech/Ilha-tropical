#!/usr/bin/env python3
"""Deterministic base heightmap generator for Ilha Tropical.

Outputs a little-endian unsigned 16-bit RAW (.r16) heightmap compatible with
Unreal Landscape import. The generated terrain is intentionally a macro base:
Landmass, Landscape Sculpt and manual level-design passes must refine it.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import struct

try:
    import numpy as np
except ImportError as exc:
    raise SystemExit(
        "numpy is required. Install it with: python -m pip install numpy"
    ) from exc

DEFAULT_RESOLUTION = 4033
DEFAULT_WIDTH_M = 4472.14
DEFAULT_Z_SCALE = 500.0
MAX_POSITIVE_METERS = 256.0 * (DEFAULT_Z_SCALE / 100.0)


def smoothstep(edge0: float, edge1: float, x):
    t = np.clip((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def gaussian_ridge(x, y, angle_rad: float, width: float, length: float, amplitude: float):
    ca = math.cos(angle_rad)
    sa = math.sin(angle_rad)
    along = x * ca + y * sa
    across = -x * sa + y * ca
    return amplitude * np.exp(-((across / width) ** 2 + (along / length) ** 4))


def carve_channel(height, x, y, x0, y0, x1, y1, width, depth):
    vx = x1 - x0
    vy = y1 - y0
    denom = vx * vx + vy * vy
    t = np.clip(((x - x0) * vx + (y - y0) * vy) / denom, 0.0, 1.0)
    px = x0 + t * vx
    py = y0 + t * vy
    dist2 = (x - px) ** 2 + (y - py) ** 2
    height -= depth * np.exp(-dist2 / (width * width))


def build_heightfield(resolution: int, seed: int):
    rng = np.random.default_rng(seed)
    axis = np.linspace(-1.0, 1.0, resolution, dtype=np.float32)
    x, y = np.meshgrid(axis, axis)

    # Slight ellipse prevents a perfectly circular island.
    ex = x / 0.97
    ey = y / 1.03
    r = np.sqrt(ex * ex + ey * ey)
    theta = np.arctan2(y, x)

    # Coast silhouette: several deterministic harmonics + low-frequency bias.
    coast = (
        0.83
        + 0.055 * np.sin(3.0 * theta + 0.4)
        + 0.035 * np.sin(5.0 * theta - 1.1)
        + 0.022 * np.cos(7.0 * theta + 0.7)
        + 0.014 * np.sin(11.0 * theta)
    )

    # Regional lobes/indentations.
    coast += 0.045 * np.exp(-((theta + 2.2) / 0.45) ** 2)  # southwest mangrove
    coast -= 0.050 * np.exp(-((theta + 1.55) / 0.38) ** 2) # southern bay
    coast -= 0.035 * np.exp(-((theta - 1.45) / 0.34) ** 2) # north inlet

    signed_inside = coast - r
    island_mask = smoothstep(-0.025, 0.055, signed_inside)

    # Base terrain: low coastal shelves rising toward the interior.
    inland = np.clip(1.0 - r / np.maximum(coast, 0.1), 0.0, 1.0)
    base = 8.0 + 105.0 * (inland ** 1.45)

    # Central volcanic/mountain mass, intentionally asymmetric.
    cx = x + 0.035
    cy = y - 0.045
    cr = np.sqrt((cx / 0.82) ** 2 + (cy / 0.92) ** 2)
    mountain = 920.0 * np.exp(-(cr / 0.39) ** 2.15)
    mountain *= 1.0 + 0.16 * np.sin(4.0 * theta + 0.25) + 0.08 * np.cos(7.0 * theta)

    # Major ridges radiating from the mountain.
    ridges = (
        gaussian_ridge(cx, cy, math.radians(20), 0.065, 0.68, 180.0)
        + gaussian_ridge(cx, cy, math.radians(145), 0.075, 0.62, 145.0)
        + gaussian_ridge(cx, cy, math.radians(255), 0.060, 0.55, 135.0)
    )

    # North side gets stronger cliff relief.
    north_relief = 95.0 * smoothstep(0.22, 0.82, y) * (inland ** 0.75)

    # Broad valley through south-central region for the first traversal route.
    valley = 125.0 * np.exp(-((x + 0.04) / 0.16) ** 2) * smoothstep(-0.82, 0.18, -y)

    # Low-frequency deterministic noise built from sines; avoids third-party noise libs.
    noise = np.zeros_like(x)
    for _ in range(9):
        fx = rng.uniform(1.0, 7.0)
        fy = rng.uniform(1.0, 7.0)
        phase = rng.uniform(-math.pi, math.pi)
        amp = rng.uniform(2.0, 11.0)
        noise += amp * np.sin(fx * x + fy * y + phase)
    noise *= np.clip(inland * 1.4, 0.0, 1.0)

    height = (base + mountain + ridges + north_relief + noise - valley) * island_mask

    # Rivers/channels descending from the central mountain.
    carve_channel(height, x, y, 0.02, -0.02, 0.04, -0.88, 0.028, 42.0)
    carve_channel(height, x, y, 0.10, 0.02, 0.78, -0.24, 0.025, 35.0)
    carve_channel(height, x, y, -0.08, 0.03, -0.72, 0.34, 0.026, 34.0)

    # South beach/vertical slice receives a wider low shelf.
    south_beach = np.exp(-((x + 0.03) / 0.35) ** 2) * np.exp(-((y + 0.78) / 0.16) ** 2)
    height = height * (1.0 - 0.38 * south_beach)

    # Ocean remains slightly below 0m to keep a clean coastline at WaterBodyOcean level.
    height = np.where(island_mask < 0.08, -18.0, height)

    # Clamp to the UE Landscape range selected for Z scale 500.
    height = np.clip(height, -120.0, 1220.0)
    return height.astype(np.float32)


def meters_to_u16(height_m, z_scale: float):
    # UE Landscape: raw 32768 represents 0, one signed unit spans 1/128 of
    # the unscaled landscape height unit. With Z scale 100, range is +/-256m.
    meters_per_raw = (256.0 * (z_scale / 100.0)) / 32768.0
    raw = np.rint(height_m / meters_per_raw + 32768.0)
    return np.clip(raw, 0, 65535).astype("<u2")


def write_r16(path: Path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw.tofile(path)


def write_preview_pgm(path: Path, height):
    normalized = (height - height.min()) / max(float(height.max() - height.min()), 1e-6)
    img = np.rint(normalized * 65535.0).astype(">u2")
    with path.open("wb") as fp:
        fp.write(f"P5\n{height.shape[1]} {height.shape[0]}\n65535\n".encode("ascii"))
        fp.write(img.tobytes())


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
        raise SystemExit("Use an odd Landscape-compatible resolution, default 4033.")

    height = build_heightfield(args.resolution, args.seed)
    raw = meters_to_u16(height, args.z_scale)
    write_r16(args.out, raw)
    write_preview_pgm(args.preview, height)

    metadata = {
        "engine_target": "5.8.3",
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
            "Do not commit Generated/ unless intentionally preserving generated assets."
        ],
    }
    args.metadata.parent.mkdir(parents=True, exist_ok=True)
    args.metadata.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(metadata, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
