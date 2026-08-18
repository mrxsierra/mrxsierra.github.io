#!/usr/bin/env python3
"""
mrxsierra.github.io - Production Verification Engine
Executes complete pre-commit verification pipeline:
  1. Lint checks (ruff)
  2. Format checks (ruff format)
  3. Type checks (mypy)
  4. Strict MkDocs build (mkdocs build --strict)
  5. Verification test suite (pytest tests/)
"""

import subprocess
import sys
import time
from pathlib import Path

# Terminal ANSI styling
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def find_binary(name: str) -> str:
    """Finds binary in .venv or falls back to PATH."""
    venv_bin = PROJECT_ROOT / ".venv" / "bin" / name
    if venv_bin.exists():
        return str(venv_bin)
    return name


def run_step(step_num: int, title: str, cmd: list[str]) -> bool:
    """Runs a single verification step and prints formatted status."""
    print(f"\n{BOLD}{CYAN}[Step {step_num}] {title}{RESET}")
    print(f"  {YELLOW}Command:{RESET} {' '.join(cmd)}")
    start_time = time.time()

    result = subprocess.run(
        cmd,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    elapsed = time.time() - start_time

    if result.returncode == 0:
        print(f"  {GREEN}✔ PASSED{RESET} ({elapsed:.2f}s)")
        if result.stdout and "--verbose" in sys.argv:
            print(result.stdout)
        return True
    else:
        print(f"  {RED}✖ FAILED{RESET} (exit code: {result.returncode}, {elapsed:.2f}s)")
        if result.stdout:
            print(f"\n--- Standard Output ---\n{result.stdout.strip()}")
        if result.stderr:
            print(f"\n--- Standard Error ---\n{result.stderr.strip()}")
        return False


def main():
    print(f"{BOLD}======================================================{RESET}")
    print(f"{BOLD}  mrxsierra.github.io - Local Verification Pipeline   {RESET}")
    print(f"{BOLD}======================================================{RESET}")

    ruff_bin = find_binary("ruff")
    mypy_bin = find_binary("mypy")
    mkdocs_bin = find_binary("mkdocs")
    pytest_bin = find_binary("pytest")

    steps = [
        ("Code Linting (Ruff)", [ruff_bin, "check", "."]),
        ("Code Formatting (Ruff)", [ruff_bin, "format", "--check", "."]),
        ("Static Type Analysis (Mypy)", [mypy_bin, "hooks", "scripts", "tests"]),
        ("MkDocs Strict Build", [mkdocs_bin, "build", "--strict"]),
        ("Automated Test Suite (Pytest)", [pytest_bin, "tests/", "-v"]),
    ]

    all_passed = True
    start_all = time.time()

    for i, (title, cmd) in enumerate(steps, start=1):
        success = run_step(i, title, cmd)
        if not success:
            all_passed = False
            # If critical build or lint fails, abort early or continue based on preference
            if "--fail-fast" in sys.argv:
                break

    total_elapsed = time.time() - start_all
    print(f"\n{BOLD}======================================================{RESET}")
    if all_passed:
        print(f"{BOLD}{GREEN}✔ ALL VERIFICATION CHECKS PASSED ({total_elapsed:.2f}s){RESET}")
        print(f"{GREEN}Safe to commit and push to remote.{RESET}")
        print(f"{BOLD}======================================================{RESET}")
        sys.exit(0)
    else:
        print(f"{BOLD}{RED}✖ VERIFICATION CHECKS FAILED ({total_elapsed:.2f}s){RESET}")
        print(f"{RED}Please fix the highlighted errors before committing.{RESET}")
        print(f"{BOLD}======================================================{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
