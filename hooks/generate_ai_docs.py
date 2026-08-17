"""
Automated AI & Machine-Readable Documentation Generator for MkDocs.
Automatically regenerates llms.txt, llms-full.txt, and root llms.txt on every build/serve.
Strips presentation HTML tags to provide clean, pure-markdown ingestion for AI agents.
"""

import os
import re
import html

def clean_html_to_markdown(raw_text: str) -> str:
    """Converts HTML markup to clean, pure Markdown text for machine ingestion."""
    text = raw_text
    
    # 1. Strip YAML frontmatter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]
            
    # 2. Remove HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    
    # 3. Convert HTML Headings to Markdown
    text = re.sub(r"<h1[^>]*>(.*?)</h1>", r"\n# \1\n", text, flags=re.DOTALL|re.IGNORECASE)
    text = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", text, flags=re.DOTALL|re.IGNORECASE)
    text = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", text, flags=re.DOTALL|re.IGNORECASE)
    text = re.sub(r"<h4[^>]*>(.*?)</h4>", r"\n#### \1\n", text, flags=re.DOTALL|re.IGNORECASE)
    
    # 4. Convert HTML Images <img src="..." alt="..."> to ![alt](src)
    def img_replace(match):
        tag = match.group(0)
        src = re.search(r'src=["\']([^"\']+)["\']', tag)
        alt = re.search(r'alt=["\']([^"\']+)["\']', tag)
        s = src.group(1) if src else ""
        a = alt.group(1) if alt else "Image"
        return f"![{a}]({s})"
    text = re.sub(r"<img[^>]+>", img_replace, text, flags=re.IGNORECASE)
    
    # 5. Convert HTML Links <a href="...">text</a> to [text](href)
    def link_replace(match):
        href = match.group(1)
        inner = match.group(2)
        clean_inner = re.sub(r"<[^>]+>", "", inner).strip()
        if not clean_inner:
            clean_inner = href
        return f"[{clean_inner}]({href})"
    text = re.sub(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', link_replace, text, flags=re.DOTALL|re.IGNORECASE)
    
    # 6. Convert inline styling tags
    text = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", text, flags=re.DOTALL|re.IGNORECASE)
    text = re.sub(r"<b[^>]*>(.*?)</b>", r"**\1**", text, flags=re.DOTALL|re.IGNORECASE)
    text = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", text, flags=re.DOTALL|re.IGNORECASE)
    text = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", text, flags=re.DOTALL|re.IGNORECASE)
    
    # 7. Strip ALL remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    
    # 8. Remove caption blocks /// caption ... ///
    text = re.sub(r"///\s*caption.*?///", "", text, flags=re.DOTALL)
    
    # 9. Decode HTML entities and clean whitespace
    text = html.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def build_ai_docs():
    docs_dir = "docs"
    if not os.path.exists(docs_dir):
        return

    # 1. Generate llms.txt (High-level index)
    llms_index_content = """# Sunil Sharma (mrxsierra) — AI & Full-Stack Systems Portfolio
> Standard: llmstxt.org Specification. High-density machine-readable index for LLMs, autonomous coding agents, and search engines.

## Developer Overview
- **Name**: Sunil Sharma
- **Handle**: @mrxsierra
- **Title**: Full-Stack & AI Systems Specialist
- **Website**: https://mrxsierra.github.io/
- **GitHub**: https://github.com/mrxsierra
- **Primary Specializations**: Autonomous Agent Architectures, Multi-RDBMS Database Engineering (PostgreSQL, MySQL, SQLite), Machine Learning Competition Pipelines, Cloud Tooling (AWS S3, LocalStack, Docker).

## Verified Accreditations & Credentials
- **GSTN National Hackathon Finalist**: Goods and Services Tax Network (GSTN) • Machine Learning Predictive Binary Classification (900K+ records)
- **Harvard CS50x**: Introduction to Computer Science • C, Python, SQL, Memory Management & Data Structures
- **Harvard CS50 SQL**: Introduction to Databases with SQL • Normalization, Views, Triggers, Optimization
- **Harvard CS50P**: Introduction to Programming with Python • OOP, Pytest, Regex, Package Architecture
- **IIRS (ISRO)**: AI/ML for Geospatial Data Analysis • Machine Learning & Spatial Data Science

---

## Featured Engineering Projects

- [GSTN Predictive Binary Classification](https://mrxsierra.github.io/projects/gstn-pbc/): National-level hackathon finalist machine learning pipeline analyzing 900,000+ real-world GST records. Implemented XGBoost, LightGBM, Random Under-Sampling, and SHAP explainability.
- [Examination Management System DB (EMS DB)](https://mrxsierra.github.io/projects/ems-db/): Production-grade multi-RDBMS architecture with parity across PostgreSQL, MySQL, and SQLite. Features automated Python database migrations, Docker Compose isolation, and GitHub Actions CI validation.
- [S3 Faker Mock Data Generator](https://mrxsierra.github.io/projects/s3-faker/): Developer-first high-throughput synthetic dataset generator with native Amazon S3 and LocalStack emulator support.
- [Paraxcel Document Toolkit](https://mrxsierra.github.io/projects/paraxcel/): High-performance DOCX-to-Excel tabular extraction engine with Pydantic validation and Tkinter desktop GUI.
- [Naukri Market Data Scraper](https://mrxsierra.github.io/projects/naukri-webscraper/): Resilient Selenium & BeautifulSoup web scraping engine with pytest test benches and Pandas export for tech hiring telemetry.
- [Real-Time Test Management Interface](https://mrxsierra.github.io/projects/test-site/): Dynamic client-side test taking application with session serialization and responsive UI.

---

## Technical Articles & Architecture Deep Dives

- [Navigating the Nuances: A Developer's Guide to SQL Dialects (SQLite, MySQL, PostgreSQL)](https://mrxsierra.github.io/blog/2025/05/07/navigating-the-nuances-a-developers-guide-to-sql-dialects-sqlite-mysql-postgresql/): Comprehensive breakdown of SQL dialect differences across DDL, triggers, data types, and index strategies.
- [Beyond the Schema: A Practical Guide to Querying and Interacting with SQLite, MySQL, & PostgreSQL](https://mrxsierra.github.io/blog/2025/05/07/beyond-the-schema-a-practical-guide-to-querying-and-interacting-with-sqlite-mysql--postgresql/): Practical patterns for CLI interaction, Dockerized connection debugging, and Python multi-database automation.

---

## Full Knowledge Base
- [Full Text Knowledge Base (llms-full.txt)](https://mrxsierra.github.io/llms-full.txt): Complete concatenated raw markdown containing full project architectures, schema scripts, and guides in a single file for direct prompt context injection.
"""

    with open("docs/llms.txt", "w", encoding="utf-8") as f:
        f.write(llms_index_content)
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(llms_index_content)

    # 2. Generate llms-full.txt (Concatenated clean knowledge base)
    files_to_bundle = [
        ('docs/index.md', 'Overview & Developer Profile'),
        ('docs/about.md', 'Background & Education'),
        ('docs/resume.md', 'Verified Accreditations & Credentials'),
        ('docs/projects/gstn-pbc.md', 'Case Study: GSTN Predictive Binary Classification'),
        ('docs/projects/ems-db.md', 'Case Study: Examination Management System DB'),
        ('docs/projects/s3-faker.md', 'Case Study: S3 Faker Mock Data Generator'),
        ('docs/projects/paraxcel.md', 'Case Study: Paraxcel Document Toolkit'),
        ('docs/projects/naukri-webscraper.md', 'Case Study: Naukri Market Data Scraper'),
        ('docs/projects/test-site.md', 'Case Study: Real-Time Test Management Interface'),
        ('docs/blog/posts/1-schema-diff.md', 'Technical Guide: Navigating SQL Dialects'),
        ('docs/blog/posts/2-query-interaction-diff.md', 'Technical Guide: Beyond the Schema (Querying & Docker)'),
    ]

    output_lines = [
        '# Sunil Sharma (mrxsierra) — Full Technical Knowledge Base',
        '# Standard: llmstxt.org Full Ingestion Format',
        '# Website: https://mrxsierra.github.io/',
        '# Source: https://github.com/mrxsierra/mrxsierra.github.io',
        '',
        '=' * 80,
        ''
    ]

    for filepath, title in files_to_bundle:
        if os.path.exists(filepath):
            output_lines.append(f'## SECTION: {title}')
            output_lines.append(f'## Path: {filepath}')
            output_lines.append('-' * 80)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                cleaned = clean_html_to_markdown(content)
                output_lines.append(cleaned)
            output_lines.append('')
            output_lines.append('=' * 80)
            output_lines.append('')

    with open('docs/llms-full.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

def on_pre_build(config, **kwargs):
    """MkDocs hook triggered before build starts."""
    try:
        build_ai_docs()
    except Exception as e:
        print(f"[AI-Docs Hook] Warning: {e}")

if __name__ == "__main__":
    build_ai_docs()
    print("AI documentation generated successfully.")
