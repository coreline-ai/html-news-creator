# Revenuecat - Refero Design MD

- Source: https://styles.refero.design/style/b5fdba21-fd4d-427e-b551-1e22c51e42db
- Original site: https://revenuecat.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
precision architecture on crisp white. Like an x-ray of meticulously organized components within a bright, airy digital lab.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#f9f9fb` | neutral | Page background or card surface |
| Deep Space Violet | `#1f1f47` | brand | Action accent / signal color |
| Digital Violet | `#576cdb` | brand | Action accent / signal color |
| Charcoal Text | `#171a1c` | neutral | Primary text or dark surface |
| Slate Text | `#3d3d5c` | neutral | Primary text or dark surface |
| Whisper Gray | `#6c7693` | neutral | Border, muted text, or supporting surface |
| Hover Violet | `#abb6ed` | brand | Action accent / signal color |
| Light Violet Stroke | `#eaedf6` | neutral | Action accent / signal color |
| Gradient Aura | `#5a73f2` | accent | Action accent / signal color |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-cloud-gray: #f9f9fb;
  --ref-deep-space-violet: #1f1f47;
  --ref-digital-violet: #576cdb;
  --ref-charcoal-text: #171a1c;
  --ref-slate-text: #3d3d5c;
  --ref-whisper-gray: #6c7693;
  --ref-hover-violet: #abb6ed;
}
```

## Typography direction
- **Object Sans**: 100, 300, 400, 500, 700, 13px, 14px, 16px, 18px, 24px, 28px, 32px, 40px, 48px, 54px, 56px, 64px, 80px, 1.00, 1.13, 1.25, 1.38, 1.50; substitute `system-ui`.
- **Helvetica Neue**: 300, 400, 500, 16px, 18px, 20px, 22px, 1.00, 1.25, 1.38, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `120px`
- Card Padding: `24px`
- Element Gap: `20px`
- Page Max Width: `1216px`
- Radius: `cards: 0px, images: 16px, buttons: 9999px, general: 16px, pill-buttons-large: 40px`

## Component cues
- **Stat Block — Hero Metrics**: Reference component style.
- **Feature Cards — Data and Tools for Every Team**: Reference component style.
- **Testimonial Card — VSCO Case Study**: Reference component style.
- **Primary Action Button**: Calls to action
- **Text Link Button**: Secondary actions, navigation, and inline links

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
