# SuperHi Basic Income - Refero Design MD

- Source: https://styles.refero.design/style/e57d9536-22a7-49db-8bd4-4306d8927ec3
- Original site: https://www.superhibasicincome.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Bifurcated digital canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| SuperHi Blue | `#2727e6` | brand | Action accent / signal color |
| Hover Sky | `#9de6fa` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-superhi-blue: #2727e6;
  --ref-hover-sky: #9de6fa;
}
```

## Typography direction
- **Basis**: 400, 500, 700, 13px, 14px, 16px, 21px, 24px, 32px, 48px, 1.14, 1.17, 1.25, 1.33, 1.46, 1.50, 1.67; substitute `system-ui`.
- **DDC**: 400, 21px, 24px, 1.00, 1.14; substitute `Georgia, serif`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `32px`
- Element Gap: `8px`
- Radius: `tags: 50px, buttons: 16px`

## Component cues
- **Text Link**: Inline navigation, references, and emphasized text.
- **Interactive Orb Button**: Primary call to action in a decorative, circular form.
- **Pill Button**: Secondary action or tag, often with text content.
- **FAQ Accordion Item**: Expandable content block for questions and answers.
- **Checkbox/Radio Button**: Interactive selections with a custom visual style.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
