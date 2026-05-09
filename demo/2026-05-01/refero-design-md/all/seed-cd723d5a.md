# Seed - Refero Design MD

- Source: https://styles.refero.design/style/cd723d5a-e7ea-4e4c-a3bb-6cf56e05057a
- Original site: https://seed.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Forest & Snow Laboratory

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Green | `#1c3a13` | brand | Action accent / signal color |
| Snow White | `#fcfcf7` | neutral | Page background or card surface |
| Pale Green | `#d3fa99` | accent | Action accent / signal color |
| Frosted Glass | `#c4c7c4` | neutral | Border, muted text, or supporting surface |
| Warm Gray | `#eeeee9` | neutral | Page background or card surface |
| Charcoal Text | `#000000` | neutral | Primary text or dark surface |
| Muted Product Green | `#757c5d` | brand | Action accent / signal color |
| Muted Product Yellow | `#9f995b` | brand | Action accent / signal color |
| Muted Product Teal | `#698e79` | brand | Action accent / signal color |
| Ghost Button Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-forest-green: #1c3a13;
  --ref-snow-white: #fcfcf7;
  --ref-pale-green: #d3fa99;
  --ref-frosted-glass: #c4c7c4;
  --ref-warm-gray: #eeeee9;
  --ref-charcoal-text: #000000;
  --ref-muted-product-green: #757c5d;
  --ref-muted-product-yellow: #9f995b;
}
```

## Typography direction
- **Seed Sans**: 300, 350, 400, 500, 8px, 10px, 12px, 14px, 16px, 18px, 20px, 24px, 32px, 40px, 48px, 0.90, 1.00, 1.10, 1.17, 1.20, 1.30, 1.40, 1.50, 2.19; substitute `Inter`.
- **Seed Sans Mono**: 300, 400, 12px, 16px, 1.50; substitute `IBM Plex Mono`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 16px, badges: 1188px, inputs: 8px, buttons: 1584px`

## Surface cues
- **Snow White Canvas** `#fcfcf7`: Primary page background and outermost UI layer, offering a clean, bright foundation.
- **Warm Gray Section** `#eeeee9`: Secondary background for distinct content sections, providing subtle visual breaks.
- **Frosted Card** `#c4c7c4`: Background for cards and elevated UI components, slightly muted and diffused.
- **Forest Green Surface** `#1c3a13`: Accent background for featured cards or UI elements to draw attention.
- **Dark Overlay** `#666666`: Background for subtle overlay elements or ghost button states.

## Component cues
- **Primary Action Button**: Main call to action
- **Ghost Action Button**: Secondary action or link
- **Ghost Pill Button**: Interactive navigation or filter
- **Nav Pill Button**: Interactive navigation or filter on light backgrounds
- **Product Card**: Displaying product information

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
