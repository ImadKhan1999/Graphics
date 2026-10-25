"""
ImadLabs Brand Studio - Master Logo System Vector Factory
Constructs the complete 16 official vector logo variations for ImadLabs
based on the approved HexaCore Matrix (with Cyber Mint #00F5A0 L-pathway and #00FFC2 quantum dot).
"""

import os
import subprocess
import shutil
from PIL import Image

MASTER_DIR = os.path.abspath("brand/master")
LOGOS_DIR = os.path.abspath("brand/logos")
EXPORTS_SVG_DIR = os.path.abspath("exports/svg")
EXPORTS_PNG_DIR = os.path.abspath("exports/png")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

for d in [MASTER_DIR, LOGOS_DIR, EXPORTS_SVG_DIR, EXPORTS_PNG_DIR]:
    os.makedirs(d, exist_ok=True)

def get_hexacore_symbol(is_monochrome=False, mono_color="#FFFFFF", is_outline=False, is_simplified=False, is_dark=True):
    """
    Returns the vector markup for the HexaCore Matrix.
    The mark combines an isometric 3D hexagonal core with an electric
    Cyber Mint (#00F5A0) isometric 'L' pathway and glowing quantum 'i' dot (#00FFC2).
    """
    if is_monochrome:
        fill_facet_top = mono_color
        fill_facet_left = mono_color
        fill_facet_right = mono_color
        stroke_l = "#000000" if mono_color == "#FFFFFF" else "#FFFFFF"
        fill_dot = stroke_l
        dot_core = mono_color
        aperture_fill = stroke_l
        opacity_top = "0.9"
        opacity_left = "0.7"
        opacity_right = "0.5"
    else:
        fill_facet_top = "url(#hex_top_grad)"
        fill_facet_left = "url(#hex_left_grad)"
        fill_facet_right = "url(#hex_right_grad)"
        stroke_l = "#00F5A0"
        fill_dot = "#00FFC2"
        dot_core = "#FFFFFF"
        aperture_fill = "#050A14" if is_dark else "#F1F5F9"
        opacity_top = "1.0"
        opacity_left = "1.0"
        opacity_right = "1.0"

    if is_outline:
        outline_stroke = mono_color if is_monochrome else "#38BDF8"
        l_color = mono_color if is_monochrome else "#00F5A0"
        return f'''
        <!-- HexaCore Matrix Outline Version -->
        <g id="imadlabs-hexacore-outline">
            <polygon points="100,20 180,66 100,112 20,66" fill="none" stroke="{outline_stroke}" stroke-width="6"/>
            <polygon points="20,76 100,122 100,212 20,166" fill="none" stroke="{outline_stroke}" stroke-width="6"/>
            <polygon points="100,122 180,76 180,166 100,212" fill="none" stroke="{outline_stroke}" stroke-width="6"/>
            <circle cx="100" cy="76" r="10" fill="none" stroke="{l_color}" stroke-width="6"/>
            <path d="M 100 122 L 100 182 L 152 152" stroke="{l_color}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        </g>
        '''
    elif is_simplified:
        return f'''
        <!-- HexaCore Matrix Simplified (16-32px) -->
        <g id="imadlabs-hexacore-simplified">
            <polygon points="100,20 180,66 100,112 20,66" fill="{ '#38BDF8' if not is_monochrome else mono_color }"/>
            <polygon points="20,76 100,122 100,212 20,166" fill="{ '#0284C7' if not is_monochrome else mono_color }" opacity="0.8"/>
            <polygon points="100,122 180,76 180,166 100,212" fill="{ '#0066FF' if not is_monochrome else mono_color }" opacity="0.6"/>
            <circle cx="100" cy="76" r="16" fill="{fill_dot}"/>
            <path d="M 100 120 L 100 182 L 152 152" stroke="{stroke_l}" stroke-width="18" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        </g>
        '''
    else:
        # Master Production Geometry
        return f'''
        <!-- Master HexaCore Matrix Emblem -->
        <g id="imadlabs-hexacore-master">
            <!-- Top Facet (Diamond) -->
            <polygon points="100,20 180,66 100,112 20,66" fill="{fill_facet_top}" opacity="{opacity_top}"/>
            
            <!-- Left Facet -->
            <polygon points="20,76 100,122 100,212 20,166" fill="{fill_facet_left}" opacity="{opacity_left}"/>
            
            <!-- Right Facet -->
            <polygon points="100,122 180,76 180,166 100,212" fill="{fill_facet_right}" opacity="{opacity_right}"/>
            
            <!-- Inner Quantum Aperture on Top Facet -->
            <polygon points="100,50 145,76 100,102 55,76" fill="{aperture_fill}" opacity="0.9"/>
            
            <!-- THE DOT: Glowing Quantum Dot of the "i" -->
            <circle cx="100" cy="76" r="14" fill="{fill_dot}" { 'filter="url(#glow_mint)"' if not is_monochrome else '' }/>
            <circle cx="100" cy="76" r="7" fill="{dot_core}"/>
            
            <!-- THE L: Kinetic Isometric Letter "L" Pathway -->
            <path d="M 100 122 L 100 182 L 152 152" 
                  stroke="{stroke_l}" 
                  stroke-width="12" 
                  stroke-linecap="round" 
                  stroke-linejoin="round" 
                  fill="none" 
                  { 'filter="url(#glow_mint)"' if not is_monochrome else '' }/>
                  
            <!-- Core highlight line inside L -->
            <path d="M 100 125 L 100 180 L 150 151" 
                  stroke="{dot_core}" 
                  stroke-width="4" 
                  stroke-linecap="round" 
                  stroke-linejoin="round" 
                  fill="none" 
                  opacity="0.8"/>
                  
            <!-- Forward velocity tick on L apex -->
            <circle cx="152" cy="152" r="5" fill="{fill_dot}"/>
        </g>
        '''

