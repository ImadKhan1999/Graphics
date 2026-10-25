"""
ImadLabs Brand Studio - Master Polish & Perfection Engine
Applies luxury specular bevels, multi-layer refractive gradients,
enhanced app icons (iTube & Hyper Downloader in HexaCore DNA),
multi-platform presets, and developer integration files.
"""

import os
import subprocess
import shutil
from PIL import Image

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def rasterize_svg(svg_path, png_path, width, height, transparent=True):
    os.makedirs(os.path.dirname(os.path.abspath(png_path)), exist_ok=True)
    bg_color_flag = "--default-background-color=00000000" if transparent else "--default-background-color=FFFFFFFF"
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--screenshot={os.path.abspath(png_path)}",
        f"--window-size={width},{height}",
        bg_color_flag,
        "--hide-scrollbars",
        os.path.abspath(svg_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.returncode == 0 and os.path.exists(png_path)

def make_ico(png_source_path, ico_dest_path, sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]):
    os.makedirs(os.path.dirname(os.path.abspath(ico_dest_path)), exist_ok=True)
    img = Image.open(png_source_path)
    img.save(ico_dest_path, format="ICO", sizes=sizes)

def get_perfected_hexacore_svg(is_dark=True, is_monochrome=False, mono_color="#FFFFFF", is_outline=False, is_simplified=False, accent_l="#00F5A0", dot_color="#00FFC2"):
    """
    Luxury-grade HexaCore Matrix vector with specular edge bevels,
    recessed quantum well, illuminated neon L conduit, and photon spark.
    """
    if is_monochrome:
        return f'''
        <!-- Monochrome HexaCore -->
        <g id="hexacore-mono">
            <polygon points="100,20 180,66 100,112 20,66" fill="{mono_color}" opacity="0.9"/>
            <polygon points="20,76 100,122 100,212 20,166" fill="{mono_color}" opacity="0.6"/>
            <polygon points="100,122 180,76 180,166 100,212" fill="{mono_color}" opacity="0.4"/>
            <circle cx="100" cy="76" r="14" fill="{ '#000000' if mono_color == '#FFFFFF' else '#FFFFFF' }"/>
            <path d="M 100 120 L 100 182 L 152 152" stroke="{ '#000000' if mono_color == '#FFFFFF' else '#FFFFFF' }" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        </g>
        '''
    elif is_outline:
        stroke_base = "#38BDF8" if is_dark else "#0284C7"
        return f'''
        <!-- Outline HexaCore -->
        <g id="hexacore-outline">
            <polygon points="100,20 180,66 100,112 20,66" fill="none" stroke="{stroke_base}" stroke-width="6"/>
            <polygon points="20,76 100,122 100,212 20,166" fill="none" stroke="{stroke_base}" stroke-width="6"/>
            <polygon points="100,122 180,76 180,166 100,212" fill="none" stroke="{stroke_base}" stroke-width="6"/>
            <circle cx="100" cy="76" r="10" fill="none" stroke="{dot_color}" stroke-width="6"/>
            <path d="M 100 120 L 100 182 L 152 152" stroke="{accent_l}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        </g>
        '''
    elif is_simplified:
        return f'''
        <!-- Simplified Small (16-32px) -->
        <g id="hexacore-small">
            <polygon points="100,20 180,66 100,112 20,66" fill="#38BDF8"/>
            <polygon points="20,76 100,122 100,212 20,166" fill="#0284C7"/>
            <polygon points="100,122 180,76 180,166 100,212" fill="#0066FF"/>
            <circle cx="100" cy="76" r="18" fill="{dot_color}"/>
            <path d="M 100 118 L 100 182 L 154 151" stroke="{accent_l}" stroke-width="20" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        </g>
        '''

    # High-Definition Luxury Vector
    top_stop1 = "#38BDF8" if is_dark else "#0284C7"
    top_stop2 = "#0284C7" if is_dark else "#0369A1"
    left_stop1 = "#0284C7" if is_dark else "#0369A1"
    left_stop2 = "#0B1930" if is_dark else "#075985"
    right_stop1 = "#0066FF" if is_dark else "#2563EB"
    right_stop2 = "#0284C7" if is_dark else "#0284C7"
    well_bg = "#040813" if is_dark else "#F1F5F9"
    bevel_color = "rgba(255, 255, 255, 0.22)" if is_dark else "rgba(255, 255, 255, 0.6)"

    return f'''
    <defs>
        <!-- Facet Gradients -->
        <linearGradient id="lux_top" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{top_stop1}"/>
            <stop offset="100%" stop-color="{top_stop2}"/>
        </linearGradient>
        <linearGradient id="lux_left" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{left_stop1}"/>
            <stop offset="100%" stop-color="{left_stop2}"/>
        </linearGradient>
        <linearGradient id="lux_right" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{right_stop1}"/>
            <stop offset="100%" stop-color="{right_stop2}"/>
        </linearGradient>
        
        <!-- L-Conduit Gradient -->
        <linearGradient id="lux_l_grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{dot_color}"/>
            <stop offset="50%" stop-color="{accent_l}"/>
            <stop offset="100%" stop-color="#00D285"/>
        </linearGradient>

        <!-- Ambient Glow Filter -->
        <filter id="lux_mint_glow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="7" result="blur"/>
            <feComposite in="SourceGraphic" in2="blur" operator="over"/>
        </filter>
        <filter id="lux_dot_pulse" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="9" result="pulse"/>
            <feComposite in="SourceGraphic" in2="pulse" operator="over"/>
        </filter>
    </defs>

    <g id="hexacore-master-luxury">
        <!-- 3D Shadow Base Elevation -->
        <polygon points="100,126 180,80 180,170 100,216 20,170 20,80" fill="none" opacity="0.15"/>

        <!-- Top Facet (Data Ingress Diamond) -->
        <polygon points="100,20 180,66 100,112 20,66" fill="url(#lux_top)" stroke="{bevel_color}" stroke-width="1.2" stroke-linejoin="round"/>
        
        <!-- Left Facet (Structural Mass) -->
        <polygon points="20,74 100,120 100,212 20,166" fill="url(#lux_left)" stroke="{bevel_color}" stroke-width="1.2" stroke-linejoin="round"/>
        
        <!-- Right Facet (Forward Velocity Plane) -->
        <polygon points="100,120 180,74 180,166 100,212" fill="url(#lux_right)" stroke="{bevel_color}" stroke-width="1.2" stroke-linejoin="round"/>

        <!-- Recessed Quantum Well / Aperture on Top Facet -->
        <polygon points="100,48 146,74 100,100 54,74" fill="{well_bg}" stroke="rgba(0, 245, 160, 0.3)" stroke-width="1.5"/>

        <!-- The Quantum Dot of the 'i' with Multilayer Aura -->
        <circle cx="100" cy="74" r="18" fill="{accent_l}" opacity="0.25" filter="url(#lux_dot_pulse)"/>
        <circle cx="100" cy="74" r="14" fill="{dot_color}" filter="url(#lux_mint_glow)"/>
        <circle cx="100" cy="74" r="7" fill="#FFFFFF"/>

        <!-- The Kinetic 'L' Energy Pathway (Descent + Sweep) -->
        <!-- Outer Neon Aura -->
        <path d="M 100 120 L 100 182 L 152 152" 
              stroke="url(#lux_l_grad)" 
              stroke-width="13" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              fill="none" 
              filter="url(#lux_mint_glow)"/>
              
        <!-- Inner Specular Conduit Core -->
        <path d="M 100 123 L 100 180 L 150 151" 
              stroke="#FFFFFF" 
              stroke-width="4.5" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              fill="none" 
              opacity="0.9"/>

        <!-- Kinetic Satellite Tip -->
        <circle cx="152" cy="152" r="5.5" fill="{dot_color}"/>
        <circle cx="152" cy="152" r="2.5" fill="#FFFFFF"/>
    </g>
    '''

