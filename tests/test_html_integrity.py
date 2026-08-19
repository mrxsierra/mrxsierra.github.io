"""
HTML integrity, link validation, and DOM quality test suite for mrxsierra.github.io.
Verifies zero broken internal links, valid asset references, valid DOM semantics, clean builds,
native Mermaid diagram compilation, and Reader Mode compatibility.
"""

from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup

SITE_DOMAIN = "https://mrxsierra.github.io"
# Sibling standalone GitHub Pages repositories (not hosted in this MkDocs site root)
EXTERNAL_REPOS = {"test-site"}


def resolve_internal_target(
    site_dir: Path, current_file: Path, href: str
) -> tuple[Path | None, str | None]:
    """
    Resolves an internal href relative to current_file or site_dir.
    Returns (target_path, anchor_id).
    """
    parsed = urlparse(href)

    # Ignore mailto, javascript, tel, and external domains
    if parsed.scheme in ("mailto", "javascript", "tel"):
        return None, None
    if parsed.scheme and not href.startswith(SITE_DOMAIN):
        return None, None

    # Handle site domain prefix
    path_part = parsed.path
    if href.startswith(SITE_DOMAIN):
        path_part = path_part.removeprefix(urlparse(SITE_DOMAIN).path)
        first_segment = path_part.strip("/").split("/")[0] if path_part.strip("/") else ""
        if first_segment in EXTERNAL_REPOS:
            return None, None

    anchor = parsed.fragment if parsed.fragment else None

    # Pure anchor on current page
    if not path_part:
        return current_file, anchor

    # Path resolution
    if path_part.startswith("/"):
        clean_path = path_part.lstrip("/")
        candidate = (site_dir / clean_path).resolve()
    else:
        candidate = (current_file.parent / path_part).resolve()

    # Normalize directory vs file
    if candidate.is_dir():
        candidate = candidate / "index.html"
    elif not candidate.exists():
        if candidate.with_suffix(".html").exists():
            candidate = candidate.with_suffix(".html")
        elif (candidate / "index.html").exists():
            candidate = candidate / "index.html"

    return candidate, anchor


def test_internal_links_integrity(site_dir: Path, all_html_files: list[Path]):
    """
    Extract and validate all internal links across the site.
    Ensures zero 404s for internal links and anchors.
    """
    broken_links: list[str] = []
    cached_soup_ids: dict[Path, set[str]] = {}

    for html_file in all_html_files:
        content = html_file.read_text(encoding="utf-8", errors="replace")
        soup = BeautifulSoup(content, "html.parser")
        rel_html_path = html_file.relative_to(site_dir)

        links = soup.find_all("a", href=True)
        for link in links:
            href = link["href"].strip()
            if not href or href.startswith("#") and len(href) == 1:
                continue

            target_path, anchor = resolve_internal_target(site_dir, html_file, href)
            if target_path is None:
                continue

            if not target_path.exists():
                broken_links.append(
                    f"[{rel_html_path}] Broken href '{href}' -> Target '{target_path}' not found"
                )
                continue

            # Validate anchor if specified
            if anchor and target_path.suffix == ".html":
                if target_path not in cached_soup_ids:
                    target_content = target_path.read_text(encoding="utf-8", errors="replace")
                    target_soup = BeautifulSoup(target_content, "html.parser")
                    ids = {el.get("id") for el in target_soup.find_all(id=True)}
                    names = {el.get("name") for el in target_soup.find_all(attrs={"name": True})}
                    cached_soup_ids[target_path] = ids.union(names)

                valid_ids = cached_soup_ids[target_path]
                clean_anchor = unquote(anchor)
                if clean_anchor not in valid_ids:
                    # Some mkdocs tab or search anchors might be dynamic; record as warning/check
                    broken_links.append(
                        f"[{rel_html_path}] Missing anchor '#{clean_anchor}' in '{target_path.relative_to(site_dir)}'"
                    )

    assert not broken_links, "Found broken internal links:\n" + "\n".join(broken_links[:20])


