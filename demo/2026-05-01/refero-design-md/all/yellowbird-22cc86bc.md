# Yellowbird® - Refero Design MD

- Source: https://styles.refero.design/style/22cc86bc-6c5f-4413-a4a2-66b8ddc82ad0
- Original site: https://www.yellowbirdfoods.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Bold yellow manifesto

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Yellowbird Yellow | `#ffe845` | brand | Action accent / signal color |
| Midnight Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Warm Paper | `#fbfaf2` | neutral | Page background or card surface |
| Electric Blue | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-yellowbird-yellow: #ffe845;
  --ref-midnight-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-warm-paper: #fbfaf2;
  --ref-electric-blue: #007aff;
}
```

## Typography direction
- **ABC Monument Grotesk**: 400, 14px, 18px, 27px, 30px, 41px, 45px, 61px, 0.78, 0.87, 0.90, 1.00, 1.10, 1.20, 1.30, 1.67, 2.14.
- **Pitch Sans**: 400, 600, 16px, 18px, 27px, 0.84, 1.00, 1.20, 1.30, 1.46.
- **Gooper**: 400, 700, 91px, 1.05.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `20px`
- Element Gap: `24px`
- Radius: `cards: 30px, buttons: 6px, default: 0px, largeCards: 36px, smallButtons: 14px, interactiveElements: 10px`

## Component cues
- **Outline Navigation Link**: Global navigation item
- **Primary Call to Action Button**: Emphasized action
- **Ghost Call to Action Button**: Secondary action or link
- **Category Filter Button**: Product filtering or classification
- **Product Card**: Display individual product items

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
