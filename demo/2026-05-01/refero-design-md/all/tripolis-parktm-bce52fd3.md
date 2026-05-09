# Tripolis-Park™ - Refero Design MD

- Source: https://styles.refero.design/style/bce52fd3-ac16-4e67-a45f-78bfc2350aad
- Original site: https://www.tripolis-park.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural grid on frosted glass

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Medium Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Light Stroke | `#e2e2e2` | neutral | Page background or card surface |
| Subtle Stroke | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Desert White | `#f0edea` | neutral | Page background or card surface |
| Tripolis Violet | `#ab8ff2` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-medium-gray: #808080;
  --ref-light-stroke: #e2e2e2;
  --ref-subtle-stroke: #cccccc;
  --ref-desert-white: #f0edea;
  --ref-tripolis-violet: #ab8ff2;
}
```

## Typography direction
- **Matter**: 400, 14px, 18px, 27px, 47px, 1.08, 1.12, 1.20, 1.25; substitute `Inter`.
- **IvarHeadline**: 400, 47px, 1.08, 1.12; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `23px`
- Element Gap: `5px`
- Page Max Width: `900px`
- Radius: `default: 0px, circular: 50%`

## Component cues
- **Ghost Button (Light)**: Navigation and secondary actions on dark backgrounds.
- **Ghost Button (Dark)**: Navigation and secondary actions on light backgrounds.
- **Circular Play Button**: Primary action button, typically for media playback.
- **Section Heading (IvarHeadline)**: Main content section titles.
- **Body Text (Matter-Regular)**: General paragraph text and descriptive content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
