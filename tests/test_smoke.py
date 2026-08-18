"""
Smoke test suite for mrxsierra.github.io.
Verifies that all essential pages, feeds, machine-readable specifications, and static assets exist.
"""

from pathlib import Path

import pytest

EXPECTED_CORE_PAGES = [
    "index.html",
    "404.html",
    "about/index.html",
    "brand/index.html",
    "resume/index.html",
    "contact/index.html",
    "projects/index.html",
    "projects/gstn-pbc/index.html",
    "projects/ems-db/index.html",
    "projects/s3-faker/index.html",
    "projects/paraxcel/index.html",
    "projects/naukri-webscraper/index.html",
    "projects/test-site/index.html",
    "blog/index.html",
    "changelog/index.html",
]

EXPECTED_MACHINE_ASSETS = [
    "llms.txt",
    "llms-full.txt",
    "robots.txt",
    "sitemap.xml",
    "sitemap.xml.gz",
]

EXPECTED_STATIC_ASSETS = [
    "stylesheets/index.css",
    "stylesheets/extra.css",
    "javascripts/index.js",
    "assets/img/favicon.ico",
    "assets/img/logo-monogram.svg",
]


@pytest.mark.parametrize("page_rel_path", EXPECTED_CORE_PAGES)
def test_core_pages_exist_and_non_empty(site_dir: Path, page_rel_path: str):
    """Ensure all expected core HTML pages are successfully built and non-empty."""
    target = site_dir / page_rel_path
    assert target.exists(), f"Missing required core page: {page_rel_path}"
    assert target.stat().st_size > 100, f"Core page is too small or empty: {page_rel_path}"


@pytest.mark.parametrize("asset_rel_path", EXPECTED_MACHINE_ASSETS)
def test_machine_and_seo_assets_exist(site_dir: Path, asset_rel_path: str):
    """Ensure SEO and AI agent discovery assets exist and are populated."""
    target = site_dir / asset_rel_path
    assert target.exists(), f"Missing required asset: {asset_rel_path}"
    assert target.stat().st_size > 10, f"Asset is empty: {asset_rel_path}"


@pytest.mark.parametrize("asset_rel_path", EXPECTED_STATIC_ASSETS)
def test_static_assets_exist(site_dir: Path, asset_rel_path: str):
    """Ensure custom stylesheets, scripts, and favicon assets exist in built site."""
    target = site_dir / asset_rel_path
    assert target.exists(), f"Missing custom static asset: {asset_rel_path}"
    assert target.stat().st_size > 0, f"Static asset is empty: {asset_rel_path}"


def test_site_has_healthy_page_count(all_html_files: list[Path]):
    """Ensure that the site build generated a realistic volume of pages (at least 10)."""
    assert len(all_html_files) >= 10, f"Expected >= 10 HTML pages, found {len(all_html_files)}"


def test_footer_directory_and_version_tag(site_dir: Path, version_str: str):
    """Ensure that the unified footer renders directory columns and the synchronized version badge."""
    index_html = (site_dir / "index.html").read_text(encoding="utf-8")
    assert "site-footer-container" in index_html, "Missing site-footer-container in index.html"
    assert "site-footer-grid" in index_html, "Missing site-footer-grid in index.html"
    assert f"v{version_str}" in index_html, f"Expected version badge v{version_str} in footer"
    assert "llms.txt" in index_html, "Missing llms.txt link in footer"
    assert "feed_rss_created.xml" in index_html, "Missing RSS feed link in footer"
