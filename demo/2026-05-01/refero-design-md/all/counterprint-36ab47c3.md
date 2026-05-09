# Counterprint - Refero Design MD

- Source: https://styles.refero.design/style/36ab47c3-3d47-42a5-af2e-1760bc348bcd
- Original site: https://www.counter-print.co.uk
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Graphic design manual on white canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Text Black | `#1c1c1c` | neutral | Primary text or dark surface |
| Border Gray | `#e5e7eb` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-text-black: #1c1c1c;
  --ref-border-gray: #e5e7eb;
}
```

## Typography direction
- **Helvetica**: 400, 700, 15px, 20px, 1.00; substitute `system-ui, sans-serif`.
- **GTStandard-M**: 400, 15px, 1.50; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `28px`
- Card Padding: `8px`
- Element Gap: `8px`
- Radius: `inputs: 15px, others: 9999px, buttons: 9999px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and content areas
- **Border Gray** `#e5e7eb`: Subtle visual separation for lists and card-like elements

## Component cues
- **Primary Ghost Button**: Interactive element
- **Text Link Button**: Interactive element
- **Search Input Field**: Data entry
- **Product Grid Item**: Display component for products
- **Nav Menu Item**: Navigation link

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