def get_wordmark_group(x, y, font_size=68, is_dark=True, accent_l="#00F5A0"):
    imad_fill = "#FFFFFF" if is_dark else "#0F172A"
    tagline_fill = "#94A3B8" if is_dark else "#475569"
    tag_size = font_size * 0.28
    tag_y = font_size * 0.44

    return f'''
    <g transform="translate({x}, {y})">
        <text x="0" y="0" font-family="'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif" font-size="{font_size}" font-weight="800" letter-spacing="-0.8" fill="{imad_fill}">Imad<tspan fill="{accent_l}">Labs</tspan></text>
        <text x="2" y="{tag_y}" font-family="'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif" font-size="{tag_size}" font-weight="700" letter-spacing="4.8" fill="{tagline_fill}">SOFTWARE STUDIO</text>
    </g>
    '''

# --- 1. BUILD ALL 16 LOGO VARIATIONS ---
def build_all_logos():
    print("Building perfected 16-variant logo suite...")
    logos_dir = "brand/logos"
    exports_png = "exports/png"
    exports_svg = "exports/svg"
    master_dir = "brand/master"

    # Variations definitions
    variations = {
        # Primary
        "imadlabs-logo-primary": f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400"><rect width="100%" height="100%" fill="#070B14"/><g transform="translate(90, 85)"><g transform="translate(0, 0) scale(1.05)">{get_perfected_hexacore_svg(is_dark=True)}</g>{get_wordmark_group(250, 120, font_size=68, is_dark=True)}</g></svg>''',
        "imadlabs-logo-primary-transparent": f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400"><g transform="translate(90, 85)"><g transform="translate(0, 0) scale(1.05)">{get_perfected_hexacore_svg(is_dark=True)}</g>{get_wordmark_group(250, 120, font_size=68, is_dark=True)}</g></svg>''',
        
        # Horizontal
        "imadlabs-logo-horizontal": f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="480" viewBox="0 0 1280 480"><rect width="100%" height="100%" fill="#070B14"/><g transform="translate(110, 115)"><g transform="translate(0, 5) scale(1.18)">{get_perfected_hexacore_svg(is_dark=True)}</g>{get_wordmark_group(280, 135, font_size=82, is_dark=True)}</g></svg>''',
        "imadlabs-logo-horizontal-light": f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="480" viewBox="0 0 1280 480"><rect width="100%" height="100%" fill="#F8FAFC"/><g transform="translate(110, 115)"><g transform="translate(0, 5) scale(1.18)">{get_perfected_hexacore_svg(is_dark=False, accent_l="#0066FF", dot_color="#00F5A0")}</g>{get_wordmark_group(280, 135, font_size=82, is_dark=False, accent_l="#0066FF")}</g></svg>''',
        "imadlabs-logo-horizontal-transparent": f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="480" viewBox="0 0 1280 480"><g transform="translate(110, 115)"><g transform="translate(0, 5) scale(1.18)">{get_perfected_hexacore_svg(is_dark=True)}</g>{get_wordmark_group(280, 135, font_size=82, is_dark=True)}</g></svg>''',
        
        # Vertical Stacked
        "imadlabs-logo-vertical": f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="700" viewBox="0 0 600 700"><rect width="100%" height="100%" fill="#070B14"/><g transform="translate(180, 95)"><g transform="scale(1.2)">{get_perfected_hexacore_svg(is_dark=True)}</g></g><g transform="translate(300, 485)"><text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="56" font-weight="800" fill="#FFFFFF" text-anchor="middle">Imad<tspan fill="#00F5A0">Labs</tspan></text><text x="0" y="32" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700" letter-spacing="5" fill="#94A3B8" text-anchor="middle">SOFTWARE STUDIO</text></g></svg>''',
        
        # Standalone Symbol
        "imadlabs-logo-standalone-symbol": f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><rect width="100%" height="100%" fill="#070B14"/><g transform="translate(106, 85) scale(1.5)">{get_perfected_hexacore_svg(is_dark=True)}</g></svg>''',
        "imadlabs-logo-standalone-symbol-transparent": f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><g transform="translate(106, 85) scale(1.5)">{get_perfected_hexacore_svg(is_dark=True)}</g></svg>''',
        
        # Wordmark Only
        "imadlabs-logo-wordmark-only": f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="260" viewBox="0 0 800 260"><rect width="100%" height="100%" fill="#070B14"/><g transform="translate(100, 140)">{get_wordmark_group(0, 0, font_size=76, is_dark=True)}</g></svg>''',
        
        # Compact
        "imadlabs-logo-compact": f'''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="200" viewBox="0 0 480 200"><rect width="100%" height="100%" fill="#070B14"/><g transform="translate(35, 30)"><g transform="scale(0.68)">{get_perfected_hexacore_svg(is_dark=True)}</g><g transform="translate(165, 82)"><text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="44" font-weight="800" fill="#FFFFFF">Imad<tspan fill="#00F5A0">Labs</tspan></text></g></g></svg>''',
        
        # Monochrome Black
        "imadlabs-logo-monochrome-black": f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400"><rect width="100%" height="100%" fill="#FFFFFF"/><g transform="translate(90, 85)"><g transform="scale(1.05)">{get_perfected_hexacore_svg(is_monochrome=True, mono_color="#000000")}</g><g transform="translate(250, 120)"><text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="68" font-weight="800" fill="#000000">Imad<tspan fill="#000000">Labs</tspan></text><text x="2" y="30" font-family="'Plus Jakarta Sans', sans-serif" font-size="19" font-weight="700" letter-spacing="4.8" fill="#000000">SOFTWARE STUDIO</text></g></g></svg>''',
        
        # Monochrome White
        "imadlabs-logo-monochrome-white": f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400"><rect width="100%" height="100%" fill="#000000"/><g transform="translate(90, 85)"><g transform="scale(1.05)">{get_perfected_hexacore_svg(is_monochrome=True, mono_color="#FFFFFF")}</g><g transform="translate(250, 120)"><text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="68" font-weight="800" fill="#FFFFFF">Imad<tspan fill="#FFFFFF">Labs</tspan></text><text x="2" y="30" font-family="'Plus Jakarta Sans', sans-serif" font-size="19" font-weight="700" letter-spacing="4.8" fill="#FFFFFF">SOFTWARE STUDIO</text></g></g></svg>''',
        
        # Light & Dark Background variants
        "imadlabs-logo-light-background": f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400"><rect width="100%" height="100%" fill="#F8FAFC"/><g transform="translate(90, 85)"><g transform="scale(1.05)">{get_perfected_hexacore_svg(is_dark=False, accent_l="#0066FF", dot_color="#00F5A0")}</g>{get_wordmark_group(250, 120, font_size=68, is_dark=False, accent_l="#0066FF")}</g></svg>''',
        "imadlabs-logo-dark-background": f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400"><rect width="100%" height="100%" fill="#070B14"/><g transform="translate(90, 85)"><g transform="scale(1.05)">{get_perfected_hexacore_svg(is_dark=True)}</g>{get_wordmark_group(250, 120, font_size=68, is_dark=True)}</g></svg>''',
        
        # Simplified Small
        "imadlabs-logo-simplified-small": f'''<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256"><rect width="100%" height="100%" fill="#070B14" rx="32"/><g transform="translate(28, 20)">{get_perfected_hexacore_svg(is_simplified=True)}</g></svg>''',
        
        # Outline
        "imadlabs-logo-outline": f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400"><rect width="100%" height="100%" fill="#070B14"/><g transform="translate(90, 85)"><g transform="scale(1.05)">{get_perfected_hexacore_svg(is_outline=True)}</g><g transform="translate(250, 120)"><text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="68" font-weight="800" fill="none" stroke="#38BDF8" stroke-width="2.5">Imad<tspan stroke="#00F5A0">Labs</tspan></text><text x="2" y="30" font-family="'Plus Jakarta Sans', sans-serif" font-size="19" font-weight="700" letter-spacing="4.8" fill="#94A3B8">SOFTWARE STUDIO</text></g></g></svg>'''
    }

    dims = {
        "imadlabs-logo-primary": (900, 400),
        "imadlabs-logo-primary-transparent": (900, 400),
        "imadlabs-logo-horizontal": (1280, 480),
        "imadlabs-logo-horizontal-light": (1280, 480),
        "imadlabs-logo-horizontal-transparent": (1280, 480),
        "imadlabs-logo-vertical": (600, 700),
        "imadlabs-logo-standalone-symbol": (512, 512),
        "imadlabs-logo-standalone-symbol-transparent": (512, 512),
        "imadlabs-logo-wordmark-only": (800, 260),
        "imadlabs-logo-compact": (480, 200),
        "imadlabs-logo-monochrome-black": (900, 400),
        "imadlabs-logo-monochrome-white": (900, 400),
        "imadlabs-logo-light-background": (900, 400),
        "imadlabs-logo-dark-background": (900, 400),
        "imadlabs-logo-simplified-small": (256, 256),
        "imadlabs-logo-outline": (900, 400)
    }

    # Save Master SVG
    with open(os.path.join(master_dir, "imadlabs-master-logo.svg"), "w", encoding="utf-8") as f:
        f.write(variations["imadlabs-logo-primary"])

    for name, content in variations.items():
        svg_p = os.path.join(logos_dir, f"{name}.svg")
        exp_svg_p = os.path.join(exports_svg, f"{name}.svg")
        with open(svg_p, "w", encoding="utf-8") as f: f.write(content)
        with open(exp_svg_p, "w", encoding="utf-8") as f: f.write(content)

        w, h = dims.get(name, (800, 400))
        png_p = os.path.join(exports_png, f"{name}.png")
        rasterize_svg(svg_p, png_p, w, h)
        shutil.copy2(png_p, os.path.join(logos_dir, f"{name}.png"))

    print("All 16 luxury logo variations generated and rendered.")