def test_internal_media_and_assets(site_dir: Path, all_html_files: list[Path]):
    """Ensure all internal image and media src attributes resolve to existing files."""
    missing_assets: list[str] = []

    for html_file in all_html_files:
        content = html_file.read_text(encoding="utf-8", errors="replace")
        soup = BeautifulSoup(content, "html.parser")
        rel_html_path = html_file.relative_to(site_dir)

        # Check images
        for img in soup.find_all("img", src=True):
            src = img["src"].strip()
            if src.startswith("data:") or src.startswith("http://") or src.startswith("https://"):
                continue

            target_path, _ = resolve_internal_target(site_dir, html_file, src)
            if target_path and not target_path.exists():
                missing_assets.append(
                    f"[{rel_html_path}] Missing img src '{src}' -> '{target_path}'"
                )

    assert not missing_assets, "Found missing internal assets:\n" + "\n".join(missing_assets)


def test_dom_semantics_and_seo_headers(all_html_files: list[Path], site_dir: Path):
    """Ensure every generated page contains valid HTML semantics, doctype, title, and viewport."""
    issues: list[str] = []

    for html_file in all_html_files:
        content = html_file.read_text(encoding="utf-8", errors="replace")
        rel_path = html_file.relative_to(site_dir)

        # Check doctype
        if not content.lstrip().startswith("<!doctype html>") and not content.lstrip().startswith(
            "<!DOCTYPE html>"
        ):
            issues.append(f"[{rel_path}] Missing <!DOCTYPE html>")

        soup = BeautifulSoup(content, "html.parser")

        # Check title
        title_tag = soup.find("title")
        if not title_tag or not title_tag.get_text(strip=True):
            issues.append(f"[{rel_path}] Missing or empty <title>")

        # Check viewport
        viewport = soup.find("meta", attrs={"name": "viewport"})
        if not viewport:
            issues.append(f"[{rel_path}] Missing <meta name='viewport'>")

    assert not issues, "Found DOM/SEO semantic issues:\n" + "\n".join(issues)


def test_no_unrendered_template_artifacts(all_html_files: list[Path], site_dir: Path):
    """Ensure no raw template tags (Jinja/MkDocs placeholders) leaked into HTML files."""
    leaks: list[str] = []
    # Known leak markers
    leak_markers = ["{{ config.", "{{ page.", "{% if ", "{% for "]

    for html_file in all_html_files:
        content = html_file.read_text(encoding="utf-8", errors="replace")
        rel_path = html_file.relative_to(site_dir)
        for marker in leak_markers:
            if marker in content:
                leaks.append(f"[{rel_path}] Contains raw template marker '{marker}'")

    assert not leaks, "Found unrendered template leaks:\n" + "\n".join(leaks)


def test_mermaid_diagrams_compiled_natively(site_dir: Path):
    """Ensure that pages with Mermaid diagrams compile to pre.mermaid elements rather than unparsed text blocks."""
    mermaid_pages = [
        site_dir / "projects" / "gstn-pbc" / "index.html",
        site_dir / "projects" / "ems-db" / "index.html",
        site_dir / "projects" / "naukri-webscraper" / "index.html",
        site_dir / "projects" / "paraxcel" / "index.html",
        site_dir / "projects" / "s3-faker" / "index.html",
        site_dir / "projects" / "test-site" / "index.html",
    ]

    for p in mermaid_pages:
        assert p.exists(), f"Page {p} must exist."
        content = p.read_text(encoding="utf-8")
        soup = BeautifulSoup(content, "html.parser")
        mermaid_blocks = soup.find_all("pre", class_="mermaid")
        assert len(mermaid_blocks) >= 1, (
            f"Expected at least 1 compiled <pre class='mermaid'> block in {p.relative_to(site_dir)}, found {len(mermaid_blocks)}"
        )


def test_reader_mode_article_headings(all_html_files: list[Path], site_dir: Path):
    """Ensure that all content article pages have an H1 element for Reader Mode parsing."""
    for html_file in all_html_files:
        if html_file.name == "404.html":
            continue
        content = html_file.read_text(encoding="utf-8")
        soup = BeautifulSoup(content, "html.parser")
        h1 = soup.find("h1")
        assert h1 is not None, (
            f"Page {html_file.relative_to(site_dir)} must contain an <h1> element for Reader Mode."
        )
