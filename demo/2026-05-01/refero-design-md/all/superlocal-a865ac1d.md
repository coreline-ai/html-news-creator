# Superlocal - Refero Design MD

- Source: https://styles.refero.design/style/a865ac1d-a4c2-425b-90db-2a7ec6d461a3
- Original site: https://superlocaldesign.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm Ink on Aged Paper — a hand-crafted, tactile aesthetic for a design conference.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Electric Blue | `#1673ff` | brand | Action accent / signal color |
| Pueblo Spice | `#3d2800` | brand | Action accent / signal color |
| Warm Button | `#604106` | brand | Action accent / signal color |
| Sunburst Orange | `#ff7b02` | accent | Action accent / signal color |
| Harvest Glow | `#ffae45` | accent | Action accent / signal color |
| Fuchsia Flush | `#e045ff` | accent | Action accent / signal color |
| Parchment | `#fbf5e7` | neutral | Page background or card surface |
| Onyx | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Light Gray Divider | `#c4c4c4` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-electric-blue: #1673ff;
  --ref-pueblo-spice: #3d2800;
  --ref-warm-button: #604106;
  --ref-sunburst-orange: #ff7b02;
  --ref-harvest-glow: #ffae45;
  --ref-fuchsia-flush: #e045ff;
  --ref-parchment: #fbf5e7;
  --ref-onyx: #000000;
}
```

## Typography direction
- **RST Reactor**: 400, 10px, 12px, 14px, 16px, 17px, 64px, 172px, 1.00, 1.20, 1.30, 1.41, 1.50, 2.00; substitute `IBM Plex Mono`.
- **Inter**: 400, 16px, 1.60; substitute `Inter`.
- **system sans-serif**: 400, 12px, 1.20.

## Spacing / shape
- Section Gap: `48-78px`
- Card Padding: `8px`
- Element Gap: `10-24px`
- Radius: `cards: 30px, buttons: 99px, pillForms: 9999px`

## Component cues
- **CTA Banner with Reserve Button**: Reference component style.
- **Cronograma Section Header**: Reference component style.
- **Partner Card Grid**: Reference component style.
- **Primary Navigation Link**: Top navigation items
- **Pueblo Spice Pill Button**: Call to action button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
