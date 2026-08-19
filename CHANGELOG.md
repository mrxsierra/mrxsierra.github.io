# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.7.0] - 2026-08-19

### Added
- **Dual-Depth Portfolio Project Template (`docs/templates/project-template.md`)**: High-converting case study blueprint featuring 3-metric executive stat cards, Mermaid system architecture flows, trade-off decision matrices, curated 20-line code highlights, automated verification benchmarks, and client inbound CTA.
- **Viral Engineering Blog Template (`docs/templates/blog-template.md`)**: Thought-leadership article template with provocative hooks, 30-second TL;DR cards, visual mental models, "Do This, Not That" diffs, production gotchas, and quotable takeaway summary cheat sheets.
- **Content Authoring & Cross-Platform Distribution Standards**: Added Section 4 in `CONTRIBUTING.md` outlining multi-audience alignment and specific distribution frameworks for X (Twitter) threads, LinkedIn stories, Dev.to/Medium syndication, and Reddit technical discussions.

### Changed
- **Styling Standardization**: Replaced legacy inline styling across project case studies, article series banners, and contact portal with shared CSS helper classes in `docs/stylesheets/index.css`.
- **Site Exclusions**: Excluded `templates/` directory from public MkDocs navigation and build output (`mkdocs.yml`).


## [0.6.0] - 2026-08-19

### Added
- **Publication Reading Standards**: Refined editorial line-height, typographic hierarchy, and responsive margins across engineering deep dives and case studies.
- **Native Mermaid Rendering**: Enabled responsive client-side Mermaid diagram rendering for system architectures and data flow charts.
- **Page-Scoped Developer Action Bar**: Positioned top-right action suite featuring "View Source", "Suggest Edit", and "Copy Raw Markdown".


## [0.5.0] - 2026-08-19

### Added
- **Segmented Pill Developer Control Bar**: Replaced standalone floating buttons with an integrated, high-contrast segmented pill control bar in the top-right header area.
- **Mobile Viewport Standardization**: Optimized touch target boundaries, typography scaling, and overflow containment on mobile devices.


## [0.4.0] - 2026-08-19

### Added
- **4-Button Page-Scoped Developer Suite**: Added interactive actions to top-right content area for direct GitHub repository linking, raw source view, and issue templates.


## [0.3.1] - 2026-08-18

### Added
- **"View Page Source" & "Suggest Edit" Developer Action Bar**: Added direct GitHub markdown source inspection (`btn-view-source`) and collaborative editing links on all content pages.
- **Machine-Readable Version Metadata**: Added `<meta name="version">` and `<meta name="docsearch:version">` tags across all site pages for automated tooling and search indexing.
- **Monotonic SemVer Tag Fallback**: Enhanced `bump_version.py` to continuously reference the highest remote Git tag, ensuring clean version progression across parallel and sequential releases.

### Fixed
- **LLM Knowledge Base Version Header**: Injected standardized `# Version: vX.Y.Z` metadata header into `llms-full.txt`.
- **GitHub Actions Release Push**: Corrected automated branch push target to `origin HEAD:main` in the CI/CD deploy stage.


## [0.3.0] - 2026-08-18

### Added
- **Dual-Tier Automated Release Architecture**: Fully automated Minor and Patch SemVer bumping, changelog categorization, and release tagging in GitHub Actions CI/CD upon PR merge, with full local support for intentional Major releases (`make bump-major`).
- **Structured Conventional Commit Changelog Extraction**: Enhanced version bumper to automatically parse commit messages into `### Added` (`feat:`), `### Fixed` (`fix:`), and `### Changed` sections.


## [0.2.1] - 2026-08-18

### Added
- **View Page Source Developer Action**: Added direct markdown source inspection button on all content pages.
- **Machine-Readable Version Metadata**: Added `<meta name="version">` and `<meta name="docsearch:version">` tags across all site pages for search indexing and automated tooling.

### Fixed
- **Monotonic SemVer Tag Fallback**: Resolved version fallback logic during rapid tag increments.


## [0.2.0] - 2026-08-18

### Added
- **Official Geometric Brand System & Engine**: Automated vector compilation pipeline (`scripts/brand_engine/`) generating SVG monograms, horizontal/stacked lockups, multi-density favicons, YouTube/broadcast watermarks, and master press kit archive (`mrxsierra-brand-press-kit.zip`).
- **Brand Standards & Press Kit Portals**: Added dedicated [`/brand/`](https://mrxsierra.github.io/brand/) and [`/press/`](https://mrxsierra.github.io/press/) portals featuring vector mark downloads, video templates, authorized speaker bios, and design system tokens.
- **FontAwesome 6.7.2 Integration**: Upgraded global icon CDN to FontAwesome 6.7.2, providing native vector support for `fa-brands fa-x-twitter` across the header, developer profile cards, and share widget.
- **Brand Kit Automated Test Suite**: Added 11 automated pytest assertions (`tests/test_brand_kit.py`) verifying vector integrity, favicon bundles, watermarks, banner dimensions, and press kit archive structure (bringing the test suite to 49 assertions).

### Changed
- **Elevated Brand Authority Navigation Hierarchy**: Restructured primary site navigation by nesting `Resume & Credentials` under the `About` dropdown (`Profile & Bio`, `Resume & Credentials`, `Press Kit`, `Brand Standards`, `Release Changelog`), streamlining the main header tabs into authoritative categories.
- **Footer Brand Monogram Integration**: Replaced text placeholder with the official constructivist vector SVG mark inside the 4-column footer directory.
- **Landing Page & Profile Card Polish**: Cleaned homepage `#connect` card by isolating AI machine endpoints to the global footer directory and suppressed git contributor boxes on the landing page hero.


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
