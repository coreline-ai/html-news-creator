# Faire ES - Refero Design MD

- Source: https://styles.refero.design/style/6fb648be-cc69-4a84-a798-9f0f006922a0
- Original site: https://www.faire.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm artisanal marketplace.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fbf8f6` | neutral | Page background or card surface |
| Surface White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#333333` | neutral | Primary text or dark surface |
| Fog Gray | `#dadada` | neutral | Page background or card surface |
| Storm Gray | `#6c6a6a` | neutral | Border, muted text, or supporting surface |
| Market Yellow | `#f1f29f` | brand | Action accent / signal color |
| Toastify Light Text | `#757575` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #fbf8f6;
  --ref-surface-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite: #333333;
  --ref-fog-gray: #dadada;
  --ref-storm-gray: #6c6a6a;
  --ref-market-yellow: #f1f29f;
  --ref-toastify-light-text: #757575;
}
```

## Typography direction
- **Graphik**: 100, 400, 14px, 16px, 18px, 22px, 28px, 30px, 1.20, 1.25, 1.27, 1.43, 1.44, 1.45, 1.50; substitute `Inter`.
- **Graphik_fix**: 400, 14px, 16px, 1.43, 1.50; substitute `Inter`.
- **nantes**: 400, 22px, 30px, 38px, 52px, 1.23, 1.27, 1.32, 1.45; substitute `Merriweather`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `tags: 40px, cards: 4px, search: 999px, buttons: 4px, default: 4px`

## Surface cues
- **Canvas White** `#fbf8f6`: Primary page background layer.
- **Surface White** `#ffffff`: Default background for cards, modals, and elevated UI elements.

## Component cues
- **Navigation Link**: Navigational elements in headers and footers.
- **Text Button**: Low-prominence actions, often inline or secondary.
- **Default Button**: General purpose buttons.
- **Primary Action Button**: Prominent calls to action, typically for sign-up or purchase.
- **Pill Button**: Category filters or tags.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
