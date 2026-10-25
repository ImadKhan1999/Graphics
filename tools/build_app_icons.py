#!/usr/bin/env python3
"""
ImadLabs Brand Studio - App Icon Builder

Builds every platform icon for an app from its master SVG
(apps/<app>/<app>-master-icon.svg). The master SVG must contain two groups:
  <g id="background"> ... </g>   rounded tile, replaced per platform
  <g id="glyph"> ... </g>        the app's symbol, edit this to customise

The SVG is rendered once at 1024x1024 with headless Chrome/Edge and then
downscaled with Pillow, so small sizes are never cropped.

Usage:
  python tools/build_app_icons.py itube hyper-downloader template
  python tools/build_app_icons.py --all
Set CHROME=<path to chrome or msedge> if the browser is not found.
"""

import os
import re
import sys
import shutil
import argparse
import subprocess
import tempfile
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = os.path.join(ROOT, "apps")
BG = "#070B14"

CHROME_CANDIDATES = [
    os.environ.get("CHROME", ""),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]

IOS_SIZES = [1024, 180, 120, 87, 80, 60, 58, 40]
ANDROID_SIZES = [48, 72, 96, 144, 192]
WEB_FAVICONS = [16, 32, 48, 64]
WEB_ICONS = [180, 192, 512]
WINDOWS_TILES = [44, 71, 150, 310]
ICO_SIZES = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]


def find_browser():
    for candidate in CHROME_CANDIDATES:
        if candidate and os.path.exists(candidate):
            return candidate
    return (shutil.which("chrome") or shutil.which("msedge") or shutil.which("google-chrome")
            or shutil.which("chromium"))


def variant(svg, mode):
    """mode: 'tile' (rounded), 'full' (square full bleed), 'foreground' (glyph only), 'background' (tile only)."""
    bg_pattern = re.compile(r'<g id="background">.*?</g>', re.S)
    glyph_pattern = re.compile(r'<g id="glyph">.*</g>', re.S)
    if mode == "tile":
        return svg
    if mode == "full":
        return bg_pattern.sub(f'<g id="background"><rect width="1024" height="1024" fill="url(#bgGlow)"/></g>', svg)
    if mode == "foreground":
        # The glyph already sits inside Android's central 66% safe zone
        return bg_pattern.sub('<g id="background"></g>', svg)
    if mode == "background":
        svg = bg_pattern.sub(f'<g id="background"><rect width="1024" height="1024" fill="url(#bgGlow)"/></g>', svg)
        return glyph_pattern.sub('<g id="glyph"></g>', svg)
    raise ValueError(mode)


def render(browser, svg_text, out_png):
    """Render an SVG string to a 1024x1024 PNG with a transparent page background."""
    with tempfile.TemporaryDirectory() as tmp:
        html = os.path.join(tmp, "icon.html")
        with open(html, "w", encoding="utf-8") as f:
            f.write('<html><body style="margin:0;background:transparent">' + svg_text + "</body></html>")
        subprocess.run([
            browser, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
            "--default-background-color=00000000", "--force-device-scale-factor=1",
            "--window-size=1024,1024", f"--screenshot={out_png}", html,
        ], capture_output=True, check=True)
    with Image.open(out_png) as im:
        im.convert("RGBA").crop((0, 0, 1024, 1024)).save(out_png)


def save_size(master, size, path, flatten=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im = master.resize((size, size), Image.LANCZOS)
    if flatten:
        bg = Image.new("RGBA", im.size, BG)
        bg.alpha_composite(im)
        im = bg.convert("RGB")
    im.save(path)


def build_app(browser, app):
    app_dir = os.path.join(APPS_DIR, app)
    master_svg = os.path.join(app_dir, f"{app}-master-icon.svg")
    with open(master_svg, encoding="utf-8") as f:
        svg = f.read()

    with tempfile.TemporaryDirectory() as tmp:
        renders = {}
        for mode in ("tile", "full", "foreground", "background"):
            out = os.path.join(tmp, f"{mode}.png")
            render(browser, variant(svg, mode), out)
            renders[mode] = Image.open(out).copy()

    for folder in ("ios", "android", "web", "windows"):
        os.makedirs(os.path.join(app_dir, folder), exist_ok=True)
    for mode in ("foreground", "background"):
        with open(os.path.join(app_dir, "android", f"adaptive-{mode}.svg"), "w", encoding="utf-8") as f:
            f.write(variant(svg, mode))

    tile, full = renders["tile"], renders["full"]
    tile.save(os.path.join(app_dir, f"{app}-1024x1024.png"))

    for s in IOS_SIZES:
        save_size(full, s, os.path.join(app_dir, "ios", f"AppIcon-{s}x{s}.png"), flatten=True)
    for s in ANDROID_SIZES:
        save_size(tile, s, os.path.join(app_dir, "android", f"icon-{s}x{s}.png"))
    renders["foreground"].save(os.path.join(app_dir, "android", "adaptive-foreground.png"))
    renders["background"].save(os.path.join(app_dir, "android", "adaptive-background.png"))
    for s in WEB_FAVICONS:
        save_size(tile, s, os.path.join(app_dir, "web", f"favicon-{s}x{s}.png"))
    for s in WEB_ICONS:
        save_size(tile, s, os.path.join(app_dir, "web", f"icon-{s}x{s}.png"))
    for s in WINDOWS_TILES:
        save_size(tile, s, os.path.join(app_dir, "windows", f"Square{s}x{s}Logo.png"))

    tile.save(os.path.join(app_dir, "web", "favicon.ico"), format="ICO", sizes=ICO_SIZES)
    tile.save(os.path.join(app_dir, "windows", f"{app}.ico"), format="ICO", sizes=ICO_SIZES)
    print(f"Built {app}")


def main():
    parser = argparse.ArgumentParser(description="Build ImadLabs app icons from master SVGs.")
    parser.add_argument("apps", nargs="*", help="App folder names under apps/")
    parser.add_argument("--all", action="store_true", help="Build every app under apps/")
    args = parser.parse_args()

    apps = sorted(os.listdir(APPS_DIR)) if args.all else args.apps
    if not apps:
        parser.error("name at least one app, or pass --all")

    browser = find_browser()
    if not browser:
        sys.exit("No Chrome/Edge found. Set CHROME to the browser executable path.")

    for app in apps:
        build_app(browser, app)


if __name__ == "__main__":
    main()
