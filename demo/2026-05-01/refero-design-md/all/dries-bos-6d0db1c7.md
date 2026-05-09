# Dries Bos - Refero Design MD

- Source: https://styles.refero.design/style/6d0db1c7-5500-40cd-b2f3-d3d9abbd3a2f
- Original site: https://www.driesbos.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Wireframe on parchment

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#e8e7e3` | neutral | Page background or card surface |
| Ink Jot | `#050200` | neutral | Primary text or dark surface |
| Ash Outline | `#747472` | neutral | Border, muted text, or supporting surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-parchment: #e8e7e3;
  --ref-ink-jot: #050200;
  --ref-ash-outline: #747472;
  --ref-pure-black: #000000;
}
```

## Typography direction
- **Sohne Buch**: 400, 20px, 1.45; substitute `Inter, Public Sans`.
- **myFont**: 400, 20px, 1.00; substitute `JetBrains Mono, IBM Plex Mono`.

## Spacing / shape
- Section Gap: `79px`
- Card Padding: `25px`
- Element Gap: `10px`
- Page Max Width: `1150px`
- Radius: `tags: 1000px, cards: 0px, buttons: 0px`

## Component cues
- **Naked Table Row Button**: Interactive row element within lists and tables, serving as a primary navigation trigger.
- **Outlined Category Tag**: Small, informational tags for categorization or status.
- **Subtle Pill Tag**: Discrete labels for content details, like 'startup' or 'mobile'.
- **Underlined Input Field**: Text input areas with a subtle bottom border.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