# --- 2. PERFECTED APPLICATION ICONS (iTube & Hyper Downloader) ---
def build_perfected_apps():
    print("Building perfected app icon suites matching HexaCore DNA...")
    
    # 1. iTube (HexaCore Media Prism)
    itube_symbol = '''
    <g transform="translate(180, 160) scale(3.2)">
        <polygon points="100,20 180,66 100,112 20,66" fill="#0284C7"/>
        <polygon points="20,74 100,120 100,212 20,166" fill="#0F172A"/>
        <polygon points="100,120 180,74 180,166 100,212" fill="#0066FF"/>
        <!-- Media Play & Download Core -->
        <polygon points="85,60 135,90 85,120" fill="#FF2A55"/>
        <circle cx="100" cy="74" r="28" fill="none" stroke="#00F5A0" stroke-width="4" stroke-dasharray="8 6"/>
        <path d="M 100 120 L 100 182 L 152 152" stroke="#00F5A0" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    </g>
    '''
    itube_master_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024"><rect width="100%" height="100%" fill="#070B14" rx="224"/><rect x="12" y="12" width="1000" height="1000" rx="214" fill="none" stroke="#1E293B" stroke-width="4"/>{itube_symbol}</svg>'''
    itube_dir = "apps/itube"
    with open(os.path.join(itube_dir, "itube-master-icon.svg"), "w", encoding="utf-8") as f: f.write(itube_master_svg)
    rasterize_svg(os.path.join(itube_dir, "itube-master-icon.svg"), os.path.join(itube_dir, "itube-1024x1024.png"), 1024, 1024)
    make_ico(os.path.join(itube_dir, "itube-1024x1024.png"), os.path.join(itube_dir, "windows", "itube.ico"))
    make_ico(os.path.join(itube_dir, "itube-1024x1024.png"), os.path.join(itube_dir, "web", "favicon.ico"))

    # 2. Hyper Downloader (HexaCore Turbo Accelerator)
    hyper_symbol = '''
    <g transform="translate(180, 160) scale(3.2)">
        <polygon points="100,20 180,66 100,112 20,66" fill="#38BDF8"/>
        <polygon points="20,74 100,120 100,212 20,166" fill="#0284C7"/>
        <polygon points="100,120 180,74 180,166 100,212" fill="#0066FF"/>
        <!-- Triple Acceleration Turbo Chevrons -->
        <path d="M 80 55 L 100 75 L 120 55" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" fill="none"/>
        <path d="M 80 75 L 100 95 L 120 75" stroke="#00FFC2" stroke-width="6" stroke-linecap="round" fill="none"/>
        <path d="M 100 120 L 100 182 L 152 152" stroke="#00F5A0" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    </g>
    '''
    hyper_master_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024"><rect width="100%" height="100%" fill="#070B14" rx="224"/><rect x="12" y="12" width="1000" height="1000" rx="214" fill="none" stroke="#1E293B" stroke-width="4"/>{hyper_symbol}</svg>'''
    hyper_dir = "apps/hyper-downloader"
    with open(os.path.join(hyper_dir, "hyper-downloader-master-icon.svg"), "w", encoding="utf-8") as f: f.write(hyper_master_svg)
    rasterize_svg(os.path.join(hyper_dir, "hyper-downloader-master-icon.svg"), os.path.join(hyper_dir, "hyper-downloader-1024x1024.png"), 1024, 1024)
    make_ico(os.path.join(hyper_dir, "hyper-downloader-1024x1024.png"), os.path.join(hyper_dir, "windows", "hyper-downloader.ico"))
    make_ico(os.path.join(hyper_dir, "hyper-downloader-1024x1024.png"), os.path.join(hyper_dir, "web", "favicon.ico"))

    print("Perfected app icons built successfully!")

