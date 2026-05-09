# Alt–Border - Refero Design MD

- Source: https://styles.refero.design/style/5fd2cdc0-05ac-4290-b67c-72e7525a532c
- Original site: https://www.alt-border.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochromatic minimalist gallery

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Grey | `#333333` | neutral | Primary text or dark surface |
| Pale Stone | `#808080` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-charcoal-grey: #333333;
  --ref-pale-stone: #808080;
}
```

## Typography direction
- **Inferi**: 200, 300, 400, 14px, 21px, 34px, 120px, 1.00, 2.00; substitute `Georgia`.
- **Neuehaasdisplay**: 300, 105px, 0.85, 0.92; substitute `Helvetica Neue`.
- **Suisseintl**: 300, 21px, 1.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `9px`
- Element Gap: `9px`
- Radius: `cards: 10px, images: 10px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for all content blocks

## Component cues
- **Navigation Link**: Primary site navigation, secondary links like 'Read more'
- **Ghost Button**: Actionable text that blends into surrounds but indicates interaction
- **Image Grid Card**: Displaying project thumbnails and content previews in a masonry-style grid
- **Content Section Headline**: Breaking up content sections with prominent descriptive text
- **Dividing Line**: Subtle visual separation between content blocks or navigation items

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
