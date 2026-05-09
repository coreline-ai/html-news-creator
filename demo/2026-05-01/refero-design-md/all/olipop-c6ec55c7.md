# OLIPOP - Refero Design MD

- Source: https://styles.refero.design/style/c6ec55c7-0bd9-47c5-a4d2-669b7790c9cc
- Original site: https://drinkolipop.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whimsical soda shop on cream. Bold, rounded letterforms and a palette of comforting dark teal and creamy white, accented by juicy fruit colors, define its inviting, playful core.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Sea Teal | `#14433d` | brand | Action accent / signal color |
| Creamy Canvas | `#fdf7e7` | neutral | Page background or card surface |
| Cloud Burst Gray | `#d3e8e3` | neutral | Page background or card surface |
| Ash Slate | `#3a3a3a` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Ruby Red | `#7e0022` | brand | Action accent / signal color |
| Candy Apple Red | `#febac4` | accent | Action accent / signal color |
| Lavender Bloom | `#e3d2ed` | accent | Action accent / signal color |
| Tropical Sky | `#4ac1e0` | accent | Action accent / signal color |
| Mellow Yellow | `#fdf4b5` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-sea-teal: #14433d;
  --ref-creamy-canvas: #fdf7e7;
  --ref-cloud-burst-gray: #d3e8e3;
  --ref-ash-slate: #3a3a3a;
  --ref-pure-white: #ffffff;
  --ref-ruby-red: #7e0022;
  --ref-candy-apple-red: #febac4;
  --ref-lavender-bloom: #e3d2ed;
}
```

## Typography direction
- **WindsorEF**: 700, 800, 900, 20px, 32px, 48px, 52px, 72px, 80px, 1.00; substitute `Georgia Pro`.
- **Ano**: 400, 600, 700, 12px, 14px, 16px, 18px, 20px, 22px, 24px, 1.00, 1.20, 1.26, 1.40, 1.48, 1.50, 1.56, 1.60, 1.67, 1.80, 1.82, 1.88, 2.33; substitute `Inter`.
- **Helvetica**: 400, 16px, 1.50; substitute `Arial`.

## Spacing / shape
- Section Gap: `40-80px`
- Card Padding: `15px`
- Element Gap: `8-20px`
- Radius: `cards: 16px, inputs: 49px, buttons: 50px, circularElements: 100px`

## Component cues
- **Product Flavor Cards Row**: Reference component style.
- **Rewards Banner — Get Rewarded for Sipping**: Reference component style.
- **Shipping Announcement Banner + Button Group**: Reference component style.
- **Primary Action Button**: Primary calls to action in hero sections and prominent areas.
- **Secondary Action Button**: Secondary CTAs, navigation items that feel like buttons.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
