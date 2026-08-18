"""
Vector Builder Module for Brand Engine.
Generates all scalable vector SVGs using pure mathematical definitions and config values.
"""

from .config import BRAND_CONFIG

# Geometric Constructivist 'S' SVG Path
GLYPH_PATH_DATA = """M 92,30
    L 92,48
    L 77,48
    C 77,40 71,34 62,34
    C 53,34 47,39 47,46
    C 47,53 53,57 63,60
    L 73,63
    C 88,68 96,75 96,89
    C 96,104 83,114 62,114
    C 42,114 28,103 28,88
    L 28,70
    L 43,70
    C 43,79 50,86 62,86
    C 72,86 78,80 78,73
    C 78,66 71,62 61,59
    L 51,56
    C 36,51 29,44 29,31
    C 29,16 43,6 62,6
    C 81,6 92,16 92,30
    Z"""


def build_core_monograms():
    """Generates standalone vector monogram marks."""
    paths = BRAND_CONFIG["paths"]
    colors = BRAND_CONFIG["colors"]

    brand_dir = paths["brand_dir"]
    img_dir = paths["img_dir"]
    brand_dir.mkdir(parents=True, exist_ok=True)
    img_dir.mkdir(parents=True, exist_ok=True)

    # 1. Monogram Dark
    dark_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="100%" height="100%">
  <!-- mrxsierra | Master Monogram Dark -->
  <rect width="128" height="128" rx="26" fill="{colors["obsidian"]}" />
  <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
</svg>"""
    (brand_dir / "monogram-dark.svg").write_text(dark_svg, encoding="utf-8")
    (img_dir / "logo-monogram.svg").write_text(dark_svg, encoding="utf-8")
    (img_dir / "favicon.svg").write_text(dark_svg, encoding="utf-8")

    # 2. Monogram Light
    light_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="100%" height="100%">
  <!-- mrxsierra | Master Monogram Light -->
  <rect width="128" height="128" rx="26" fill="{colors["white"]}" stroke="#E2E8F0" stroke-width="1.5" />
  <path fill="{colors["obsidian"]}" d="{GLYPH_PATH_DATA}" />
</svg>"""
    (brand_dir / "monogram-light.svg").write_text(light_svg, encoding="utf-8")

    # 3. Monogram Transparent (White Glyph)
    trans_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="100%" height="100%">
  <!-- mrxsierra | Monogram Transparent White -->
  <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
</svg>"""
    (brand_dir / "monogram-transparent.svg").write_text(trans_svg, encoding="utf-8")

    # 4. Monogram Transparent Dark (Dark Glyph)
    trans_dark_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="100%" height="100%">
  <!-- mrxsierra | Monogram Transparent Dark -->
  <path fill="{colors["obsidian"]}" d="{GLYPH_PATH_DATA}" />
</svg>"""
    (brand_dir / "monogram-transparent-dark.svg").write_text(trans_dark_svg, encoding="utf-8")


def build_logotypes():
    """Generates horizontal and stacked logotypes."""
    paths = BRAND_CONFIG["paths"]
    colors = BRAND_CONFIG["colors"]
    brand_dir = paths["brand_dir"]

    # Horizontal Logotype
    h_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 96" width="100%" height="100%">
  <!-- mrxsierra | Master Horizontal Logotype -->
  <defs>
    <style>
      .brand-title {{ font-family: 'Inter', sans-serif; font-size: 28px; font-weight: 800; fill: {colors["white"]}; letter-spacing: -0.5px; }}
      .brand-sub {{ font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 500; fill: {colors["accent_glow"]}; letter-spacing: 0.5px; }}
    </style>
  </defs>
  <g transform="translate(12, 12)">
    <rect width="72" height="72" rx="16" fill="{colors["obsidian"]}" stroke="{colors["border"]}" stroke-width="1.5" />
    <g transform="scale(0.5625)">
      <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
    </g>
  </g>
  <text x="104" y="46" class="brand-title">{BRAND_CONFIG["handle"]}</text>
  <text x="104" y="68" class="brand-sub">{BRAND_CONFIG["name"].upper()} • SYSTEMS &amp; ML</text>
