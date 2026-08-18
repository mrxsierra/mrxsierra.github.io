"""
Rasterizer Module for Brand Engine.
Uses ImageMagick (magick) to compile true vector SVGs into pixel-perfect PNGs and multi-layer ICOs.
"""

import shutil
import subprocess
from pathlib import Path

from PIL import Image

from .config import BRAND_CONFIG


def svg_to_png(svg_path: Path, png_path: Path, width: int, height: int, density: int = 300):
    """Renders a vector SVG file directly into an exact, anti-aliased 8-bit RGBA PNG."""
    cmd = [
        "magick",
        "-background",
        "none",
        "-density",
        str(density),
        str(svg_path),
        "-resize",
        f"{width}x{height}!",
        "-depth",
        "8",
        str(png_path),
    ]
    subprocess.run(cmd, check=True)


def rasterize_favicons():
    """Compiles exact raster favicons directly from monogram-dark.svg."""
    paths = BRAND_CONFIG["paths"]
    img_dir = paths["img_dir"]
    brand_dir = paths["brand_dir"]
    master_svg = brand_dir / "monogram-dark.svg"

    # 1. 512x512 Master PNG & Android Icon
    p512 = img_dir / "android-chrome-512x512.png"
    svg_to_png(master_svg, p512, 512, 512, density=600)
    shutil.copyfile(p512, img_dir / "favicon.png")

    # 2. 192x192 Android Icon
    svg_to_png(master_svg, img_dir / "android-chrome-192x192.png", 192, 192, density=400)

    # 3. 180x180 Apple Touch Icon
    svg_to_png(master_svg, img_dir / "apple-touch-icon.png", 180, 180, density=400)

    # 4. 32x32 and 16x16 Favicons
    p32 = img_dir / "favicon-32x32.png"
    p16 = img_dir / "favicon-16x16.png"
    svg_to_png(master_svg, p32, 32, 32, density=300)
    svg_to_png(master_svg, p16, 16, 16, density=300)

    # 5. Multi-resolution ICO (16, 32, 48, 64)
    p48 = img_dir / "temp_48.png"
    p64 = img_dir / "temp_64.png"
    svg_to_png(master_svg, p48, 48, 48, density=300)
    svg_to_png(master_svg, p64, 64, 64, density=300)

    img16 = Image.open(p16).convert("RGBA")
    img32 = Image.open(p32).convert("RGBA")
    img48 = Image.open(p48).convert("RGBA")
    img64 = Image.open(p64).convert("RGBA")
    master_img = Image.open(p512).convert("RGBA")

    master_img.save(
        img_dir / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64)],
        append_images=[img16, img32, img48, img64],
    )
    p48.unlink(missing_ok=True)
    p64.unlink(missing_ok=True)
    print("✓ Favicon & App Icon raster suite compiled.")


def rasterize_watermarks():
    """Compiles true transparent vector watermarks for YouTube and video production."""
    paths = BRAND_CONFIG["paths"]
    video_dir = paths["video_dir"]
    brand_dir = paths["brand_dir"]
    transparent_svg = brand_dir / "monogram-transparent.svg"
    square_badge_svg = video_dir / "watermark-square.svg"

    # 1. 150x150 Transparent PNG Watermark (YouTube Standard)
    svg_to_png(transparent_svg, video_dir / "watermark-150x150.png", 150, 150, density=400)

    # 2. 150x150 Dark Squircle Badge Watermark
    svg_to_png(square_badge_svg, video_dir / "watermark-badge-150x150.png", 150, 150, density=400)

    # 3. 512x512 High-Res Transparent Watermark
    svg_to_png(transparent_svg, video_dir / "watermark-512x512.png", 512, 512, density=600)
    print("✓ Video watermarks compiled.")


def rasterize_banners():
    """Renders exact high-res raster PNGs from vector SVG banners."""
    paths = BRAND_CONFIG["paths"]
    banners_dir = paths["banners_dir"]
    img_dir = paths["img_dir"]
    articles_dir = paths["articles_dir"]

    # 1. GitHub Banner (1280x640)
    svg_to_png(
        banners_dir / "github-banner.svg", banners_dir / "github-banner.png", 1280, 640, density=300
    )

    # 2. LinkedIn Banner (1584x396)
    svg_to_png(
        banners_dir / "linkedin-banner.svg",
        banners_dir / "linkedin-banner.png",
        1584,
        396,
        density=300,
    )

    # 3. X Banner (1500x500)
    svg_to_png(
        banners_dir / "x-twitter-banner.svg",
        banners_dir / "x-twitter-banner.png",
        1500,
        500,
        density=300,
    )

    # 4. YouTube Banner (2560x1440)
    svg_to_png(
        banners_dir / "youtube-banner.svg",
        banners_dir / "youtube-banner.png",
        2560,
        1440,
        density=300,
    )

    # 5. OpenGraph preview.png (1200x630)
    if (articles_dir / "article-cover-16x9.svg").exists():
        svg_to_png(
            articles_dir / "article-cover-16x9.svg", img_dir / "preview.png", 1200, 630, density=300
        )
    print("✓ Social banners and OpenGraph preview compiled.")


def rasterize_all_assets():
    """Executes all rasterization tasks."""
    rasterize_favicons()
    rasterize_watermarks()
    rasterize_banners()
    print("✓ All raster assets compiled successfully.")
