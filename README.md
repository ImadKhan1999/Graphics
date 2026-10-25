# ImadLabs — Complete Brand Identity & Graphics Factory

[![Brand Version](https://img.shields.io/badge/Brand%20Version-1.0.0-0066FF.svg?style=flat-square)](CHANGELOG.md)
[![Concept](https://img.shields.io/badge/Approved%20Identity-Concept%2003%20Dynamic%20Nexus-00F5D4.svg?style=flat-square)](BRAND_GUIDELINES.md)
[![Assets](https://img.shields.io/badge/Production%20Assets-290%2B%20Files-38BDF8.svg?style=flat-square)](ASSET_CATALOG.md)
[![License](https://img.shields.io/badge/License-Proprietary-070B14.svg?style=flat-square)](README.md)

Welcome to the official **ImadLabs Brand Studio & Graphics Factory**. This repository contains the complete, production-grade visual identity system, vector master artwork, multi-platform application icon suites, Telegram branding package, social media kits, design tokens, and an automated Python asset export utility for **ImadLabs** — a software development brand dedicated to building high-performance applications, media downloaders, system utilities, and digital tools.

---

## ⚡ Quick Navigation

- 📘 [Brand Guidelines (`BRAND_GUIDELINES.md`)](BRAND_GUIDELINES.md) — Official rules, color codes (HEX/RGB/HSL), typography hierarchy, clear space, and usage constraints.
- 🎨 [Design System (`DESIGN_SYSTEM.md`)](DESIGN_SYSTEM.md) — Design tokens, component rules, glassmorphic UI patterns, and platform icon specifications.
- 📂 [Asset Catalog (`ASSET_CATALOG.md`)](ASSET_CATALOG.md) — Complete inventory of all 290+ assets with file paths, formats, dimensions, and intended uses.
- 🤖 [Agent & Developer Guide (`CLAUDE.md`)](CLAUDE.md) — Instructions for Claude Code and automated agents building new ImadLabs apps.
- 🚀 [Automated Asset Generator (`tools/export_assets.py`)](tools/export_assets.py) — CLI utility to generate multi-resolution PNGs, ICOs, and PDFs.
- 👁️ [Interactive Concept Dashboard (`previews/logo-concepts/index.html`)](previews/logo-concepts/index.html) — Live interactive concept explorer with dark/light themes.

---

## 💎 The Official Brand Identity: The HexaCore Matrix

The official company brandmark for ImadLabs is **The HexaCore Matrix** (Approved Concept 02 Refined).

- **Isometric Hexagonal Chassis:** An architectural 3D hexagon composed of three interlocking dimensional facets representing modular software architecture, microservices, and downloadable software packages.
- **Kinetic "L" Energy Pathway:** An electric **Cyber Mint (`#00F5A0`)** isometric vector conduit that descends along the central vertical seam of the cube and sweeps outward along the 30-degree isometric plane. It forms an unmistakable high-contrast letterform **"L"** that shines with neon clarity on dark interfaces.
- **Quantum Aperture & Photon Dot:** A recessed hexagonal aperture centered in the top facet housing a glowing quantum core dot (`#00FFC2` with `#FFFFFF` center), serving as the luminous tittle of the letterform **"i"**.
- **Wordmark:** Customized **Plus Jakarta Sans** with geometric kerning, rendering `Imad` in crisp white/slate and `Labs` highlighted in Cyber Mint (`#00F5A0`).

### Master File Locations
- **Master SVG:** [`brand/master/imadlabs-master-logo.svg`](brand/master/imadlabs-master-logo.svg)
- **Primary Logo:** [`brand/logos/imadlabs-logo-primary.svg`](brand/logos/imadlabs-logo-primary.svg)
- **Standalone Symbol:** [`brand/logos/imadlabs-logo-standalone-symbol.svg`](brand/logos/imadlabs-logo-standalone-symbol.svg)
- **Horizontal Header:** [`brand/logos/imadlabs-logo-horizontal.svg`](brand/logos/imadlabs-logo-horizontal.svg)

---

## 🎨 Color Palette & Design Tokens

| Role | Color Name | HEX | RGB | HSL | Preview |
|---|---|---|---|---|---|
| **Primary Accent (L)** | Cyber Mint | `#00F5A0` | `0, 245, 160` | `159°, 100%, 48%` | <span style="background:#00F5A0;width:24px;height:14px;display:inline-block;border-radius:2px;"></span> |
| **Quantum Dot Core** | Quantum Dot | `#00FFC2` | `0, 255, 194` | `166°, 100%, 50%` | <span style="background:#00FFC2;width:24px;height:14px;display:inline-block;border-radius:2px;"></span> |
| **HexaCore Base** | Electric Cobalt | `#0066FF` | `0, 102, 255` | `216°, 100%, 50%` | <span style="background:#0066FF;width:24px;height:14px;display:inline-block;border-radius:2px;"></span> |
| **Top Facet Highlight**| Sky Diamond | `#38BDF8` | `56, 189, 248` | `199°, 92%, 60%` | <span style="background:#38BDF8;width:24px;height:14px;display:inline-block;border-radius:2px;"></span> |
| **Dark Canvas**| Deep Void | `#070B14` | `7, 11, 20` | `222°, 48%, 5%` | <span style="background:#070B14;width:24px;height:14px;display:inline-block;border-radius:2px;"></span> |
| **Dark Card** | Surface Card | `#111827` | `17, 24, 39` | `220°, 39%, 11%` | <span style="background:#111827;width:24px;height:14px;display:inline-block;border-radius:2px;"></span> |
| **Dark Border**| Border Line | `#1E293B` | `30, 41, 59` | `217°, 33%, 17%` | <span style="background:#1E293B;width:24px;height:14px;display:inline-block;border-radius:2px;"></span> |
| **Light Canvas**| Pure Light | `#F8FAFC` | `248, 250, 252`| `210°, 40%, 98%` | <span style="background:#F8FAFC;width:24px;height:14px;display:inline-block;border-radius:2px;"></span> |

Tokens are available in JSON and CSS:
- JSON: [`brand/colors/tokens.json`](brand/colors/tokens.json)
- CSS: [`brand/colors/colors.css`](brand/colors/colors.css)

---

## 📱 Application Icon Suites

The branding factory includes dedicated multi-platform icon packages for ImadLabs products:

### 1. iTube (Video Downloader & Media Player)
- **Concept:** Continuous stream orbit loop with accelerated media play chevron and downloader vector.
- **Location:** [`apps/itube/`](apps/itube/)
- **Includes:** 1024×1024 Master PNG/SVG, Android Adaptive Icons (Foreground + Background), iOS AppIcon pack (40px to 1024px), Windows Multi-Resolution `.ico`, and Web Favicon suite.

### 2. Hyper Downloader (Turbo-Charged Download Manager)
- **Concept:** Triple velocity accelerator tracks with downward multi-threaded throughput pulse.
- **Location:** [`apps/hyper-downloader/`](apps/hyper-downloader/)
- **Includes:** Full Android, iOS, Windows ICO, and Web Favicon suites.

### 3. Application Starter Template
- **Concept:** Reusable template for launching any future ImadLabs application.
- **Location:** [`apps/template/`](apps/template/)

---

## ✈️ Telegram Branding Package

- **Master Profile Picture (1024×1024):** High-resolution, circular-crop safe avatar in dark and light modes ([`brand/telegram/`](brand/telegram/)).
- **Channel Announcement Templates (1280×720):**
  1. `telegram-template-welcome`: Community welcome banner.
  2. `telegram-template-app-release`: New application launch template.
  3. `telegram-template-app-update`: Version changelog and update announcement.
  4. `telegram-template-feature-announcement`: Major feature highlight.
  5. `telegram-template-milestone`: Community milestone celebration.
  6. `telegram-template-promotional`: Product suite spotlight.

---

## 🌐 Social Media & Marketing Package

- **YouTube:** Channel Banner (`2560 × 1440 px`), Video Thumbnail Template (`1280 × 720 px`).
- **Twitter / X:** Profile Header (`1500 × 500 px`).
- **LinkedIn:** Company Page Banner (`1584 × 396 px`).
- **Instagram:** Square Feed Post (`1080 × 1080 px`), Portrait Post (`1080 × 1350 px`), Story (`1080 × 1920 px`).
- **Marketing:** Official Launch Hero Banner (`1920 × 1080 px`).

---

## 🛠️ Automated Asset Generator (`tools/export_assets.py`)

A standalone Python automation utility to resize, package, and validate graphics without quality loss.

### Installation
```bash
pip install -r tools/requirements.txt
```

### Usage Examples
```bash
# 1. Run complete brand export across all sizes and presets
python tools/export_assets.py --profile all

# 2. Export custom sizes from any master SVG
python tools/export_assets.py --input brand/master/imadlabs-master-logo.svg --output exports/custom --sizes 128,256,512,1024

# 3. Export square icon suite
python tools/export_assets.py --input apps/itube/itube-master-icon.svg --output apps/itube/custom_exports
```

---

## 📁 Repository Directory Structure

```
imadlabs-brand-kit/
│
├── README.md                           # Main Project Overview & Guide
├── CLAUDE.md                           # Agent & Developer Brand Rules
├── BRAND_GUIDELINES.md                 # Complete Brand Identity Manual
├── DESIGN_SYSTEM.md                    # UI Tokens, Patterns & Platform Specs
├── ASSET_CATALOG.md                    # Exhaustive 290+ Asset Inventory
├── CHANGELOG.md                        # Version Release History
│
├── brand/                              # Official Brand Identity Assets
│   ├── master/                         # Master SVG Source Files
│   ├── logos/                          # 16 Vector Logo Variations
│   ├── telegram/                       # Telegram Avatars & Post Templates
│   ├── colors/                         # tokens.json, colors.css
│   └── typography/                     # typography.json, typography.css
│
├── apps/                               # Application Branding Suites
│   ├── itube/                          # iTube Video Downloader Assets
│   ├── hyper-downloader/               # Hyper Downloader Assets
│   └── template/                       # Future App Starter Template
│
├── social-media/                       # Channel Banners & Social Post Assets
│   ├── telegram/
│   ├── youtube/
│   ├── instagram/
│   ├── facebook/
│   ├── x/
│   └── linkedin/
│
├── marketing/                          # Promotional & Launch Graphics
│   ├── launches/
│   ├── updates/
│   └── promotions/
│
├── exports/                            # Production Export Presets
│   ├── png/                            # Square & Horizontal PNGs (16px to 2048px)
│   ├── svg/                            # Production SVGs
│   ├── ico/                            # Windows Multi-Resolution ICOs
│   ├── pdf/                            # High-Res 300 DPI PDF Assets
│   └── web/                            # Favicons & PWA Icons
│
├── templates/                          # Editable Vector Templates
│   ├── app-branding/
│   └── social-posts/
│
├── tools/                              # Automation Scripts
│   ├── export_assets.py                # Multi-Format CLI Asset Exporter
│   ├── requirements.txt                # Python Dependencies
│   ├── build_logo_system.py            # Master Logo Vector Generator
│   ├── build_all_graphics.py           # Apps, Telegram & Social Builder
│   └── build_asset_catalog.py          # Automatic Catalog Generator
│
└── previews/                           # Visual Previews & Presentations
    ├── logo-concepts/                  # 10 Explored Concepts & Interactive Viewer
    ├── icon-concepts/                  # App Icon Explorations
    └── brand-presentations/            # Presentation Materials
```

---

## 🚀 Publishing to GitHub (`imadlabs-brand-kit`)

To publish this project to GitHub as **`imadlabs-brand-kit`**:

```bash
# 1. Initialize git repository
git init

# 2. Add all files
git add .

# 3. Create initial commit
git commit -m "feat: complete ImadLabs brand identity & graphics factory v1.0.0"

# 4. Set default branch to main
git branch -M main

# 5. Add remote GitHub repository (replace with your GitHub username)
git remote add origin https://github.com/<your-username>/imadlabs-brand-kit.git

# 6. Push to GitHub
git push -u origin main
```

---

## 🛡️ Quality Assurance Verification

- [x] **Brand Spelling:** Verified 100% consistent spelling of **ImadLabs** throughout all assets, code, and documentation.
- [x] **Vector Purity:** All 16 logo variations and app marks are pure, scalable SVGs without distorted curves or unwanted artifacts.
- [x] **Multi-Platform Compliance:** Android Adaptive layers, iOS square icons, Windows 7-in-1 `.ico` files, and Web favicons tested and validated.
- [x] **Full Size Matrix:** Generated from `16 × 16 px` favicons up to `2048 × 2048 px` ultra-high-resolution masters.
- [x] **Transparency:** Alpha channels verified for all transparent PNG exports.
- [x] **Design Tokens:** Provided in both machine-readable JSON and standard CSS custom properties.

---

© 2026 ImadLabs. All Rights Reserved. Engineered for excellence in software development.
