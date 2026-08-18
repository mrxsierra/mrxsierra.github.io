#!/usr/bin/env python3
"""
mrxsierra.github.io - Semantic Versioning & Changelog Synchronizer
Manages single-source versioning across VERSION, pyproject.toml, and CHANGELOG.md.

Usage:
  python scripts/bump_version.py current
  python scripts/bump_version.py patch
  python scripts/bump_version.py minor
  python scripts/bump_version.py major
  python scripts/bump_version.py auto
  python scripts/bump_version.py set <version>
"""

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = PROJECT_ROOT / "VERSION"
PYPROJECT_FILE = PROJECT_ROOT / "pyproject.toml"
CHANGELOG_FILE = PROJECT_ROOT / "CHANGELOG.md"


def get_current_version() -> str:
    """Reads current version from VERSION file, with git tag fallback for monotonic consistency."""
    file_ver = (
        VERSION_FILE.read_text(encoding="utf-8").strip() if VERSION_FILE.exists() else "0.0.1"
    )
    try:
        tag_result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if tag_result.returncode == 0 and tag_result.stdout.strip():
            tag_ver = tag_result.stdout.strip().lstrip("v")
            if parse_semver(tag_ver) > parse_semver(file_ver):
                return tag_ver
    except Exception:
        pass
    return file_ver


def parse_semver(version_str: str) -> tuple[int, int, int]:
    """Parses a semver string into (major, minor, patch)."""
    clean_ver = version_str.lstrip("v").strip()
    parts = clean_ver.split(".")
    if len(parts) != 3:
        raise ValueError(f"Invalid SemVer string: {version_str}")
    try:
        return int(parts[0]), int(parts[1]), int(parts[2])
    except ValueError as e:
        raise ValueError(f"Non-numeric SemVer components in '{version_str}': {e}") from e


def format_semver(major: int, minor: int, patch: int) -> str:
    """Formats components back to a SemVer string."""
    return f"{major}.{minor}.{patch}"


