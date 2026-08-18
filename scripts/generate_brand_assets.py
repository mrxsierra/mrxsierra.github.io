"""
Automated Brand Asset & OpenGraph Preview Generator.
Generates:
- Multi-resolution favicons (favicon.ico, favicon.png, apple-touch-icon.png)
- High-contrast 1200x630 Open Graph preview image (preview.png)
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PROJECT_ROOT = Path(__file__).parent.parent
IMG_DIR = PROJECT_ROOT / "docs" / "assets" / "img"
AVATAR_PATH = PROJECT_ROOT / "docs" / "assets" / "mrxss_400x400.jpg"


def draw_geometric_s(
    draw: ImageDraw.ImageDraw,
    scale: float,
    offset_x: float = 0,
    offset_y: float = 0,
    fill_color=(255, 255, 255),
):
    """Draws the Geometric Constructivist 'S' glyph at a given scale and offset."""
    pass


def render_master_monogram(size: int = 512) -> Image.Image:
    """Renders the master monogram at specified size with anti-aliasing."""
    # 4x oversampling for crisp edges
    super_size = size * 4
    canvas = Image.new("RGBA", (super_size, super_size), (8, 9, 13, 255))
    draw = ImageDraw.Draw(canvas)

    s = super_size / 128.0

    # Rounded squircle background
    radius = int(26 * s)
    mask = Image.new("L", (super_size, super_size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([(0, 0), (super_size, super_size)], radius=radius, fill=255)

    # Draw geometric S components
    # Top horizontal & right vertical
    w = int(15 * s)
    # Top bar
    draw.rounded_rectangle(
        [(int(29 * s), int(10 * s)), (int(92 * s), int(10 * s) + w)],
        radius=int(6 * s),
        fill=(255, 255, 255),
    )
    # Top right leg
    draw.rounded_rectangle(
        [(int(92 * s) - w, int(10 * s)), (int(92 * s), int(48 * s))],
        radius=int(6 * s),
        fill=(255, 255, 255),
    )
    # Mid bar
    draw.rounded_rectangle(
        [(int(29 * s), int(48 * s) - w), (int(92 * s), int(48 * s))],
        radius=int(6 * s),
        fill=(255, 255, 255),
    )
    # Central transition spine
    draw.rounded_rectangle(
        [(int(29 * s), int(48 * s) - w), (int(92 * s), int(74 * s) + w)],
        radius=int(18 * s),
        fill=(255, 255, 255),
    )
    # Inner cutout to maintain S negative space
    draw.rounded_rectangle(
        [(int(29 * s) + w, int(25 * s)), (int(92 * s) - w, int(48 * s) - int(2 * s))],
        radius=int(6 * s),
        fill=(8, 9, 13),
    )
    draw.rounded_rectangle(
        [(int(29 * s) + w, int(74 * s) + int(2 * s)), (int(92 * s) - w, int(98 * s))],
        radius=int(6 * s),
        fill=(8, 9, 13),
    )
    # Bottom left leg
    draw.rounded_rectangle(
        [(int(29 * s), int(74 * s)), (int(29 * s) + w, int(114 * s) - int(10 * s))],
        radius=int(6 * s),
        fill=(255, 255, 255),
    )
    # Bottom bar
    draw.rounded_rectangle(
        [(int(29 * s), int(114 * s) - w - int(10 * s)), (int(92 * s), int(114 * s) - int(10 * s))],
        radius=int(6 * s),
        fill=(255, 255, 255),
    )

    canvas.putalpha(mask)
    return canvas.resize((size, size), Image.Resampling.LANCZOS)


def generate_favicons():
    """Generates favicon.ico, favicon.png, and apple-touch-icon.png."""
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    # 1. 512x512 Master PNG
    master_512 = render_master_monogram(512)
    master_512.save(IMG_DIR / "favicon.png", "PNG")

    # 2. 180x180 Apple Touch Icon
    touch_180 = render_master_monogram(180)
    touch_180.save(IMG_DIR / "apple-touch-icon.png", "PNG")

    # 3. Multi-resolution ICO (16, 32, 48, 64)
    ico_16 = render_master_monogram(16)
    ico_32 = render_master_monogram(32)
    ico_48 = render_master_monogram(48)
    ico_64 = render_master_monogram(64)

    master_512.save(
        IMG_DIR / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64)],
        append_images=[ico_16, ico_32, ico_48, ico_64],
    )
    print("Favicon suite generated successfully.")


def generate_og_preview():
    """Generates 1200x630 OpenGraph social sharing card (preview.png)."""
    width, height = 1200, 630
    og_img = Image.new("RGB", (width, height), (8, 9, 13))
    draw = ImageDraw.Draw(og_img)

    # Subtle structural hairline frame
    draw.rectangle([(20, 20), (width - 20, height - 20)], outline=(30, 32, 40), width=1)
    draw.rectangle([(28, 28), (width - 28, height - 28)], outline=(20, 22, 28), width=1)

    # Place Monogram mark on top-left (100x100)
    monogram = render_master_monogram(96)
    og_img.paste(monogram, (64, 64), monogram)

    # Embed Circular Avatar on right side (280x280)
    if AVATAR_PATH.exists():
        avatar = Image.open(AVATAR_PATH).convert("RGBA")
        avatar_size = 280
        avatar = avatar.resize((avatar_size, avatar_size), Image.Resampling.LANCZOS)

        # Circular mask with smooth anti-aliased edge
        mask = Image.new("L", (avatar_size * 2, avatar_size * 2), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse([(0, 0), (avatar_size * 2, avatar_size * 2)], fill=255)
        mask = mask.resize((avatar_size, avatar_size), Image.Resampling.LANCZOS)

        # Border around avatar
        avatar_x, avatar_y = 820, 175
        draw.ellipse(
            [
                (avatar_x - 4, avatar_y - 4),
                (avatar_x + avatar_size + 4, avatar_y + avatar_size + 4),
            ],
            fill=(24, 27, 36),
        )
        draw.ellipse(
            [
                (avatar_x - 2, avatar_y - 2),
                (avatar_x + avatar_size + 2, avatar_y + avatar_size + 2),
            ],
            fill=(99, 102, 241),
        )

        og_img.paste(avatar, (avatar_x, avatar_y), mask)

    # Clean Typography (Fallback to clean default if custom font unavailable)
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
        font_name = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        font_tag = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    except Exception:
        font_title = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_tag = ImageFont.load_default()

    # Category Pill
    draw.rounded_rectangle(
        [(64, 200), (320, 236)], radius=18, fill=(18, 20, 28), outline=(40, 44, 58), width=1
    )
    draw.text((80, 208), "ENGINEERING PORTFOLIO", fill=(129, 140, 248), font=font_tag)

    # Name & Handle
    draw.text((64, 260), "Sunil Sharma", fill=(255, 255, 255), font=font_title)
    draw.text((64, 330), "mrxsierra.github.io", fill=(148, 163, 184), font=font_name)

    # Tagline & Disciplines
    draw.text(
        (64, 410),
        "Full-Stack Web Architect • Machine Learning Pipelines",
        fill=(226, 232, 240),
        font=font_sub,
    )
    draw.text(
        (64, 450),
        "Multi-RDBMS Systems • Production Data Engineering",
        fill=(148, 163, 184),
        font=font_sub,
    )

    # Domain footer badge
    draw.line([(64, 530), (740, 530)], fill=(30, 34, 46), width=1)
    draw.text((64, 550), "https://mrxsierra.github.io", fill=(99, 102, 241), font=font_sub)

    # Save to preview.png
    og_img.save(IMG_DIR / "preview.png", "PNG", quality=95)
    print("Open Graph preview banner generated successfully at docs/assets/img/preview.png")


if __name__ == "__main__":
    generate_favicons()
    generate_og_preview()
