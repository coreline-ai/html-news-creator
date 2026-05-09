# D.S. & DURGA - Refero Design MD

- Source: https://styles.refero.design/style/391bd401-06d7-4444-8243-8573e96eab24
- Original site: https://www.dsanddurga.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
curated gallery, artisanal display

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#f2e9de` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-parchment: #f2e9de;
  --ref-midnight-ink: #000000;
}
```

## Typography direction
- **Sofia Pro**: 400, 600, 800, 12px, 14px, 16px, 18px, 30px, 60px, 120px, 0.83, 0.92, 1.17, 1.22, 1.25, 1.27, 1.43; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `all: 0px`

## Component cues
- **Text Button - Canvas Background**: Standard button for actions and navigation, with a subtle background.
- **Ghost Button - Transparent**: Secondary action or link, blending into the background.
- **Navigation Link**: Primary navigation items in the header and footer.
- **Product Input Field**: Single-line text input for search or forms.
- **Information Banner**: Promotional or notification banner, often for shipping or offers.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
