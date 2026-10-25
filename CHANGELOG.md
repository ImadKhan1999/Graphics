# Changelog

All notable changes to the **ImadLabs Brand Studio & Graphics Factory** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.4.0] - 2026-10-25

### Changed
- **App icons no longer use the HexaCore cube.** iTube, Hyper Downloader and the app template were redrawn as flat symbols on the dark rounded tile with the ImadLabs quantum dot, so each app can be customised. The cube stays as the company logo.
- Master icon SVGs now have separate `background` and `glyph` groups.
- Removed the archived Dynamic Nexus assets and rejected explorations.

### Added
- `tools/build_app_icons.py` builds iOS, Android (incl. adaptive layers), web and Windows icons from a master SVG. It renders once at 1024px and downscales, so small sizes are no longer cropped.

---

## [1.3.0] - 2026-10-25

### Cleanup
- Deleted `previews/logo-concepts/` — all non-HexaCore concept artwork (Concepts 01–10 including the Dynamic Nexus Monogram) permanently removed.
- Archived `tools/generate_concepts.py` → `tools/_archived_generate_concepts.py` — original multi-concept generator no longer needed.

### Added
- **Icon Concept Previews** (`previews/icon-concepts/`):
  - 4 design directions per app (Gradient Badge, Dark Premium, Glassmorphism, Minimal Flat).
  - iTube concept sheet (920×270) and Hyper Downloader concept sheet.
- **App Branding Templates** (`templates/app-branding/`):
  - `app-launch-template-1080x1080.svg/png` — reusable square launch announcement.
  - `app-update-template-1280x720.svg/png` — landscape update announcement.
  - `app-branding-template-editor.html` — interactive browser-based template editor with live preview.
- **Social Media: Facebook** (`social-media/facebook/`):
  - Cover: 820×312, Profile: 360×360.
- **Social Media: Instagram** (`social-media/instagram/`):
  - Portrait post: 1080×1350, Story: 1080×1920.
- **Social Media: YouTube** (`social-media/youtube/`):
  - Thumbnail template: 1280×720.
- **Social Media: X** (`social-media/x/`):
  - Portrait post: 1080×1350.
- **Marketing extras** (`marketing/`):
  - Business card design: front & back (1050×600).
  - Email signature banner: 600×120.
- **Updated `index.html`**:
  - Animated SVG HexaCore Matrix hero panel with breathing glow, pulsing quantum dot, and scanning line effect.
  - New `#apps` section: iTube and Hyper Downloader icon showcase with concept exploration previews.
  - New `#social` section: 10-card social media grid + marketing assets row.
  - Updated file count stats to 380+.
- **Rebuilt `ASSET_CATALOG.md`** — reflects all new additions.

---

## [1.0.0] - 2026-10-25

### Added
- **Logo Concept Exploration Suite (Phase 1):**
  - Explored 10 distinct creative directions with vector SVG masters and high-res PNG renders.
  - Interactive comparison dashboard (`previews/logo-concepts/index.html`) with dark/light mode toggles.
  - Master comparison sheet in SVG and PNG (2500×2100).
- **Official Brand Approval:**
  - Client approved **Concept 03: The Dynamic Nexus Monogram** as official company identity.
- **Complete Logo System (16 Variations):**
  - Master SVG, Primary (dark, light, transparent), Horizontal (dark, light, transparent), Vertical, Standalone Symbol, Wordmark-Only, Compact, Monochrome Black, Monochrome White, Simplified Small (16–32px), and Outline version.
- **Design Tokens & Design System:**
  - `brand/colors/tokens.json` & `brand/colors/colors.css`.
  - `brand/typography/typography.json` & `brand/typography/typography.css`.
  - Comprehensive `BRAND_GUIDELINES.md` and `DESIGN_SYSTEM.md`.
- **Telegram Branding Package:**
  - 1024×1024 master circular profile avatar (dark and light variants).
  - 6 announcement graphics (Welcome, App Release, App Update, Feature Announcement, Community Milestone, Promotional Spotlight).
- **Application Icon Suites:**
  - **iTube:** Video streaming & downloader emblem, Android adaptive assets, iOS icon pack, Windows multi-size ICO, Web favicons.
  - **Hyper Downloader:** Turbo-charged multi-thread accelerator emblem, Android adaptive, iOS pack, Windows multi-size ICO, Web favicons.
  - **App Template:** Reusable scaffolding for future ImadLabs products.
- **Social Media & Marketing Graphics:**
  - YouTube channel banner (2560×1440).
  - Twitter / X profile header (1500×500).
  - LinkedIn company cover (1584×396).
  - Instagram square post (1080×1080).
  - Product launch hero showcase banner (1920×1080).
- **Automated Graphics Factory (`tools/export_assets.py`):**
  - CLI automation tool for multi-resolution exports (16×16 to 2048×2048).
  - Multi-resolution Windows ICO generation (16px to 256px).
  - High-res 300 DPI PDF generation.
  - Aspect ratio preservation, transparent background validation, and summary reporting.
- **Documentation & Catalog:**
  - Complete `ASSET_CATALOG.md` indexing 292 production assets.
  - `CLAUDE.md` developer and agent instruction manual.
  - `README.md` repository guide.
