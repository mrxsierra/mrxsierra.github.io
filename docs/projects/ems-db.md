---
date:
  created: 2024-04-10
  updated: 2025-03-15
tags:
  - Database Design
  - Database Management
  - PostgreSQL
  - MySQL
  - SQLite
  - Python
  - Docker
description: >
  Production-grade multi-RDBMS academic examination platform with cross-engine parity across PostgreSQL, MySQL, and SQLite, Python automation, and Dockerized test workflows.
---

# Examination Management System DB

<div class="project-header-card">
  <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px;">
    <div>
      <span class="project-category-badge">Database Architecture • Multi-RDBMS Parity</span>
      <h2 style="margin: 6px 0 0 0; font-size: 22px; font-weight: 700;">Examination Management System Database</h2>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
      <a href="https://github.com/mrxsierra/ems-db" target="_blank" rel="noopener" class="btn btn-primary">
        <i class="fab fa-github"></i> Repository
      </a>
      <a href="https://youtu.be/CRT4_j3kZes" target="_blank" rel="noopener" class="btn btn-secondary">
        <i class="fab fa-youtube"></i> Video Walkthrough
      </a>
    </div>
  </div>

  <div class="project-meta-grid">
    <div class="project-meta-item">
      <span class="project-meta-label">Role</span>
      <span class="project-meta-val">Sole Database Architect &amp; Developer</span>
    </div>
    <div class="project-meta-item">
      <span class="project-meta-label">Supported Engines</span>
      <span class="project-meta-val">PostgreSQL 17, MySQL 8.4, SQLite 3</span>
    </div>
    <div class="project-meta-item">
      <span class="project-meta-label">Automation Stack</span>
      <span class="project-meta-val">Python, Pytest, Docker Compose, UV</span>
    </div>
    <div class="project-meta-item">
      <span class="project-meta-label">Accreditation</span>
      <span class="project-meta-val">Harvard CS50 SQL with Distinction</span>
    </div>
  </div>

  <div class="project-impact-box">
    <i class="fas fa-database"></i>
    <span><strong>Multi-Engine Consistency:</strong> 100% trigger and relational logic parity validated across PostgreSQL, MySQL, and SQLite using automated pytest test benches.</span>
  </div>
</div>

## Architecture &amp; Parity Pipeline

```mermaid
graph TD
    A["Relational Requirements &amp; ER Modeling"] --> B["Multi-Dialect DDL Schemas"]
    B --> C1["PostgreSQL (PL/pgSQL Functions)"]
    B --> C2["MySQL (Delimiter Triggers)"]
    B --> C3["SQLite (Embedded Triggers &amp; CHECKs)"]
    C1 --> D["Containerized Docker Environments"]
    C2 --> D
    C3 --> D
    D --> E["Automated Python Automation ('db.py')"]
    E --> F["Pytest Verification Test Harnesses"]
    F --> G["Materialized Analytical Reporting Views"]
```

## Executive Overview

The **Examination Management System (EMS DB)** project is a modular, production-ready relational database architecture designed to administer educational examinations. It models students, proctors, tests, dynamic question banks, timed test sessions, audit events, and computed academic scores.

The architecture was engineered with strict **multi-RDBMS parity**: the system maintains three synchronized dialect implementations (**PostgreSQL**, **MySQL**, and **SQLite**) with automated Python test harnesses validating identical business logic execution across all three engines.

## Technical Challenges &amp; Architectural Solutions

### 1. Multi-Engine Relational &amp; Trigger Parity
- **Challenge:** Differences in dialect features (PL/pgSQL trigger functions vs MySQL delimiters vs SQLite embedded triggers) risked behavioral discrepancies.
- **Solution:** Designed modular directory hierarchies (`/psql`, `/mysql`, `/sqlite`) with corresponding migration scripts, automating query testing via engine-specific Python drivers (`psycopg2`, `mysql-connector-python`, `sqlite3`).

### 2. Temporal Logic &amp; Session Auto-Termination
- **Challenge:** Dynamically computing test session termination timestamps without race conditions.
- **Solution:** Implemented engine-native triggers (`set_end_for_test_session`) calculating interval arithmetic directly at write time based on test duration configurations.

### 3. Reporting Query Optimization
- **Challenge:** Heavy joins across student records, question options, and audit history caused query latency.
- **Solution:** Created targeted composite indexes and encapsulated analytical reporting logic into optimized SQL views (`tests_history`, `summary_reports`).

## Verified Accreditation

<div style="max-width: 650px; margin: 20px 0;">
  <a href="../../cert/1713864822125-cs50s.jpeg" class="glightbox" data-gallery="certs" data-title="Harvard CS50 SQL Certificate">
    <img src="../../cert/1713864822125-cs50s.jpeg" alt="Harvard CS50 SQL Certificate" style="border-radius: 8px; border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);" loading="lazy">
  </a>
  <p style="font-size: 12.5px; color: var(--color-text-muted); margin-top: 6px; text-align: center;">
    Harvard CS50 SQL: Introduction to Databases with SQL • Harvard University (CS50)
  </p>
</div>

## Entity Relationship Architecture

<div style="max-width: 800px; margin: 20px 0;">
  <a href="https://raw.githubusercontent.com/mrxsierra/ems-db/main/assets/erDiagram.png" class="glightbox" data-gallery="ems" data-title="Examination Management System ER Diagram">
    <img src="https://raw.githubusercontent.com/mrxsierra/ems-db/main/assets/erDiagram.png" alt="EMS DB ER Diagram" style="border-radius: 8px; border: 1px solid var(--color-border);" loading="lazy">
  </a>
</div>

## Related Technical Deep Dives

- [**Navigating the Nuances: A Developer's Guide to SQL Dialects**](../blog/posts/1-schema-diff.md): Deep dive into DDL differences, autoincrement sequence strategies, and trigger syntax across SQLite, MySQL, and PostgreSQL.
- [**Beyond the Schema: Querying, CLI Interaction, &amp; Docker Nuances**](../blog/posts/2-query-interaction-diff.md): Practical patterns for script piping, container networking, and auto-increment resets.

<!-- Sequential Case Study Navigation -->
<div class="project-nav-footer">
  <a href="../gstn-pbc/" class="project-nav-card">
    <span class="project-nav-dir"><i class="fas fa-arrow-left"></i> Previous Project</span>
    <span class="project-nav-title">GSTN Predictive Binary Classification</span>
  </a>
  <a href="../s3-faker/" class="project-nav-card" style="text-align: right;">
    <span class="project-nav-dir" style="justify-content: flex-end;">Next Project <i class="fas fa-arrow-right"></i></span>
    <span class="project-nav-title">S3 Faker Mock Data Generator</span>
  </a>
</div>
