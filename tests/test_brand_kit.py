"""
Automated Test Suite for Brand Identity, Vector Marks, Content Creation Suite, and Press Kit.
Verifies:
1. Core vector marks exist and are valid SVG XML.
2. Web favicons (SVG, ICO, Apple Touch, Android Chrome) exist.
3. Video watermarks (150x150 PNG, lower third, end card) exist.
4. Social headers (GitHub, LinkedIn, X, YouTube, preview.png) exist.
5. Master Press Kit ZIP exists and contains structured directories.
6. Web Manifest is valid JSON.
7. Dedicated Press Kit page (/press/) exists and has download links.
8. Brand Engine Python package modules exist and are importable.
"""

import json
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


def test_core_vector_marks_exist(site_dir: Path):
    brand_dir = site_dir / "assets" / "brand"
    assert brand_dir.exists(), "Brand directory must exist in compiled site."

    expected_svgs = [
        "monogram-dark.svg",
        "monogram-light.svg",
        "monogram-transparent.svg",
        "logo-horizontal.svg",
        "logo-stacked.svg",
    ]
    for svg_name in expected_svgs:
        svg_file = brand_dir / svg_name
        assert svg_file.exists(), f"Vector SVG {svg_name} must exist."
        tree = ET.parse(svg_file)
        root = tree.getroot()
        assert "svg" in root.tag.lower(), f"{svg_name} root must be an SVG element."


def test_favicon_and_app_suite(site_dir: Path):
    img_dir = site_dir / "assets" / "img"
    assert img_dir.exists()

    required_favicons = [
        "favicon.svg",
        "favicon.ico",
        "favicon.png",
        "apple-touch-icon.png",
        "android-chrome-192x192.png",
        "android-chrome-512x512.png",
        "site.webmanifest",
        "preview.png",
    ]
    for asset in required_favicons:
        p = img_dir / asset
        assert p.exists(), f"App asset {asset} must exist."
        assert p.stat().st_size > 0, f"{asset} must not be empty."

    # Validate site.webmanifest
    manifest_file = img_dir / "site.webmanifest"
    manifest_data = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert manifest_data.get("name") == "Sunil Sharma | mrxsierra"
    assert manifest_data.get("short_name") == "mrxsierra"
    assert len(manifest_data.get("icons", [])) >= 2


def test_video_and_multimedia_suite(site_dir: Path):
    video_dir = site_dir / "assets" / "brand" / "video"
    assert video_dir.exists()

    video_assets = [
        "watermark-150x150.png",
        "watermark-square.svg",
        "lower-third.svg",
        "video-end-screen.svg",
        "thumbnail-frame.svg",
    ]
    for va in video_assets:
        p = video_dir / va
        assert p.exists(), f"Video asset {va} must exist."
        assert p.stat().st_size > 0


def test_social_banners_suite(site_dir: Path):
    banners_dir = site_dir / "assets" / "brand" / "banners"
    assert banners_dir.exists()

    social_assets = [
        "github-banner.svg",
        "github-banner.png",
        "linkedin-banner.svg",
        "linkedin-banner.png",
        "x-twitter-banner.svg",
        "x-twitter-banner.png",
        "youtube-banner.svg",
        "youtube-banner.png",
    ]
    for sa in social_assets:
        p = banners_dir / sa
        assert p.exists(), f"Social banner {sa} must exist."
        assert p.stat().st_size > 0


def test_master_press_kit_zip(site_dir: Path):
    zip_path = site_dir / "assets" / "brand" / "mrxsierra-brand-press-kit.zip"
    assert zip_path.exists(), "Master Press Kit ZIP must exist."
    assert zip_path.stat().st_size > 10_000, "Press Kit ZIP must contain substantial assets."

    with zipfile.ZipFile(zip_path, "r") as zf:
        namelist = zf.namelist()
        assert any("vector" in n for n in namelist), "ZIP must contain vector marks."
        assert any("favicons" in n for n in namelist), "ZIP must contain favicons."
        assert any("social" in n for n in namelist), "ZIP must contain social banners."
        assert any("00-PRESS-KIT-BIO-SHEET" in n for n in namelist), "ZIP must contain bio sheet."


def test_press_kit_page_integrity(site_dir: Path):
    press_html = site_dir / "press" / "index.html"
    assert press_html.exists(), "Press Kit /press/ page must be built."
    content = press_html.read_text(encoding="utf-8")
    assert "Press Kit &amp; Media Resources" in content or "Press Kit" in content
    assert "mrxsierra-brand-press-kit.zip" in content
    assert "Media Fast Facts" in content


def test_brand_engine_module_importable():
    from scripts.brand_engine.config import BRAND_CONFIG
    from scripts.brand_engine.packager import build_press_kit_zip
    from scripts.brand_engine.rasterizer import rasterize_all_assets
    from scripts.brand_engine.vector_builder import build_all_vectors

    assert BRAND_CONFIG["handle"] == "mrxsierra"
    assert callable(build_all_vectors)
    assert callable(rasterize_all_assets)
    assert callable(build_press_kit_zip)
