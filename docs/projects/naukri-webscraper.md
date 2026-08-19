---
date:
  created: 2024-03-10
  updated: 2025-04-05
tags:
  - Python
  - Web Scraping
  - Selenium
  - Automation
  - Data Analysis
description: >
  Automated job market telemetry and data extraction pipeline using Selenium WebDriver, BeautifulSoup, and Pandas with comprehensive pytest test coverage.
---

# Naukri Market Data Scraper

<div class="project-header-card">
  <div class="project-header-top">
    <div>
      <span class="project-category-badge">Web Automation • Data Extraction</span>
      <h2 class="project-header-title">Naukri Market Telemetry Scraper</h2>
    </div>
    <div class="project-header-actions">
      <a href="https://github.com/mrxsierra/naukari-webscraper" target="_blank" rel="noopener" class="btn btn-primary">
        <i class="fab fa-github"></i> Repository
      </a>
      <a href="https://www.youtube.com/watch?v=ls_uxjfADN4" target="_blank" rel="noopener" class="btn btn-secondary">
        <i class="fab fa-youtube"></i> Video Demo
      </a>
    </div>
  </div>

  <div class="project-meta-grid">
    <div class="project-meta-item">
      <span class="project-meta-label">Role</span>
      <span class="project-meta-val">Sole Tooling Architect</span>
    </div>
    <div class="project-meta-item">
      <span class="project-meta-label">Core Engine</span>
      <span class="project-meta-val">Selenium WebDriver, Chrome Headless</span>
    </div>
    <div class="project-meta-item">
      <span class="project-meta-label">Data Pipeline</span>
      <span class="project-meta-val">Pandas Vectorized Filtering &amp; CSV Export</span>
    </div>
    <div class="project-meta-item">
      <span class="project-meta-label">Accreditation</span>
      <span class="project-meta-val">Harvard CS50P Python Programming</span>
    </div>
  </div>

  <div class="project-impact-box">
    <i class="fas fa-spider"></i>
    <span><strong>Resilient Automation:</strong> Extracts paginated job market telemetry (titles, salary bands, required skills, locations) with graceful fallback handling and pytest test benches.</span>
  </div>
</div>

## Architecture &amp; Scraping Flow

```mermaid
graph TD
    A["Target Search Query (Skills, Location, Experience)"] --> B["Headless Selenium Session Initialization"]
    B --> C["Explicit Polling with WebDriverWait"]
    C --> D["DOM Extraction &amp; Fallback Normalization ('get_text_or_default')"]
    D --> E["Pandas Multi-Criterion Skill Filtering"]
    E --> F["Structured CSV Telemetry Output"]
```

## Executive Overview

**Naukri Market Data Scraper** is a Python automation tool that extracts job listings from Naukri.com to facilitate programmatic tech hiring telemetry, salary benchmarking, and skill requirement analysis.

The scraper automates browser navigation across paginated listings, resolves asynchronously hydrated DOM components, normalizes inconsistent compensation notations, and filters results against user-defined skill matrices before exporting clean datasets for downstream analytics.

## Technical Challenges &amp; Architectural Solutions

### 1. Dynamic Client-Side Content Hydration
- **Challenge:** Target pages use asynchronous client-side JavaScript, causing standard static HTTP scrapers to fail due to DOM race conditions.
- **Solution:** Implemented explicit polling utilizing Selenium's `WebDriverWait` and expected conditions, ensuring DOM elements are fully hydrated prior to traversal.

### 2. Inconsistent DOM Schema Normalization
- **Challenge:** Varied markup across sponsored, promoted, and standard job card templates frequently resulted in `NoSuchElementException` crashes.
- **Solution:** Built fault-tolerant fallback parser helpers (`get_text_or_default`) that normalize missing fields to default values without halting the extraction pipeline.

### 3. Automated Regression Testing
- **Challenge:** Ensuring scraper parser logic remains resilient against minor frontend updates.
- **Solution:** Authored a complete test suite in `test_project.py` using `pytest`, featuring mocked DOM responses and fixture-driven parser validation.

## Verified Accreditation

<div class="media-container-650">
  <a href="../../cert/1708063772979-cs50p.jpeg" class="glightbox" data-gallery="certs" data-title="Harvard CS50P Certificate">
    <img src="../../cert/1708063772979-cs50p.jpeg" alt="Harvard CS50P Certificate" class="media-img-rounded" loading="lazy">
  </a>
  <p class="media-caption">
    Harvard CS50P: Introduction to Programming with Python • Harvard University (CS50)
  </p>
</div>

## Video Demonstration

<div class="media-container-650">
  <a href="https://www.youtube.com/watch?v=ls_uxjfADN4" target="_blank" rel="noopener">
    <img src="https://img.youtube.com/vi/ls_uxjfADN4/maxresdefault.jpg" alt="Video Demo Walkthrough" class="media-img-rounded" loading="lazy">
  </a>
</div>

<!-- Sequential Case Study Navigation -->
<div class="project-nav-footer">
  <a href="../paraxcel/" class="project-nav-card">
    <span class="project-nav-dir"><i class="fas fa-arrow-left"></i> Previous Project</span>
    <span class="project-nav-title">Paraxcel Document Toolkit</span>
  </a>
  <a href="../test-site/" class="project-nav-card nav-right">
    <span class="project-nav-dir dir-right">Next Project <i class="fas fa-arrow-right"></i></span>
    <span class="project-nav-title">Real-Time Test Management Interface</span>
  </a>
</div>