# --- 3. DEVELOPER INTEGRATIONS (Tailwind & SCSS) ---
def build_dev_integrations():
    tailwind_js = '''/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    extend: {
      colors: {
        imad: {
          primary: '#0066FF',
          accent: '#00F5A0',
          dot: '#00FFC2',
          sky: '#38BDF8',
          bg: '#070B14',
          surface: '#0B0F19',
          card: '#111827',
          hover: '#162032',
          border: '#1E293B',
          amber: '#FFB703',
          coral: '#FF2A55'
        }
      },
      fontFamily: {
        heading: ['Plus Jakarta Sans', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace']
      }
    }
  }
};
'''
    with open("brand/colors/tailwind.config.imadlabs.js", "w", encoding="utf-8") as f:
        f.write(tailwind_js)

    scss_tokens = '''// ImadLabs Design Tokens - SCSS
$imad-primary: #0066FF;
$imad-accent: #00F5A0;
$imad-dot: #00FFC2;
$imad-sky: #38BDF8;

$imad-bg-dark: #070B14;
$imad-surface-dark: #0B0F19;
$imad-card-dark: #111827;
$imad-border-dark: #1E293B;

$imad-font-heading: 'Plus Jakarta Sans', sans-serif;
$imad-font-body: 'Inter', sans-serif;
$imad-font-mono: 'JetBrains Mono', monospace;
'''
    with open("brand/colors/colors.scss", "w", encoding="utf-8") as f:
        f.write(scss_tokens)

    print("Created tailwind.config.imadlabs.js and colors.scss!")

def main():
    build_all_logos()
    build_perfected_apps()
    build_dev_integrations()
    print("Master brand perfection pipeline completed!")

if __name__ == '__main__':
    main()
