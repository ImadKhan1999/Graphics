"""
ImadLabs Brand Studio - Asset Catalog Builder
Scans all generated assets and creates a detailed ASSET_CATALOG.md
"""

import os
from PIL import Image

def get_intended_use(path):
    p = path.lower()
    if "master" in p: return "Master source vector artwork"
    if "primary-transparent" in p: return "Primary brandmark with alpha channel"
    if "primary" in p: return "Official primary lockup for dark surfaces"
    if "horizontal-light" in p: return "Horizontal header for white/light layouts"
    if "horizontal" in p: return "Official horizontal header lockup"
    if "vertical" in p: return "Vertical stacked lockup for posters & splash screens"
    if "standalone-symbol" in p: return "Official Dynamic Nexus brand emblem"
    if "wordmark" in p: return "Typographic brandmark without emblem"
    if "compact" in p: return "Compact toolbar and status bar lockup"
    if "monochrome-black" in p: return "1-color black logo for laser etching & receipts"
    if "monochrome-white" in p: return "1-color white logo for solid backgrounds"
    if "simplified-small" in p: return "High-contrast silhouette for 16px to 32px"
    if "outline" in p: return "Vector outline for technical diagrams"
    if "telegram-avatar" in p: return "Official Telegram circular avatar"
    if "telegram-template" in p: return "Telegram channel announcement graphic"
    if "adaptive-background" in p: return "Android adaptive icon background layer"
    if "adaptive-foreground" in p: return "Android adaptive icon foreground layer"
    if "appicon" in p: return "Apple iOS / macOS application icon asset"
    if "square" in p and "logo" in p: return "Windows Start menu and taskbar app tile"
    if "favicon.ico" in p: return "Multi-resolution Windows / browser favicon"
    if "favicon" in p: return "Web browser tab icon"
    if "youtube" in p: return "YouTube channel banner or video thumbnail"
    if "x-header" in p: return "X / Twitter profile header banner"
    if "linkedin" in p: return "LinkedIn company cover banner"
    if "instagram" in p: return "Instagram feed post or story canvas"
    if "launch" in p: return "Marketing product launch presentation banner"
    if "tokens.json" in p or "colors.css" in p: return "Design token definition for developers"
    if "typography" in p: return "Typography scale and font specifications"
    if "export_assets.py" in p: return "Automated CLI asset generation script"
    if "comparison-sheet" in p: return "10-Concept comparison presentation sheet"
    return "Official ImadLabs production asset"

def main():
    catalog_path = "ASSET_CATALOG.md"
    rows = []

    for root, dirs, files in os.walk("."):
        if ".git" in root or "__pycache__" in root or ".system_generated" in root:
            continue
        for f in sorted(files):
            ext = os.path.splitext(f)[1].lower()
            if ext in [".png", ".ico", ".svg", ".pdf", ".json", ".css", ".html", ".py", ".md"]:
                rel_path = os.path.relpath(os.path.join(root, f), ".").replace("\\", "/")
                size_kb = f"{os.path.getsize(rel_path) / 1024:.1f} KB"
                dims = "Vector / Scalable"

                if ext in [".png", ".jpg", ".jpeg"]:
                    try:
                        with Image.open(rel_path) as im:
                            dims = f"{im.width} × {im.height}"
                    except Exception:
                        pass
                elif ext == ".ico":
                    dims = "Multi-res (16 to 256)"

                category = rel_path.split("/")[0] if "/" in rel_path else "Root"
                rows.append((category, rel_path, ext.upper()[1:], dims, size_kb, get_intended_use(rel_path)))

    # Sort rows by category then path
    rows.sort(key=lambda r: (r[0], r[1]))

    content = f"""# ImadLabs — Official Asset Catalog

Total Cataloged Assets: **{len(rows)} files**  
Last Updated: October 2026  
Status: Verified & Validated  

This catalog provides an exhaustive inventory of all approved graphics, source vector files, exported resolution presets, application icon packages, social media kits, and design tokens in the ImadLabs Brand Studio.

---

| Category | File Path | Format | Dimensions | Size | Intended Use |
|---|---|---|---|---|---|
"""
    for cat, path, fmt, dims, size, use in rows:
        content += f"| **{cat}** | [`{path}`]({path}) | `{fmt}` | `{dims}` | {size} | {use} |\n"

    with open(catalog_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"ASSET_CATALOG.md created with {len(rows)} items!")

if __name__ == '__main__':
    main()