def detect_bump_type_from_git() -> str:
    """
    Detects bump type based on git commits since last tag:
    - Breaking changes -> 'major'
    - Feature PR merges / feat commits -> 'minor'
    - Otherwise -> 'patch'
    """
    try:
        # Get last tag
        tag_result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if tag_result.returncode == 0 and tag_result.stdout.strip():
            last_tag = tag_result.stdout.strip()
            log_range = f"{last_tag}..HEAD"
        else:
            log_range = "HEAD~5..HEAD"

        log_result = subprocess.run(
            ["git", "log", log_range, "--pretty=format:%s%n%b"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        commit_text = log_result.stdout.lower()

        if "breaking change:" in commit_text or "feat!:" in commit_text:
            return "major"
        if "feat:" in commit_text or "feat(" in commit_text or "merge pull request" in commit_text:
            return "minor"
        return "patch"
    except Exception:
        return "patch"


def calculate_next_version(current_ver: str, bump_type: str) -> str:
    """Calculates next SemVer based on bump type."""
    major, minor, patch = parse_semver(current_ver)

    if bump_type == "patch":
        return format_semver(major, minor, patch + 1)
    elif bump_type == "minor":
        return format_semver(major, minor + 1, 0)
    elif bump_type == "major":
        return format_semver(major + 1, 0, 0)
    elif bump_type.startswith("set:"):
        custom = bump_type.split(":", 1)[1].strip().lstrip("v")
        # Validate syntax
        parse_semver(custom)
        return custom
    else:
        raise ValueError(f"Unknown bump type: {bump_type}")


MKDOCS_FILE = PROJECT_ROOT / "mkdocs.yml"
INDEX_MD_FILE = PROJECT_ROOT / "docs" / "index.md"


def sync_version_files(new_version: str, dry_run: bool = False) -> None:
    """Updates VERSION, pyproject.toml, mkdocs.yml, and docs/index.md with new version."""
    if dry_run:
        print(f"[DRY-RUN] Would update {VERSION_FILE} to '{new_version}'")
        print(f"[DRY-RUN] Would update {PYPROJECT_FILE} version to '{new_version}'")
        print(f"[DRY-RUN] Would update {MKDOCS_FILE} extra.version to '{new_version}'")
        print(f"[DRY-RUN] Would update {INDEX_MD_FILE} telemetry version to '{new_version}'")
        return

    # 1. Update VERSION file
    VERSION_FILE.write_text(f"{new_version}\n", encoding="utf-8")

    # 2. Update pyproject.toml
    if PYPROJECT_FILE.exists():
        content = PYPROJECT_FILE.read_text(encoding="utf-8")
        updated = re.sub(r'version\s*=\s*"[^"]+"', f'version = "{new_version}"', content, count=1)
        PYPROJECT_FILE.write_text(updated, encoding="utf-8")

    # 3. Update mkdocs.yml extra.version
    if MKDOCS_FILE.exists():
        content = MKDOCS_FILE.read_text(encoding="utf-8")
        updated = re.sub(
            r"(\bversion:\s*)[0-9]+\.[0-9]+\.[0-9]+", rf"\g<1>{new_version}", content, count=1
        )
        MKDOCS_FILE.write_text(updated, encoding="utf-8")

    # 4. Update docs/index.md terminal preview widget
    if INDEX_MD_FILE.exists():
        content = INDEX_MD_FILE.read_text(encoding="utf-8")
        updated = re.sub(
            r"v[0-9]+\.[0-9]+\.[0-9]+\s*•\s*Verified\s*&amp;\s*Automated\s*CI/CD",
            f"v{new_version} • Verified &amp; Automated CI/CD",
            content,
            count=1,
        )
        INDEX_MD_FILE.write_text(updated, encoding="utf-8")


def extract_categorized_git_commits() -> dict[str, list[str]]:
    """Extracts and groups git commits since last release tag."""
    categories: dict[str, list[str]] = {"Added": [], "Fixed": [], "Changed": []}
    try:
        tag_result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        log_range = (
            f"{tag_result.stdout.strip()}..HEAD"
            if tag_result.returncode == 0 and tag_result.stdout.strip()
            else "HEAD~5..HEAD"
        )

        log_result = subprocess.run(
            ["git", "log", log_range, "--pretty=format:%s"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        lines = [line.strip() for line in log_result.stdout.splitlines() if line.strip()]

        for line in lines:
            # Skip automated merge and release commit messages
            if (
                line.startswith("Merge pull request")
                or line.startswith("Merge branch")
                or "chore(release):" in line
                or "[skip ci]" in line
            ):
                continue

            clean_msg = line
            if ":" in line:
                prefix, rest = line.split(":", 1)
                prefix_clean = prefix.lower().strip()
                desc = rest.strip()
                if desc:
                    desc = desc[0].upper() + desc[1:]

                if prefix_clean.startswith("feat"):
                    categories["Added"].append(f"**{prefix.strip()}**: {desc}")
                elif prefix_clean.startswith("fix"):
                    categories["Fixed"].append(f"**{prefix.strip()}**: {desc}")
                else:
                    categories["Changed"].append(f"**{prefix.strip()}**: {desc}")
            else:
                categories["Changed"].append(clean_msg)

    except Exception:
        pass

    return categories


def append_changelog_entry(new_version: str, dry_run: bool = False) -> None:
    """Appends a new categorized version entry header to CHANGELOG.md if not already present."""
    if not CHANGELOG_FILE.exists():
        return

    today_str = date.today().isoformat()
    entry_header = f"## [{new_version}] - {today_str}"

    content = CHANGELOG_FILE.read_text(encoding="utf-8")
    if entry_header in content:
        return

    # Extract categorized commits
    groups = extract_categorized_git_commits()
    sections: list[str] = []

    if groups["Added"]:
        sections.append("### Added\n" + "\n".join(f"- {item}" for item in groups["Added"]))
    if groups["Fixed"]:
        sections.append("### Fixed\n" + "\n".join(f"- {item}" for item in groups["Fixed"]))
    if groups["Changed"]:
        sections.append("### Changed\n" + "\n".join(f"- {item}" for item in groups["Changed"]))

    if not sections:
        body = "### Changed\n- Maintenance updates, routine site improvements, and verified CI/CD releases."
    else:
        body = "\n\n".join(sections)

    changelog_chunk = f"{entry_header}\n\n{body}\n"

    if dry_run:
        print(f"[DRY-RUN] Would prepend changelog entry:\n{changelog_chunk}")
        return

    # Insert after '---'
    if "---" in content:
        parts = content.split("---", 1)
        new_content = f"{parts[0]}---\n\n{changelog_chunk}\n{parts[1].lstrip()}"
        CHANGELOG_FILE.write_text(new_content, encoding="utf-8")


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry_run = "--dry-run" in sys.argv

    action = args[0] if args else "current"

    current = get_current_version()

    if action == "current":
        print(current)
        return

    if action == "auto":
        bump_type = detect_bump_type_from_git()
        print(f"Auto-detected bump type based on git history: '{bump_type}'")
    elif action in ("patch", "minor", "major"):
        bump_type = action
    elif action == "set" and len(args) > 1:
        bump_type = f"set:{args[1]}"
    else:
        print(f"Usage: {sys.argv[0]} [current|patch|minor|major|auto|set <ver>] [--dry-run]")
        sys.exit(1)

    next_ver = calculate_next_version(current, bump_type)
    print(f"Version bump: {current} -> {next_ver} (mode: {bump_type})")

    sync_version_files(next_ver, dry_run=dry_run)
    append_changelog_entry(next_ver, dry_run=dry_run)

    if not dry_run:
        print(f"✔ Successfully synchronized version {next_ver} across repository files.")


if __name__ == "__main__":
    main()
