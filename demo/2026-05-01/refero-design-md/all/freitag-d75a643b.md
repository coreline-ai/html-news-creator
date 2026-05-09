# Freitag - Refero Design MD

- Source: https://styles.refero.design/style/d75a643b-a518-4550-b430-679cd989a447
- Original site: https://freitag.ch/en_ID
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Recycled canvas gallery

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Silver Foam | `#cacaca` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Graphite Outline | `#404040` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#f1f1f1` | neutral | Page background or card surface |
| Muted Ash | `#616161` | neutral | Border, muted text, or supporting surface |
| Iron Oxide | `#1a1b1e` | neutral | Primary text or dark surface |
| Shadow Tint | `#969696` | neutral | Border, muted text, or supporting surface |
| Swiper Blue | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-silver-foam: #cacaca;
  --ref-canvas-white: #ffffff;
  --ref-graphite-outline: #404040;
  --ref-light-gray: #f1f1f1;
  --ref-muted-ash: #616161;
  --ref-iron-oxide: #1a1b1e;
  --ref-shadow-tint: #969696;
}
```

## Typography direction
- **ui-sans-serif**: 400, 11px, 16px, 1.15, 1.50; substitute `system-ui`.
- **AkkStdRg**: 400, 8px, 10px, 11px, 16px, 24px, 32px, 48px, 0.74, 0.97, 1.10, 1.15, 1.28, 1.50; substitute `Inter`.
- **FRg**: 400, 10px, 0.74; substitute `Roboto Condensed`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `12px`
- Page Max Width: `1200px`
- Radius: `cards: 0px, images: 12px, buttons: 9999px, navigation: 16px`

## Surface cues
- **Silver Foam Canvas** `#cacaca`: Primary page background and overall site foundation.
- **Canvas White Panel** `#ffffff`: Content cards, product displays, and button fills.
- **Light Gray Accent** `#f1f1f1`: Secondary background for buttons or navigation hover states.

## Component cues
- **Pill Button - Canvas Fill**: Primary action button
- **Pill Button - Light Gray Fill**: Secondary action button
- **Ghost Button**: Subtle action button
- **Square Button**: Action button in contained spaces
- **Product Display Card**: Showcasing individual products or categories

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
