# A-WARE - Refero Design MD

- Source: https://styles.refero.design/style/5681f7b6-c665-44b8-a065-da7180133149
- Original site: https://a-ware.at
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist alpine clean

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Alabaster White | `#ffffff` | neutral | Page background or card surface |
| Greige Canvas | `#f7f5ee` | neutral | Page background or card surface |
| Stone Whisper | `#ece9df` | neutral | Page background or card surface |
| Subtle Ash | `#888783` | neutral | Border, muted text, or supporting surface |
| Harvest Gold | `#a77a41` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-alabaster-white: #ffffff;
  --ref-greige-canvas: #f7f5ee;
  --ref-stone-whisper: #ece9df;
  --ref-subtle-ash: #888783;
  --ref-harvest-gold: #a77a41;
}
```

## Typography direction
- **practice**: 400, 600, 14px, 16px, 18px, 23px, 25px, 36px, 38px, 88px, 1.00, 1.05, 1.19, 1.20, 1.40, 1.45; substitute `Inter`.
- **plantin**: 300, 400, 24px, 38px, 1.05, 1.20, 1.33; substitute `Playfair Display`.
- **lab-mono**: 400, 12px, 1.33; substitute `Space Mono`.

## Spacing / shape
- Card Padding: `72px`
- Element Gap: `24px`
- Radius: `cards: 12px, badges: 6px, inputs: 8px, buttons: 32px, general: 6px`

## Surface cues
- **Alabaster White Canvas** `#ffffff`: Primary page background, base for light elements.
- **Greige Canvas Card** `#f7f5ee`: Background for elevated content sections, cards, and product listings, providing a subtle visual separation and warmth.
- **Stone Whisper Footer** `#ece9df`: Background for the footer and other grounding structural elements for a slightly cooler and darker contrast against the canvas.

## Component cues
- **Ghost Outline Button (Light Text)**: Primary Call to Action on dark backgrounds.
- **Ghost Outline Button (Dark Text)**: Secondary Call to Action, active state for navigation.
- **Pill Button (Filled)**: Primary Call to Action on light backgrounds.
- **Product Card**: Displaying product information and features.
- **Text Input Field**: Collecting user input.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
