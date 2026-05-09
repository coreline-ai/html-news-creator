# Woven - Refero Design MD

- Source: https://styles.refero.design/style/76483bd1-37d3-4fb9-889b-aecf27b08b83
- Original site: https://wovenwhisky.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Artisanal parchment and charcoal calligraphy

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#232323` | neutral | Primary text or dark surface |
| Parchment | `#eeede5` | neutral | Page background or card surface |
| Porcelain | `#ffffff` | neutral | Page background or card surface |
| Slate | `#4a4a4a` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-carbon: #232323;
  --ref-parchment: #eeede5;
  --ref-porcelain: #ffffff;
  --ref-slate: #4a4a4a;
}
```

## Typography direction
- **Spezia Semi-Mono**: 400, 700, 12px, 14px, 15px, 16px, 18px, 20px, 1.20, 1.50, 1.63, 1.71, 2.40; substitute `IBM Plex Mono`.
- **Spezia**: 400, 16px, 20px, 24px, 32px, 1.00, 1.13, 1.20, 1.23, 1.50, 1.63, 1.71, 2.40; substitute `Inter`.
- **Figtree**: 400, 700, 12px, 14px, 1.63, 1.71; substitute `Figtree`.

## Spacing / shape
- Section Gap: `150px`
- Card Padding: `26px`
- Element Gap: `20px`
- Radius: `none: 0px, circle: 50%`

## Surface cues
- **Parchment Canvas** `#eeede5`: Dominant background for the entire page, providing a foundational warm neutral tone.
- **Porcelain Card** `#ffffff`: Elevated background for content blocks, product cards, or modals, offering clean contrast.

## Component cues
- **Ghost Button**: Interactive element (e.g. navigation, menu toggles)
- **Primary Filled Button**: Call to action
- **Product Card**: Displaying product listings
- **Circular Card**: Decorative or iconic element container
- **Underlined Input Field**: Text input areas

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
