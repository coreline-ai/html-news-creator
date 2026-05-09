# Elementor - Refero Design MD

- Source: https://styles.refero.design/style/4bbc63cf-c995-4c56-9873-e7f300f1c9e7
- Original site: https://elementor.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-stakes monochrome printing press — a system where black and white do all the heavy lifting, Roobert's compressed weight-900 headlines stamped like bold ink on paper.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Press Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Ink | `#212121` | neutral | Primary text or dark surface |
| Blank Canvas | `#ffffff` | neutral | Page background or card surface |
| Fog Sheet | `#f6f6f6` | neutral | Page background or card surface |
| Ash Border | `#d1d1d1` | neutral | Border, muted text, or supporting surface |
| Slate Text | `#a6a6a6` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#69727d` | neutral | Border, muted text, or supporting surface |
| Pixel Blush | `#ffb8e5` | accent | Action accent / signal color |
| Neon Loop | `#ed01ee` | accent | Action accent / signal color |
| Codeberry | `#620856` | accent | Action accent / signal color |

```css
:root {
  --ref-press-black: #000000;
  --ref-charcoal-ink: #212121;
  --ref-blank-canvas: #ffffff;
  --ref-fog-sheet: #f6f6f6;
  --ref-ash-border: #d1d1d1;
  --ref-slate-text: #a6a6a6;
  --ref-steel-gray: #69727d;
  --ref-pixel-blush: #ffb8e5;
}
```

## Typography direction
- **Roobert**: 400, 500, 600, 700, 900, 14px, 16px, 18px, 19px, 20px, 24px, 32px, 36px, 40px, 48px, 56px, 64px, 88px, 1.10–1.50 (tighter at large display sizes: 1.10 at 88px, 1.20 at 56–64px, 1.30–1.40 at 32–48px, 1.50 at body sizes); substitute `Cabinet Grotesk, Satoshi, or Plus Jakarta Sans at matching weights`.
- **Times**: 400, 16px, 24px, 32px, 1.00–1.20; substitute `Georgia`.

## Spacing / shape
- Section Gap: `96px`
- Element Gap: `8-16px`
- Page Max Width: `1200px`
- Radius: `cards: 16px, badges: 8px, images: 16px, inputs: 8px, buttons: 8px, imagePill: 160px`

## Component cues
- **Button Group — Primary, Secondary, Ghost**: Reference component style.
- **Stat Counter Block**: Reference component style.
- **Feature Cards — White on Black**: Reference component style.
- **Primary CTA Button (Black Fill)**: Main call-to-action across hero and section endings
- **Secondary Button (White Fill)**: Secondary action alongside primary CTAs

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
