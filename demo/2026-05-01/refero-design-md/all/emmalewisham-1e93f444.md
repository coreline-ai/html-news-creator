# Emmalewisham - Refero Design MD

- Source: https://styles.refero.design/style/1e93f444-0b01-4412-aa2b-877be5ef08d7
- Original site: https://emmalewisham.co.uk
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Soft Pink Marble with Deep Orchid

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Vanilla Cream | `#ffffff` | neutral | Page background or card surface |
| Powder Pink | `#f2f1ef` | neutral | Action accent / signal color |
| Charcoal Ink | `#000000` | neutral | Primary text or dark surface |
| Smoke Gray | `#a09c97` | neutral | Border, muted text, or supporting surface |
| Deep Plum | `#49369e` | brand | Action accent / signal color |
| Lavender Mist | `#a9a7db` | accent | Action accent / signal color |
| Warm Petal | `#ec9bad` | accent | Action accent / signal color |

```css
:root {
  --ref-vanilla-cream: #ffffff;
  --ref-powder-pink: #f2f1ef;
  --ref-charcoal-ink: #000000;
  --ref-smoke-gray: #a09c97;
  --ref-deep-plum: #49369e;
  --ref-lavender-mist: #a9a7db;
  --ref-warm-petal: #ec9bad;
}
```

## Typography direction
- **Martina Plantijn**: 300, 400, 700, 11px, 13px, 14px, 16px, 20px, 30px, 1.00, 1.20, 1.25, 1.38, 1.40, 1.50, 1.63, 1.69, 1.82, 1.86; substitute `Playfair Display`.
- **Regola Pro Book**: 400, 16px, 20px, 24px, 80px, 1.20, 1.25, 1.40, 1.63; substitute `Inter`.

## Spacing / shape
- Section Gap: `30px`
- Element Gap: `5px`
- Radius: `body: 10px, cards: 0px, buttons: 3px, navBadges: 50px`

## Surface cues
- **Page Canvas** `#f2f1ef`: The primary background for all page content, providing a soft, uniform base.
- **Content Card** `#ffffff`: Background for secondary content areas and cards, creating a subtle lift from the canvas.

## Component cues
- **Ghost Button - Deep Plum**: Primary call to action for interactive elements.
- **Ghost Button - Charcoal Ink**: Secondary call to action.
- **Image Card**: Product display or informational cards.
- **Text Input**: User input fields.
- **Navigation Badge - Warm Petal**: Small, functional numerical indicators in navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
