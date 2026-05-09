# Spacelab - Refero Design MD

- Source: https://styles.refero.design/style/7fdcf5eb-4d65-49a2-b887-60119bca4edc
- Original site: https://spacelab.co.uk
- Theme: `light`
- Industry: `design`
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
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#2c2222` | neutral | Primary text or dark surface |
| Stone Gray | `#b2b4b1` | neutral | Border, muted text, or supporting surface |
| Deep Violet | `#495472` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite: #2c2222;
  --ref-stone-gray: #b2b4b1;
  --ref-deep-violet: #495472;
}
```

## Typography direction
- **Helvetica Neue**: 400, 15px, 17px, 19px, 21px, 30px, 62px, 1.00, 1.07, 1.10, 1.15, 1.20; substitute `Arial`.
- **HelveticaNeue-Light**: 400, 17px, 1.2.

## Spacing / shape
- Section Gap: `42px`
- Card Padding: `21px`
- Element Gap: `21px`
- Radius: `none: 0px, cards: 0px, small: 4px, buttons: 0px`

## Component cues
- **Primary Action Button**: Interactive element
- **Navigation Link List**: Navigation element
- **Feature Card**: Content display
- **Circular Image Card**: Visual content display
- **Subtle Link Text**: Secondary navigation or semantic link

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
