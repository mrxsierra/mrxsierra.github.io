"""
Brand Engine Configuration (Single Source of Truth).
Modify values here to customize colors, titles, bios, or paths across all generated brand assets.
"""

from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
ASSETS_DIR = DOCS_DIR / "assets"
BRAND_DIR = ASSETS_DIR / "brand"
IMG_DIR = ASSETS_DIR / "img"
VIDEO_DIR = BRAND_DIR / "video"
BANNERS_DIR = BRAND_DIR / "banners"
ARTICLES_DIR = BRAND_DIR / "articles"
SOCIAL_DIR = BRAND_DIR / "social"
DECKS_DIR = BRAND_DIR / "decks"
AVATAR_PATH = ASSETS_DIR / "mrxss_400x400.jpg"

BRAND_CONFIG = {
    # Core Identity
    "name": "Sunil Sharma",
    "handle": "mrxsierra",
    "domain": "https://mrxsierra.github.io",
    "github": "https://github.com/mrxsierra",
    "twitter": "@mrxsierra",
    "title": "Full-Stack Architect • Machine Learning Systems Specialist",
    "tagline": "Autonomous Agents • Distributed Databases • Production Verification",
    # Design Tokens & Palette
    "colors": {
        "obsidian": "#08090D",
        "surface": "#18181B",
        "border": "#27272A",
        "border_subtle": "#3F3F46",
        "accent": "#6366F1",
        "accent_glow": "#818CF8",
        "accent_muted": "#A5B4FC",
        "white": "#FFFFFF",
        "text_secondary": "#CBD5E1",
        "text_muted": "#94A3B8",
    },
    # Typography
    "typography": {
        "display": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
        "code": "'JetBrains Mono', 'Fira Code', monospace",
    },
    # Standard Media Bios
    "bios": {
        "one_liner": "Sunil Sharma (mrxsierra) is a Full-Stack Web Architect and Machine Learning Systems Engineer.",
        "short_50": "Sunil Sharma is a Full-Stack Systems Engineer and ML Specialist based in India. He builds robust multi-RDBMS data platforms, autonomous AI agent pipelines, and high-throughput automation tooling with Python, PostgreSQL, and modern web frameworks.",
        "full_100": "Sunil Sharma (mrxsierra) is a software engineer specializing in autonomous agent workflows, machine learning pipelines, and distributed relational database architectures. A national finalist in the GSTN Predictive Binary Classification hackathon, Sunil designs production-grade software with rigorous pytest test suites, cross-engine SQL parity, and zero-downtime CI/CD automation. He publishes technical architecture guides and open-source tooling for the global developer ecosystem.",
        "technical_abstract": "Specialized in Python (FastAPI/Flask), PostgreSQL/MySQL/SQLite cross-engine reliability, XGBoost/LightGBM tabular predictive systems, Dockerized orchestration, and multi-tier pytest verification architectures.",
    },
    # Directory Mappings
    "paths": {
        "project_root": PROJECT_ROOT,
        "docs_dir": DOCS_DIR,
        "assets_dir": ASSETS_DIR,
        "brand_dir": BRAND_DIR,
        "img_dir": IMG_DIR,
        "video_dir": VIDEO_DIR,
        "banners_dir": BANNERS_DIR,
        "articles_dir": ARTICLES_DIR,
        "social_dir": SOCIAL_DIR,
        "decks_dir": DECKS_DIR,
        "avatar_path": AVATAR_PATH,
        "zip_path": BRAND_DIR / "mrxsierra-brand-press-kit.zip",
    },
}
