# Flowers For Society - Refero Design MD

- Source: https://styles.refero.design/style/e00519a1-7b8a-4171-b49b-550c64a57d3c
- Original site: https://flowersforsociety.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Organic Modernity — grounded, yet forward-looking

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Deep Cobalt | `#203b90` | brand | Action accent / signal color |
| Muted Indigo | `#7989bc` | neutral | Border, muted text, or supporting surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Pale Ash | `#f2f2f2` | neutral | Page background or card surface |
| Charcoal Border | `#1b1b1b` | neutral | Primary text or dark surface |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-deep-cobalt: #203b90;
  --ref-muted-indigo: #7989bc;
  --ref-ink-black: #000000;
  --ref-pale-ash: #f2f2f2;
  --ref-charcoal-border: #1b1b1b;
}
```

## Typography direction
- **Soehne**: 400, 700, 11px, 14px, 16px, 18px, 1.20, 1.30, 1.40, 1.50, 1.80; substitute `system-ui`.
- **Integral**: 400, 13px, 15px, 18px, 35px, 37px, 45px, 52px, 0.92, 1.00, 1.10, 1.28; substitute `serif`.
- **Arial**: 400, 700, 14px, 1.20; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `30px`
- Element Gap: `5px`
- Radius: `cards: 4px, inputs: 41px, buttons: 41px, smallElements: 4px`

## Surface cues
- **Page Canvas** `#ffffff`: The primary background for most page content and interactive elements.
- **Section Background** `#f2f2f2`: Used to differentiate major content sections, providing subtle visual breaks.

## Component cues
- **Primary Filled Button**: Main call-to-action button, conveying primary intent.
- **Ghost Button**: Secondary action or navigational button, designed to be less prominent.
- **Large Rounded Heading Button**: Specialized large button for key conceptual actions or navigation between sections.
- **Text Input (Rounded)**: Standard form input for user data entry.
- **Text Input (Subtle)**: Alternative simple text input, potentially for smaller forms or searches.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
