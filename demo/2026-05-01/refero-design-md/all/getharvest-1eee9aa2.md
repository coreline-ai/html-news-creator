# Getharvest - Refero Design MD

- Source: https://styles.refero.design/style/1eee9aa2-1e23-4675-9f6e-fb98c93969bd
- Original site: https://www.getharvest.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, organized workspace: like an inviting desk with neatly arranged tools and a single, bright sticky note.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Amber Glow | `#fa5d00` | brand | Action accent / signal color |
| Harvest Cream | `#fff8f1` | neutral | Page background or card surface |
| Deep Graphite | `#1d1e1c` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Soft Fog | `#c0bbb6` | neutral | Border, muted text, or supporting surface |
| Pale Sand | `#e3d6c5` | neutral | Border, muted text, or supporting surface |
| Muted Stone | `#8e8b87` | neutral | Border, muted text, or supporting surface |
| Link Gray | `#615f5c` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#d9d9d9` | neutral | Page background or card surface |
| Golden Wash | `#fee3b5` | accent | Action accent / signal color |

```css
:root {
  --ref-amber-glow: #fa5d00;
  --ref-harvest-cream: #fff8f1;
  --ref-deep-graphite: #1d1e1c;
  --ref-canvas-white: #ffffff;
  --ref-soft-fog: #c0bbb6;
  --ref-pale-sand: #e3d6c5;
  --ref-muted-stone: #8e8b87;
  --ref-link-gray: #615f5c;
}
```

## Typography direction
- **MuotoWeb**: 400, 500, 600, 700, 13px, 14px, 16px, 17px, 18px, 20px, 22px, 24px, 25px, 26px, 28px, 34px, 48px, 50px, 1.00, 1.10, 1.15, 1.20, 1.26, 1.30, 1.35, 1.38, 1.40, 1.50; substitute `Inter`.
- **Monarch**: 400, 72px, 1.20; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 20px, other: 16px, images: 16px, inputs: 16px, buttons: 16px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and base for prominent content.
- **Harvest Cream** `#fff8f1`: Background for secondary content blocks and feature cards, providing a soft, subtle lift.
- **Amber Glow Solid** `#fa5d00`: Filled interactive components, indicating active state or primary action.

## Component cues
- **Primary Action Button**: Call-to-action button
- **Standard Content Card**: Informational content container
- **Elevated Content Card**: Prominent content container
- **Text Input Field**: User data input

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
