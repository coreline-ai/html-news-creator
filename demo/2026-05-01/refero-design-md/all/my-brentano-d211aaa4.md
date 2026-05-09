# My Brentano - Refero Design MD

- Source: https://styles.refero.design/style/d211aaa4-e09b-4ef9-a9bf-f6fa8495de73
- Original site: https://mybrentano.ch
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Earthy botanical canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Text | `#212529` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-charcoal-text: #212529;
}
```

## Typography direction
- **Studio Feixen Sans Writer Book**: 400, 12px, 15px, 18px, 25px, 30px, 60px, 1.20, 1.67, 2.08, 2.50; substitute `Inter`.
- **Studio Feixen Sans Writer Book**: 700, 12px, 15px, 18px, 25px, 30px, 60px, 1.20, 1.67, 2.08, 2.50; substitute `Inter`.
- **Studio Feixen Sans Book**: 400, 15px, 30px, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `10px`
- Element Gap: `10px`
- Radius: `default: 0px, circularElements: 100%`

## Component cues
- **Circular Ghost Button**: Decorative or iconic buttons, cart badge.
- **Rectangular Outlined Button**: Primary action buttons for purchasing or navigation.
- **Ghost Navigation Link**: Subtle navigation elements.
- **Basic Input**: Form fields for user entry.
- **Header Navigation Item**: Interactive clickable item in the main site navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
