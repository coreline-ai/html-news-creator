# Sequence - Refero Design MD

- Source: https://styles.refero.design/style/707a9081-3d1d-4a0b-b1aa-b58b3fab09af
- Original site: https://www.sequencehq.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#f7f7f7` | neutral | Page background or card surface |
| Ghost Gray | `#efefef` | neutral | Page background or card surface |
| Stone Grey | `#e5e7eb` | neutral | Page background or card surface |
| Graphite | `#505050` | neutral | Border, muted text, or supporting surface |
| Dark Slate | `#42424a` | neutral | Border, muted text, or supporting surface |
| Ash | `#757575` | neutral | Border, muted text, or supporting surface |
| Deep Ink | `#1d1d20` | neutral | Primary text or dark surface |
| Sequence Violet | `#a565ff` | brand | Action accent / signal color |
| Deep Violet | `#5e5cff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-cloud-gray: #f7f7f7;
  --ref-ghost-gray: #efefef;
  --ref-stone-grey: #e5e7eb;
  --ref-graphite: #505050;
  --ref-dark-slate: #42424a;
  --ref-ash: #757575;
  --ref-deep-ink: #1d1d20;
}
```

## Typography direction
- **twkLausanne**: 300, 400, 500, 600, 700, 8px, 9px, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 24px, 1.00, 1.10, 1.20, 1.25, 1.33, 1.40, 1.43, 1.45, 1.50, 1.56, 1.60, 1.63, 1.67, 1.71, 1.75, 1.78, 1.80, 1.82, 1.85, 2.00; substitute `system-ui`.
- **moderatSerif**: 300, 400, 40px, 46px, 1.00; substitute `Georgia, serif`.
- **sfMono**: 400, 10px, 1.50, 1.80; substitute `Menlo, monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `tags: 20px, cards: 8px, buttons: 9999px, default: 4px, largeCards: 16px`

## Surface cues
- **Canvas Background** `#e5e7eb`: Dominant background color for the overall page, providing a very subtle off-white base.
- **Base Surface** `#ffffff`: Default background for most cards, content blocks, and UI elements, ensuring crisp contrast.
- **Nested Surface** `#f7f7f7`: Slightly darker secondary background used for nested cards or to subtly differentiate content areas.
- **Elevated Surface** `#ffffff`: Transparent white background with subtle shadow, indicating an elevated or interactive card element.

## Component cues
- **Primary Ghost Button**: Action button with an invisible background and text that blends with surrounds till hovered.
- **Secondary Ghost Button**: Muted action button or navigation link for less prominent interactions.
- **Branded Pill Button**: Primary call to action, drawing attention with the brand accent color.
- **Outline Pill Button**: Subtle, secondary call to action that needs slightly more emphasis than a ghost button.
- **Content Card - Default**: Container for articles, features, or small product showcases.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
