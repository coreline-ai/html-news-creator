# BUTT STUDIO - Refero Design MD

- Source: https://styles.refero.design/style/c6e55968-fa2d-47c9-b833-2c4ad1e74906
- Original site: https://www.butt-studio.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist canvas, bold typography, selective accents.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Deep Space | `#131313` | neutral | Primary text or dark surface |
| Smoke Gray | `#e0e0e0` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-pitch-black: #000000;
  --ref-deep-space: #131313;
  --ref-smoke-gray: #e0e0e0;
}
```

## Typography direction
- **helvetica**: 400, 20px, 40px, 1.00, 1.20; substitute `Avenir Next, Arial`.
- **Caslon**: 400, 42px, 1.00; substitute `Libre Caslon Display`.
- **Sometimes Times**: 400, 20px, 1.20; substitute `Times New Roman (with custom stylistic sets)`.

## Spacing / shape
- Section Gap: `180px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 10px, buttons: 50px, headings: 68px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background providing expansive whitespace.
- **Smoke Gray** `#e0e0e0`: Subtle surfaces for buttons and secondary content blocks.
- **Deep Space** `#131313`: High-contrast background for media players or distinct dark UI sections.

## Component cues
- **Pill Button**: Text button with rounded corners for primary actions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
