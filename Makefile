.PHONY: help install serve build test lint format typecheck verify hook-install version bump-patch bump-minor bump-major brand clean

PYTHON ?= .venv/bin/python
RUFF ?= .venv/bin/ruff
MYPY ?= .venv/bin/mypy
MKDOCS ?= .venv/bin/mkdocs
PYTEST ?= .venv/bin/pytest

help:
	@echo "Available commands:"
	@echo "  make serve        - Start local MkDocs dev server"
	@echo "  make build        - Build site in strict mode"
	@echo "  make test         - Run pytest verification suite"
	@echo "  make lint         - Run ruff linter checks"
	@echo "  make format       - Format code using ruff"
	@echo "  make typecheck    - Run mypy static type checking"
	@echo "  make verify       - Run full verification pipeline (lint, types, build, tests)"
	@echo "  make brand        - Compile all vector marks, favicons, banners, and Press Kit"
	@echo "  make version      - Print current repository version"
	@echo "  make bump-patch   - Bump patch version (0.0.X)"
	@echo "  make bump-minor   - Bump minor version (0.X.0)"
	@echo "  make bump-major   - Bump major version (X.0.0)"
	@echo "  make hook-install - Install git pre-commit verification hook"
	@echo "  make clean        - Remove build artifacts and temporary cache"

serve:
	$(MKDOCS) serve

build:
	$(MKDOCS) build --strict

test:
	$(PYTEST) tests/ -v

lint:
	$(RUFF) check .
	$(RUFF) format --check .

format:
	$(RUFF) format .
	$(RUFF) check --fix .

typecheck:
	$(MYPY) hooks scripts tests

verify:
	$(PYTHON) scripts/verify.py

brand:
	$(PYTHON) scripts/brand_engine/cli.py --all

version:
	$(PYTHON) scripts/bump_version.py current

bump-patch:
	$(PYTHON) scripts/bump_version.py patch

bump-minor:
	$(PYTHON) scripts/bump_version.py minor

bump-major:
	$(PYTHON) scripts/bump_version.py major

hook-install:
	$(PYTHON) scripts/install_hooks.py

clean:
	rm -rf site/ .pytest_cache/ .mypy_cache/ .ruff_cache/
