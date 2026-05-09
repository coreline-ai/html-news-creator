# Wemakethings - Refero Design MD

- Source: https://styles.refero.design/style/15d57573-513b-49aa-91c7-1b7f87bb1a55
- Original site: https://wemakethings.de
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome architectural blueprint

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Headline Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-headline-black: #000000;
}
```

## Typography direction
- **Maison Neue**: 400, 500, 16px, 18px, 24px, 43px, 65px, 1.11, 1.20, 1.33, 2.50; substitute `Inter`.
- **Unzyale**: 400, 58px, 1.20; substitute `Playfair Display`.
- **BASEBLOOM**: 400, 864px, 0.83; substitute `Bebas Neue`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `none: 0px`

## Surface cues
- **Page Background** `#ffffff`: The foundational canvas for all content, providing a stark, clean base.
- **Card Surface** `#ffffff`: Used for informational blocks and interactive components, delineated by a strong 1px black border.

## Component cues
- **Navigation Link**: Primary navigation element
- **Outlined Button**: Call to action for external links
- **Scroll Indicator**: Visual cue for more content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
