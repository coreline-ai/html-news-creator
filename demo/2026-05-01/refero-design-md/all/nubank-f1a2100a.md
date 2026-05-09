# Nubank - Refero Design MD

- Source: https://styles.refero.design/style/f1a2100a-7cda-4787-b8af-5c5edcfcdff0
- Original site: https://nubank.com.br
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Royalty Violet and Pill Forms — a playful, digital-first financial presence.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Royalty Violet | `#820ad1` | brand | Action accent / signal color |
| Deep Violet Shadow | `#290b4d` | brand | Action accent / signal color |
| Subtle Violet | `#714f8f` | brand | Action accent / signal color |
| Noir | `#000000` | neutral | Primary text or dark surface |
| Porcelain White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#f4f4f4` | neutral | Page background or card surface |
| Silver Mist | `#a2a2a2` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Dark Charcoal | `#666666` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#777777` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-royalty-violet: #820ad1;
  --ref-deep-violet-shadow: #290b4d;
  --ref-subtle-violet: #714f8f;
  --ref-noir: #000000;
  --ref-porcelain-white: #ffffff;
  --ref-ash-gray: #f4f4f4;
  --ref-silver-mist: #a2a2a2;
  --ref-medium-gray: #b3b3b3;
}
```

## Typography direction
- **Graphik Medium**: 400, 500, 12px, 14px, 16px, 18px, 20px, 22px, 24px, 36px, 48px, 56px, 1.00, 1.10, 1.20, 1.30, 1.44, 1.50, 1.66, 2.22, 2.50, 2.80; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16-32px`
- Element Gap: `8-24px`
- Radius: `cards: 12px, images: 32px, inputs: 24px, buttons: 999px, default: 8px`

## Component cues
- **CPF Sign-up Card**: Reference component style.
- **Product Carousel Cards**: Reference component style.
- **Primary & Secondary Button Group**: Reference component style.
- **Primary Action Button**: Call-to-action
- **Ghost Navigation Button**: Navigation and secondary actions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