def get_defs(is_dark=True):
    top_stop1 = "#38BDF8" if is_dark else "#0284C7"
    top_stop2 = "#0284C7" if is_dark else "#0369A1"
    left_stop1 = "#0284C7" if is_dark else "#0369A1"
    left_stop2 = "#0B1930" if is_dark else "#075985"
    right_stop1 = "#0066FF" if is_dark else "#2563EB"
    right_stop2 = "#0284C7" if is_dark else "#0284C7"

    return f'''
    <defs>
        <linearGradient id="hex_top_grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{top_stop1}"/>
            <stop offset="100%" stop-color="{top_stop2}"/>
        </linearGradient>
        <linearGradient id="hex_left_grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{left_stop1}"/>
            <stop offset="100%" stop-color="{left_stop2}"/>
        </linearGradient>
        <linearGradient id="hex_right_grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{right_stop1}"/>
            <stop offset="100%" stop-color="{right_stop2}"/>
        </linearGradient>
        <filter id="glow_mint" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="8" result="blur"/>
            <feComposite in="SourceGraphic" in2="blur" operator="over"/>
        </filter>
    </defs>
    '''

def get_wordmark(x, y, font_size=52, fill_imad="#FFFFFF", fill_labs="#00F5A0", show_tagline=True, tagline_fill="#94A3B8"):
    tagline_svg = ""
    if show_tagline:
        tag_size = font_size * 0.28
        tag_y = font_size * 0.44
        tagline_svg = f'''<text x="2" y="{tag_y}" font-family="'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif" font-size="{tag_size}" font-weight="700" letter-spacing="4.5" fill="{tagline_fill}">SOFTWARE STUDIO</text>'''
    
    return f'''
    <g transform="translate({x}, {y})">
        <text x="0" y="0" font-family="'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif" font-size="{font_size}" font-weight="800" letter-spacing="-0.8" fill="{fill_imad}">Imad<tspan fill="{fill_labs}">Labs</tspan></text>
        {tagline_svg}
    </g>
    '''

# --- 16 Logo Generators ---

def make_primary_logo(is_dark=True, is_transparent=False):
    bg_color = "transparent" if is_transparent else ("#070B14" if is_dark else "#F8FAFC")
    text_color = "#FFFFFF" if is_dark else "#0F172A"
    tagline_color = "#94A3B8" if is_dark else "#475569"
    labs_color = "#00F5A0" if is_dark else "#0066FF"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400">
    <rect width="100%" height="100%" fill="{bg_color}"/>
    {get_defs(is_dark)}
    <g transform="translate(90, 85)">
        <!-- HexaCore Symbol -->
        <g transform="translate(0, 0) scale(1.05)">
            {get_hexacore_symbol(is_dark=is_dark)}
        </g>
        <!-- Wordmark -->
        {get_wordmark(250, 120, font_size=68, fill_imad=text_color, fill_labs=labs_color, show_tagline=True, tagline_fill=tagline_color)}
    </g>
