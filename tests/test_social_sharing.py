"""
Social sharing, Open Graph metadata, and RSS feed verification suite.
Validates that OpenGraph / Twitter Card tags are properly generated on all documentation pages,
that the social share widget renders exactly once without duplicates across articles and project case studies,
and that valid RSS syndication feeds are generated across multi-channel endpoints (Combined, Blog, Projects).
"""

import xml.etree.ElementTree as ET
from pathlib import Path

from bs4 import Tag

from tests.conftest import HTMLDoc


def test_opengraph_and_twitter_cards_present(site_dir: Path, parsed_html_docs: dict[Path, HTMLDoc]):
    """Verify that OpenGraph and Twitter Card tags exist on all standard site pages."""
    assert len(parsed_html_docs) > 0, "No built HTML files found in site/ directory."

    for path, doc in parsed_html_docs.items():
        if path.name == "404.html":
            continue

        soup = doc.soup
        rel_path = doc.relative_path

        # Open Graph Tags
        og_type = soup.find("meta", property="og:type")
        og_title = soup.find("meta", property="og:title")
        og_url = soup.find("meta", property="og:url")
        og_site_name = soup.find("meta", property="og:site_name")

        assert og_type is not None, f"Missing og:type in {rel_path}"
        assert og_title is not None, f"Missing og:title in {rel_path}"
        assert og_url is not None, f"Missing og:url in {rel_path}"
        assert og_site_name is not None, f"Missing og:site_name in {rel_path}"

        # Twitter Cards
        tw_card = soup.find("meta", attrs={"name": "twitter:card"})
        tw_site = soup.find("meta", attrs={"name": "twitter:site"})

        assert tw_card is not None, f"Missing twitter:card in {rel_path}"
        assert tw_site is not None, f"Missing twitter:site in {rel_path}"


def test_social_share_widget_present_and_not_duplicated(
    site_dir: Path, parsed_html_docs: dict[Path, HTMLDoc]
):
    """Verify that social sharing widget is present exactly once on content pages without duplicates."""
    content_pages = [
        "about/index.html",
        "resume/index.html",
        "contact/index.html",
        "projects/index.html",
        "projects/gstn-pbc/index.html",
        "projects/ems-db/index.html",
        "projects/naukri-webscraper/index.html",
        "projects/paraxcel/index.html",
        "projects/s3-faker/index.html",
        "projects/test-site/index.html",
    ]

    for rel_path in content_pages:
        target_path = site_dir / rel_path
        if target_path not in parsed_html_docs:
            continue

        soup = parsed_html_docs[target_path].soup
        widgets = soup.find_all(id="social-share-widget")
        assert len(widgets) == 1, (
            f"Expected exactly 1 social-share-widget in {rel_path}, found {len(widgets)}"
        )
        assert isinstance(widgets[0], Tag), f"social-share-widget is not a Tag in {rel_path}"

        # Verify all buttons including RSS and Pinterest
        expected_btn_ids = [
            "btn-share-native",
            "btn-share-x",
            "btn-share-linkedin",
            "btn-share-reddit",
            "btn-share-pinterest",
            "btn-share-hn",
            "btn-share-whatsapp",
            "btn-share-telegram",
            "btn-share-rss",
            "btn-share-copy",
        ]
        for btn_id in expected_btn_ids:
            btn = widgets[0].find(id=btn_id)
            assert btn is not None, f"Missing {btn_id} in {rel_path}"


def test_social_share_widget_excluded_on_homepage_and_404(
    site_dir: Path, parsed_html_docs: dict[Path, HTMLDoc]
):
    """Verify that the social sharing widget is not rendered on the landing page and 404 page."""
    excluded_pages = ["index.html", "404.html"]

    for rel_path in excluded_pages:
        target_path = site_dir / rel_path
        if target_path not in parsed_html_docs:
            continue

        soup = parsed_html_docs[target_path].soup
        widget = soup.find(id="social-share-widget")
        assert widget is None, f"social-share-widget unexpectedly found in {rel_path}"


def test_rss_feeds_generated_and_valid(site_dir: Path):
    """Verify that RSS syndication XML feeds are generated and contain valid items."""
    feeds = [
        "feed_rss_created.xml",
        "feed_rss_updated.xml",
        "feed.xml",
        "feed_blog.xml",
        "feed_projects.xml",
    ]
    for feed_name in feeds:
        feed_path = site_dir / feed_name
        assert feed_path.exists(), f"Missing RSS feed: {feed_name}"
        assert feed_path.stat().st_size > 300, f"RSS feed {feed_name} is too small"

        tree = ET.parse(str(feed_path))
        root = tree.getroot()
        assert root.tag == "rss", f"{feed_name} root is not <rss>"

        channel = root.find("channel")
        assert channel is not None, f"Missing <channel> in {feed_name}"

        items = channel.findall("item")
        assert len(items) >= 1, f"Expected at least 1 item in {feed_name}, got {len(items)}"
        for item in items:
            title_node = item.find("title")
            link_node = item.find("link")
            pub_date_node = item.find("pubDate")
            assert title_node is not None and bool(title_node.text)
            assert (
                link_node is not None
                and link_node.text is not None
                and link_node.text.startswith("https://")
            )
            assert pub_date_node is not None and bool(pub_date_node.text)


def test_rss_discovery_tags_and_badges_in_html(
    site_dir: Path, parsed_html_docs: dict[Path, HTMLDoc]
):
    """Verify that RSS auto-discovery tags and index badges are present in HTML."""
    homepage = site_dir / "index.html"
    if homepage in parsed_html_docs:
        soup = parsed_html_docs[homepage].soup
        rss_link = soup.find("link", rel="alternate", type="application/rss+xml")
        assert rss_link is not None, "Missing RSS auto-discovery link tag in homepage <head>"

    blog_index = site_dir / "blog" / "index.html"
    if blog_index in parsed_html_docs:
        soup = parsed_html_docs[blog_index].soup
        badge = soup.find("a", class_="rss-subscribe-badge")
        assert badge is not None, "Missing rss-subscribe-badge on blog index page"

    projects_index = site_dir / "projects" / "index.html"
    if projects_index in parsed_html_docs:
        soup = parsed_html_docs[projects_index].soup
        badge = soup.find("a", class_="rss-subscribe-badge")
        assert badge is not None, "Missing rss-subscribe-badge on projects index page"
