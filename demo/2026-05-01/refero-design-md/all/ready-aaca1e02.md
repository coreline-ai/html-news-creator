# Ready - Refero Design MD

- Source: https://styles.refero.design/style/aaca1e02-7b5a-4c03-ac40-454f0d477356
- Original site: https://ready.so
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
layered frosted glass

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Mist | `#f5f3f2` | neutral | Page background or card surface |
| Graphite Text | `#333333` | neutral | Primary text or dark surface |
| Slate Link | `#8b8c96` | neutral | Border, muted text, or supporting surface |
| Deep Plum | `#55269c` | brand | Action accent / signal color |
| Amethyst Haze | `#6c77b0` | brand | Action accent / signal color |
| Lavender Sky | `#817da6` | brand | Action accent / signal color |
| Radiant Orchid | `#8f4d75` | brand | Action accent / signal color |
| Violet Flash | `#7b4096` | brand | Action accent / signal color |
| Action Lavender | `#7366fe` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ash-mist: #f5f3f2;
  --ref-graphite-text: #333333;
  --ref-slate-link: #8b8c96;
  --ref-deep-plum: #55269c;
  --ref-amethyst-haze: #6c77b0;
  --ref-lavender-sky: #817da6;
  --ref-radiant-orchid: #8f4d75;
}
```

## Typography direction
- **GT Walsheim**: 700, 56px, 64px, 1.00; substitute `Montserrat`.
- **GT America Standard**: 300, 400, 500, 12px, 14px, 16px, 18px, 24px, 1.25, 1.33, 1.43, 1.50; substitute `Inter`.
- **GT America Standard**: 300, 400, 500, 12px, 14px, 16px, 18px, 24px, 1.25, 1.33, 1.43, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `cards: 32px, images: 16px, inputs: 24px, buttons: 24px`

## Component cues
- **Primary Header Heading**: Main page titles and prominent section headings.
- **Sub-Heading Text**: Secondary headings or large body text emphasis.
- **Body Text Standard**: General paragraph content and descriptions.
- **Muted Link/Label**: Navigation links, secondary actions, or helper text.
- **Product Feature Card**: Showcasing key features or content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
