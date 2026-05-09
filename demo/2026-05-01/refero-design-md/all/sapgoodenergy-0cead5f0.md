# SAPGOODENERGY - Refero Design MD

- Source: https://styles.refero.design/style/0cead5f0-0a56-401f-b637-81d1fe457259
- Original site: https://sapgoodenergy.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Athletic Minimalism: black ink on white canvas, with bursts of energetic orange.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Alabaster | `#fffffb` | neutral | Page background or card surface |
| Ash Grey | `#e7e7e7` | neutral | Page background or card surface |
| Graphite | `#303030` | neutral | Primary text or dark surface |
| Pewter | `#c0c0c0` | neutral | Border, muted text, or supporting surface |
| Slate | `#707070` | neutral | Border, muted text, or supporting surface |
| Energy Burst Orange | `#ff7840` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-alabaster: #fffffb;
  --ref-ash-grey: #e7e7e7;
  --ref-graphite: #303030;
  --ref-pewter: #c0c0c0;
  --ref-slate: #707070;
  --ref-energy-burst-orange: #ff7840;
}
```

## Typography direction
- **GT Pressura LC Standard**: 400, 500, 600, 700, 10px, 13px, 14px, 16px, 24px, 1.00, 1.08, 1.13, 1.14, 1.20, 1.60; substitute `Inter`.
- **Helvetica Neue LT Std**: 500, 800, 14px, 18px, 30px, 38px, 53px, 56px, 1.00, 1.03, 1.11, 1.60; substitute `Arial`.
- **GTStandard-M**: 500, 14px, 1.50; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `24px`
- Element Gap: `4px`
- Radius: `cards: 18px, inputs: 7px, buttons: 7px, interactiveElements: 14px, smallInteractiveElements: 4px`

## Component cues
- **Primary Action Button**: Filled button
- **Secondary Ghost Button**: Outlined/ghost button
- **Tertiary Ghost Button**: Outlined/ghost button (muted)
- **Callout Card**: Informational card with soft background
- **Content Card**: Container card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
