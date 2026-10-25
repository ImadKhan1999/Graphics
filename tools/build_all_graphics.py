"""
ImadLabs Brand Studio - Comprehensive Graphics Factory
Builds all Telegram assets, App Icons (iTube, Hyper Downloader),
Social Media suites, Marketing templates, Favicons, and multi-resolution ICOs
using the approved HexaCore Matrix (Cyber Mint #00F5A0 L-pathway and #00FFC2 quantum dot).
"""

import os
import subprocess
from PIL import Image

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def rasterize_svg(svg_path, png_path, width, height):
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--screenshot={png_path}",
        f"--window-size={width},{height}",
        "--default-background-color=00000000",
        "--hide-scrollbars",
        svg_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.returncode == 0 and os.path.exists(png_path)

def make_ico(png_source_path, ico_dest_path, sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]):
    img = Image.open(png_source_path)
    img.save(ico_dest_path, format="ICO", sizes=sizes)
    print(f"Created ICO: {ico_dest_path}")

def get_hexacore_snippet(scale=1.0, is_dark=True):
    top_stop1 = "#38BDF8" if is_dark else "#0284C7"
    top_stop2 = "#0284C7" if is_dark else "#0369A1"
    left_stop1 = "#0284C7" if is_dark else "#0369A1"
    left_stop2 = "#0B1930" if is_dark else "#075985"
    right_stop1 = "#0066FF" if is_dark else "#2563EB"
    right_stop2 = "#0284C7" if is_dark else "#0284C7"
    aperture_fill = "#050A14" if is_dark else "#F1F5F9"

    return f'''
    <defs>
        <linearGradient id="g_hex_top" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{top_stop1}"/>
            <stop offset="100%" stop-color="{top_stop2}"/>
        </linearGradient>
        <linearGradient id="g_hex_left" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{left_stop1}"/>
            <stop offset="100%" stop-color="{left_stop2}"/>
        </linearGradient>
        <linearGradient id="g_hex_right" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{right_stop1}"/>
            <stop offset="100%" stop-color="{right_stop2}"/>
        </linearGradient>
        <filter id="g_glow_mint" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="8" result="blur"/>
            <feComposite in="SourceGraphic" in2="blur" operator="over"/>
        </filter>
    </defs>
    <g transform="scale({scale})">
        <polygon points="100,20 180,66 100,112 20,66" fill="url(#g_hex_top)"/>
        <polygon points="20,76 100,122 100,212 20,166" fill="url(#g_hex_left)"/>
        <polygon points="100,122 180,76 180,166 100,212" fill="url(#g_hex_right)"/>
        <polygon points="100,50 145,76 100,102 55,76" fill="{aperture_fill}" opacity="0.9"/>
        <circle cx="100" cy="76" r="14" fill="#00FFC2" filter="url(#g_glow_mint)"/>
        <circle cx="100" cy="76" r="7" fill="#FFFFFF"/>
        <path d="M 100 122 L 100 182 L 152 152" stroke="#00F5A0" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none" filter="url(#g_glow_mint)"/>
        <path d="M 100 125 L 100 180 L 150 151" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none" opacity="0.8"/>
        <circle cx="152" cy="152" r="5" fill="#00FFC2"/>
    </g>
    '''

# --- 1. TELEGRAM PACKAGE ---

def build_telegram_package():
    tg_dir = os.path.abspath("brand/telegram")
    tg_social_dir = os.path.abspath("social-media/telegram")
    templates_dir = os.path.abspath("templates/social-posts")
    os.makedirs(tg_dir, exist_ok=True)
    os.makedirs(tg_social_dir, exist_ok=True)
    os.makedirs(templates_dir, exist_ok=True)

    # 1. Telegram Profile Picture (1024x1024 Master) - Dark Mode
    profile_dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
    <defs>
        <radialGradient id="tg_bg_grad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#0F172A"/>
            <stop offset="100%" stop-color="#050811"/>
        </radialGradient>
    </defs>
    <rect width="1024" height="1024" fill="url(#tg_bg_grad)"/>
    <circle cx="512" cy="512" r="480" fill="none" stroke="#1E293B" stroke-width="2" stroke-dasharray="12 12"/>
    <circle cx="512" cy="512" r="420" fill="none" stroke="#00F5A0" stroke-width="1.5" opacity="0.25"/>

    <!-- Centered HexaCore Matrix scaled 3.0x -->
    <g transform="translate(212, 180)">
        {get_hexacore_snippet(scale=3.0, is_dark=True)}
    </g>
