# CLAUDE.md — Agent & Developer Brand Instructions for ImadLabs

This file contains mandatory instructions for Claude Code, Antigravity, Cursor, and any automated AI coding assistant developing applications, downloaders, utilities, or digital products under the **ImadLabs** brand.

---

## 1. Non-Negotiable Brand Rules

1. **Exact Brand Spelling:**
   - Always spell the brand as **`ImadLabs`**.
   - **Never** write `Imad Labs`, `imadlabs`, `IMADLABS`, `Imad-Labs`, or `Imad_Labs`.
   - In code identifiers, use `ImadLabs` (PascalCase), `imadLabs` (camelCase), or `imad-labs` (kebab-case).

2. **Official Logo Concept:**
   - The official company identity is **The HexaCore Matrix**: an isometric 3D software core with an electric Cyber Mint (`#00F5A0`) kinetic 'L' pathway and glowing quantum 'i' dot (`#00FFC2`).
   - Master files are located in [`brand/master/`](brand/master/) and [`brand/logos/`](brand/logos/).
   - **Never** substitute generic logos, placeholder icons, or arbitrary geometrical shapes when building an ImadLabs product.

---

## 2. Color Palette & Design Tokens

Always reference the official design tokens when styling UI components:
- **Tokens JSON:** [`brand/colors/tokens.json`](brand/colors/tokens.json)
- **CSS Variables:** [`brand/colors/colors.css`](brand/colors/colors.css)

### Core Color Constants

```css
/* Core Brand */
--imad-color-primary:    #0066FF;  /* Electric Cobalt */
--imad-color-accent:     #00F5A0;  /* Cyber Mint (The L) */
--imad-color-dot:        #00FFC2;  /* Quantum Dot Core */
--imad-color-sky:        #38BDF8;  /* Sky Diamond Facet */

/* Dark Mode Surfaces (Default) */
--imad-bg:               #070B14;  /* Deep Void */
--imad-surface:          #0B0F19;  /* Slate Obsidian */
--imad-surface-card:     #111827;  /* Card Background */
--imad-surface-hover:    #162032;  /* Hover Row / State */
--imad-border:           #1E293B;  /* Structural Borders */
--imad-border-focus:     #38BDF8;  /* Focus Rings */

/* Text */
--imad-text-primary:     #F8FAFC;  /* High-Contrast White */
--imad-text-secondary:   #94A3B8;  /* Readable Slate */
--imad-text-muted:       #64748B;  /* Placeholders / Muted */

/* Semantics */
--imad-success:          #10B981;  /* Emerald */
--imad-warning:          #F59E0B;  /* Amber */
--imad-error:            #EF4444;  /* Crimson */
--imad-info:             #0066FF;  /* Azure */
```

---

## 3. Creating a New ImadLabs Application

When tasked with generating a new desktop, web, or mobile application:

### Step 1: Copy Application Branding Starter
Use [`apps/template/`](apps/template/) as the foundation:
- `apps/template/template-master-icon.svg` (edit the `glyph` group; leave the `background` group alone)
- `apps/template/ios/`, `apps/template/android/`, `apps/template/web/`, `apps/template/windows/`

### Step 2: Establish the App's Distinct Silhouette
- App icons do **not** use the HexaCore cube. The cube is the company logo only.
- Every app gets its own bold symbol on the dark rounded tile (e.g., play button for **iTube**, download arrow and tray for **Hyper Downloader**), drawn in the Electric Cobalt gradient and Cyber Mint.
- Every app icon carries the ImadLabs quantum dot (`#00FFC2` glow with a white core) in the top-right as the brand signature.

### Step 3: Generate Platform Icons Automatically
Copy `apps/template/` to `apps/<app_name>/`, rename the master SVG to `<app_name>-master-icon.svg`, edit its `glyph` group, then build every size (iOS, Android, web, Windows, .ico):
```bash
python tools/build_app_icons.py <app_name>
```

---

## 4. UI Design Principles for ImadLabs Apps

1. **Dark Mode First:** Default to dark slate interfaces (`#070B14` canvas, `#111827` cards, `#1E293B` borders).
2. **Glassmorphism:** Apply subtle backdrop blurs (`backdrop-filter: blur(16px)`) and 1px borders with low-opacity white glow (`rgba(255,255,255,0.06)`).
3. **Typography:**
   - Headings: `Plus Jakarta Sans` (SemiBold / Bold / ExtraBold)
   - UI Body: `Inter` (Regular / Medium)
   - Data / Code: `JetBrains Mono`
4. **Download & Utility Progress Bars:**
   - Track: `#1E293B`
   - Fill: `linear-gradient(90deg, #00F5D4 0%, #0066FF 100%)`
   - Glow: `0 0 10px rgba(0, 245, 212, 0.4)`

---

## 5. Directory Reference Quick Lookup

| Asset | Location |
|---|---|
| Master Vector Logo | [`brand/master/imadlabs-master-logo.svg`](brand/master/imadlabs-master-logo.svg) |
| Horizontal Logo Lockup | [`brand/logos/imadlabs-logo-horizontal.svg`](brand/logos/imadlabs-logo-horizontal.svg) |
| Standalone Symbol | [`brand/logos/imadlabs-logo-standalone-symbol.svg`](brand/logos/imadlabs-logo-standalone-symbol.svg) |
| Multi-size Favicon | [`exports/web/favicon.ico`](exports/web/favicon.ico) |
| Telegram Profile | [`brand/telegram/telegram-avatar-1024-dark.png`](brand/telegram/telegram-avatar-1024-dark.png) |
| iTube App Icon | [`apps/itube/itube-1024x1024.png`](apps/itube/itube-1024x1024.png) |
| Hyper Downloader App Icon | [`apps/hyper-downloader/hyper-downloader-1024x1024.png`](apps/hyper-downloader/hyper-downloader-1024x1024.png) |
| Asset Export Utility | [`tools/export_assets.py`](tools/export_assets.py) |
