"""
Packager Module for Brand Engine.
Compiles the master Press Kit ZIP archive bundling all vector marks, raster exports,
social banners, video watermarks, and media bio copy.
"""

import zipfile

from .config import BRAND_CONFIG


def build_press_kit_zip():
    """Packages all brand assets into a clean, well-structured ZIP archive."""
    paths = BRAND_CONFIG["paths"]
    bios = BRAND_CONFIG["bios"]

    brand_dir = paths["brand_dir"]
    video_dir = paths["video_dir"]
    banners_dir = paths["banners_dir"]
    articles_dir = paths["articles_dir"]
    social_dir = paths["social_dir"]
    decks_dir = paths["decks_dir"]
    img_dir = paths["img_dir"]
    avatar_path = paths["avatar_path"]
    zip_path = paths["zip_path"]

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # 1. Vector SVGs
        for f in brand_dir.glob("*.svg"):
            zf.write(f, arcname=f"01-vector-marks/{f.name}")

        # 2. Video Assets & Watermarks
        for f in video_dir.glob("*.*"):
            zf.write(f, arcname=f"02-video-watermarks/{f.name}")

        # 3. Social Headers & Covers
        for f in banners_dir.glob("*.*"):
            zf.write(f, arcname=f"03-social-banners/{f.name}")
        for f in social_dir.glob("*.*"):
            zf.write(f, arcname=f"03-social-banners/{f.name}")

        # 4. Publication & Article Templates
        for f in articles_dir.glob("*.*"):
            zf.write(f, arcname=f"04-article-covers/{f.name}")

        # 5. Slide Masters & Decks
        for f in decks_dir.glob("*.*"):
            zf.write(f, arcname=f"05-presentation-decks/{f.name}")

        # 6. Favicons & Web Icons
        for f in img_dir.glob("*.*"):
            if f.name not in ["paraxcel.ico", "temp_48.png", "temp_64.png"]:
                zf.write(f, arcname=f"06-web-favicons/{f.name}")

        # 7. Headshot Photos
        if avatar_path.exists():
            zf.write(avatar_path, arcname=f"07-headshots/{avatar_path.name}")

        # 8. Text Bio Sheets
        bio_text = f"""================================================================================
OFFICIAL MEDIA BIOS & BRAND STANDARDS: {BRAND_CONFIG["name"]} ({BRAND_CONFIG["twitter"]})
Website: {BRAND_CONFIG["domain"]}
GitHub:  {BRAND_CONFIG["github"]}
================================================================================

1. ONE-LINER (Social Bios & Short Introductions)
--------------------------------------------------------------------------------
{bios["one_liner"]}

2. SHORT BIO (50 Words for Conference Introductions & Podcast Notes)
--------------------------------------------------------------------------------
{bios["short_50"]}

3. FULL BIO (100 Words for Formal Publication Bylines & Keynotes)
--------------------------------------------------------------------------------
{bios["full_100"]}

4. TECHNICAL ABSTRACT & EXPERTISE
--------------------------------------------------------------------------------
{bios["technical_abstract"]}

5. BRAND USAGE & PERMISSIONS
--------------------------------------------------------------------------------
- Naming: Reference as "Sunil Sharma" or handle "mrxsierra" / "@mrxsierra".
- Monogram: Maintain at least 25% clear space around the mark.
- Background: Use Obsidian (#08090D) or pure white (#FFFFFF) backgrounds.
================================================================================
"""
        zf.writestr("00-PRESS-KIT-BIO-SHEET.txt", bio_text)

    print(f"✓ Master Press Kit ZIP compiled ({zip_path.stat().st_size / 1024:.1f} KB).")
