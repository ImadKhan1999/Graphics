"""
ImadLabs Brand Factory - Final Completion Engine v1.3.0
Builds ALL missing deliverables:
  - Icon concept previews for iTube & Hyper Downloader
  - App branding templates (SVG/HTML)
  - Social media: Facebook cover, portrait posts, stories, YouTube thumbnail template
  - Marketing: additional templates
  - Regenerates improved brand showcase HTML
"""

import os
import subprocess
import textwrap
from PIL import Image

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = r"f:\ImadLabs"

# ─── Brand Colors ───────────────────────────────────────────────────────────
BG_DARK      = "#070B14"
SURFACE      = "#0B0F19"
CARD         = "#111827"
BORDER       = "#1E293B"
BLUE_PRIMARY = "#0066FF"
SKY_BLUE     = "#38BDF8"
BLUE_MID     = "#0284C7"
ACCENT_L     = "#00F5A0"   # Cyber Mint — L-pathway
DOT_COLOR    = "#00FFC2"   # Quantum Core — dot
TEXT_PRIMARY = "#F8FAFC"
TEXT_SECONDARY = "#94A3B8"
TEXT_MUTED   = "#64748B"

def rasterize(svg_path, png_path, width, height, transparent=True):
    os.makedirs(os.path.dirname(os.path.abspath(png_path)), exist_ok=True)
    bg = "--default-background-color=00000000" if transparent else "--default-background-color=070B1400"
    cmd = [
        CHROME_PATH, "--headless=new", "--disable-gpu", "--no-sandbox",
        f"--screenshot={os.path.abspath(png_path)}",
        f"--window-size={width},{height}", bg,
        "--hide-scrollbars", os.path.abspath(svg_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.returncode == 0 and os.path.exists(png_path)

def save_svg(content, path):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def make_ico(png_path, ico_path):
    os.makedirs(os.path.dirname(os.path.abspath(ico_path)), exist_ok=True)
    img = Image.open(png_path).convert("RGBA")
    sizes = [(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)]
    img.save(ico_path, format="ICO", sizes=sizes)

# ═══════════════════════════════════════════════════════════════════════════
# HEXACORE SYMBOL — inline SVG group (reusable snippet)
# ═══════════════════════════════════════════════════════════════════════════
def hexacore_defs():
    return """
  <defs>
    <linearGradient id="hc-top" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <linearGradient id="hc-left" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#0066FF"/>
    </linearGradient>
    <linearGradient id="hc-right" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0066FF"/>
      <stop offset="100%" stop-color="#003DB3"/>
    </linearGradient>
    <radialGradient id="hc-dot-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00FFC2"/>
      <stop offset="60%" stop-color="#00F5A0" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#00E090" stop-opacity="0"/>
    </radialGradient>
    <filter id="hc-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="hc-dot-blur">
      <feGaussianBlur stdDeviation="4"/>
    </filter>
  </defs>
"""

def hexacore_symbol(cx=100, cy=100, scale=1.0, accent=ACCENT_L, dot=DOT_COLOR):
    """Returns the HexaCore group centered at (cx,cy) with given scale."""
    s = scale
    ox, oy = cx - 100*s, cy - 116*s  # top of symbol is at y=20*s, center at ~y=116*s
    def pt(x, y):
        return f"{ox + x*s:.1f},{oy + y*s:.1f}"
    def px(x):
        return f"{ox + x*s:.1f}"
    def py(y):
        return f"{oy + y*s:.1f}"

    return f"""
  <g id="hexacore" filter="url(#hc-glow)">
    <!-- Top facet -->
    <polygon points="{pt(100,20)} {pt(180,66)} {pt(100,112)} {pt(20,66)}"
             fill="url(#hc-top)" opacity="0.95"/>
    <!-- Left facet -->
    <polygon points="{pt(20,76)} {pt(100,122)} {pt(100,212)} {pt(20,166)}"
             fill="url(#hc-left)" opacity="0.85"/>
    <!-- Right facet -->
    <polygon points="{pt(100,122)} {pt(180,76)} {pt(180,166)} {pt(100,212)}"
             fill="url(#hc-right)" opacity="0.75"/>
    <!-- Quantum dot glow halo -->
    <circle cx="{px(100)}" cy="{py(76)}" r="{28*s:.1f}" fill="url(#hc-dot-glow)" opacity="0.5"/>
    <!-- Quantum dot outer -->
    <circle cx="{px(100)}" cy="{py(76)}" r="{14*s:.1f}" fill="{dot}"/>
    <!-- Quantum dot inner -->
    <circle cx="{px(100)}" cy="{py(76)}" r="{7*s:.1f}" fill="white" opacity="0.9"/>
    <!-- L-pathway -->
    <path d="M {px(100)} {py(120)} L {px(100)} {py(182)} L {px(152)} {py(152)}"
          stroke="{accent}" stroke-width="{12*s:.1f}" stroke-linecap="round"
          stroke-linejoin="round" fill="none"/>
    <!-- Satellite tip -->
    <circle cx="{px(152)}" cy="{py(152)}" r="{5.5*s:.1f}" fill="{dot}"/>
  </g>
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. ICON CONCEPT PREVIEWS
# ═══════════════════════════════════════════════════════════════════════════

def build_icon_concepts():
    print("\n[1/5] Building icon concept previews...")
    out = os.path.join(BASE, "previews", "icon-concepts")
    os.makedirs(out, exist_ok=True)

    apps = {
        "itube": {
            "label": "iTube",
            "tagline": "YouTube Downloader",
            "bg_grad": ("linear-gradient(135deg, #FF0000 0%, #CC0000 50%, #8B0000 100%)", "#FF0000", "#FF6B6B"),
            "icon_path": ["M 80 70 L 130 100 L 80 130 Z"],  # play triangle
            "icon_color": "white",
            "ring_color": "#FF4444",
        },
        "hyper-downloader": {
            "label": "Hyper Downloader",
            "tagline": "Universal Download Manager",
            "bg_grad": ("linear-gradient(135deg, #7C3AED 0%, #5B21B6 50%, #3B0764 100%)", "#7C3AED", "#A78BFA"),
            "icon_path": ["M 100 65 L 100 135", "M 70 108 L 100 140 L 130 108"],  # download arrow
            "icon_color": "white",
            "ring_color": "#A78BFA",
        },
    }

    for slug, app in apps.items():
        # Generate 4 concept variations for each app
        concepts = [
            {"name": "gradient-badge", "desc": "Gradient Badge with App Symbol"},
            {"name": "dark-premium", "desc": "Dark Premium Rounded Square"},
            {"name": "glass-morph", "desc": "Glassmorphism Style"},
            {"name": "minimal-flat", "desc": "Minimal Flat Design"},
        ]

        accent_color = app["bg_grad"][1]
        light_color = app["bg_grad"][2]

        for idx, concept in enumerate(concepts):
            cname = concept["name"]
            svg_path = os.path.join(out, f"{slug}-{cname}.svg")
            png_path = os.path.join(out, f"{slug}-{cname}.png")

            if idx == 0:  # Gradient Badge
                bg = f'<rect width="200" height="200" rx="44" fill="url(#app-bg)"/>'
                defs = f'''<defs>
                  <linearGradient id="app-bg" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="{light_color}"/>
                    <stop offset="100%" stop-color="{accent_color}"/>
                  </linearGradient>
                </defs>'''
                overlay = ""
            elif idx == 1:  # Dark Premium
                bg = f'<rect width="200" height="200" rx="44" fill="#0B0F19"/><rect width="200" height="200" rx="44" fill="{accent_color}" fill-opacity="0.12"/>'
                defs = ""
                overlay = f'<rect x="2" y="2" width="196" height="196" rx="42" fill="none" stroke="{accent_color}" stroke-width="2" opacity="0.6"/>'
            elif idx == 2:  # Glassmorphism
                bg = f'<rect width="200" height="200" rx="44" fill="{accent_color}" fill-opacity="0.15"/><rect width="200" height="200" rx="44" fill="white" fill-opacity="0.05"/>'
                defs = ""
                overlay = f'<rect x="1" y="1" width="198" height="198" rx="43" fill="none" stroke="white" stroke-width="1" opacity="0.4"/>'
            else:  # Minimal Flat
                bg = f'<rect width="200" height="200" rx="44" fill="white"/>'
                defs = ""
                overlay = f'<rect x="2" y="2" width="196" height="196" rx="42" fill="none" stroke="{accent_color}" stroke-width="4"/>'
                app["icon_color"] = accent_color

            # Icon symbol
            icon_svg = ""
            for p in app["icon_path"]:
                if "M" in p and "L" in p and "Z" in p:
                    icon_svg += f'<path d="{p}" fill="{app["icon_color"]}"/>\n    '
                elif "M" in p and "L" in p:
                    icon_svg += f'<path d="{p}" stroke="{app["icon_color"]}" stroke-width="10" stroke-linecap="round" fill="none"/>\n    '

            # HexaCore DNA badge (small, bottom-right)
            dna_badge = f"""
    <!-- HexaCore DNA badge -->
    <g transform="translate(135,135) scale(0.28)">
      <polygon points="100,20 180,66 100,112 20,66" fill="{SKY_BLUE}" opacity="0.9"/>
      <polygon points="20,76 100,122 100,212 20,166" fill="{BLUE_MID}" opacity="0.8"/>
      <polygon points="100,122 180,76 180,166 100,212" fill="{BLUE_PRIMARY}" opacity="0.7"/>
      <circle cx="100" cy="76" r="14" fill="{DOT_COLOR}"/>
      <path d="M 100 120 L 100 182 L 152 152" stroke="{ACCENT_L}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    </g>"""

            svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  {defs}
  {bg}
  {icon_svg}
  {dna_badge}
  {overlay}
</svg>"""
            save_svg(svg, svg_path)
            if rasterize(svg_path, png_path, 200, 200):
                print(f"  ✓ {slug}-{cname}.png")
            app["icon_color"] = "white"  # reset

        # Also create a concept comparison sheet
        sheet_svg_path = os.path.join(out, f"{slug}-icon-concepts.svg")
        sheet_png_path = os.path.join(out, f"{slug}-icon-concepts.png")

        cells = ""
        for idx, concept in enumerate(concepts):
            col = idx * 220 + 20
            cname = concept["name"]
            cells += f"""
  <text x="{col+100}" y="240" fill="{TEXT_SECONDARY}" font-size="12"
        font-family="Plus Jakarta Sans, sans-serif" text-anchor="middle">{concept['desc']}</text>
  <image href="{slug}-{cname}.png" x="{col}" y="30" width="200" height="200"/>"""

        sheet = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 920 270" width="920" height="270">
  <rect width="920" height="270" fill="{BG_DARK}"/>
  <text x="460" y="22" fill="{TEXT_PRIMARY}" font-size="14" font-weight="700"
        font-family="Plus Jakarta Sans, sans-serif" text-anchor="middle">
    {app['label']} — Icon Concept Explorations
  </text>
  {cells}
</svg>"""
        save_svg(sheet, sheet_svg_path)
        if rasterize(sheet_svg_path, sheet_png_path, 920, 270):
            print(f"  ✓ {slug}-icon-concepts.png")

    print("  ✓ Icon concept previews complete")


# ═══════════════════════════════════════════════════════════════════════════
# 2. APP BRANDING TEMPLATES (SVG + HTML)
# ═══════════════════════════════════════════════════════════════════════════

def build_app_branding_templates():
    print("\n[2/5] Building app branding templates...")
    out = os.path.join(BASE, "templates", "app-branding")
    os.makedirs(out, exist_ok=True)

    # App launch announcement template (reusable SVG with editable text)
    template_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B14"/>
      <stop offset="70%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="top-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00F5A0" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#00F5A0" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hc-top" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <linearGradient id="hc-left" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#0066FF"/>
    </linearGradient>
    <linearGradient id="hc-right" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0066FF"/>
      <stop offset="100%" stop-color="#003DB3"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="12" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1080" height="1080" fill="url(#bg-grad)"/>
  <rect width="1080" height="300" fill="url(#top-grad)"/>

  <!-- Grid accent lines -->
  <line x1="0" y1="200" x2="1080" y2="200" stroke="{ACCENT_L}" stroke-width="1" opacity="0.15"/>
  <line x1="0" y1="880" x2="1080" y2="880" stroke="{ACCENT_L}" stroke-width="1" opacity="0.15"/>
  <line x1="200" y1="0" x2="200" y2="1080" stroke="{ACCENT_L}" stroke-width="1" opacity="0.08"/>
  <line x1="880" y1="0" x2="880" y2="1080" stroke="{ACCENT_L}" stroke-width="1" opacity="0.08"/>

  <!-- Corner accents -->
  <path d="M 40 80 L 40 40 L 80 40" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.6"/>
  <path d="M 1000 40 L 1040 40 L 1040 80" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.6"/>
  <path d="M 40 1000 L 40 1040 L 80 1040" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.6"/>
  <path d="M 1000 1040 L 1040 1040 L 1040 1000" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.6"/>

  <!-- ImadLabs wordmark top-left -->
  <text x="60" y="66" font-family="Plus Jakarta Sans, sans-serif" font-size="28" font-weight="800" fill="{TEXT_PRIMARY}">
    Imad<tspan fill="{ACCENT_L}">Labs</tspan>
  </text>

  <!-- App icon placeholder (replace with your app icon) -->
  <rect x="390" y="140" width="300" height="300" rx="72" fill="{CARD}" stroke="{BORDER}" stroke-width="2"/>
  <!-- [REPLACE: Insert your app icon here] -->
  <text x="540" y="305" font-family="Plus Jakarta Sans, sans-serif" font-size="20" fill="{TEXT_MUTED}" text-anchor="middle">APP ICON</text>
  <text x="540" y="332" font-family="Plus Jakarta Sans, sans-serif" font-size="14" fill="{TEXT_MUTED}" text-anchor="middle">300×300px</text>

  <!-- App name -->
  <text x="540" y="510" font-family="Plus Jakarta Sans, sans-serif" font-size="64" font-weight="800"
        fill="{TEXT_PRIMARY}" text-anchor="middle" letter-spacing="-1">
    <!-- [REPLACE: App Name] -->
    App Name
  </text>

  <!-- Tagline -->
  <text x="540" y="580" font-family="Plus Jakarta Sans, sans-serif" font-size="28" font-weight="400"
        fill="{TEXT_SECONDARY}" text-anchor="middle">
    <!-- [REPLACE: App tagline or short description] -->
    Your App Tagline Here
  </text>

  <!-- Version badge -->
  <rect x="458" y="620" width="164" height="48" rx="24" fill="{ACCENT_L}" opacity="0.15"/>
  <rect x="458" y="620" width="164" height="48" rx="24" fill="none" stroke="{ACCENT_L}" stroke-width="1.5"/>
  <text x="540" y="651" font-family="JetBrains Mono, monospace" font-size="20" font-weight="600"
        fill="{ACCENT_L}" text-anchor="middle">
    <!-- [REPLACE: Version] -->
    v1.0.0
  </text>

  <!-- Feature highlights area -->
  <text x="540" y="740" font-family="Plus Jakarta Sans, sans-serif" font-size="18" font-weight="600"
        fill="{TEXT_MUTED}" text-anchor="middle" letter-spacing="4">FEATURES</text>

  <!-- Feature 1 -->
  <circle cx="200" cy="810" r="6" fill="{ACCENT_L}"/>
  <text x="220" y="816" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_SECONDARY}">Feature One</text>

  <!-- Feature 2 -->
  <circle cx="200" cy="858" r="6" fill="{DOT_COLOR}"/>
  <text x="220" y="864" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_SECONDARY}">Feature Two</text>

  <!-- Feature 3 -->
  <circle cx="200" cy="906" r="6" fill="{SKY_BLUE}"/>
  <text x="220" y="912" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_SECONDARY}">Feature Three</text>

  <!-- Website / CTA -->
  <text x="540" y="980" font-family="Plus Jakarta Sans, sans-serif" font-size="20" font-weight="500"
        fill="{TEXT_MUTED}" text-anchor="middle">imadlabs.io · @ImadLabs</text>

  <!-- HexaCore symbol bottom-right -->
  <g transform="translate(880,780) scale(0.55)" filter="url(#glow)">
    <polygon points="100,20 180,66 100,112 20,66" fill="url(#hc-top)" opacity="0.9"/>
    <polygon points="20,76 100,122 100,212 20,166" fill="url(#hc-left)" opacity="0.85"/>
    <polygon points="100,122 180,76 180,166 100,212" fill="url(#hc-right)" opacity="0.75"/>
    <circle cx="100" cy="76" r="14" fill="{DOT_COLOR}"/>
    <circle cx="100" cy="76" r="7" fill="white" opacity="0.9"/>
    <path d="M 100 120 L 100 182 L 152 152" stroke="{ACCENT_L}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <circle cx="152" cy="152" r="5.5" fill="{DOT_COLOR}"/>
  </g>
