# Ingmar Coenen - Refero Design MD

- Source: https://styles.refero.design/style/f8c92b6b-a3a7-4141-ae61-3d865a106761
- Original site: https://ingmarcoenen.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome typographic canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Subtle Gray | `#f2f2f2` | neutral | Page background or card surface |
| Dark Charcoal | `#3a4042` | neutral | Primary text or dark surface |
| Medium Gray | `#919191` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-subtle-gray: #f2f2f2;
  --ref-dark-charcoal: #3a4042;
  --ref-medium-gray: #919191;
  --ref-light-gray: #cccccc;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `Helvetica Neue`.
- **Megazoid Regular**: 400, 295px, 0.90; substitute `Anton`.
- **ITC Garamond Std Light Condensed**: 400, 36px, 0.94; substitute `Garamond Light Condensed`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `14px`
- Element Gap: `10px`
- Radius: `cards: 12px, links: 4px, buttons: 100px, general: 12px`

## Component cues
- **Pill Navigation Button**: Primary navigation links and interactive controls.
- **Ghost Navigation Button**: Secondary navigation links and interactive controls, visually less prominent than filled buttons.
- **Start Project Button**: Prominent call to action, visually contrasting with other buttons.
- **Text Link Button**: Minimal interactive elements with a default browser link style.
- **Portfolio Grid Item**: Card-like containers for portfolio pieces.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
