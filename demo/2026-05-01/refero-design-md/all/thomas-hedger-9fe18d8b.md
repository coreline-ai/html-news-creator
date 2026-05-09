# Thomas Hedger - Refero Design MD

- Source: https://styles.refero.design/style/9fe18d8b-58b7-404d-bcc6-9e8a73b8862c
- Original site: https://thomashedger.co.uk
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid Canvas

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Grey | `#29242b` | neutral | Primary text or dark surface |
| Border Fog | `#e5e5e5` | neutral | Page background or card surface |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-canvas-white: #ffffff;
  --ref-ink-grey: #29242b;
  --ref-border-fog: #e5e5e5;
}
```

## Typography direction
- **Diatype**: 400, 9px, 19px, 1.10, 1.30; substitute `Inter`.
- **Diatype Variable**: 500, 700, 26px, 1.10; substitute `Inter`.
- **Times**: 400, 13px, 1.20; substitute `Times New Roman`.

## Spacing / shape
- Card Padding: `0px`
- Element Gap: `3px`
- Radius: `none: 0px`

## Component cues
- **Artwork Grid Item**: Primary display for artwork portfolio items.
- **Navigation Link**: Interactive text links in the header and footer.
- **Header Branding**: Site title in the main header.
- **Footer Copyright Text**: Small, legal text at the bottom of the page.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
