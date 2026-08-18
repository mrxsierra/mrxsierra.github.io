"""
Unit and functional tests for MkDocs hooks and AI documentation generators.
"""

from pathlib import Path

from hooks.generate_ai_docs import build_ai_docs, clean_html_to_markdown


def test_clean_html_to_markdown_conversions():
    """Verify HTML cleanup logic converts elements into clean markdown without style remnants."""
    raw_sample = """---
title: Sample Page
---
<!-- Comment to remove -->
<h1>Main Title</h1>
<p>This is <strong>bold</strong> and <em>italic</em> with <code>inline_code</code>.</p>
<a href="https://example.com" class="link-class"><span>Link Text</span></a>
<img src="/img/sample.png" alt="Sample Alt" class="responsive">
/// caption
Ignored caption block
///
<div class="custom-card">
  <h2>Sub Title</h2>
</div>
"""
    cleaned = clean_html_to_markdown(raw_sample)

    # Assert YAML frontmatter stripped
    assert "title: Sample Page" not in cleaned
    # Assert comment stripped
    assert "Comment to remove" not in cleaned
    # Assert headers converted
    assert "# Main Title" in cleaned
    assert "## Sub Title" in cleaned
    # Assert inline elements converted
    assert "**bold**" in cleaned
    assert "*italic*" in cleaned
    assert "`inline_code`" in cleaned
    # Assert link and image conversion
    assert "[Link Text](https://example.com)" in cleaned
    assert "![Sample Alt](/img/sample.png)" in cleaned
    # Assert caption block removed
    assert "Ignored caption block" not in cleaned
    # Assert div tags removed
    assert "<div" not in cleaned


def test_build_ai_docs_generation(project_root: Path):
    """Verify that build_ai_docs generates valid llms.txt and llms-full.txt files."""
    build_ai_docs()

    root_llms = project_root / "llms.txt"
    docs_llms = project_root / "docs" / "llms.txt"
    docs_full_llms = project_root / "docs" / "llms-full.txt"

    assert root_llms.exists() and root_llms.stat().st_size > 500
    assert docs_llms.exists() and docs_llms.stat().st_size > 500
    assert docs_full_llms.exists() and docs_full_llms.stat().st_size > 1000

    # Verify llms.txt spec contents
    content = root_llms.read_text(encoding="utf-8")
    assert "Sunil Sharma" in content
    assert "llmstxt.org" in content
    assert "## Featured Engineering Projects" in content
