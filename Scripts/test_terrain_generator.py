from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "Scripts" / "terrain" / "generate_island_heightmap.py"


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = pathlib.Path(tmp)
        out = tmp_path / "test.r16"
        meta = tmp_path / "test.meta.json"
        preview = tmp_path / "test.pgm"

        subprocess.run(
            [
                sys.executable,
                str(GENERATOR),
                "--resolution", "513",
                "--seed", "583",
                "--out", str(out),
                "--metadata", str(meta),
                "--preview", str(preview),
            ],
            check=True,
        )

        expected_size = 513 * 513 * 2
        actual_size = out.stat().st_size
        if actual_size != expected_size:
            raise SystemExit(f"R16 size mismatch: {actual_size} != {expected_size}")

        data = json.loads(meta.read_text(encoding="utf-8"))
        if data["engine_target"] != "5.8.3":
            raise SystemExit("Engine target mismatch")
        if data["max_height_m"] < 800.0:
            raise SystemExit(f"Mountain too low: {data['max_height_m']}")
        if data["min_height_m"] > -5.0:
            raise SystemExit(f"Ocean floor not generated: {data['min_height_m']}")
        if not preview.exists() or preview.stat().st_size < 1024:
            raise SystemExit("Preview not generated")

    print("TERRAIN GENERATOR TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