</svg>"""
    (brand_dir / "logo-horizontal.svg").write_text(h_svg, encoding="utf-8")

    # Stacked Logotype
    s_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <!-- mrxsierra | Master Stacked Logotype -->
  <defs>
    <style>
      .stacked-title {{ font-family: 'Inter', sans-serif; font-size: 22px; font-weight: 800; fill: {colors["white"]}; letter-spacing: -0.5px; text-anchor: middle; }}
      .stacked-sub {{ font-family: 'JetBrains Mono', monospace; font-size: 9.5px; font-weight: 600; fill: {colors["accent_glow"]}; letter-spacing: 1px; text-anchor: middle; }}
    </style>
  </defs>
  <g transform="translate(52, 16)">
    <rect width="96" height="96" rx="20" fill="{colors["obsidian"]}" stroke="{colors["border"]}" stroke-width="1.5" />
    <g transform="scale(0.75)">
      <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
    </g>
  </g>
  <text x="100" y="148" class="stacked-title">{BRAND_CONFIG["handle"]}</text>
  <text x="100" y="170" class="stacked-sub">ENGINEERING &amp; RESEARCH</text>
</svg>"""
    (brand_dir / "logo-stacked.svg").write_text(s_svg, encoding="utf-8")


def build_video_vectors():
    """Generates video watermarks, lower-thirds, end-screens, and thumbnail frames."""
    paths = BRAND_CONFIG["paths"]
    colors = BRAND_CONFIG["colors"]
    video_dir = paths["video_dir"]
    video_dir.mkdir(parents=True, exist_ok=True)

    # 1. Watermark Square SVG
    wm_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 150" width="100%" height="100%">
  <!-- YouTube Branding Watermark (150x150 Vector Master) -->
  <rect width="150" height="150" rx="30" fill="{colors["obsidian"]}" opacity="0.95" />
  <g transform="translate(11, 11)">
    <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
  </g>
