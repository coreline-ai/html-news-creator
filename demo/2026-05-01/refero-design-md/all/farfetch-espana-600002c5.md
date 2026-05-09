# FARFETCH España - Refero Design MD

- Source: https://styles.refero.design/style/600002c5-c5f5-4df0-adf6-6324ee6255c0
- Original site: https://farfetch.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Wall of Luxury — crisp white walls, perfect lighting, and all attention drawn to the curated pieces within.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Raven Black | `#222222` | neutral | Primary text or dark surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#e6e6e6` | neutral | Page background or card surface |
| Ash Gray | `#b6b6b6` | neutral | Border, muted text, or supporting surface |
| Ghost White | `#f5f5f5` | neutral | Page background or card surface |
| Steel Gray | `#727272` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-raven-black: #222222;
  --ref-polar-white: #ffffff;
  --ref-cloud-gray: #e6e6e6;
  --ref-ash-gray: #b6b6b6;
  --ref-ghost-white: #f5f5f5;
  --ref-steel-gray: #727272;
}
```

## Typography direction
- **Farfetch Basis**: 400, 700, 13px, 15px, 22px, 30px, 1.20, 1.27, 1.31, 1.33; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `10px`
- Radius: `all: 0px`

## Component cues
- **Announcement Banner + Search Bar**: Reference component style.
- **Section Category Cards — Elige una sección**: Reference component style.
- **Fashion Category Grid — Moda para mujer**: Reference component style.
- **Invisible Action Button**: Navigation, product links, and interactive text elements.
- **Outline Accent Button**: Secondary calls to action, filtering, or options with less emphasis.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
