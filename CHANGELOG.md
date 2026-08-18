# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.0.1] - 2026-08-17

### Added
- Enterprise-grade local verification test suite (`pytest`, `beautifulsoup4`) covering smoke tests, DOM semantics, zero broken links, and template leak checks.
- Standalone 5-stage pre-commit verification engine (`scripts/verify.py`).
- Single source of truth versioning system starting at `0.0.1` (`VERSION`, `pyproject.toml`).
- Automated AI documentation generator lifecycle hook (`hooks/generate_ai_docs.py`) for `llms.txt` and `llms-full.txt` (llmstxt.org specification).
- Standardized developer shortcuts (`Makefile`) and Git pre-commit hook runner (`.githooks/pre-commit`).
- Modern GitHub Actions CI/CD pipeline (`.github/workflows/ci.yml`) with pull request gating, strict builds, and automated deployment.
- Contributor and AI coding agent guidelines (`CONTRIBUTING.md`).
- GitHub issue forms (`bug_report.yml`, `feature_request.yml`) and pull request template (`PULL_REQUEST_TEMPLATE.md`).
