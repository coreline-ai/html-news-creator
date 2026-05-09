# HNST Studio - Refero Design MD

- Source: https://styles.refero.design/style/7de578bc-9fbd-4664-a731-6223515bb601
- Original site: https://www.letsbehonest.eu
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm minimum, strong accent — natural fibers on a stark, bright loom.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Soft Mist | `#f9f6f2` | neutral | Page background or card surface |
| Desert Sand | `#eee5d9` | neutral | Page background or card surface |
| Graphite | `#0e0e0e` | neutral | Primary text or dark surface |
| Ash | `#868686` | neutral | Border, muted text, or supporting surface |
| Silver | `#b7b7b7` | neutral | Border, muted text, or supporting surface |
| Crimson | `#892500` | brand | Action accent / signal color |
| Rose Blush | `#ea9195` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas: #ffffff;
  --ref-soft-mist: #f9f6f2;
  --ref-desert-sand: #eee5d9;
  --ref-graphite: #0e0e0e;
  --ref-ash: #868686;
  --ref-silver: #b7b7b7;
  --ref-crimson: #892500;
  --ref-rose-blush: #ea9195;
}
```

## Typography direction
- **Poppins**: 500, 600, 700, 11px, 13px, 16px, 20px, 62px, 1.15, 1.20, 1.25, 2.27; substitute `system-ui`.
- **Raleway**: 400, 600, 700, 12px, 13px, 14px, 15px, 16px, 1.20, 1.67, 1.70, 1.79; substitute `system-ui`.

## Spacing / shape
- Section Gap: `75px`
- Card Padding: `42px`
- Element Gap: `15px`
- Radius: `cards: 10px, badges: 0px, buttons: 0px`

## Surface cues
- **Base Canvas** `#ffffff`: Primary page background, high-contrast areas.
- **Content Surface** `#f9f6f2`: Main content backgrounds, providing a subtle shift from the base canvas.
- **Elevated Card** `#eee5d9`: Backgrounds for cards, badges, and other distinct content blocks.
- **Deep Accent** `#0e0e0`: Darkest surface, used for button backgrounds and strong visual anchors.

## Component cues
- **Primary Filled Button**: Call to action button
- **Image Overlay Badge**: Informational overlay on images
- **Product Category Badge**: Categorization tag for products
- **Navigation Link**: Main navigation item

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
