# Zipline - Refero Design MD

- Source: https://styles.refero.design/style/4a248569-2b5a-4416-bb2a-c78890218b9f
- Original site: https://www.zipline.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Open-air flight path – vast, clean, and direct.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cream Canvas | `#f7f4e8` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#c6c3ba` | neutral | Border, muted text, or supporting surface |
| Zipline Violet | `#643aed` | brand | Action accent / signal color |

```css
:root {
  --ref-cream-canvas: #f7f4e8;
  --ref-midnight-ink: #000000;
  --ref-cloud-gray: #c6c3ba;
  --ref-zipline-violet: #643aed;
}
```

## Typography direction
- **fkGroteskNeue**: 400, 500, 600, 700, 14px, 16px, 18px, 22px, 120px, 0.85, 1.00, 1.20, 1.40; substitute `Inter`.
- **fkScreamer**: 700, 40px, 90px, 120px, 150px, 0.85; substitute `Bebas Neue`.
- **fkDisplay**: 400, 22px, 0.85; substitute `Oswald`.

## Spacing / shape
- Section Gap: `53px`
- Card Padding: `14px`
- Element Gap: `24px`
- Page Max Width: `1320px`
- Radius: `cards: 20px, images: 20px, buttons: 20px`

## Surface cues
- **Cream Canvas** `#f7f4e8`: Primary page background and lightest surface level.
- **Cloud Gray** `#c6c3ba`: Secondary background for alternating sections or subtle differentiation.
- **Zipline Violet** `#643aed`: Elevated, branded surface for emphasized cards or content blocks.
- **Midnight Ink** `#000000`: Most prominent surface, used for filled buttons and strong containers.

## Component cues
- **Filled Primary Button**: Call to action
- **Outlined Secondary Button**: Secondary action
- **Ghost Text Button**: Navigation or tertiary action
- **Standard Card**: Content grouping
- **Branded Violet Card**: Emphasized content grouping

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