</svg>"""

    svg_path = os.path.join(out, "app-launch-template-1080x1080.svg")
    png_path = os.path.join(out, "app-launch-template-1080x1080.png")
    save_svg(template_svg, svg_path)
    if rasterize(svg_path, png_path, 1080, 1080):
        print("  ✓ app-launch-template-1080x1080.png")

    # App Update template (landscape 1280x720 for Telegram)
    update_template = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070B14"/>
      <stop offset="100%" stop-color="#0B1520"/>
    </linearGradient>
    <linearGradient id="hc-top" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <linearGradient id="hc-left" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#0066FF"/>
    </linearGradient>
    <linearGradient id="hc-right" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0066FF"/>
      <stop offset="100%" stop-color="#003DB3"/>
    </linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="10" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="1280" height="720" fill="url(#bg)"/>
  <!-- Left stripe -->
  <rect x="0" y="0" width="6" height="720" fill="{ACCENT_L}"/>
  <!-- Header bar -->
  <rect x="0" y="0" width="1280" height="80" fill="{CARD}" opacity="0.8"/>
  <!-- Brand name -->
  <text x="40" y="52" font-family="Plus Jakarta Sans, sans-serif" font-size="26" font-weight="800" fill="{TEXT_PRIMARY}">
    Imad<tspan fill="{ACCENT_L}">Labs</tspan>
  </text>
  <!-- Update label -->
  <rect x="1100" y="20" width="140" height="40" rx="20" fill="{ACCENT_L}"/>
  <text x="1170" y="46" font-family="Plus Jakarta Sans, sans-serif" font-size="18" font-weight="700" fill="#000000" text-anchor="middle">UPDATE</text>
  <!-- App icon placeholder -->
  <rect x="80" y="140" width="200" height="200" rx="44" fill="{CARD}" stroke="{BORDER}" stroke-width="2"/>
  <text x="180" y="248" font-family="Plus Jakarta Sans, sans-serif" font-size="16" fill="{TEXT_MUTED}" text-anchor="middle">APP ICON</text>
  <!-- App name -->
  <text x="320" y="200" font-family="Plus Jakarta Sans, sans-serif" font-size="52" font-weight="800" fill="{TEXT_PRIMARY}">App Name</text>
  <!-- Version -->
  <rect x="320" y="220" width="140" height="38" rx="19" fill="{ACCENT_L}" fill-opacity="0.12"/>
  <rect x="320" y="220" width="140" height="38" rx="19" fill="none" stroke="{ACCENT_L}" stroke-width="1"/>
  <text x="390" y="245" font-family="JetBrains Mono, monospace" font-size="18" fill="{ACCENT_L}" text-anchor="middle">v2.0.0</text>
  <!-- What's new -->
  <text x="320" y="295" font-family="Plus Jakarta Sans, sans-serif" font-size="16" font-weight="600" fill="{TEXT_MUTED}" letter-spacing="3">WHAT'S NEW</text>
  <!-- Changes -->
  <circle cx="330" cy="340" r="5" fill="{ACCENT_L}"/>
  <text x="350" y="347" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_SECONDARY}">New feature or fix here</text>
  <circle cx="330" cy="390" r="5" fill="{DOT_COLOR}"/>
  <text x="350" y="397" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_SECONDARY}">Another improvement</text>
  <circle cx="330" cy="440" r="5" fill="{SKY_BLUE}"/>
  <text x="350" y="447" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_SECONDARY}">Performance enhancements</text>
  <!-- Website -->
  <text x="640" y="680" font-family="Plus Jakarta Sans, sans-serif" font-size="18" fill="{TEXT_MUTED}" text-anchor="middle">imadlabs.io · @ImadLabs</text>
  <!-- HexaCore -->
  <g transform="translate(1080,380) scale(0.5)" filter="url(#glow)">
    <polygon points="100,20 180,66 100,112 20,66" fill="url(#hc-top)" opacity="0.9"/>
    <polygon points="20,76 100,122 100,212 20,166" fill="url(#hc-left)" opacity="0.85"/>
    <polygon points="100,122 180,76 180,166 100,212" fill="url(#hc-right)" opacity="0.75"/>
    <circle cx="100" cy="76" r="14" fill="{DOT_COLOR}"/>
    <circle cx="100" cy="76" r="7" fill="white" opacity="0.9"/>
    <path d="M 100 120 L 100 182 L 152 152" stroke="{ACCENT_L}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <circle cx="152" cy="152" r="5.5" fill="{DOT_COLOR}"/>
  </g>
</svg>"""

    upd_svg = os.path.join(out, "app-update-template-1280x720.svg")
    upd_png = os.path.join(out, "app-update-template-1280x720.png")
    save_svg(update_template, upd_svg)
    if rasterize(upd_svg, upd_png, 1280, 720):
        print("  ✓ app-update-template-1280x720.png")

    # HTML interactive template editor
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ImadLabs App Branding Template Editor</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: {BG_DARK}; color: {TEXT_PRIMARY}; font-family: 'Plus Jakarta Sans', sans-serif; padding: 40px; }}
h1 {{ font-size: 32px; font-weight: 800; margin-bottom: 8px; }}
h1 span {{ color: {ACCENT_L}; }}
.subtitle {{ color: {TEXT_SECONDARY}; margin-bottom: 40px; font-size: 16px; }}
.layout {{ display: grid; grid-template-columns: 320px 1fr; gap: 32px; }}
.panel {{ background: {CARD}; border: 1px solid {BORDER}; border-radius: 16px; padding: 24px; }}
.panel h2 {{ font-size: 16px; font-weight: 700; color: {TEXT_SECONDARY}; margin-bottom: 20px; letter-spacing: 2px; text-transform: uppercase; }}
label {{ display: block; font-size: 13px; color: {TEXT_MUTED}; margin-bottom: 6px; margin-top: 16px; }}
input, textarea {{ width: 100%; background: {SURFACE}; border: 1px solid {BORDER}; border-radius: 8px; color: {TEXT_PRIMARY}; padding: 10px 14px; font-size: 15px; font-family: inherit; outline: none; }}
input:focus, textarea:focus {{ border-color: {ACCENT_L}; }}
textarea {{ height: 80px; resize: vertical; }}
.preview-wrap {{ background: {BG_DARK}; border: 1px solid {BORDER}; border-radius: 16px; overflow: hidden; display: flex; align-items: center; justify-content: center; min-height: 600px; }}
.preview-canvas {{ width: 600px; height: 600px; background: linear-gradient(135deg, #070B14, #0B1520); border-radius: 12px; position: relative; overflow: hidden; }}
.hex-badge {{ position: absolute; bottom: 30px; right: 30px; opacity: 0.7; }}
.wordmark {{ position: absolute; top: 30px; left: 30px; font-size: 18px; font-weight: 800; }}
.wordmark .labs {{ color: {ACCENT_L}; }}
.app-icon-slot {{ width: 180px; height: 180px; background: {CARD}; border: 2px dashed {BORDER}; border-radius: 40px; display: flex; align-items: center; justify-content: center; color: {TEXT_MUTED}; font-size: 13px; margin: 0 auto 24px; cursor: pointer; position: relative; overflow: hidden; }}
.app-icon-slot img {{ width: 100%; height: 100%; object-fit: cover; border-radius: 38px; }}
.app-name-text {{ font-size: 42px; font-weight: 800; text-align: center; margin-bottom: 8px; }}
.app-tag-text {{ font-size: 18px; color: {TEXT_SECONDARY}; text-align: center; margin-bottom: 16px; }}
.version-badge {{ display: inline-block; padding: 6px 18px; border: 1.5px solid {ACCENT_L}; border-radius: 20px; color: {ACCENT_L}; font-family: 'JetBrains Mono', monospace; font-size: 16px; text-align: center; margin: 0 auto 20px; }}
.features-list {{ padding: 0 20px; }}
.feat-item {{ display: flex; align-items: center; gap: 10px; margin-bottom: 10px; font-size: 16px; color: {TEXT_SECONDARY}; }}
.feat-dot {{ width: 8px; height: 8px; border-radius: 50%; background: {ACCENT_L}; flex-shrink: 0; }}
.app-content {{ padding: 30px; display: flex; flex-direction: column; height: 100%; }}
.center {{ text-align: center; }}
</style>
</head>
<body>
<h1>ImadLabs <span>App Branding</span> Template Editor</h1>
<p class="subtitle">Fill in the fields below to generate your app announcement graphic</p>
<div class="layout">
  <div class="panel">
    <h2>App Details</h2>
    <label>App Name</label>
    <input type="text" id="appName" value="My App" oninput="updatePreview()">
    <label>Tagline</label>
    <input type="text" id="tagline" value="Your App Tagline Here" oninput="updatePreview()">
    <label>Version</label>
    <input type="text" id="version" value="v1.0.0" oninput="updatePreview()">
    <label>Feature 1</label>
    <input type="text" id="feat1" value="Amazing new feature" oninput="updatePreview()">
    <label>Feature 2</label>
    <input type="text" id="feat2" value="Blazing fast performance" oninput="updatePreview()">
    <label>Feature 3</label>
    <input type="text" id="feat3" value="Beautiful redesign" oninput="updatePreview()">
    <label>App Icon (click to upload)</label>
    <div class="app-icon-slot" id="iconSlot" onclick="document.getElementById('iconInput').click()">
      <span id="iconPlaceholder">Click to upload icon</span>
      <img id="iconPreview" style="display:none">
    </div>
    <input type="file" id="iconInput" accept="image/*" style="display:none" onchange="loadIcon(this)">
  </div>
  <div class="panel">
    <h2>Preview</h2>
    <div class="preview-wrap">
      <div class="preview-canvas" id="previewCanvas">
        <div class="wordmark">Imad<span class="labs">Labs</span></div>
        <div class="app-content">
          <div style="height:30px"></div>
          <div class="app-icon-slot" style="pointer-events:none;border-style:solid" id="previewIcon">
            <span style="color:{TEXT_MUTED};font-size:13px">APP ICON</span>
          </div>
          <div class="app-name-text" id="prevName">My App</div>
          <div class="app-tag-text" id="prevTag">Your App Tagline Here</div>
          <div class="center"><div class="version-badge" id="prevVer">v1.0.0</div></div>
          <div class="features-list">
            <div class="feat-item"><div class="feat-dot"></div><span id="prevFeat1">Amazing new feature</span></div>
            <div class="feat-item"><div class="feat-dot" style="background:{DOT_COLOR}"></div><span id="prevFeat2">Blazing fast performance</span></div>
            <div class="feat-item"><div class="feat-dot" style="background:{SKY_BLUE}"></div><span id="prevFeat3">Beautiful redesign</span></div>
          </div>
        </div>
        <div class="hex-badge">
          <svg width="60" height="80" viewBox="0 0 200 232">
            <defs>
              <linearGradient id="t" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="{SKY_BLUE}"/><stop offset="100%" stop-color="{BLUE_MID}"/></linearGradient>
              <linearGradient id="l" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="{BLUE_MID}"/><stop offset="100%" stop-color="{BLUE_PRIMARY}"/></linearGradient>
              <linearGradient id="r" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{BLUE_PRIMARY}"/><stop offset="100%" stop-color="#003DB3"/></linearGradient>
            </defs>
            <polygon points="100,20 180,66 100,112 20,66" fill="url(#t)"/>
            <polygon points="20,76 100,122 100,212 20,166" fill="url(#l)"/>
            <polygon points="100,122 180,76 180,166 100,212" fill="url(#r)"/>
            <circle cx="100" cy="76" r="14" fill="{DOT_COLOR}"/>
            <circle cx="100" cy="76" r="7" fill="white" opacity="0.9"/>
            <path d="M100,120 L100,182 L152,152" stroke="{ACCENT_L}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
            <circle cx="152" cy="152" r="5.5" fill="{DOT_COLOR}"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
</div>
<script>
function updatePreview() {{
  document.getElementById('prevName').textContent = document.getElementById('appName').value || 'My App';
  document.getElementById('prevTag').textContent = document.getElementById('tagline').value || 'Tagline';
  document.getElementById('prevVer').textContent = document.getElementById('version').value || 'v1.0.0';
  document.getElementById('prevFeat1').textContent = document.getElementById('feat1').value;
  document.getElementById('prevFeat2').textContent = document.getElementById('feat2').value;
  document.getElementById('prevFeat3').textContent = document.getElementById('feat3').value;
}}
function loadIcon(input) {{
  if (input.files && input.files[0]) {{
    const reader = new FileReader();
    reader.onload = e => {{
      const img = document.getElementById('iconPreview');
      const ph = document.getElementById('iconPlaceholder');
      const prev = document.getElementById('previewIcon');
      img.src = e.target.result;
      img.style.display = 'block';
      ph.style.display = 'none';
      prev.innerHTML = '<img src="' + e.target.result + '" style="width:100%;height:100%;object-fit:cover;border-radius:38px">';
    }};
    reader.readAsDataURL(input.files[0]);
  }}
}}
</script>
</body>
</html>"""

    html_path = os.path.join(out, "app-branding-template-editor.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print("  ✓ app-branding-template-editor.html")
    print("  ✓ App branding templates complete")


# ═══════════════════════════════════════════════════════════════════════════
# 3. SOCIAL MEDIA — MISSING ASSETS
# ═══════════════════════════════════════════════════════════════════════════

def build_social_media_missing():
    print("\n[3/5] Building missing social media assets...")

    def hc_snippet(scale=1.0, ox=0, oy=0):
        s = scale
        return f"""
    <polygon points="{ox+100*s:.0f},{oy+20*s:.0f} {ox+180*s:.0f},{oy+66*s:.0f} {ox+100*s:.0f},{oy+112*s:.0f} {ox+20*s:.0f},{oy+66*s:.0f}" fill="url(#hc-top)" opacity="0.9"/>
    <polygon points="{ox+20*s:.0f},{oy+76*s:.0f} {ox+100*s:.0f},{oy+122*s:.0f} {ox+100*s:.0f},{oy+212*s:.0f} {ox+20*s:.0f},{oy+166*s:.0f}" fill="url(#hc-left)" opacity="0.85"/>
    <polygon points="{ox+100*s:.0f},{oy+122*s:.0f} {ox+180*s:.0f},{oy+76*s:.0f} {ox+180*s:.0f},{oy+166*s:.0f} {ox+100*s:.0f},{oy+212*s:.0f}" fill="url(#hc-right)" opacity="0.75"/>
    <circle cx="{ox+100*s:.0f}" cy="{oy+76*s:.0f}" r="{14*s:.0f}" fill="{DOT_COLOR}"/>
    <circle cx="{ox+100*s:.0f}" cy="{oy+76*s:.0f}" r="{7*s:.0f}" fill="white" opacity="0.9"/>
    <path d="M {ox+100*s:.0f} {oy+120*s:.0f} L {ox+100*s:.0f} {oy+182*s:.0f} L {ox+152*s:.0f} {oy+152*s:.0f}" stroke="{ACCENT_L}" stroke-width="{12*s:.0f}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <circle cx="{ox+152*s:.0f}" cy="{oy+152*s:.0f}" r="{5.5*s:.0f}" fill="{DOT_COLOR}"/>"""

    hc_defs = f"""<defs>
    <linearGradient id="hc-top" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{SKY_BLUE}"/>
      <stop offset="100%" stop-color="{BLUE_MID}"/>
    </linearGradient>
    <linearGradient id="hc-left" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{BLUE_MID}"/>
      <stop offset="100%" stop-color="{BLUE_PRIMARY}"/>
    </linearGradient>
    <linearGradient id="hc-right" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BLUE_PRIMARY}"/>
      <stop offset="100%" stop-color="#003DB3"/>
    </linearGradient>
    <linearGradient id="bg-h" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#070B14"/>
      <stop offset="100%" stop-color="#0B1520"/>
    </linearGradient>
    <linearGradient id="accent-bar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{ACCENT_L}"/>
      <stop offset="100%" stop-color="{DOT_COLOR}"/>
    </linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="10" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>"""

    # ── Facebook Cover 820×312 ──
    fb_out = os.path.join(BASE, "social-media", "facebook")
    os.makedirs(fb_out, exist_ok=True)

    fb_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 312" width="820" height="312">
  {hc_defs}
  <rect width="820" height="312" fill="url(#bg-h)"/>
  <rect x="0" y="0" width="820" height="5" fill="url(#accent-bar)"/>
  <rect x="0" y="307" width="820" height="5" fill="url(#accent-bar)"/>
  <g filter="url(#glow)" transform="translate(60, 40) scale(1.0)">
    {hc_snippet(1.0, 0, 0)}
  </g>
  <text x="300" y="140" font-family="Plus Jakarta Sans, sans-serif" font-size="52" font-weight="800" fill="{TEXT_PRIMARY}">
    Imad<tspan fill="{ACCENT_L}">Labs</tspan>
  </text>
  <text x="300" y="185" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_SECONDARY}">Software Development · Digital Products · Tools</text>
  <text x="300" y="240" font-family="Plus Jakarta Sans, sans-serif" font-size="18" fill="{TEXT_MUTED}">imadlabs.io · @ImadLabs</text>
</svg>"""

    fb_svg_path = os.path.join(fb_out, "facebook-cover-820x312.svg")
    fb_png_path = os.path.join(fb_out, "facebook-cover-820x312.png")
    save_svg(fb_svg, fb_svg_path)
    if rasterize(fb_svg_path, fb_png_path, 820, 312):
        print("  ✓ facebook-cover-820x312.png")

    # Facebook profile (360×360)
    fb_profile_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 360" width="360" height="360">
  {hc_defs}
  <rect width="360" height="360" fill="#070B14"/>
  <g filter="url(#glow)" transform="translate(80, 70) scale(1.0)">
    {hc_snippet(1.0, 0, 0)}
  </g>
  <text x="180" y="300" font-family="Plus Jakarta Sans, sans-serif" font-size="34" font-weight="800" fill="{TEXT_PRIMARY}" text-anchor="middle">
    Imad<tspan fill="{ACCENT_L}">Labs</tspan>
  </text>
</svg>"""
    fb_prof_svg = os.path.join(fb_out, "facebook-profile-360x360.svg")
    fb_prof_png = os.path.join(fb_out, "facebook-profile-360x360.png")
    save_svg(fb_profile_svg, fb_prof_svg)
    if rasterize(fb_prof_svg, fb_prof_png, 360, 360):
        print("  ✓ facebook-profile-360x360.png")

    # ── Instagram Portrait Post 1080×1350 ──
    ig_out = os.path.join(BASE, "social-media", "instagram")
    os.makedirs(ig_out, exist_ok=True)

    ig_portrait = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" width="1080" height="1350">
  {hc_defs}
  <rect width="1080" height="1350" fill="#070B14"/>
  <!-- Gradient overlay top -->
  <rect width="1080" height="400" fill="{ACCENT_L}" fill-opacity="0.04"/>
  <!-- Corner accents -->
  <path d="M 40 80 L 40 40 L 80 40" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.5"/>
  <path d="M 1000 40 L 1040 40 L 1040 80" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.5"/>
  <path d="M 40 1270 L 40 1310 L 80 1310" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.5"/>
  <path d="M 1000 1310 L 1040 1310 L 1040 1270" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.5"/>
  <!-- Large HexaCore centered -->
  <g filter="url(#glow)" transform="translate(340, 180) scale(2.0)">
    {hc_snippet(2.0, 0, 0)}
  </g>
  <!-- Content area -->
  <text x="540" y="730" font-family="Plus Jakarta Sans, sans-serif" font-size="72" font-weight="800"
        fill="{TEXT_PRIMARY}" text-anchor="middle">
    Imad<tspan fill="{ACCENT_L}">Labs</tspan>
  </text>
  <text x="540" y="800" font-family="Plus Jakarta Sans, sans-serif" font-size="28" fill="{TEXT_SECONDARY}" text-anchor="middle">
    Software Development
  </text>
  <!-- Divider -->
  <rect x="440" y="840" width="200" height="2" fill="url(#accent-bar)" rx="1"/>
  <!-- Post content area placeholder -->
  <rect x="60" y="880" width="960" height="340" rx="20" fill="{CARD}" stroke="{BORDER}" stroke-width="1"/>
  <text x="540" y="1040" font-family="Plus Jakarta Sans, sans-serif" font-size="28" fill="{TEXT_MUTED}"
        text-anchor="middle">[Post Content Here]</text>
  <text x="540" y="1080" font-family="Plus Jakarta Sans, sans-serif" font-size="20" fill="{TEXT_MUTED}"
        text-anchor="middle">Replace with your announcement text</text>
  <!-- Footer -->
  <text x="540" y="1300" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_MUTED}"
        text-anchor="middle">@ImadLabs · imadlabs.io</text>
</svg>"""

    ig_port_svg = os.path.join(ig_out, "instagram-portrait-1080x1350.svg")
    ig_port_png = os.path.join(ig_out, "instagram-portrait-1080x1350.png")
    save_svg(ig_portrait, ig_port_svg)
    if rasterize(ig_port_svg, ig_port_png, 1080, 1350):
        print("  ✓ instagram-portrait-1080x1350.png")

    # ── Instagram Story 1080×1920 ──
    ig_story = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1920" width="1080" height="1920">
  {hc_defs}
  <rect width="1080" height="1920" fill="#070B14"/>
  <!-- Top accent stripe -->
  <rect x="0" y="0" width="1080" height="6" fill="url(#accent-bar)"/>
  <!-- Bottom accent stripe -->
  <rect x="0" y="1914" width="1080" height="6" fill="url(#accent-bar)"/>
  <!-- Corner accents -->
  <path d="M 40 100 L 40 60 L 80 60" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.6"/>
  <path d="M 1000 60 L 1040 60 L 1040 100" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.6"/>
  <path d="M 40 1820 L 40 1860 L 80 1860" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.6"/>
  <path d="M 1000 1860 L 1040 1860 L 1040 1820" stroke="{ACCENT_L}" stroke-width="3" fill="none" opacity="0.6"/>
  <!-- Branding top -->
  <text x="540" y="130" font-family="Plus Jakarta Sans, sans-serif" font-size="32" font-weight="800"
        fill="{TEXT_PRIMARY}" text-anchor="middle">
    Imad<tspan fill="{ACCENT_L}">Labs</tspan>
  </text>
  <!-- Large HexaCore -->
  <g filter="url(#glow)" transform="translate(280, 300) scale(2.6)">
    {hc_snippet(2.6, 0, 0)}
  </g>
  <!-- Content center -->
  <text x="540" y="1060" font-family="Plus Jakarta Sans, sans-serif" font-size="80" font-weight="800"
        fill="{TEXT_PRIMARY}" text-anchor="middle">NEW</text>
  <text x="540" y="1150" font-family="Plus Jakarta Sans, sans-serif" font-size="40" font-weight="700"
        fill="{ACCENT_L}" text-anchor="middle">App Name</text>
  <text x="540" y="1220" font-family="Plus Jakarta Sans, sans-serif" font-size="28" fill="{TEXT_SECONDARY}"
        text-anchor="middle">Your announcement here</text>
  <!-- CTA button -->
  <rect x="290" y="1300" width="500" height="80" rx="40" fill="{ACCENT_L}"/>
  <text x="540" y="1350" font-family="Plus Jakarta Sans, sans-serif" font-size="26" font-weight="700"
        fill="#000000" text-anchor="middle">Download Now →</text>
  <!-- Feature list -->
  <circle cx="380" cy="1460" r="6" fill="{ACCENT_L}"/>
  <text x="405" y="1467" font-family="Plus Jakarta Sans, sans-serif" font-size="26" fill="{TEXT_SECONDARY}">Feature One</text>
  <circle cx="380" cy="1520" r="6" fill="{DOT_COLOR}"/>
  <text x="405" y="1527" font-family="Plus Jakarta Sans, sans-serif" font-size="26" fill="{TEXT_SECONDARY}">Feature Two</text>
  <circle cx="380" cy="1580" r="6" fill="{SKY_BLUE}"/>
  <text x="405" y="1587" font-family="Plus Jakarta Sans, sans-serif" font-size="26" fill="{TEXT_SECONDARY}">Feature Three</text>
  <!-- Swipe up / link -->
  <text x="540" y="1800" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_MUTED}"
        text-anchor="middle">Swipe up · imadlabs.io</text>
</svg>"""

    ig_story_svg = os.path.join(ig_out, "instagram-story-1080x1920.svg")
    ig_story_png = os.path.join(ig_out, "instagram-story-1080x1920.png")
    save_svg(ig_story, ig_story_svg)
    if rasterize(ig_story_svg, ig_story_png, 1080, 1920):
        print("  ✓ instagram-story-1080x1920.png")

    # ── YouTube Thumbnail Template 1280×720 ──
    yt_out = os.path.join(BASE, "social-media", "youtube")
    os.makedirs(yt_out, exist_ok=True)

    yt_thumb = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">
  {hc_defs}
  <rect width="1280" height="720" fill="#070B14"/>
  <!-- Left bright gradient -->
  <rect x="0" y="0" width="500" height="720" fill="{ACCENT_L}" fill-opacity="0.05"/>
  <!-- Accent left bar -->
  <rect x="0" y="0" width="8" height="720" fill="url(#accent-bar)"/>
  <!-- HexaCore left -->
  <g filter="url(#glow)" transform="translate(40, 180) scale(1.4)">
    {hc_snippet(1.4, 0, 0)}
  </g>
  <!-- Right content area (dark) -->
  <rect x="600" y="0" width="680" height="720" fill="{CARD}" fill-opacity="0.5"/>
  <!-- Thumbnail title area -->
  <text x="640" y="220" font-family="Plus Jakarta Sans, sans-serif" font-size="22" font-weight="600"
        fill="{ACCENT_L}" letter-spacing="3">NEW RELEASE</text>
  <text x="640" y="320" font-family="Plus Jakarta Sans, sans-serif" font-size="64" font-weight="800"
        fill="{TEXT_PRIMARY}">App</text>
  <text x="640" y="400" font-family="Plus Jakarta Sans, sans-serif" font-size="64" font-weight="800"
        fill="{ACCENT_L}">Name</text>
  <text x="640" y="460" font-family="Plus Jakarta Sans, sans-serif" font-size="24" fill="{TEXT_SECONDARY}">Feature or announcement text</text>
  <!-- Version -->
  <rect x="640" y="500" width="120" height="40" rx="20" fill="{ACCENT_L}" fill-opacity="0.15"/>
  <rect x="640" y="500" width="120" height="40" rx="20" fill="none" stroke="{ACCENT_L}" stroke-width="1.5"/>
  <text x="700" y="526" font-family="JetBrains Mono, monospace" font-size="18" fill="{ACCENT_L}" text-anchor="middle">v1.0.0</text>
  <!-- Brand tag bottom right -->
  <text x="1240" y="698" font-family="Plus Jakarta Sans, sans-serif" font-size="18" font-weight="700"
        fill="{TEXT_SECONDARY}" text-anchor="end">ImadLabs</text>
</svg>"""

    yt_svg = os.path.join(yt_out, "youtube-thumbnail-template-1280x720.svg")
    yt_png = os.path.join(yt_out, "youtube-thumbnail-template-1280x720.png")
    save_svg(yt_thumb, yt_svg)
    if rasterize(yt_svg, yt_png, 1280, 720):
        print("  ✓ youtube-thumbnail-template-1280x720.png")

    # ── X (Twitter) Portrait Post 1080×1350 ──
    x_out = os.path.join(BASE, "social-media", "x")
    os.makedirs(x_out, exist_ok=True)

    x_portrait = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" width="1080" height="1350">
  {hc_defs}
  <rect width="1080" height="1350" fill="#070B14"/>
  <rect x="0" y="0" width="1080" height="6" fill="url(#accent-bar)"/>
  <g filter="url(#glow)" transform="translate(340, 200) scale(2.0)">
    {hc_snippet(2.0, 0, 0)}
  </g>
  <text x="540" y="760" font-family="Plus Jakarta Sans, sans-serif" font-size="68" font-weight="800"
        fill="{TEXT_PRIMARY}" text-anchor="middle">
    Imad<tspan fill="{ACCENT_L}">Labs</tspan>
  </text>
  <text x="540" y="830" font-family="Plus Jakarta Sans, sans-serif" font-size="26" fill="{TEXT_SECONDARY}"
        text-anchor="middle">Building the future of digital tools</text>
  <rect x="440" y="870" width="200" height="2" fill="url(#accent-bar)" rx="1"/>
  <text x="540" y="960" font-family="Plus Jakarta Sans, sans-serif" font-size="32" fill="{TEXT_PRIMARY}"
        text-anchor="middle">[Post headline here]</text>
  <text x="540" y="1020" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_SECONDARY}"
        text-anchor="middle">Replace with your tweet content</text>
  <text x="540" y="1290" font-family="Plus Jakarta Sans, sans-serif" font-size="22" fill="{TEXT_MUTED}"
        text-anchor="middle">@ImadLabs · imadlabs.io</text>
</svg>"""

    x_svg = os.path.join(x_out, "x-portrait-1080x1350.svg")
    x_png = os.path.join(x_out, "x-portrait-1080x1350.png")
    save_svg(x_portrait, x_svg)
    if rasterize(x_svg, x_png, 1080, 1350):
        print("  ✓ x-portrait-1080x1350.png")

    print("  ✓ Social media missing assets complete")


# ═══════════════════════════════════════════════════════════════════════════
# 4. MARKETING — ADDITIONAL TEMPLATES
# ═══════════════════════════════════════════════════════════════════════════

def build_marketing_extra():
    print("\n[4/5] Building extra marketing assets...")

    def hc_at(ox, oy, scale, gid="hc"):
        s = scale
        return f"""
  <g id="{gid}">
    <polygon points="{ox+100*s:.0f},{oy+20*s:.0f} {ox+180*s:.0f},{oy+66*s:.0f} {ox+100*s:.0f},{oy+112*s:.0f} {ox+20*s:.0f},{oy+66*s:.0f}" fill="url(#hc-top)" opacity="0.9"/>
    <polygon points="{ox+20*s:.0f},{oy+76*s:.0f} {ox+100*s:.0f},{oy+122*s:.0f} {ox+100*s:.0f},{oy+212*s:.0f} {ox+20*s:.0f},{oy+166*s:.0f}" fill="url(#hc-left)" opacity="0.85"/>
    <polygon points="{ox+100*s:.0f},{oy+122*s:.0f} {ox+180*s:.0f},{oy+76*s:.0f} {ox+180*s:.0f},{oy+166*s:.0f} {ox+100*s:.0f},{oy+212*s:.0f}" fill="url(#hc-right)" opacity="0.75"/>
    <circle cx="{ox+100*s:.0f}" cy="{oy+76*s:.0f}" r="{14*s:.0f}" fill="{DOT_COLOR}"/>
    <circle cx="{ox+100*s:.0f}" cy="{oy+76*s:.0f}" r="{7*s:.0f}" fill="white" opacity="0.9"/>
    <path d="M {ox+100*s:.0f} {oy+120*s:.0f} L {ox+100*s:.0f} {oy+182*s:.0f} L {ox+152*s:.0f} {oy+152*s:.0f}" stroke="{ACCENT_L}" stroke-width="{12*s:.0f}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <circle cx="{ox+152*s:.0f}" cy="{oy+152*s:.0f}" r="{5.5*s:.0f}" fill="{DOT_COLOR}"/>
  </g>"""

    hc_defs_str = f"""<defs>
    <linearGradient id="hc-top" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="{SKY_BLUE}"/><stop offset="100%" stop-color="{BLUE_MID}"/></linearGradient>
    <linearGradient id="hc-left" x1="100%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="{BLUE_MID}"/><stop offset="100%" stop-color="{BLUE_PRIMARY}"/></linearGradient>
    <linearGradient id="hc-right" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{BLUE_PRIMARY}"/><stop offset="100%" stop-color="#003DB3"/></linearGradient>
    <linearGradient id="acc" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="{ACCENT_L}"/><stop offset="100%" stop-color="{DOT_COLOR}"/></linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="10" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>"""

    # Business card 1050×600
    bc_out = os.path.join(BASE, "marketing")
    os.makedirs(bc_out, exist_ok=True)

    bc_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1050 600" width="1050" height="600">
  {hc_defs_str}
  <!-- Front card -->
  <rect x="0" y="30" width="490" height="290" rx="20" fill="#0B0F19"/>
  <rect x="0" y="30" width="490" height="290" rx="20" fill="none" stroke="{BORDER}" stroke-width="1.5"/>
  <rect x="0" y="30" width="490" height="5" rx="2" fill="url(#acc)" opacity="0.6"/>
  <g filter="url(#glow)" transform="translate(30, 80) scale(0.65)">
    {hc_at(0, 0, 0.65)}
  </g>
  <text x="140" y="120" font-family="Plus Jakarta Sans, sans-serif" font-size="32" font-weight="800" fill="{TEXT_PRIMARY}">
    Imad<tspan fill="{ACCENT_L}">Labs</tspan>
  </text>
  <text x="140" y="155" font-family="Plus Jakarta Sans, sans-serif" font-size="16" fill="{TEXT_SECONDARY}">Software Development Studio</text>
  <text x="30" y="250" font-family="Plus Jakarta Sans, sans-serif" font-size="14" fill="{TEXT_MUTED}">imadlabs.io</text>
  <text x="30" y="274" font-family="Plus Jakarta Sans, sans-serif" font-size="14" fill="{TEXT_MUTED}">@ImadLabs</text>
  <!-- Back card -->
  <rect x="560" y="30" width="490" height="290" rx="20" fill="#070B14"/>
  <rect x="560" y="30" width="490" height="290" rx="20" fill="none" stroke="{BORDER}" stroke-width="1.5"/>
  <g filter="url(#glow)" transform="translate(660, 80) scale(1.0)">
    {hc_at(0, 0, 1.0)}
  </g>
  <text x="805" y="240" font-family="Plus Jakarta Sans, sans-serif" font-size="26" font-weight="800"
        fill="{TEXT_PRIMARY}" text-anchor="middle">
    Imad<tspan fill="{ACCENT_L}">Labs</tspan>
  </text>
  <text x="30" y="380" font-family="Plus Jakarta Sans, sans-serif" font-size="18" font-weight="700"
        fill="{TEXT_SECONDARY}">Business Card — Front &amp; Back</text>
  <text x="30" y="408" font-family="Plus Jakarta Sans, sans-serif" font-size="14" fill="{TEXT_MUTED}">3.5 × 2 inches · 300 DPI print-ready</text>
</svg>"""

    bc_svg_path = os.path.join(bc_out, "business-card-design.svg")
    bc_png_path = os.path.join(bc_out, "business-card-design.png")
    save_svg(bc_svg, bc_svg_path)
    if rasterize(bc_svg_path, bc_png_path, 1050, 600):
        print("  ✓ business-card-design.png")

    # Email signature banner 600×120
    sig_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 120" width="600" height="120">
  {hc_defs_str}
  <rect width="600" height="120" fill="#070B14"/>
  <rect x="0" y="0" width="600" height="3" fill="url(#acc)"/>
  <g filter="url(#glow)" transform="translate(15, 15) scale(0.45)">
    {hc_at(0, 0, 0.45)}
  </g>
  <text x="100" y="52" font-family="Plus Jakarta Sans, sans-serif" font-size="26" font-weight="800" fill="{TEXT_PRIMARY}">
    Imad<tspan fill="{ACCENT_L}">Labs</tspan>
  </text>
  <text x="100" y="78" font-family="Plus Jakarta Sans, sans-serif" font-size="14" fill="{TEXT_SECONDARY}">Software Development · Digital Products</text>
  <text x="100" y="100" font-family="Plus Jakarta Sans, sans-serif" font-size="13" fill="{TEXT_MUTED}">imadlabs.io · @ImadLabs</text>
  <rect x="560" y="10" width="30" height="100" rx="4" fill="{ACCENT_L}" fill-opacity="0.15"/>
</svg>"""

    sig_svg_path = os.path.join(bc_out, "email-signature-banner-600x120.svg")
    sig_png_path = os.path.join(bc_out, "email-signature-banner-600x120.png")
    save_svg(sig_svg, sig_svg_path)
    if rasterize(sig_svg_path, sig_png_path, 600, 120):
        print("  ✓ email-signature-banner-600x120.png")

    print("  ✓ Extra marketing assets complete")


# ═══════════════════════════════════════════════════════════════════════════
# 5. REBUILD ASSET CATALOG
# ═══════════════════════════════════════════════════════════════════════════

def rebuild_asset_catalog():
    print("\n[5/5] Rebuilding ASSET_CATALOG.md...")
    catalog_script = os.path.join(BASE, "tools", "build_asset_catalog.py")
    if os.path.exists(catalog_script):
        res = subprocess.run(["python", catalog_script], capture_output=True, text=True, cwd=BASE)
        if res.returncode == 0:
            print("  ✓ ASSET_CATALOG.md rebuilt")
        else:
            print(f"  ⚠ Catalog rebuild warning: {res.stderr[:200]}")
    else:
        print("  ⚠ build_asset_catalog.py not found, skipping")


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("  ImadLabs Brand Factory — Final Completion v1.3.0")
    print("=" * 60)

    build_icon_concepts()
    build_app_branding_templates()
    build_social_media_missing()
    build_marketing_extra()
    rebuild_asset_catalog()

    print("\n" + "=" * 60)
    print("  ✅ Brand Factory Complete!")
    print("=" * 60)
