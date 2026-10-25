# ImadLabs — Application Design System & UI Specifications

Version: `1.0.0`  
Theme: Glassmorphic Modern Dark (Default) + Clean Minimal Light  
Target Platforms: Desktop (Windows, macOS, Linux), Mobile (Android, iOS), Web & Telegram Mini Apps  

---

## 1. Design Token Architecture

The ImadLabs design tokens are organized in a 3-tier hierarchy:
1. **Global Tokens:** Raw color primitives, scales, and base fonts.
2. **Semantic / Alias Tokens:** Purpose-driven roles (e.g., `brand-primary`, `surface-card`, `status-success`).
3. **Component Tokens:** Element-specific assignments (e.g., `button-primary-bg`, `navbar-border`).

The system is fully portable and exported as:
- JSON Tokens: [`brand/colors/tokens.json`](brand/colors/tokens.json)
- CSS Variables: [`brand/colors/colors.css`](brand/colors/colors.css)
- Typography Tokens: [`brand/typography/typography.json`](brand/typography/typography.json)
- Typography Styles: [`brand/typography/typography.css`](brand/typography/typography.css)

---

## 2. Platform-Specific Icon Specifications

Every ImadLabs application (such as **iTube** and **Hyper Downloader**) includes dedicated, platform-compliant icon assets:

### A. Android Adaptive Icons
- **Foreground:** `512 × 512 px` transparent SVG/PNG containing the centered app emblem within the central `66%` safe circular zone (`338 px` diameter).
- **Background:** `512 × 512 px` opaque SVG/PNG filled with Deep Void `#070B14`.
- **Legacy Densities:** Generated in `mdpi` (48px), `hdpi` (72px), `xhdpi` (96px), `xxhdpi` (144px), and `xxxhdpi` (192px).
- **Directory:** `apps/[app-slug]/android/`

### B. Apple / iOS & macOS App Icons
- **Master Canvas:** `1024 × 1024 px` PNG with **no alpha transparency** (solid background `#070B14` or dark gradient).
- **Corner Radii:** Apple handles squircle clipping automatically via `UIImageView` / App Store mask. Source PNGs must remain full square.
- **Icon Set Sizes:** 1024 (App Store), 180 (iPhone @3x), 120 (iPhone @2x), 87 (Settings @3x), 80 (Spotlight @2x), 58 (Settings @2x), 40 (Notification).
- **Directory:** `apps/[app-slug]/ios/`

### C. Windows Desktop & App Tile Assets
- **Multi-Resolution ICO:** `apps/[app-slug]/windows/[app-slug].ico` contains 7 embedded resolutions: `16×16`, `24×24`, `32×32`, `48×48`, `64×64`, `128×128`, and `256×256` pixels.
- **Modern Tile PNGs:**
  - `Square44x44Logo.png` (Taskbar & small list)
  - `Square71x71Logo.png` (Small Start Menu tile)
  - `Square150x150Logo.png` (Medium Start Menu tile)
  - `Square310x310Logo.png` (Large Start Menu tile)
- **Directory:** `apps/[app-slug]/windows/`

### D. Web, Progressive Web Apps (PWA) & Favicons
- `favicon.ico`: Multi-layer favicon supporting 16px, 32px, 48px.
- `favicon-16x16.png` & `favicon-32x32.png`: Modern standard browser tab icons.
- `apple-touch-icon.png` (180×180): Mobile Safari bookmark icon.
- `icon-192x192.png` & `icon-512x512.png`: PWA install manifests.
- **Directory:** `apps/[app-slug]/web/` and `exports/web/`

---

## 3. UI Component System

### Buttons & Interactive Controls
- **Primary Action:**
  - Background: `var(--imad-gradient-brand)` (Linear 135deg `#00F5D4` to `#0066FF`)
  - Text: `#070B14` (High-contrast bold font)
  - Border-radius: `10px`
  - Shadow: `0 4px 14px rgba(0, 245, 212, 0.3)`
  - Hover: Opacity `0.92`, transform `translateY(-1px)`
- **Secondary Action:**
  - Background: `var(--imad-surface-card)` (`#111827`)
  - Text: `#F8FAFC`
  - Border: `1px solid var(--imad-border)` (`#1E293B`)
  - Hover: Border color `var(--imad-border-focus)` (`#38BDF8`)
- **Danger / Destructive:**
  - Background: `rgba(239, 68, 68, 0.15)`
  - Text: `#EF4444`
  - Border: `1px solid rgba(239, 68, 68, 0.3)`

### Cards & Glassmorphic Surfaces
- **Card Chassis:**
  - Background: `rgba(17, 24, 39, 0.85)`
  - Backdrop-filter: `blur(16px)`
  - Border: `1px solid rgba(30, 41, 59, 0.7)`
  - Border-radius: `16px`
  - Inner shadow: `inset 0 1px 0 rgba(255, 255, 255, 0.05)`

### Progress Indicators (Downloaders & Utilities)
- **Track:** Height `6px`, background `#1E293B`, border-radius `3px`
- **Fill Bar:** Background `linear-gradient(90deg, #00F5D4 0%, #0066FF 100%)`
- **Glow Pulse:** Box-shadow `0 0 12px rgba(0, 245, 212, 0.5)`

---

## 4. Figma & UI Design Tool Integration

The project is structured for 1-click import into Figma:
1. **Color Tokens:** Import `brand/colors/tokens.json` via Figma Tokens / Tokens Studio plugin.
2. **Typography Styles:** Match styles using Google Fonts `Plus Jakarta Sans`, `Inter`, and `JetBrains Mono`.
3. **Master SVG Graphics:** Drag and drop files from `brand/logos/*.svg` and `apps/*/*.svg` directly onto the Figma canvas.
4. **Auto-Layout Ready:** All SVG components are drawn with exact pixel coordinates, whole numbers, and bounded bounding boxes.
