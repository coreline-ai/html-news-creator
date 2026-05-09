# Sneak in Peace - Refero Design MD

- Source: https://styles.refero.design/style/643f90ba-dc30-428b-a145-26f02fe70551
- Original site: https://www.sneakinpeace.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Overlaid fashion showcase

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#3d3d3d` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Concrete Gray | `#8d8d8d` | neutral | Border, muted text, or supporting surface |
| Pale Ash | `#f0eeed` | neutral | Page background or card surface |
| Wolf Gray | `#9e9e9e` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#b5b5b5` | neutral | Border, muted text, or supporting surface |
| Digital Violet | `#142161` | accent | Action accent / signal color |
| Action Crimson | `#ba2223` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #3d3d3d;
  --ref-canvas-white: #ffffff;
  --ref-deep-space: #000000;
  --ref-concrete-gray: #8d8d8d;
  --ref-pale-ash: #f0eeed;
  --ref-wolf-gray: #9e9e9e;
  --ref-silver-mist: #b5b5b5;
  --ref-digital-violet: #142161;
}
```

## Typography direction
- **NTNeuss**: 400, 500, 8px, 9px, 10px, 11px, 12px, 13px, 14px, 1.00, 1.20, 1.50, 2.10; substitute `Inter`.
- **RecklessNeue-Book**: 400, 16px, 21px, 1.40, 1.50; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `40px`
- Element Gap: `6px`
- Radius: `tags: 26px, cards: 6px, badges: 4px, inputs: 6px, buttons: 6px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and main content cards
- **Pale Ash** `#f0eeed`: Secondary background for badges and subtle sections
- **Concrete Gray** `#8d8d8d`: Background for interactive linked cards and product listings

## Component cues
- **Live Indicator Button**: Primary Call to Action
- **Ghost Schedule Button**: Secondary Action
- **Navigation Link Button**: Tertiary Navigation Link
- **Product Info Card (Detailed)**: Content Display, Primary Information Card
- **Product Item Card (Compact)**: List Item, Product Thumbnail

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