</svg>"""
    (video_dir / "watermark-square.svg").write_text(wm_svg, encoding="utf-8")

    # 2. Lower Third Broadcast Overlay
    lt_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
  <!-- Video Lower Third Broadcast Overlay (1920x1080) -->
  <defs>
    <style>
      .lt-name {{ font-family: 'Inter', sans-serif; font-size: 38px; font-weight: 800; fill: {colors["white"]}; letter-spacing: -0.5px; }}
      .lt-role {{ font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 500; fill: {colors["accent_glow"]}; letter-spacing: 0.5px; }}
    </style>
  </defs>
  <g transform="translate(120, 860)">
    <rect width="680" height="120" rx="20" fill="{colors["obsidian"]}" fill-opacity="0.94" stroke="{colors["border"]}" stroke-width="1.5" />
    <rect x="0" y="24" width="6" height="72" rx="3" fill="{colors["accent"]}" />
    <g transform="translate(28, 24)">
      <rect width="72" height="72" rx="14" fill="{colors["surface"]}" stroke="{colors["border_subtle"]}" stroke-width="1" />
      <g transform="scale(0.5625)">
        <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
      </g>
    </g>
    <text x="124" y="58" class="lt-name">{BRAND_CONFIG["name"]}</text>
    <text x="124" y="92" class="lt-role">FULL-STACK &amp; ML SYSTEMS • {BRAND_CONFIG["twitter"]}</text>
  </g>
</svg>"""
    (video_dir / "lower-third.svg").write_text(lt_svg, encoding="utf-8")

    # 3. Video End Screen
    es_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
  <!-- YouTube 16:9 Video End Screen / Outro Template (1920x1080) -->
  <defs>
    <style>
      .es-bg {{ fill: {colors["obsidian"]}; }}
      .es-slot {{ fill: #111218; stroke: {colors["border"]}; stroke-width: 2; stroke-dasharray: 6 6; rx: 16px; }}
      .es-label {{ font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 600; fill: #71717A; text-anchor: middle; }}
      .es-title {{ font-family: 'Inter', sans-serif; font-size: 48px; font-weight: 800; fill: {colors["white"]}; letter-spacing: -1px; }}
      .es-sub {{ font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 500; fill: {colors["text_muted"]}; }}
      .es-link {{ font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 600; fill: {colors["accent_glow"]}; }}
    </style>
  </defs>
  <rect width="1920" height="1080" class="es-bg" />
  <g transform="translate(140, 220)">
    <rect width="112" height="112" rx="24" fill="{colors["surface"]}" stroke="{colors["border_subtle"]}" stroke-width="2" />
    <g transform="scale(0.875)">
      <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
    </g>
    <text x="0" y="190" class="es-title">Thanks for Watching.</text>
    <text x="0" y="240" class="es-sub">Subscribe for deep dives in ML, databases, and systems architecture.</text>
    <g transform="translate(0, 310)">
      <rect width="360" height="64" rx="32" fill="{colors["accent"]}" />
      <text x="180" y="40" font-family="'Inter', sans-serif" font-size="20" font-weight="700" fill="{colors["white"]}" text-anchor="middle">SUBSCRIBE / {BRAND_CONFIG["twitter"]}</text>
    </g>
    <text x="0" y="440" class="es-link">{BRAND_CONFIG["domain"]}</text>
  </g>
  <rect x="1140" y="160" width="620" height="348" class="es-slot" />
  <text x="1450" y="340" class="es-label">BEST FOR VIEWER</text>
  <rect x="1140" y="560" width="620" height="348" class="es-slot" />
  <text x="1450" y="740" class="es-label">RECENT UPLOAD</text>
  <circle cx="940" cy="530" r="80" class="es-slot" />
  <text x="940" y="538" class="es-label" font-size="16">AVATAR</text>
</svg>"""
    (video_dir / "video-end-screen.svg").write_text(es_svg, encoding="utf-8")

    # 4. Thumbnail Frame
    tf_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="100%" height="100%">
  <!-- YouTube 16:9 Thumbnail Frame Template (1280x720) -->
  <defs>
    <style>
      .thumb-bg {{ fill: {colors["obsidian"]}; }}
      .thumb-border {{ stroke: {colors["accent"]}; stroke-width: 4; fill: none; }}
      .thumb-tag {{ font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; fill: {colors["accent_glow"]}; letter-spacing: 2px; }}
      .thumb-title {{ font-family: 'Inter', sans-serif; font-size: 64px; font-weight: 900; fill: {colors["white"]}; letter-spacing: -2px; }}
    </style>
  </defs>
  <rect width="1280" height="720" class="thumb-bg" />
  <rect x="16" y="16" width="1248" height="688" rx="20" class="thumb-border" />
  <g transform="translate(64, 56)">
    <rect width="64" height="64" rx="14" fill="{colors["surface"]}" stroke="{colors["border_subtle"]}" stroke-width="1.5" />
    <g transform="scale(0.5)">
      <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
    </g>
    <text x="84" y="42" class="thumb-tag">ENGINEERING DEEP DIVE</text>
  </g>
  <g transform="translate(64, 340)">
    <text x="0" y="0" class="thumb-title">BUILDING DISTRIBUTED</text>
    <text x="0" y="76" class="thumb-title" fill="{colors["accent_glow"]}">DATABASE ARCHITECTURES</text>
  </g>
  <text x="64" y="640" font-family="'JetBrains Mono', monospace" font-size="22" font-weight="600" fill="{colors["text_muted"]}">{BRAND_CONFIG["handle"]}.github.io • {BRAND_CONFIG["name"]}</text>
</svg>"""
    (video_dir / "thumbnail-frame.svg").write_text(tf_svg, encoding="utf-8")


def build_social_banner_vectors():
    """Generates vector banners for GitHub, LinkedIn, X, and YouTube."""
    paths = BRAND_CONFIG["paths"]
    colors = BRAND_CONFIG["colors"]
    banners_dir = paths["banners_dir"]
    banners_dir.mkdir(parents=True, exist_ok=True)

    # 1. GitHub Banner (1280x640)
    gh_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" width="100%" height="100%">
  <!-- GitHub Profile & Repository Header Banner (1280x640) -->
  <defs>
    <style>
      .gh-bg {{ fill: {colors["obsidian"]}; }}
      .gh-border {{ stroke: {colors["border"]}; stroke-width: 1.5; fill: none; }}
      .gh-kicker {{ font-family: 'JetBrains Mono', monospace; font-size: 16px; font-weight: 700; fill: {colors["accent_glow"]}; letter-spacing: 2px; }}
      .gh-name {{ font-family: 'Inter', sans-serif; font-size: 56px; font-weight: 900; fill: {colors["white"]}; letter-spacing: -1.5px; }}
      .gh-title {{ font-family: 'Inter', sans-serif; font-size: 26px; font-weight: 500; fill: {colors["text_secondary"]}; }}
      .gh-badge {{ font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 600; fill: {colors["text_muted"]}; }}
    </style>
  </defs>
  <rect width="1280" height="640" class="gh-bg" />
  <rect x="24" y="24" width="1232" height="592" rx="20" class="gh-border" />
  <g transform="translate(80, 80)">
    <rect width="80" height="80" rx="18" fill="{colors["surface"]}" stroke="{colors["border_subtle"]}" stroke-width="1.5" />
    <g transform="scale(0.625)">
      <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
    </g>
    <text x="100" y="46" class="gh-kicker">ENGINEERING &amp; RESEARCH ECOSYSTEM</text>
  </g>
  <g transform="translate(80, 240)">
    <text x="0" y="0" class="gh-name">{BRAND_CONFIG["name"]}</text>
    <text x="0" y="50" class="gh-title">{BRAND_CONFIG["title"]}</text>
  </g>
  <g transform="translate(80, 360)">
    <rect x="0" y="0" width="130" height="36" rx="8" fill="{colors["surface"]}" stroke="{colors["border"]}" stroke-width="1" />
    <text x="65" y="23" class="gh-badge" text-anchor="middle">PYTHON</text>
    <rect x="146" y="0" width="160" height="36" rx="8" fill="{colors["surface"]}" stroke="{colors["border"]}" stroke-width="1" />
    <text x="226" y="23" class="gh-badge" text-anchor="middle">POSTGRESQL</text>
    <rect x="322" y="0" width="140" height="36" rx="8" fill="{colors["surface"]}" stroke="{colors["border"]}" stroke-width="1" />
    <text x="392" y="23" class="gh-badge" text-anchor="middle">FASTAPI</text>
    <rect x="478" y="0" width="160" height="36" rx="8" fill="{colors["surface"]}" stroke="{colors["border"]}" stroke-width="1" />
    <text x="558" y="23" class="gh-badge" text-anchor="middle">XGBOOST / ML</text>
    <rect x="654" y="0" width="150" height="36" rx="8" fill="{colors["surface"]}" stroke="{colors["border"]}" stroke-width="1" />
    <text x="729" y="23" class="gh-badge" text-anchor="middle">DOCKER CI/CD</text>
  </g>
  <g transform="translate(80, 540)">
    <line x1="0" y1="-20" x2="1120" y2="-20" stroke="{colors["border"]}" stroke-width="1" />
    <text x="0" y="20" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="600" fill="{colors["accent_glow"]}">{BRAND_CONFIG["github"]} • {BRAND_CONFIG["domain"]}</text>
  </g>
</svg>"""
    (banners_dir / "github-banner.svg").write_text(gh_svg, encoding="utf-8")

    # 2. LinkedIn Banner (1584x396)
    li_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1584 396" width="100%" height="100%">
  <!-- LinkedIn Profile Cover Banner (1584x396) -->
  <defs>
    <style>
      .li-bg {{ fill: {colors["obsidian"]}; }}
      .li-kicker {{ font-family: 'JetBrains Mono', monospace; font-size: 15px; font-weight: 700; fill: {colors["accent_glow"]}; letter-spacing: 2px; }}
      .li-name {{ font-family: 'Inter', sans-serif; font-size: 44px; font-weight: 900; fill: {colors["white"]}; letter-spacing: -1px; }}
      .li-role {{ font-family: 'Inter', sans-serif; font-size: 21px; font-weight: 500; fill: {colors["text_secondary"]}; }}
      .li-sub {{ font-family: 'JetBrains Mono', monospace; font-size: 15px; font-weight: 500; fill: {colors["text_muted"]}; }}
    </style>
  </defs>
  <rect width="1584" height="396" class="li-bg" />
  <rect x="16" y="16" width="1552" height="364" rx="14" fill="none" stroke="{colors["border"]}" stroke-width="1.5" />
  <g transform="translate(380, 80)">
    <g transform="translate(0, 0)">
      <rect width="48" height="48" rx="10" fill="{colors["surface"]}" stroke="{colors["border_subtle"]}" stroke-width="1" />
      <g transform="scale(0.375)">
        <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
      </g>
      <text x="64" y="32" class="li-kicker">FULL-STACK &amp; AI SYSTEMS ARCHITECT</text>
    </g>
    <text x="0" y="96" class="li-name">{BRAND_CONFIG["name"]}</text>
    <text x="0" y="136" class="li-role">{BRAND_CONFIG["tagline"]}</text>
    <text x="0" y="180" class="li-sub">{BRAND_CONFIG["domain"]} • {BRAND_CONFIG["github"]}</text>
  </g>
  <g transform="translate(1380, 80)">
    <circle cx="80" cy="110" r="70" fill="none" stroke="{colors["border"]}" stroke-width="1" stroke-dasharray="3 3" />
    <circle cx="80" cy="110" r="40" fill="none" stroke="{colors["border_subtle"]}" stroke-width="1" />
    <circle cx="80" cy="110" r="4" fill="{colors["accent"]}" />
  </g>
</svg>"""
    (banners_dir / "linkedin-banner.svg").write_text(li_svg, encoding="utf-8")

    # 3. X Banner (1500x500)
    x_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1500 500" width="100%" height="100%">
  <!-- X (Twitter) Profile Header Banner (1500x500) -->
  <defs>
    <style>
      .x-bg {{ fill: {colors["obsidian"]}; }}
      .x-kicker {{ font-family: 'JetBrains Mono', monospace; font-size: 16px; font-weight: 700; fill: {colors["accent_glow"]}; letter-spacing: 2px; }}
      .x-name {{ font-family: 'Inter', sans-serif; font-size: 52px; font-weight: 900; fill: {colors["white"]}; letter-spacing: -1.5px; }}
      .x-title {{ font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 500; fill: {colors["text_secondary"]}; }}
      .x-sub {{ font-family: 'JetBrains Mono', monospace; font-size: 17px; font-weight: 500; fill: {colors["text_muted"]}; }}
    </style>
  </defs>
  <rect width="1500" height="500" class="x-bg" />
  <rect x="20" y="20" width="1460" height="460" rx="16" fill="none" stroke="{colors["border"]}" stroke-width="1.5" />
  <g transform="translate(380, 110)">
    <g transform="translate(0, 0)">
      <rect width="52" height="52" rx="12" fill="{colors["surface"]}" stroke="{colors["border_subtle"]}" stroke-width="1" />
      <g transform="scale(0.40625)">
        <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
      </g>
      <text x="68" y="34" class="x-kicker">ENGINEERING &amp; RESEARCH</text>
    </g>
    <text x="0" y="110" class="x-name">{BRAND_CONFIG["name"]} ({BRAND_CONFIG["twitter"]})</text>
    <text x="0" y="160" class="x-title">{BRAND_CONFIG["title"]}</text>
    <text x="0" y="210" class="x-sub">{BRAND_CONFIG["domain"]}</text>
  </g>
</svg>"""
    (banners_dir / "x-twitter-banner.svg").write_text(x_svg, encoding="utf-8")

    # 4. YouTube Banner (2560x1440)
    yt_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2560 1440" width="100%" height="100%">
  <!-- YouTube Channel Banner Master (2560x1440) -->
  <defs>
    <style>
      .yt-bg {{ fill: {colors["obsidian"]}; }}
      .yt-kicker {{ font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; fill: {colors["accent_glow"]}; letter-spacing: 3px; }}
      .yt-name {{ font-family: 'Inter', sans-serif; font-size: 72px; font-weight: 900; fill: {colors["white"]}; letter-spacing: -2px; }}
      .yt-title {{ font-family: 'Inter', sans-serif; font-size: 32px; font-weight: 500; fill: {colors["text_secondary"]}; }}
      .yt-sub {{ font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 500; fill: {colors["text_muted"]}; }}
    </style>
  </defs>
  <rect width="2560" height="1440" class="yt-bg" />
  <g transform="translate(600, 560)">
    <g transform="translate(0, 0)">
      <rect width="88" height="88" rx="20" fill="{colors["surface"]}" stroke="{colors["border_subtle"]}" stroke-width="1.5" />
      <g transform="scale(0.6875)">
        <path fill="{colors["white"]}" d="{GLYPH_PATH_DATA}" />
      </g>
      <text x="110" y="52" class="yt-kicker">ENGINEERING &amp; ARCHITECTURE</text>
    </g>
    <text x="0" y="160" class="yt-name">{BRAND_CONFIG["name"]} ({BRAND_CONFIG["twitter"]})</text>
    <text x="0" y="220" class="yt-title">{BRAND_CONFIG["title"]}</text>
    <text x="0" y="280" class="yt-sub">{BRAND_CONFIG["domain"]} • Weekly Engineering Deep Dives</text>
  </g>
</svg>"""
    (banners_dir / "youtube-banner.svg").write_text(yt_svg, encoding="utf-8")


def build_all_vectors():
    """Compiles all vector assets."""
    build_core_monograms()
    build_logotypes()
    build_video_vectors()
    build_social_banner_vectors()
    print("✓ All vector SVGs built successfully.")
