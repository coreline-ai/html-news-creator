# Tparkes - Refero Design MD

- Source: https://styles.refero.design/style/a21cf7a4-80e0-4f4a-9297-823a5180c2d3
- Original site: https://www.tparkes.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital canvas.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Carbon Text | `#333333` | neutral | Primary text or dark surface |
| Smoke Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Midnight Black | `#000000` | neutral | Primary text or dark surface |
| Mist Border | `#d6d6d6` | neutral | Border, muted text, or supporting surface |
| Silver Link | `#808080` | neutral | Border, muted text, or supporting surface |
| Accent Yellow | `#f5ffbe` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-carbon-text: #333333;
  --ref-smoke-gray: #b3b3b3;
  --ref-midnight-black: #000000;
  --ref-mist-border: #d6d6d6;
  --ref-silver-link: #808080;
  --ref-accent-yellow: #f5ffbe;
}
```

## Typography direction
- **Instrumentsans**: 600, 700, 10px, 17px, 22px, 24px, 86px, 0.83, 0.95, 1.09, 1.18, 1.20, 1.80; substitute `Montserrat, Inter`.
- **Arial**: 400, 14px, 1.43; substitute `Helvetica Neue, sans-serif`.

## Spacing / shape
- Section Gap: `120px`
- Card Padding: `10px`
- Element Gap: `20px`
- Radius: `cards: 12px, icons: 8px, images: 16px, buttons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background.
- **Accent Yellow** `#f5ffbe`: Subtle background for highlighted content cards.

## Component cues
- **Text Accent Card**: Highlights specific content blocks or portfolio entries.
- **Header Navigation Link**: Primary navigation elements in the page header.
- **Ghost Action Link**: Interactive elements, typically for navigation or calls to explore.
- **Profile Avatar**: User or brand identifier.
- **Project Preview Image**: Visual representation of projects or work.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