</svg>'''

    # 2. Telegram Profile Picture - Light Mode
    profile_light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
    <defs>
        <radialGradient id="tg_bg_light" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#FFFFFF"/>
            <stop offset="100%" stop-color="#F1F5F9"/>
        </radialGradient>
    </defs>
    <rect width="1024" height="1024" fill="url(#tg_bg_light)"/>
    <circle cx="512" cy="512" r="480" fill="none" stroke="#E2E8F0" stroke-width="2"/>
    <g transform="translate(212, 180)">
        {get_hexacore_snippet(scale=3.0, is_dark=False)}
    </g>
</svg>'''

    for name, content in [
        ("telegram-avatar-1024-dark", profile_dark_svg),
        ("telegram-avatar-1024-light", profile_light_svg)
    ]:
        s_path = os.path.join(tg_dir, f"{name}.svg")
        p_path = os.path.join(tg_dir, f"{name}.png")
        with open(s_path, "w", encoding="utf-8") as f: f.write(content)
        rasterize_svg(s_path, p_path, 1024, 1024)
        with open(os.path.join(tg_social_dir, f"{name}.svg"), "w", encoding="utf-8") as f: f.write(content)
        rasterize_svg(s_path, os.path.join(tg_social_dir, f"{name}.png"), 1024, 1024)

    # 3. Post Announcement Templates (1280x720)
    templates = [
        {
            "filename": "telegram-template-welcome",
            "badge": "OFFICIAL COMMUNITY",
            "title": "Welcome to ImadLabs",
            "subtitle": "Engineering modern desktop utilities, media downloaders & digital tools.",
            "bullet1": "🚀 Early access to new application releases",
            "bullet2": "⚡ Ultra-fast performance updates & changelogs",
            "bullet3": "💡 Direct developer feedback and feature requests",
            "cta": "Join the channel & stay tuned: @ImadLabs"
        },
        {
            "filename": "telegram-template-app-release",
            "badge": "NEW APPLICATION LAUNCH",
            "title": "Introducing [APP_NAME] v1.0",
            "subtitle": "Next-generation utility built for speed, simplicity, and power.",
            "bullet1": "✨ High-speed multi-threaded engine",
            "bullet2": "🎨 Clean modern glassmorphic interface",
            "bullet3": "🛡️ 100% Secure, privacy-first architecture",
            "cta": "Download now at: imadlabs.com/[app-slug]"
        },
        {
            "filename": "telegram-template-app-update",
            "badge": "RELEASE UPDATE • V[VERSION]",
            "title": "[APP_NAME] Update Released",
            "subtitle": "Performance improvements, enhanced stability, and new capabilities.",
            "bullet1": "⚡ Up to 40% faster throughput and responsiveness",
            "bullet2": "🐛 Bug fixes and stability optimizations",
            "bullet3": "🌟 Revamped dark mode and refined UI controls",
            "cta": "Update available via auto-updater or: imadlabs.com/updates"
        },
        {
            "filename": "telegram-template-feature-announcement",
            "badge": "NEW CAPABILITY",
            "title": "Major Feature: [FEATURE_NAME]",
            "subtitle": "Expanding productivity with smart automated workflows.",
            "bullet1": "🔥 Deep integration with popular formats and services",
            "bullet2": "⚙️ Granular customization and power-user shortcuts",
            "bullet3": "📊 Real-time analytics and progress monitoring",
            "cta": "Explore feature details: imadlabs.com/features"
        },
        {
            "filename": "telegram-template-milestone",
            "badge": "COMMUNITY MILESTONE",
            "title": "Celebrating [MILESTONE]!",
            "subtitle": "Thank you for supporting ImadLabs applications worldwide.",
            "bullet1": "🎉 Over [NUMBER] active daily downloads",
            "bullet2": "🌍 Trusted by users across 120+ countries",
            "bullet3": "🚀 Exciting new roadmap items coming soon",
            "cta": "Discover our software catalog: imadlabs.com"
        },
        {
            "filename": "telegram-template-promotional",
            "badge": "SPECIAL SPOTLIGHT",
            "title": "Discover the ImadLabs Suite",
            "subtitle": "A complete ecosystem of software engineered for modern workflows.",
            "bullet1": "📺 iTube — Seamless video streaming & media downloader",
            "bullet2": "⚡ Hyper Downloader — Turbo-charged multi-threaded manager",
            "bullet3": "🛠️ System Utilities — Lightweight, reliable, portable",
            "cta": "Get the complete bundle: imadlabs.com/apps"
        }
    ]

    for t in templates:
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">
        <defs>
            <linearGradient id="t_bg_{t['filename']}" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#070B14"/>
                <stop offset="60%" stop-color="#0E1626"/>
                <stop offset="100%" stop-color="#080D18"/>
            </linearGradient>
            <pattern id="t_grid_{t['filename']}" width="40" height="40" patternUnits="userSpaceOnUse">
                <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1E293B" stroke-width="0.7" opacity="0.6"/>
            </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#t_bg_{t['filename']})"/>
        <rect width="100%" height="100%" fill="url(#t_grid_{t['filename']})"/>

        <!-- Ambient Glow -->
        <circle cx="1100" cy="200" r="350" fill="#0066FF" opacity="0.12" filter="blur(60px)"/>
        <circle cx="200" cy="600" r="250" fill="#00F5A0" opacity="0.08" filter="blur(50px)"/>

        <!-- Header Brand Bar -->
        <g transform="translate(80, 65)">
            <g transform="translate(0, -10) scale(0.38)">
                {get_hexacore_snippet(scale=1.0, is_dark=True)}
            </g>
            <text x="85" y="44" font-family="'Plus Jakarta Sans', sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">Imad<tspan fill="#00F5A0">Labs</tspan></text>
            <text x="235" y="44" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" fill="#64748B">/ OFFICIAL TELEGRAM</text>
        </g>

        <!-- Main Card Container -->
        <g transform="translate(80, 160)">
            <rect width="1120" height="480" rx="20" fill="#0E1626" stroke="#1E293B" stroke-width="2"/>

            <!-- Badge -->
            <rect x="50" y="45" width="260" height="32" rx="8" fill="#162238" stroke="#00F5A0" stroke-width="1"/>
            <text x="180" y="66" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" letter-spacing="1.5" fill="#00F5A0" text-anchor="middle">{t['badge']}</text>

            <!-- Headline -->
            <text x="50" y="130" font-family="'Plus Jakarta Sans', sans-serif" font-size="44" font-weight="800" fill="#FFFFFF">{t['title']}</text>
            <text x="50" y="175" font-family="'Inter', sans-serif" font-size="18" font-weight="400" fill="#94A3B8">{t['subtitle']}</text>

            <!-- Divider -->
            <line x1="50" y1="215" x2="1070" y2="215" stroke="#1E293B" stroke-width="1.5"/>

            <!-- Bullet Points -->
            <g transform="translate(50, 260)">
                <text x="0" y="0" font-family="'Inter', sans-serif" font-size="18" font-weight="600" fill="#F8FAFC">{t['bullet1']}</text>
                <text x="0" y="44" font-family="'Inter', sans-serif" font-size="18" font-weight="600" fill="#F8FAFC">{t['bullet2']}</text>
                <text x="0" y="88" font-family="'Inter', sans-serif" font-size="18" font-weight="600" fill="#F8FAFC">{t['bullet3']}</text>
            </g>

            <!-- Bottom CTA Pill -->
            <g transform="translate(50, 400)">
                <rect width="1020" height="50" rx="10" fill="#131F35" stroke="#00F5A0" stroke-width="1" opacity="0.9"/>
                <text x="510" y="31" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700" fill="#00F5A0" text-anchor="middle">👉 {t['cta']}</text>
            </g>
        </g>
    </svg>'''

        s_file = os.path.join(tg_dir, f"{t['filename']}.svg")
        p_file = os.path.join(tg_dir, f"{t['filename']}.png")
        with open(s_file, "w", encoding="utf-8") as f: f.write(svg_content)
        rasterize_svg(s_file, p_file, 1280, 720)
        with open(os.path.join(templates_dir, f"{t['filename']}.svg"), "w", encoding="utf-8") as f: f.write(svg_content)

    print("Telegram package and templates refreshed with HexaCore Matrix!")

# --- 2. SOCIAL MEDIA & MARKETING ---

def build_social_media():
    social_root = os.path.abspath("social-media")
    marketing_root = os.path.abspath("marketing")

    # YouTube Banner (2560x1440)
    yt_banner_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="2560" height="1440" viewBox="0 0 2560 1440">
    <defs>
        <linearGradient id="yt_bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#070B14"/>
            <stop offset="50%" stop-color="#0E1626"/>
            <stop offset="100%" stop-color="#050811"/>
        </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#yt_bg)"/>

    <g transform="translate(680, 560)">
        <g transform="translate(0, 0)">
            {get_hexacore_snippet(scale=1.5, is_dark=True)}
        </g>
        <g transform="translate(340, 150)">
            <text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="104" font-weight="800" fill="#FFFFFF">Imad<tspan fill="#00F5A0">Labs</tspan></text>
            <text x="4" y="44" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="700" letter-spacing="8" fill="#94A3B8">SOFTWARE DEVELOPMENT &amp; DIGITAL PRODUCTS</text>
        </g>
    </g>
</svg>'''

    yt_s = os.path.join(social_root, "youtube", "youtube-channel-banner-2560x1440.svg")
    yt_p = os.path.join(social_root, "youtube", "youtube-channel-banner-2560x1440.png")
    with open(yt_s, "w", encoding="utf-8") as f: f.write(yt_banner_svg)
    rasterize_svg(yt_s, yt_p, 2560, 1440)

    # Twitter / X Header (1500x500)
    x_header_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="500" viewBox="0 0 1500 500">
    <defs>
        <linearGradient id="x_bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#070B14"/>
            <stop offset="100%" stop-color="#0E1626"/>
        </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#x_bg)"/>
    <g transform="translate(460, 130)">
        <g transform="translate(0, 0)">
            {get_hexacore_snippet(scale=1.15, is_dark=True)}
        </g>
        <g transform="translate(260, 130)">
            <text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="76" font-weight="800" fill="#FFFFFF">Imad<tspan fill="#00F5A0">Labs</tspan></text>
            <text x="4" y="34" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="700" letter-spacing="6" fill="#94A3B8">SOFTWARE &amp; UTILITIES</text>
        </g>
    </g>
