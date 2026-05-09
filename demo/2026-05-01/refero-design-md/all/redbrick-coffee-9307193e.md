# Redbrick Coffee - Refero Design MD

- Source: https://styles.refero.design/style/9307193e-7ce3-48c1-b650-8ab77aa83c3f
- Original site: https://redbrick.coffee
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Red enamel on white canvas.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Crimson Roast | `#e82c2a` | brand | Action accent / signal color |
| Inkwell | `#212529` | neutral | Primary text or dark surface |
| Cloud Cover | `#f2f2f2` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Deep Space | `#121212` | neutral | Primary text or dark surface |

```css
:root {
  --ref-crimson-roast: #e82c2a;
  --ref-inkwell: #212529;
  --ref-cloud-cover: #f2f2f2;
  --ref-pure-white: #ffffff;
  --ref-deep-space: #121212;
}
```

## Typography direction
- **Surt**: 400, 15px, 20px, 30px, 35px, 1.00, 1.20, 1.30, 1.50; substitute `Inter`.
- **Editorial Old**: 300, 100px, 105px, 150px, 0.99, 1.10, 1.20; substitute `Playfair Display`.
- **system-ui**: 400, 10px, 1.50; substitute `Arial`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `cards: 25px, links: 3.75px, images: 25px, inputs: 50px, buttons: 50px`

## Surface cues
- **Pure White Canvas** `#ffffff`: Dominant page background, providing a clean, bright foundation.
- **Cloud Cover Card** `#f2f2f2`: Background for product cards, providing a subtle differentiation from the main canvas.
- **Crimson Roast Accent** `#e82c2a`: Used as prominent background for banners or active states, drawing immediate attention.
- **Deep Space Overlay** `#121212`: Highly contrasting background for specific, usually interactive, calls to action like 'Skip to content'.

## Component cues
- **Outlined Call to Action Button**: Primary interactive element for actions.
- **Product Card**: Displays individual product items in a grid.
- **Outlined Input Field**: User input fields.
- **Navigation Link**: Top-level navigation items.
- **Hero Headline**: Large, attention-grabbing titles.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
