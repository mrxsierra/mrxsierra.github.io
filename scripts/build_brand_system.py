#!/usr/bin/env python3
"""
Master Brand System Compiler & Cross-Platform Asset Generator.
Compiles the exact Geometric Constructivist 'S' vector master into:
1. Web Favicon & App Icon Bundle (favicon.ico, apple-touch-icon, android-chrome, webmanifest)
2. Video & Multimedia Watermarks (YouTube 150x150 transparent PNG)
3. Social Banners (GitHub, LinkedIn, X, YouTube, OpenGraph preview.png)
4. Master Press Kit ZIP Archive (mrxsierra-brand-press-kit.zip)
"""

import zipfile
from pathlib import Path

from PIL import Image, ImageDraw

PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
BRAND_DIR = DOCS_DIR / "assets" / "brand"
IMG_DIR = DOCS_DIR / "assets" / "img"
VIDEO_DIR = BRAND_DIR / "video"
BANNERS_DIR = BRAND_DIR / "banners"
AVATAR_PATH = DOCS_DIR / "assets" / "mrxss_400x400.jpg"


def render_master_monogram_image(
    size: int,
    bg_color=(8, 9, 13, 255),
    glyph_color=(255, 255, 255, 255),
    transparent_bg: bool = False,
) -> Image.Image:
    """
    Renders the exact Geometric Constructivist 'S' with 4x super-sampling
    and anti-aliased Lanczos downsampling.
    """
    # 4x Oversampling for razor-sharp geometric precision
    scale = 4
    canvas_size = size * scale

    if transparent_bg:
        canvas = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    else:
        canvas = Image.new("RGBA", (canvas_size, canvas_size), bg_color)

    draw = ImageDraw.Draw(canvas)
    s = canvas_size / 128.0

    # Draw rounded squircle background if not transparent
    if not transparent_bg:
        mask = Image.new("L", (canvas_size, canvas_size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle(
            [(0, 0), (canvas_size, canvas_size)], radius=int(26 * s), fill=255
        )
        canvas.putalpha(mask)

    # Re-draw on top with alpha mask applied
    draw = ImageDraw.Draw(canvas)

    # Geometric Constructivist 'S' Path Specification:
    # 1. Top bar: (29, 6) to (92, 21)
    # 2. Top-right leg: (77, 21) to (92, 48)
    # 3. Middle transition: (29, 48) to (92, 63)
    # 4. Bottom-left leg: (29, 70) to (44, 98)
    # 5. Bottom bar: (29, 98) to (92, 114)
    # Outer radius 24, inner radius 8

    w = 15.0 * s
    r_outer = 16.0 * s
    r_inner = 6.0 * s

    # Upper horizontal bar
    draw.rounded_rectangle(
        [(int(29 * s), int(8 * s)), (int(92 * s), int(8 * s + w))],
        radius=int(r_outer),
        fill=glyph_color,
    )
    # Upper right vertical leg
    draw.rounded_rectangle(
        [(int(92 * s - w), int(8 * s)), (int(92 * s), int(48 * s))],
        radius=int(r_outer),
        fill=glyph_color,
    )
    # Middle horizontal transition
    draw.rounded_rectangle(
        [(int(29 * s), int(48 * s - w)), (int(92 * s), int(74 * s))],
        radius=int(r_outer),
        fill=glyph_color,
    )
    # Cutout top-left inner space to isolate clean 'S' loop
    cutout_color = (0, 0, 0, 0) if transparent_bg else bg_color
    draw.rounded_rectangle(
        [(int(29 * s + w), int(8 * s + w)), (int(92 * s - w), int(48 * s - int(3 * s)))],
        radius=int(r_inner),
        fill=cutout_color,
    )
    # Cutout bottom-right inner space
    draw.rounded_rectangle(
        [
            (int(29 * s + w), int(74 * s + int(3 * s))),
            (int(92 * s - w), int(114 * s - w - int(8 * s))),
        ],
        radius=int(r_inner),
        fill=cutout_color,
    )
    # Bottom left vertical leg
    draw.rounded_rectangle(
        [(int(29 * s), int(70 * s)), (int(29 * s + w), int(114 * s - int(8 * s)))],
        radius=int(r_outer),
        fill=glyph_color,
    )
    # Bottom horizontal bar
    draw.rounded_rectangle(
        [(int(29 * s), int(114 * s - w - int(8 * s))), (int(92 * s), int(114 * s - int(8 * s)))],
        radius=int(r_outer),
        fill=glyph_color,
    )

    return canvas.resize((size, size), Image.Resampling.LANCZOS)


def build_favicons():
    """Generates the full favicon and app icon suite."""
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    # 512x512 Master
    m512 = render_master_monogram_image(512)
    m512.save(IMG_DIR / "favicon.png", "PNG")
    m512.save(IMG_DIR / "android-chrome-512x512.png", "PNG")

    # 192x192 Android
    m192 = render_master_monogram_image(192)
    m192.save(IMG_DIR / "android-chrome-192x192.png", "PNG")

    # 180x180 Apple Touch
    m180 = render_master_monogram_image(180)
    m180.save(IMG_DIR / "apple-touch-icon.png", "PNG")

    # 32x32 & 16x16 Favicons
    m32 = render_master_monogram_image(32)
    m32.save(IMG_DIR / "favicon-32x32.png", "PNG")
    m16 = render_master_monogram_image(16)
    m16.save(IMG_DIR / "favicon-16x16.png", "PNG")

    # Multi-res ICO (16, 32, 48, 64)
    m48 = render_master_monogram_image(48)
    m64 = render_master_monogram_image(64)
    m512.save(
        IMG_DIR / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64)],
        append_images=[m16, m32, m48, m64],
    )
    print("✓ Favicon & App Icon suite compiled.")


