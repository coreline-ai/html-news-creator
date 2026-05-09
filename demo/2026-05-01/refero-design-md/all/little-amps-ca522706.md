# Little Amps - Refero Design MD

- Source: https://styles.refero.design/style/ca522706-03ed-48cb-acb3-1bb2a22f2eda
- Original site: https://littleampscoffee.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm vinyl cafe

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cream Canvas | `#fff9f2` | neutral | Page background or card surface |
| Warm Beige | `#f6ede3` | neutral | Page background or card surface |
| Smoky Ash | `#e6dad4` | neutral | Page background or card surface |
| Muted Taupe | `#977e77` | neutral | Border, muted text, or supporting surface |
| Fawn Gray | `#cbbbb4` | neutral | Border, muted text, or supporting surface |
| Vinyl Brown | `#522c25` | brand | Action accent / signal color |
| Roast Red | `#c03001` | brand | Action accent / signal color |
| Mellow Ochre | `#c46500` | brand | Action accent / signal color |
| Community Blue | `#89b4ca` | brand | Action accent / signal color |
| Sunbeam Yellow | `#febf6f` | brand | Action accent / signal color |

```css
:root {
  --ref-cream-canvas: #fff9f2;
  --ref-warm-beige: #f6ede3;
  --ref-smoky-ash: #e6dad4;
  --ref-muted-taupe: #977e77;
  --ref-fawn-gray: #cbbbb4;
  --ref-vinyl-brown: #522c25;
  --ref-roast-red: #c03001;
  --ref-mellow-ochre: #c46500;
}
```

## Typography direction
- **Inclusive Sans**: 400, 12px, 13px, 14px, 15px, 16px, 1.00, 1.10, 1.20, 1.60; substitute `Open Sans`.
- **Necto Mono**: 400, 500, 10px, 12px, 13px, 14px, 16px, 0.80, 0.85, 1.00, 1.10, 1.20; substitute `Space Mono`.
- **Little Amps**: 500, 20px, 22px, 41px, 45px, 50px, 51px, 0.80, 1.00; substitute `League Spartan`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `36px`
- Element Gap: `6px`
- Radius: `cards: 8px, badges: 3px, images: 3px, inputs: 3px, buttons: 3px, largeCards: 22px`

## Component cues
- **Primary Action Button**: Filled button indicating the primary action.
- **Mellow Action Button**: Alternative action button, visually softer than the primary.
- **Community Action Button**: Accent button for specific calls to action, often related to community content.
- **Ghost Link Button**: Minimalist button for secondary or navigational actions.
- **Product Card**: Container for product listings or content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