</svg>'''
    x_s = os.path.join(social_root, "x", "x-header-1500x500.svg")
    x_p = os.path.join(social_root, "x", "x-header-1500x500.png")
    with open(x_s, "w", encoding="utf-8") as f: f.write(x_header_svg)
    rasterize_svg(x_s, x_p, 1500, 500)

    # LinkedIn Cover (1584x396)
    li_s = os.path.join(social_root, "linkedin", "linkedin-cover-1584x396.svg")
    li_p = os.path.join(social_root, "linkedin", "linkedin-cover-1584x396.png")
    with open(li_s, "w", encoding="utf-8") as f: 
        f.write(x_header_svg.replace('width="1500" height="500"', 'width="1584" height="396"').replace('viewBox="0 0 1500 500"', 'viewBox="0 0 1584 396"'))
    rasterize_svg(li_s, li_p, 1584, 396)

    # Instagram Square Post (1080x1080)
    ig_square_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080" viewBox="0 0 1080 1080">
    <defs>
        <linearGradient id="ig_bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#070B14"/>
            <stop offset="100%" stop-color="#111827"/>
        </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#ig_bg)"/>
    <rect x="50" y="50" width="980" height="980" rx="24" fill="none" stroke="#1E293B" stroke-width="2"/>
    <g transform="translate(290, 240)">
        {get_hexacore_snippet(scale=2.5, is_dark=True)}
    </g>
    <g transform="translate(540, 830)">
        <text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="64" font-weight="800" fill="#FFFFFF" text-anchor="middle">Imad<tspan fill="#00F5A0">Labs</tspan></text>
        <text x="0" y="38" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="700" letter-spacing="6" fill="#94A3B8" text-anchor="middle">NEXT-GEN SOFTWARE CREATION</text>
    </g>
</svg>'''
    ig_s = os.path.join(social_root, "instagram", "instagram-post-square-1080x1080.svg")
    ig_p = os.path.join(social_root, "instagram", "instagram-post-square-1080x1080.png")
    with open(ig_s, "w", encoding="utf-8") as f: f.write(ig_square_svg)
    rasterize_svg(ig_s, ig_p, 1080, 1080)

    # Marketing Launch Poster (1920x1080)
    launch_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">
    <defs>
        <linearGradient id="m_bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050811"/>
            <stop offset="50%" stop-color="#0B1120"/>
            <stop offset="100%" stop-color="#050811"/>
        </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#m_bg)"/>
    <g transform="translate(180, 240)">
        <rect x="0" y="0" width="220" height="38" rx="8" fill="#162238" stroke="#00F5A0" stroke-width="1"/>
        <text x="110" y="24" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" letter-spacing="2" fill="#00F5A0" text-anchor="middle">OFFICIAL LAUNCH</text>
        <text x="0" y="140" font-family="'Plus Jakarta Sans', sans-serif" font-size="84" font-weight="900" fill="#FFFFFF">Imad<tspan fill="#00F5A0">Labs</tspan> Software Suite</text>
        <text x="0" y="210" font-family="'Inter', sans-serif" font-size="26" font-weight="400" fill="#94A3B8">High-performance downloaders, media tools, and modern utilities engineered for speed.</text>
    </g>
    <g transform="translate(1220, 260)">
        {get_hexacore_snippet(scale=2.8, is_dark=True)}
    </g>
