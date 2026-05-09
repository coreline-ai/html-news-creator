# Bongusta - Refero Design MD

- Source: https://styles.refero.design/style/588b79ff-97ee-4e90-951e-401ece6c5fe1
- Original site: https://bongusta.dk
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm Minimalism Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Plum Core | `#321929` | brand | Action accent / signal color |
| Concrete Gray | `#e0dddf` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Shadow Tint | `#808080` | neutral | Border, muted text, or supporting surface |
| Input Charcoal | `#1d1d1f` | neutral | Primary text or dark surface |
| Ghost Gray | `#f0f0f0` | neutral | Page background or card surface |
| Muted Stone | `#636363` | neutral | Border, muted text, or supporting surface |
| Faded Text | `#6f6d6b` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-paper-white: #ffffff;
  --ref-plum-core: #321929;
  --ref-concrete-gray: #e0dddf;
  --ref-ink-black: #000000;
  --ref-shadow-tint: #808080;
  --ref-input-charcoal: #1d1d1f;
  --ref-ghost-gray: #f0f0f0;
  --ref-muted-stone: #636363;
}
```

## Typography direction
- **NeueHaasGrotesk**: 400, 11px, 14px, 15px, 16px, 18px, 22px, 1.00, 1.30, 1.38, 1.50, 1.70; substitute `Helvetica Neue`.
- **Bongusta**: 500, 28px, 1.50; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `4-10px`
- Radius: `cards: 0px, other: 40px, buttons: 9999px, navigation: 3.5px`

## Surface cues
- **Canvas** `#808080`: The deepest background layer, rare but present, establishing the base tone.
- **Base Surface** `#ffffff`: Primary background for pages, cards, and other content blocks, creating a clean white canvas.

## Component cues
- **Pill Ghost Button**: Primary interactive element for calls to action.
- **Product Card**: Displaying product listings, features, and content modules.
- **Filled Input Field**: User input for forms and subscriptions.
- **Outline Ghost Button**: Secondary action or navigation within content area.
- **White Background Button**: Used for specific interactive elements that need to stand out on darker backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
