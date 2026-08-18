# mrxsierra.github.io

[![Version](https://img.shields.io/badge/version-0.0.1-blue?style=flat)](VERSION)
[![CI/CD Pipeline](https://github.com/mrxsierra/mrxsierra.github.io/actions/workflows/ci.yml/badge.svg)](https://github.com/mrxsierra/mrxsierra.github.io/actions/workflows/ci.yml)
[![Site Status](https://img.shields.io/badge/Site-Live-2ea44f?style=flat&logo=github)](https://mrxsierra.github.io/)
[![Standard: llms.txt](https://img.shields.io/badge/Standard-llms.txt-blue?style=flat)](https://mrxsierra.github.io/llms.txt)
[![Tests](https://img.shields.io/badge/Tests-Pytest-yellow?style=flat&logo=pytest)](tests/)
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
| `make verify` | Run full pre-commit pipeline (Ruff, Mypy, MkDocs strict, Pytest) |
| `make test` | Run automated pytest suite (smoke, link checker, HTML integrity) |
| `make lint` | Run Ruff linter and format validation |
| `make format` | Auto-format Python code and fix lint issues |
| `make typecheck` | Run Mypy static type analysis on hooks and tests |
| `make version` | Display current SemVer version from `VERSION` |
| `make bump-patch` | Increment patch version (`0.0.X`) for fixes/chores |
| `make bump-minor` | Increment minor version (`0.X.0`) for feature releases |
| `make bump-major` | Increment major version (`X.0.0`) for major overhauls |
| `make build` | Build static production site to `site/` with `--strict` |
| `make hook-install` | Configure local git pre-commit verification hook |

---

## 🏗️ Architecture & Technology Stack

- **Static Site Engine**: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **Build Hooks**: Custom Python pre-build lifecycle hooks (`hooks/generate_ai_docs.py`) generating [`llms.txt`](https://mrxsierra.github.io/llms.txt) and [`llms-full.txt`](https://mrxsierra.github.io/llms-full.txt) per [llmstxt.org](https://llmstxt.org) standard.
- **Verification Engine**: Automated multi-tier testing via `pytest`, `beautifulsoup4`, `ruff`, and `mypy`.
- **CI/CD Automation**: Multi-stage GitHub Actions pipeline (`.github/workflows/ci.yml`) with PR validation gating and automated GitHub Pages deployment.

---

## 📖 Contributing & SDLC Guidelines

For development workflows, project layout details, link resolution rules, and agent conventions, see the **[Contributor & Agent Engineering Guide (CONTRIBUTING.md)](CONTRIBUTING.md)**.

---

## 📄 License

© 2025 Sunil Sharma ([@mrxsierra](https://github.com/mrxsierra)). All rights reserved.