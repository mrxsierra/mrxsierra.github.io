#!/usr/bin/env python3
"""
mrxsierra.github.io - Git Hook Installer
Installs local git pre-commit hooks to automate verification before committing.
"""

import os
import stat
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GIT_HOOKS_DIR = PROJECT_ROOT / ".git" / "hooks"
SOURCE_HOOK = PROJECT_ROOT / ".githooks" / "pre-commit"
TARGET_HOOK = GIT_HOOKS_DIR / "pre-commit"


def install() -> None:
    if not (PROJECT_ROOT / ".git").exists():
        print("Error: .git directory not found. Not a git repository.")
        sys.exit(1)

    if not SOURCE_HOOK.exists():
        print(f"Error: Source hook {SOURCE_HOOK} does not exist.")
        sys.exit(1)

    # Make source hook executable
    st_src = os.stat(SOURCE_HOOK)
    os.chmod(SOURCE_HOOK, st_src.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

    # Configure git to use .githooks directory
    try:
        subprocess.run(
            ["git", "config", "core.hooksPath", ".githooks"],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
        )
        print("✔ Configured git hooks path: 'git config core.hooksPath .githooks'")
        print("Pre-commit verification will now run automatically on every 'git commit'.")
        return
    except Exception:
        pass

    # Fallback to copying into .git/hooks/pre-commit
    try:
        GIT_HOOKS_DIR.mkdir(parents=True, exist_ok=True)
        content = SOURCE_HOOK.read_text(encoding="utf-8")
        TARGET_HOOK.write_text(content, encoding="utf-8")
        st = os.stat(TARGET_HOOK)
        os.chmod(TARGET_HOOK, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
        print("✔ Git pre-commit hook installed into .git/hooks/pre-commit")
    except Exception as e:
        print(f"Notice: Could not write directly to .git/hooks ({e}).")
        print("You can enable hooks manually anytime by running:")
        print("  git config core.hooksPath .githooks")


if __name__ == "__main__":
    install()
