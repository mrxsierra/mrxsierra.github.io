"""
Unit and verification tests for Semantic Versioning and synchronization.
"""

import tomllib
from pathlib import Path

from scripts.bump_version import (
    calculate_next_version,
    format_semver,
    parse_semver,
)


def test_version_files_synchronized(project_root: Path):
    """Verify that VERSION, pyproject.toml, and CHANGELOG.md are synchronized."""
    version_file = project_root / "VERSION"
    pyproject_file = project_root / "pyproject.toml"
    changelog_file = project_root / "CHANGELOG.md"

    assert version_file.exists(), "VERSION file missing"
    assert pyproject_file.exists(), "pyproject.toml missing"
    assert changelog_file.exists(), "CHANGELOG.md missing"

    version_str = version_file.read_text(encoding="utf-8").strip()
    # Validate valid semver format
    major, minor, patch = parse_semver(version_str)
    assert f"{major}.{minor}.{patch}" == version_str

    # Validate pyproject.toml matches
    with open(pyproject_file, "rb") as f:
        pyproject_data = tomllib.load(f)
    pyproject_version = pyproject_data.get("project", {}).get("version")
    assert pyproject_version == version_str, (
        f"pyproject.toml version ({pyproject_version}) != VERSION ({version_str})"
    )

    # Validate changelog contains the version section
    changelog_content = changelog_file.read_text(encoding="utf-8")
    assert f"[{version_str}]" in changelog_content, (
        f"CHANGELOG.md does not contain entry for [{version_str}]"
    )

    # Validate mkdocs.yml matches
    mkdocs_file = project_root / "mkdocs.yml"
    assert mkdocs_file.exists(), "mkdocs.yml missing"
    mkdocs_content = mkdocs_file.read_text(encoding="utf-8")
    assert f"version: {version_str}" in mkdocs_content, (
        f"mkdocs.yml extra.version does not contain 'version: {version_str}'"
    )


def test_semver_parse_and_format():
    """Verify semver parsing and formatting roundtrip."""
    assert parse_semver("0.0.1") == (0, 0, 1)
    assert parse_semver("v1.2.3") == (1, 2, 3)
    assert format_semver(0, 0, 1) == "0.0.1"
    assert format_semver(2, 4, 10) == "2.4.10"


def test_version_bump_calculations():
    """Verify patch, minor, major, and custom version bumps."""
    base = "0.0.1"

    # Patch bump
    assert calculate_next_version(base, "patch") == "0.0.2"
    assert calculate_next_version("0.1.9", "patch") == "0.1.10"

    # Minor bump (resets patch to 0)
    assert calculate_next_version(base, "minor") == "0.1.0"
    assert calculate_next_version("0.0.5", "minor") == "0.1.0"
    assert calculate_next_version("0.3.12", "minor") == "0.4.0"

    # Major bump (resets minor and patch to 0)
    assert calculate_next_version(base, "major") == "1.0.0"
    assert calculate_next_version("0.4.2", "major") == "1.0.0"
    assert calculate_next_version("1.2.3", "major") == "2.0.0"

    # Custom set
    assert calculate_next_version(base, "set:0.5.0") == "0.5.0"
    assert calculate_next_version(base, "set:v1.0.0") == "1.0.0"