def build_video_watermarks():
    """Generates YouTube 150x150 transparent watermark."""
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)

    # 150x150 transparent watermark (YouTube standard)
    wm150 = render_master_monogram_image(150, transparent_bg=True)
    wm150.save(VIDEO_DIR / "watermark-150x150.png", "PNG")

    # 512x512 transparent watermark
    wm512 = render_master_monogram_image(512, transparent_bg=True)
    wm512.save(VIDEO_DIR / "watermark-512x512.png", "PNG")
    print("✓ Video & YouTube watermarks compiled.")


def build_social_banners():
    """Renders high-res raster PNGs for social banners."""
    BANNERS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. GitHub Banner (1280x640)
    gh = Image.new("RGB", (1280, 640), (8, 9, 13))
    draw = ImageDraw.Draw(gh)
    draw.rectangle([(24, 24), (1256, 616)], outline=(39, 39, 42), width=1)
    mono_gh = render_master_monogram_image(80)
    gh.paste(mono_gh, (80, 80), mono_gh)

    # Avatar on right side if available
    if AVATAR_PATH.exists():
        av = Image.open(AVATAR_PATH).convert("RGBA").resize((220, 220), Image.Resampling.LANCZOS)
        mask = Image.new("L", (440, 440), 0)
        ImageDraw.Draw(mask).ellipse([(0, 0), (440, 440)], fill=255)
        mask = mask.resize((220, 220), Image.Resampling.LANCZOS)
        draw.ellipse([(956, 176), (1184, 404)], fill=(99, 102, 241))
        gh.paste(av, (960, 180), mask)

    gh.save(BANNERS_DIR / "github-banner.png", "PNG")

    # 2. LinkedIn Banner (1584x396)
    li = Image.new("RGB", (1584, 396), (8, 9, 13))
    draw_li = ImageDraw.Draw(li)
    draw_li.rectangle([(16, 16), (1568, 380)], outline=(39, 39, 42), width=1)
    mono_li = render_master_monogram_image(56)
    li.paste(mono_li, (380, 80), mono_li)
    li.save(BANNERS_DIR / "linkedin-banner.png", "PNG")

    # 3. X Banner (1500x500)
    x_img = Image.new("RGB", (1500, 500), (8, 9, 13))
    draw_x = ImageDraw.Draw(x_img)
    draw_x.rectangle([(20, 20), (1480, 480)], outline=(39, 39, 42), width=1)
    mono_x = render_master_monogram_image(64)
    x_img.paste(mono_x, (380, 110), mono_x)
    x_img.save(BANNERS_DIR / "x-twitter-banner.png", "PNG")

    # 4. YouTube Banner (2560x1440)
    yt = Image.new("RGB", (2560, 1440), (8, 9, 13))
    mono_yt = render_master_monogram_image(96)
    yt.paste(mono_yt, (600, 560), mono_yt)
    yt.save(BANNERS_DIR / "youtube-banner.png", "PNG")

    # 5. OpenGraph preview.png (1200x630)
    og = Image.new("RGB", (1200, 630), (8, 9, 13))
    draw_og = ImageDraw.Draw(og)
    draw_og.rectangle([(24, 24), (1176, 606)], outline=(39, 39, 42), width=1)
    mono_og = render_master_monogram_image(96)
    og.paste(mono_og, (64, 64), mono_og)
    if AVATAR_PATH.exists():
        av_og = Image.open(AVATAR_PATH).convert("RGBA").resize((280, 280), Image.Resampling.LANCZOS)
        mask_og = Image.new("L", (560, 560), 0)
        ImageDraw.Draw(mask_og).ellipse([(0, 0), (560, 560)], fill=255)
        mask_og = mask_og.resize((280, 280), Image.Resampling.LANCZOS)
        draw_og.ellipse([(816, 171), (820 + 284, 175 + 284)], fill=(99, 102, 241))
        og.paste(av_og, (820, 175), mask_og)
    og.save(IMG_DIR / "preview.png", "PNG")
    print("✓ Social banners and OpenGraph preview compiled.")


def build_press_kit_zip():
    """Packages all brand assets into a master press kit ZIP archive."""
    zip_path = BRAND_DIR / "mrxsierra-brand-press-kit.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # Vector marks
        for svg_file in BRAND_DIR.glob("*.svg"):
            zf.write(svg_file, arcname=f"vector-svg/{svg_file.name}")
        for video_file in VIDEO_DIR.glob("*.*"):
            zf.write(video_file, arcname=f"video-assets/{video_file.name}")
        for banner_file in BANNERS_DIR.glob("*.*"):
            zf.write(banner_file, arcname=f"social-banners/{banner_file.name}")
        for fav_file in IMG_DIR.glob("*.*"):
            if fav_file.name not in ["paraxcel.ico"]:
                zf.write(fav_file, arcname=f"favicons-and-app-icons/{fav_file.name}")
        if AVATAR_PATH.exists():
            zf.write(AVATAR_PATH, arcname=f"headshots/{AVATAR_PATH.name}")

    print(f"✓ Master Press Kit ZIP compiled ({zip_path.stat().st_size / 1024:.1f} KB).")


if __name__ == "__main__":
    build_favicons()
    build_video_watermarks()
    build_social_banners()
    build_press_kit_zip()
    print("\nAll brand assets successfully compiled.")
