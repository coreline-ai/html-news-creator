# Microsoft - Refero Design MD

- Source: https://styles.refero.design/style/c70a9990-bc4b-4a64-a69b-aeb7b344fb74
- Original site: https://www.microsoft.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp White Blueprint

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ocean Blue | `#0067b8` | brand | Action accent / signal color |
| Charcoal Black | `#000000` | neutral | Primary text or dark surface |
| Graphite Gray | `#616161` | neutral | Border, muted text, or supporting surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#f2f2f2` | neutral | Page background or card surface |
| Dark Slate | `#262626` | neutral | Primary text or dark surface |
| Deep Ash | `#171717` | neutral | Primary text or dark surface |

```css
:root {
  --ref-ocean-blue: #0067b8;
  --ref-charcoal-black: #000000;
  --ref-graphite-gray: #616161;
  --ref-cloud-white: #ffffff;
  --ref-fog-gray: #f2f2f2;
  --ref-dark-slate: #262626;
  --ref-deep-ash: #171717;
}
```

## Typography direction
- **Segoe UI**: 400, 600, 11px, 13px, 14px, 15px, 16px, 29px, 37px, 1.00, 1.20, 1.33, 1.45, 1.50, 2.27; substitute `Arial`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `48px`
- Element Gap: `8px`
- Radius: `cards: 0px, buttons: 2px`

## Surface cues
- **Fog Gray** `#f2f2f2`: Primary page canvas and background for alternating sections.
- **Cloud White** `#ffffff`: Elevated card surfaces, content blocks, and UI components that require visual separation from the canvas.

## Component cues
- **Primary Action Button**: Filled button
- **Ghost Border Button**: Outlined button
- **Subtle Link Button**: Text link styled as button
- **Circular Icon Button**: Icon button
- **Feature Card**: Information display card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