</svg>'''
    m_s = os.path.join(marketing_root, "launches", "product-launch-hero-1920x1080.svg")
    m_p = os.path.join(marketing_root, "launches", "product-launch-hero-1920x1080.png")
    with open(m_s, "w", encoding="utf-8") as f: f.write(launch_svg)
    rasterize_svg(m_s, m_p, 1920, 1080)

    print("Social and marketing graphics rebuilt with HexaCore Matrix!")

# --- 3. REFRESH TEMPLATE APP ---
def build_template_app():
    tmpl_dir = os.path.abspath("apps/template")
    m_svg = os.path.join(tmpl_dir, "template-master-icon.svg")
    m_png = os.path.join(tmpl_dir, "template-1024x1024.png")
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
    <rect width="100%" height="100%" fill="#070B14" rx="224"/>
    <rect x="12" y="12" width="1000" height="1000" rx="214" fill="none" stroke="#1E293B" stroke-width="4"/>
    <g transform="translate(212, 180)">
        {get_hexacore_snippet(scale=3.0, is_dark=True)}
    </g>
</svg>'''
    with open(m_svg, "w", encoding="utf-8") as f: f.write(svg_content)
    rasterize_svg(m_svg, m_png, 1024, 1024)
    make_ico(m_png, os.path.join(tmpl_dir, "windows", "template.ico"))
    make_ico(m_png, os.path.join(tmpl_dir, "web", "favicon.ico"))
    print("Template app refreshed with HexaCore Matrix!")

def main():
    print("Executing graphics pipeline for HexaCore Matrix...")
    build_telegram_package()
    build_social_media()
    build_template_app()
    print("Graphics pipeline completed!")

if __name__ == '__main__':
    main()
