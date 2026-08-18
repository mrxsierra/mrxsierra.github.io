# mrxsierra.github.io

[![Version](https://img.shields.io/badge/version-0.2.0-blue?style=flat)](VERSION)
[![CI/CD Pipeline](https://github.com/mrxsierra/mrxsierra.github.io/actions/workflows/ci.yml/badge.svg)](https://github.com/mrxsierra/mrxsierra.github.io/actions/workflows/ci.yml)
[![Site Status](https://img.shields.io/badge/Site-Live-2ea44f?style=flat&logo=github)](https://mrxsierra.github.io/)
[![Standard: llms.txt](https://img.shields.io/badge/Standard-llms.txt-blue?style=flat)](https://mrxsierra.github.io/llms.txt)
[![Tests](https://img.shields.io/badge/Tests-49%20Passed-brightgreen?style=flat&logo=pytest)](tests/)
[![Code Style](https://img.shields.io/badge/Code%20Style-Ruff-000000?style=flat&logo=ruff)](https://github.com/astral-sh/ruff)

> Personal portfolio, technical case studies, and engineering blog of **Sunil Sharma (@mrxsierra)**.  
> Live site: **[https://mrxsierra.github.io/](https://mrxsierra.github.io/)**

---

## ⚡ Quickstart

```bash
# 1. Start local dev server (live reload at http://127.0.0.1:8000)
make serve

# 2. Run full 5-stage pre-commit verification pipeline
make verify

# 3. Build static site in strict mode
make build
```

---

## 🛠️ Command Matrix

| Command | Purpose |
| :--- | :--- |
| `make serve` | Start local MkDocs preview server with live reload |
| `make verify` | Run full 5-stage pre-commit pipeline (Ruff, Mypy, MkDocs strict, Pytest) |
| `make test` | Run full 49-test automated pytest verification suite |
| `make lint` | Run Ruff linter and format validation |
| `make format` | Auto-format Python code and fix lint issues |
| `make typecheck` | Run Mypy static type analysis on hooks, scripts, and tests |
| `make version` | Display current SemVer version from `VERSION` |
| `make bump-patch` | Increment patch version (`0.X.Y`) for fixes/chores |
| `make bump-minor` | Increment minor version (`0.X.0`) for feature releases |
| `make bump-major` | Increment major version (`X.0.0`) for major overhauls |
| `make build` | Build static production site to `site/` with `--strict` |
| `make hook-install` | Configure local git pre-commit verification and branch guard |

---

## 🏗️ Architecture & Technology Stack

- **Static Site Engine**: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) with custom overrides (`overrides/`)
- **Brand System & Press Engine**: Automated vector compilation pipeline (`scripts/brand_engine/`) for multi-density icons, banners, watermarks, and press packages.
- **Build Hooks & Automation**:
  - `hooks/generate_ai_docs.py`: Pre-build hook generating [`llms.txt`](https://mrxsierra.github.io/llms.txt), [`llms-full.txt`](https://mrxsierra.github.io/llms-full.txt), and syncing [`docs/changelog.md`](https://mrxsierra.github.io/changelog/).
  - `hooks/generate_rss_feed.py`: Post-build hook generating W3C RSS 2.0 multi-channel feeds (`feed.xml`, `feed_blog.xml`, `feed_projects.xml`).
- **Interactive UI Components**:
  - 8-platform responsive social sharing widget (`overrides/partials/social_share.html`) with copy-to-clipboard toast.
  - Persistent footer version badge linking to `/changelog/`.
- **Verification Engine**: 49 automated test cases via `pytest`, `beautifulsoup4`, `ruff`, and `mypy` (`scripts/verify.py`).
- **Governance & CI/CD**:
  - GitHub Actions CI/CD (`.github/workflows/ci.yml`) with automated tagging on deployment.
  - Branch protection rulesets (`.github/rulesets/main-protection.json`) and local pre-commit branch guards (`.githooks/pre-commit`).

---

## 📖 Contributing & SDLC Guidelines

For development workflows, project layout details, link resolution rules, and agent conventions, see the **[Contributor & Agent Engineering Guide (CONTRIBUTING.md)](CONTRIBUTING.md)**.

---

## 📄 License

© 2025 Sunil Sharma ([@mrxsierra](https://github.com/mrxsierra)). All rights reserved.