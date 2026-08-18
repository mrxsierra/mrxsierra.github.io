---
title: Changelog & Release History
description: Release history, feature milestones, and automated changelog for mrxsierra.github.io.
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2026-08-18

### Added
- **Unified Developer Footer Navigation**: Bespoke 4-column engineering directory and dual-tile directional navigation (`md-footer__link`) with 1px neutral border framing, subtle hover elevation, topic pills, and directional chevrons.
- **Pinterest Domain Verification**: Global site verification metadata (`<meta name="p:domain_verify">`) and Pinterest profile integration under developer social channels.
- **Automated AI Knowledge Base Expansion**: Updated `llms.txt` and `llms-full.txt` endpoints with complete syndication, RSS feed directory, and release changelog sections.
- **Main Branch Protection Ruleset**: Automated GitHub Repository Ruleset enforcement (`Protect main branch`) requiring pull request reviews and passing CI status checks.

### Changed
- Refactored `hooks/generate_ai_docs.py` with content-differential caching (`write_if_changed`) to eliminate infinite reload loops during local `mkdocs serve`.
- Standardized editorial typography and project header meta cards across all 6 engineering case studies.


## [0.0.1] - 2026-08-17

### Added
- **Multi-Tier Automated Test Suite**: 38 pytest assertions across 6 test modules (`test_smoke.py`, `test_html_integrity.py`, `test_hooks.py`, `test_social_sharing.py`, `test_versioning.py`, `conftest.py`) verifying zero broken links, valid DOM semantics, and zero template leaks.
- **5-Stage Pre-Commit Engine**: CLI verification engine (`scripts/verify.py`) running Ruff lint, Ruff format, Mypy static analysis, MkDocs strict build, and Pytest.
- **Branch Protection & Governance**: Local `.githooks/pre-commit` guard preventing accidental direct commits on `main` and GitHub Repository Rulesets (`.github/rulesets/main-protection.json`).
- **Multi-Channel RSS Syndication**: Automated post-build hook (`hooks/generate_rss_feed.py`) generating W3C RSS 2.0 feeds (`feed.xml`, `feed_blog.xml`, `feed_projects.xml`) with RSS auto-discovery tags.
- **Responsive Social Sharing Widget**: 8-platform share component (`overrides/partials/social_share.html`, `docs/javascripts/index.js`, `docs/stylesheets/extra.css`) with copy-to-clipboard toast feedback.
- **Single Source of Truth SemVer**: Root `VERSION` file (`0.0.1`) synchronized with `pyproject.toml`, `mkdocs.yml`, and auto-generated `docs/changelog.md` via `scripts/bump_version.py`.
- **Persistent Footer Version Tag**: Clean interactive version pill in `overrides/partials/copyright.html` linking directly to `/changelog/`.
- **AI Documentation Endpoints**: Pre-build hook (`hooks/generate_ai_docs.py`) generating [`llms.txt`](https://mrxsierra.github.io/llms.txt) and [`llms-full.txt`](https://mrxsierra.github.io/llms-full.txt) following the llmstxt.org standard.
- **GitHub Workflow Automation**: Multi-stage CI/CD pipeline (`.github/workflows/ci.yml`), issue forms (`bug_report.yml`, `feature_request.yml`), and PR template (`PULL_REQUEST_TEMPLATE.md`).