</svg>'''

def make_horizontal_logo(is_dark=True, is_transparent=False):
    bg_color = "transparent" if is_transparent else ("#070B14" if is_dark else "#F8FAFC")
    text_color = "#FFFFFF" if is_dark else "#0F172A"
    tagline_color = "#94A3B8" if is_dark else "#475569"
    labs_color = "#00F5A0" if is_dark else "#0066FF"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="480" viewBox="0 0 1280 480">
    <rect width="100%" height="100%" fill="{bg_color}"/>
    {get_defs(is_dark)}
    <g transform="translate(110, 115)">
        <!-- HexaCore Symbol -->
        <g transform="translate(0, 5) scale(1.18)">
            {get_hexacore_symbol(is_dark=is_dark)}
        </g>
        <!-- Wordmark -->
        {get_wordmark(280, 135, font_size=82, fill_imad=text_color, fill_labs=labs_color, show_tagline=True, tagline_fill=tagline_color)}
    </g>
</svg>'''

def make_vertical_logo(is_dark=True, is_transparent=False):
    bg_color = "transparent" if is_transparent else ("#070B14" if is_dark else "#F8FAFC")
    text_color = "#FFFFFF" if is_dark else "#0F172A"
    tagline_color = "#94A3B8" if is_dark else "#475569"
    labs_color = "#00F5A0" if is_dark else "#0066FF"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="700" viewBox="0 0 600 700">
    <rect width="100%" height="100%" fill="{bg_color}"/>
    {get_defs(is_dark)}
    <g transform="translate(180, 95)">
        <!-- Centered HexaCore Symbol -->
        <g transform="translate(0, 0) scale(1.2)">
            {get_hexacore_symbol(is_dark=is_dark)}
        </g>
    </g>
    <g transform="translate(300, 485)">
        <text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="56" font-weight="800" letter-spacing="-0.5" fill="{text_color}" text-anchor="middle">Imad<tspan fill="{labs_color}">Labs</tspan></text>
        <text x="0" y="32" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700" letter-spacing="5" fill="{tagline_color}" text-anchor="middle">SOFTWARE STUDIO</text>
    </g>
</svg>'''

def make_standalone_symbol(is_dark=True, is_transparent=False):
    bg_color = "transparent" if is_transparent else ("#070B14" if is_dark else "#F8FAFC")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
    <rect width="100%" height="100%" fill="{bg_color}"/>
    {get_defs(is_dark)}
    <g transform="translate(106, 85) scale(1.5)">
        {get_hexacore_symbol(is_dark=is_dark)}
    </g>
</svg>'''

def make_wordmark_only(is_dark=True, is_transparent=False):
    bg_color = "transparent" if is_transparent else ("#070B14" if is_dark else "#F8FAFC")
    text_color = "#FFFFFF" if is_dark else "#0F172A"
    labs_color = "#00F5A0" if is_dark else "#0066FF"
    tagline_color = "#94A3B8" if is_dark else "#475569"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="260" viewBox="0 0 800 260">
    <rect width="100%" height="100%" fill="{bg_color}"/>
    <g transform="translate(100, 140)">
        {get_wordmark(0, 0, font_size=76, fill_imad=text_color, fill_labs=labs_color, show_tagline=True, tagline_fill=tagline_color)}
    </g>
</svg>'''

def make_compact_logo(is_dark=True, is_transparent=False):
    bg_color = "transparent" if is_transparent else ("#070B14" if is_dark else "#F8FAFC")
    text_color = "#FFFFFF" if is_dark else "#0F172A"
    labs_color = "#00F5A0" if is_dark else "#0066FF"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="200" viewBox="0 0 480 200">
    <rect width="100%" height="100%" fill="{bg_color}"/>
    {get_defs(is_dark)}
    <g transform="translate(35, 30)">
        <g transform="translate(0, 0) scale(0.68)">
            {get_hexacore_symbol(is_dark=is_dark)}
        </g>
        <g transform="translate(165, 82)">
            <text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="44" font-weight="800" fill="{text_color}">Imad<tspan fill="{labs_color}">Labs</tspan></text>
        </g>
    </g>
</svg>'''

def make_monochrome_black():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400">
    <rect width="100%" height="100%" fill="#FFFFFF"/>
    <g transform="translate(90, 85)">
        <g transform="translate(0, 0) scale(1.05)">
            {get_hexacore_symbol(is_monochrome=True, mono_color="#000000")}
        </g>
        {get_wordmark(250, 120, font_size=68, fill_imad="#000000", fill_labs="#000000", show_tagline=True, tagline_fill="#000000")}
    </g>
