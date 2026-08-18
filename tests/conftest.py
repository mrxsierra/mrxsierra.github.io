"""
Shared pytest fixtures and utilities for mrxsierra.github.io site verification.
"""

import subprocess
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = PROJECT_ROOT / "site"
DOCS_DIR = PROJECT_ROOT / "docs"


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Returns the repository root directory."""
    return PROJECT_ROOT


@pytest.fixture(scope="session")
def docs_dir() -> Path:
    """Returns the docs directory."""
    return DOCS_DIR


@pytest.fixture(scope="session")
def site_dir() -> Path:
    """
    Returns the built site directory.
    If the site directory does not exist or is empty, it runs mkdocs build --strict.
    """
    if not SITE_DIR.exists() or not (SITE_DIR / "index.html").exists():
        result = subprocess.run(
            [".venv/bin/mkdocs", "build", "--strict"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            subprocess.run(
                ["mkdocs", "build", "--strict"],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True,
                check=True,
            )
    return SITE_DIR


@pytest.fixture(scope="session")
def all_html_files(site_dir: Path) -> list[Path]:
    """Returns all generated HTML files in the built site."""
    return sorted(list(site_dir.rglob("*.html")))


class HTMLDoc:
    """Helper wrapper around BeautifulSoup for HTML inspection."""

    def __init__(self, path: Path, soup: BeautifulSoup):
        self.path = path
        self.soup = soup
        self.relative_path = path.relative_to(SITE_DIR)

    @property
    def title(self) -> str:
        tag = self.soup.find("title")
        return tag.get_text(strip=True) if tag else ""


@pytest.fixture(scope="session")
def parsed_html_docs(all_html_files: list[Path]) -> dict[Path, HTMLDoc]:
    """Parses all HTML files once and returns a mapping from Path to HTMLDoc."""
    docs = {}
    for html_file in all_html_files:
        content = html_file.read_text(encoding="utf-8", errors="replace")
        soup = BeautifulSoup(content, "html.parser")
        docs[html_file] = HTMLDoc(path=html_file, soup=soup)
    return docs
