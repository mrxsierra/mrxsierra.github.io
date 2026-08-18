"""
Automated Multi-Channel RSS Feed Generator Hook for MkDocs.
Generates valid W3C RSS 2.0 XML feeds:
- Combined Main Feed: site/feed_rss_created.xml, site/feed_rss_updated.xml, site/feed.xml
- Blog Posts Feed: site/feed_blog.xml, site/blog/feed_rss_created.xml
- Project Case Studies Feed: site/feed_projects.xml, site/projects/feed_rss_created.xml
"""

import re
import xml.etree.ElementTree as ET
from datetime import UTC, date, datetime
from email.utils import format_datetime
from pathlib import Path

import yaml


def extract_frontmatter(content: str) -> dict:
    """Extract and parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}

    try:
        data = yaml.safe_load(parts[1])
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def parse_date(date_val) -> datetime:
    """Parses various date representations into a timezone-aware UTC datetime."""
    if isinstance(date_val, dict):
        date_val = date_val.get("created") or date_val.get("updated")
    if isinstance(date_val, datetime):
        return date_val.replace(tzinfo=UTC) if date_val.tzinfo is None else date_val
    if isinstance(date_val, date):
        return datetime(date_val.year, date_val.month, date_val.day, 12, 0, 0, tzinfo=UTC)
    if isinstance(date_val, str):
        try:
            dt = datetime.fromisoformat(date_val.strip())
            return dt.replace(tzinfo=UTC) if dt.tzinfo is None else dt
        except Exception:
            pass
    return datetime.now(UTC)


def create_rss_xml(
    channel_title: str,
    channel_link: str,
    channel_desc: str,
    feed_url: str,
    items: list[dict[str, str]],
) -> ET.ElementTree:
    """Constructs a W3C-compliant RSS 2.0 ElementTree with Atom self-link."""
    rss = ET.Element("rss", version="2.0", attrib={"xmlns:atom": "http://www.w3.org/2005/Atom"})
    channel = ET.SubElement(rss, "channel")

    title_elem = ET.SubElement(channel, "title")
    title_elem.text = channel_title

    link_elem = ET.SubElement(channel, "link")
    link_elem.text = channel_link

    desc_elem = ET.SubElement(channel, "description")
    desc_elem.text = channel_desc

    lang_elem = ET.SubElement(channel, "language")
    lang_elem.text = "en-us"

    last_build = ET.SubElement(channel, "lastBuildDate")
    last_build.text = format_datetime(datetime.now(UTC))

    ET.SubElement(
        channel,
        "atom:link",
        attrib={"href": feed_url, "rel": "self", "type": "application/rss+xml"},
    )

    for item in items:
        item_elem = ET.SubElement(channel, "item")

        it_title = ET.SubElement(item_elem, "title")
        it_title.text = item["title"]

        it_link = ET.SubElement(item_elem, "link")
        it_link.text = item["link"]

        it_guid = ET.SubElement(item_elem, "guid", isPermaLink="true")
        it_guid.text = item["link"]

        it_desc = ET.SubElement(item_elem, "description")
        it_desc.text = item["description"]

        it_date = ET.SubElement(item_elem, "pubDate")
        it_date.text = item["pub_date"]

    xml_tree = ET.ElementTree(rss)
    ET.indent(xml_tree, space="  ")
    return xml_tree


def build_rss_feeds(site_dir: Path, site_url: str = "https://mrxsierra.github.io/"):
    """Scans blog and project markdown files and builds multi-channel RSS 2.0 feeds."""
    project_root = site_dir.parent if site_dir.name == "site" else site_dir
    docs_dir = project_root / "docs"

    site_url = site_url.rstrip("/") + "/"
    blog_items: list[dict[str, str]] = []
    project_items: list[dict[str, str]] = []

    # 1. Collect Blog Posts
    blog_dir = docs_dir / "blog"
    if blog_dir.exists():
        for md_file in blog_dir.glob("posts/**/*.md"):
            content = md_file.read_text(encoding="utf-8", errors="replace")
            meta = extract_frontmatter(content)

            title = meta.get("title", "")
            if not title:
                match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                title = match.group(1).strip() if match else md_file.stem

            description = str(meta.get("description", "")).strip()
            dt = parse_date(meta.get("date"))
            slug = meta.get("slug") or md_file.stem
            date_prefix = dt.strftime("%Y/%m/%d")
            clean_link = f"{site_url}blog/{date_prefix}/{slug}/"

            blog_items.append(
                {
                    "title": title,
                    "link": clean_link,
                    "description": description or f"Technical article on {title}",
                    "pub_date": format_datetime(dt),
                    "timestamp": str(dt.timestamp()),
                }
            )

    # 2. Collect Project Articles
    projects_dir = docs_dir / "projects"
    if projects_dir.exists():
        for md_file in projects_dir.glob("*.md"):
            if md_file.name == "index.md":
                continue
            content = md_file.read_text(encoding="utf-8", errors="replace")
            meta = extract_frontmatter(content)

            title = meta.get("title", "")
            if not title:
                match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                title = match.group(1).strip() if match else md_file.stem

            description = str(meta.get("description", "")).strip()
            dt = datetime.fromtimestamp(md_file.stat().st_mtime, tz=UTC)
            clean_link = f"{site_url}projects/{md_file.stem}/"

            project_items.append(
                {
                    "title": title,
                    "link": clean_link,
                    "description": description or f"Engineering project case study: {title}",
                    "pub_date": format_datetime(dt),
                    "timestamp": str(dt.timestamp()),
                }
            )

    # Sort each list newest first
    blog_items.sort(key=lambda x: float(x["timestamp"]), reverse=True)
    project_items.sort(key=lambda x: float(x["timestamp"]), reverse=True)
    combined_items = sorted(
        blog_items + project_items, key=lambda x: float(x["timestamp"]), reverse=True
    )

    # 3. Build & Write Feeds

    # Combined Feed (Blog + Projects)
    combined_tree = create_rss_xml(
        channel_title="mrxsierra | Sunil Sharma",
        channel_link=site_url,
        channel_desc="Engineering portfolio, technical writing, and machine learning articles by Sunil Sharma.",
        feed_url=f"{site_url}feed_rss_created.xml",
        items=combined_items,
    )
    for name in ["feed_rss_created.xml", "feed_rss_updated.xml", "feed.xml"]:
        combined_tree.write(str(site_dir / name), encoding="utf-8", xml_declaration=True)

    # Blog-Only Feed
    blog_tree = create_rss_xml(
        channel_title="mrxsierra | Technical Blog",
        channel_link=f"{site_url}blog/",
        channel_desc="In-depth database engineering, SQL dialect comparisons, and systems automation articles by Sunil Sharma.",
        feed_url=f"{site_url}feed_blog.xml",
        items=blog_items,
    )
    blog_tree.write(str(site_dir / "feed_blog.xml"), encoding="utf-8", xml_declaration=True)
    (site_dir / "blog").mkdir(parents=True, exist_ok=True)
    blog_tree.write(
        str(site_dir / "blog" / "feed_rss_created.xml"), encoding="utf-8", xml_declaration=True
    )

    # Projects-Only Feed
    projects_tree = create_rss_xml(
        channel_title="mrxsierra | Engineering Projects & Case Studies",
        channel_link=f"{site_url}projects/",
        channel_desc="Case studies, architecture breakdowns, and open-source project releases by Sunil Sharma.",
        feed_url=f"{site_url}feed_projects.xml",
        items=project_items,
    )
    projects_tree.write(str(site_dir / "feed_projects.xml"), encoding="utf-8", xml_declaration=True)
    (site_dir / "projects").mkdir(parents=True, exist_ok=True)
    projects_tree.write(
        str(site_dir / "projects" / "feed_rss_created.xml"), encoding="utf-8", xml_declaration=True
    )


def on_post_build(config, **kwargs):
    """MkDocs hook entrypoint: triggers multi-channel RSS feed generation after site build."""
    site_dir = Path(config["site_dir"])
    site_url = config.get("site_url", "https://mrxsierra.github.io/")
    build_rss_feeds(site_dir, site_url)
