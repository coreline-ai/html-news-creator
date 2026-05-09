# Everlane - Refero Design MD

- Source: https://styles.refero.design/style/34b4856c-cc2b-4164-ab90-1b87cf8e0213
- Original site: https://everlane.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Raw linen and exposed grain. This design feels like natural fibers and honest construction, prioritizing unadorned function and understated elegance.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Slate Gray | `#4c4c4c` | neutral | Border, muted text, or supporting surface |
| Cement Gray | `#737373` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#9b9b9b` | neutral | Border, muted text, or supporting surface |
| Forest Green | `#d9e9bb` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-slate-gray: #4c4c4c;
  --ref-cement-gray: #737373;
  --ref-ash-gray: #9b9b9b;
  --ref-forest-green: #d9e9bb;
}
```

## Typography direction
- **Maison Neue Book**: 400, 700, 10px, 12px, 14px, 15px, 16px, 20px, 24px, 32px, 1.00, 1.20, 1.25, 1.30, 1.33, 1.35, 1.40, 1.43, 1.50, 1.60, 1.80, 2.25; substitute `Inter, Arial`.
- **Maison Neue Demi**: 600, 12px, 1.33; substitute `Inter Bold, Arial Bold`.
- **GTStandard-M**: 400, 16px, 1.50; substitute `Roboto Mono, Space Mono`.

## Spacing / shape
- Section Gap: `48-80px`
- Card Padding: `15px`
- Element Gap: `4-16px`
- Radius: `all: 0px`

## Component cues
- **Promotional Banner**: Reference component style.
- **Product Grid**: Reference component style.
- **Editorial Content Block**: Reference component style.
- **Navigation Link**: Interactive text link within navigation menus.
- **Primary Action Button (Text)**: Main call-to-action on promotional sections or product details.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