</svg>'''

def make_monochrome_white():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400">
    <rect width="100%" height="100%" fill="#000000"/>
    <g transform="translate(90, 85)">
        <g transform="translate(0, 0) scale(1.05)">
            {get_hexacore_symbol(is_monochrome=True, mono_color="#FFFFFF")}
        </g>
        {get_wordmark(250, 120, font_size=68, fill_imad="#FFFFFF", fill_labs="#FFFFFF", show_tagline=True, tagline_fill="#FFFFFF")}
    </g>
</svg>'''

def make_simplified_small():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
    <rect width="100%" height="100%" fill="#070B14" rx="32"/>
    {get_defs(True)}
    <g transform="translate(28, 20) scale(1.0)">
        {get_hexacore_symbol(is_simplified=True)}
    </g>
</svg>'''

def make_outline_version():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400">
    <rect width="100%" height="100%" fill="#070B14"/>
    <g transform="translate(90, 85)">
        <g transform="translate(0, 0) scale(1.05)">
            {get_hexacore_symbol(is_outline=True)}
        </g>
        <g transform="translate(250, 120)">
            <text x="0" y="0" font-family="'Plus Jakarta Sans', sans-serif" font-size="68" font-weight="800" fill="none" stroke="#38BDF8" stroke-width="2.5" letter-spacing="-0.8">Imad<tspan stroke="#00F5A0">Labs</tspan></text>
            <text x="2" y="30" font-family="'Plus Jakarta Sans', sans-serif" font-size="19" font-weight="700" letter-spacing="4.5" fill="#94A3B8">SOFTWARE STUDIO</text>
        </g>
    </g>
</svg>'''

LOGO_SYSTEM = {
    "imadlabs-logo-primary": make_primary_logo(is_dark=True, is_transparent=False),
    "imadlabs-logo-primary-transparent": make_primary_logo(is_dark=True, is_transparent=True),
    "imadlabs-logo-horizontal": make_horizontal_logo(is_dark=True, is_transparent=False),
    "imadlabs-logo-horizontal-light": make_horizontal_logo(is_dark=False, is_transparent=False),
    "imadlabs-logo-horizontal-transparent": make_horizontal_logo(is_dark=True, is_transparent=True),
    "imadlabs-logo-vertical": make_vertical_logo(is_dark=True, is_transparent=False),
    "imadlabs-logo-standalone-symbol": make_standalone_symbol(is_dark=True, is_transparent=False),
    "imadlabs-logo-standalone-symbol-transparent": make_standalone_symbol(is_dark=True, is_transparent=True),
    "imadlabs-logo-wordmark-only": make_wordmark_only(is_dark=True, is_transparent=False),
    "imadlabs-logo-compact": make_compact_logo(is_dark=True, is_transparent=False),
    "imadlabs-logo-monochrome-black": make_monochrome_black(),
    "imadlabs-logo-monochrome-white": make_monochrome_white(),
    "imadlabs-logo-light-background": make_primary_logo(is_dark=False, is_transparent=False),
    "imadlabs-logo-dark-background": make_primary_logo(is_dark=True, is_transparent=False),
    "imadlabs-logo-simplified-small": make_simplified_small(),
    "imadlabs-logo-outline": make_outline_version()
}

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

def main():
    print("Building ImadLabs Master Logo System (Approved HexaCore Matrix with Cyber Mint #00F5A0 L & Dot)...")

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
    master_svg_path = os.path.join(MASTER_DIR, "imadlabs-master-logo.svg")
    with open(master_svg_path, "w", encoding="utf-8") as f:
        f.write(LOGO_SYSTEM["imadlabs-logo-primary"])

    # Save all variations into brand/logos and exports/svg
    for name, content in LOGO_SYSTEM.items():
        svg_file = os.path.join(LOGOS_DIR, f"{name}.svg")
        export_svg_file = os.path.join(EXPORTS_SVG_DIR, f"{name}.svg")

        with open(svg_file, "w", encoding="utf-8") as f:
            f.write(content)
        with open(export_svg_file, "w", encoding="utf-8") as f:
            f.write(content)

        w, h = dims.get(name, (800, 400))
        png_file = os.path.join(EXPORTS_PNG_DIR, f"{name}.png")
        rasterize_svg(svg_file, png_file, w, h)
        shutil.copy2(png_file, os.path.join(LOGOS_DIR, f"{name}.png"))
        print(f"Generated {name} (SVG & PNG {w}x{h})")

    print("\nMaster logo system rebuild for HexaCore Matrix completed!")

if __name__ == '__main__':
    main()
