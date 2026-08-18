#!/usr/bin/env python3
"""
Brand Engine CLI Entrypoint.
Supports execution as:
    python scripts/brand_engine/cli.py --all
    python -m scripts.brand_engine.cli --all
"""

import argparse
import sys
from pathlib import Path

# Add project root to sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.brand_engine.packager import build_press_kit_zip  # noqa: E402
from scripts.brand_engine.rasterizer import (  # noqa: E402
    rasterize_all_assets,
    rasterize_banners,
    rasterize_favicons,
    rasterize_watermarks,
)
from scripts.brand_engine.vector_builder import build_all_vectors  # noqa: E402


def main():
    parser = argparse.ArgumentParser(
        description="mrxsierra Brand Engine: Compile vector marks, favicons, watermarks, and press kits."
    )
    parser.add_argument(
        "--all", action="store_true", help="Compile everything (vectors, rasters, and ZIP archive)."
    )
    parser.add_argument(
        "--vectors", action="store_true", help="Compile all SVG vector marks and templates."
    )
    parser.add_argument(
        "--favicons", action="store_true", help="Compile favicons, app icons, and ICO bundles."
    )
    parser.add_argument(
        "--watermarks", action="store_true", help="Compile YouTube & video watermarks."
    )
    parser.add_argument(
        "--banners", action="store_true", help="Compile social media and profile banners."
    )
    parser.add_argument(
        "--zip", action="store_true", help="Package all brand assets into Press Kit ZIP archive."
    )

    args = parser.parse_args()

    if len(sys.argv) == 1 or args.all:
        print("=== Compiling Complete Brand System ===")
        build_all_vectors()
        rasterize_all_assets()
        build_press_kit_zip()
        print("=== Complete Brand System Compilation Finished ===")
        return

    if args.vectors:
        build_all_vectors()
    if args.favicons:
        rasterize_favicons()
    if args.watermarks:
        rasterize_watermarks()
    if args.banners:
        rasterize_banners()
    if args.zip:
        build_press_kit_zip()


if __name__ == "__main__":
    main()
