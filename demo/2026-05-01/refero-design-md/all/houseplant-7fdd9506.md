# HOUSEPLANT - Refero Design MD

- Source: https://styles.refero.design/style/7fdd9506-0a85-41a5-b2a7-c5ce1f31d863
- Original site: https://www.houseplant.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Artisanal Collector's Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#f4f1e0` | neutral | Page background or card surface |
| Houseplant Deep Bark | `#321e1e` | brand | Action accent / signal color |
| Text Carbon | `#464545` | neutral | Border, muted text, or supporting surface |
| Surface Shadow | `#bdb498` | neutral | Border, muted text, or supporting surface |
| Button Shadow | `#463938` | neutral | Primary text or dark surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |
| Pure White Text | `#f4f4f4` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-parchment: #f4f1e0;
  --ref-houseplant-deep-bark: #321e1e;
  --ref-text-carbon: #464545;
  --ref-surface-shadow: #bdb498;
  --ref-button-shadow: #463938;
  --ref-pure-black: #000000;
  --ref-pure-white-text: #f4f4f4;
}
```

## Typography direction
- **Houseplant**: 400, 500, 600, 14px, 16px, 18px, 20px, 21px, 28px, 30px, 32px, 45px, 60px, 70px, 1.00, 1.15, 1.30, 1.33, 1.44, 1.71, 2.50, 2.79; substitute `Playfair Display`.
- **Roboto**: 400, 16px, 2.00; substitute `Roboto`.
- **NeueHelvetica55Roman**: 400, 16px, 1.15, 1.63; substitute `Helvetica Neue`.

## Spacing / shape
- Card Padding: `0px`
- Element Gap: `20px`
- Radius: `cards: 8px, buttons: 4px`

## Surface cues
- **Canvas Parchment** `#f4f1e0`: Dominant page background, providing a warm, inviting base for content.
- **Elevated Card Surface** `#f4f1e0`: Used for product cards and informational panels, providing slight elevation with a subtle shadow.
- **Content Block Dark** `#463938`: Background for specific feature sections or calls to action, providing a deep, grounding contrast.
- **Button Dark Fill** `#321e1`: Background for primary interactive elements, offering the strongest dark tone in the palette.

## Component cues
- **Filled Brand Button**: Primary call to action.
- **Circular Icon Button**: Utility actions like cart or user profile.
- **Ghost Header Navigation Link**: Top-level navigation items.
- **Ghost Footer Nav Link**: Footer navigation and secondary links.
- **Shop Now Button (Product Card)**: Secondary action within product cards.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
