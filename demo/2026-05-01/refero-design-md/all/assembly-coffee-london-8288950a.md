# Assembly Coffee London - Refero Design MD

- Source: https://styles.refero.design/style/8288950a-2731-44fd-85ef-211aecd8091d
- Original site: https://assemblycoffee.co.uk
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shadowy Gallery Vignettes

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ember | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Smoke | `#333333` | neutral | Primary text or dark surface |
| Ghost Marble | `#f6f7f2` | neutral | Page background or card surface |
| Greige Outline | `#dfdbca` | neutral | Page background or card surface |
| Moss Badge | `#cadcac` | semantic | Action accent / signal color |
| Goldenrod Badge | `#faf080` | semantic | Action accent / signal color |
| Sunken Gold Highlight | `#cfa53b` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ember: #000000;
  --ref-canvas-white: #ffffff;
  --ref-charcoal-smoke: #333333;
  --ref-ghost-marble: #f6f7f2;
  --ref-greige-outline: #dfdbca;
  --ref-moss-badge: #cadcac;
  --ref-goldenrod-badge: #faf080;
  --ref-sunken-gold-highlight: #cfa53b;
}
```

## Typography direction
- **GT America Standard**: 300, 400, 500, 600, 11px, 12px, 13px, 14px, 16px, 18px, 20px, 21px, 24px, 42px, 0.75, 1.20, 1.25, 1.40, 1.50, 2.00; substitute `system-ui`.
- **ID00 Serif**: 300, 400, 16px, 18px, 30px, 36px, 42px, 1.00, 1.20, 1.25, 1.50; substitute `serif`.
- **Helvetica**: 400, 500, 11px, 14px, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `pill: 9999px, default: 4px, largeButton: 60px`

## Surface cues
- **Midnight Canvas** `#000000`: Base page background, providing a deep, dark foundation.
- **Charcoal Smoke Card** `#333333`: Background for elevated content cards, subtly differentiated from the base canvas.
- **Greige Highlight** `#dfdbca`: Background for specific, light-themed sections or product cards where a higher contrast is desired.
- **Canvas White Panel** `#ffffff`: Background for pop-ups, modals, or focused content areas requiring maximum contrast with black text.

## Component cues
- **Text Button - Dark**: Ghost button for navigation and secondary actions on dark backgrounds.
- **Filled Button - Dark**: Primary call to action button.
- **Filled Button - Light**: Alternative primary call to action button for dark backgrounds.
- **Product Card - Transparent**: Gallery-style displays for products with visual emphasis on imagery.
- **Product Card - Elevated**: Content card for showcasing product details or features within sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
