# Graf Lantz - Refero Design MD

- Source: https://styles.refero.design/style/f1a690c7-234d-4ee9-9806-5790934e7043
- Original site: https://glob.land
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White canvas, sharp monochrome details.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Text Black | `#212121` | neutral | Primary text or dark surface |
| Graphite Text | `#474747` | neutral | Border, muted text, or supporting surface |
| Subtle Gray | `#eeeeee` | neutral | Page background or card surface |
| Deepest Gray | `#000000` | neutral | Primary text or dark surface |
| Muted Silver | `#7b7b7b` | neutral | Border, muted text, or supporting surface |
| Violet Action | `#574cd5` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-text-black: #212121;
  --ref-graphite-text: #474747;
  --ref-subtle-gray: #eeeeee;
  --ref-deepest-gray: #000000;
  --ref-muted-silver: #7b7b7b;
  --ref-violet-action: #574cd5;
}
```

## Typography direction
- **NeueHaasUnicaW1G**: 400, 500, 900, 12px, 14px, 16px, 1.00, 1.20, 1.40, 1.50; substitute `Helvetica Neue`.
- **Instrument Sans**: 400, 500, 14px, 16px, 32px, 1.20; substitute `Inter`.
- **accessibly**: 400, 16px, 35px, 1.00; substitute `System UI`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `15px`
- Element Gap: `15px`
- Radius: `pill: 50px, inputs: 0px, buttons: 0px, elements: 0px`

## Component cues
- **Primary Action Button**: Main interactive button
- **Search Input Field**: User input for search queries
- **Secondary Ghost Button**: Secondary action or navigational button
- **Header Navigation Link**: Top-level navigation items
- **Pill Button**: Small, high-contrast action or tag.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
