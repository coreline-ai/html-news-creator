# SuperMush - Refero Design MD

- Source: https://styles.refero.design/style/71a9583d-1710-4696-9269-50ca8c9a2cfa
- Original site: https://supermush.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Juicy electric canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Off White Clay | `#f5f4f1` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#707170` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#eeeeee` | neutral | Page background or card surface |
| Accent Blue | `#2f59f8` | brand | Action accent / signal color |
| Highlight Orange | `#ff632a` | brand | Action accent / signal color |
| Active Yellow | `#eaff00` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-off-white-clay: #f5f4f1;
  --ref-midnight-ink: #000000;
  --ref-graphite: #707170;
  --ref-steel-gray: #eeeeee;
  --ref-accent-blue: #2f59f8;
  --ref-highlight-orange: #ff632a;
  --ref-active-yellow: #eaff00;
}
```

## Typography direction
- **Founders Grotesk**: 400, 500, 700, 12px, 14px, 16px, 17px, 18px, 20px, 32px, 34px, 36px, 40px, 43px, 48px, 1.00, 1.04, 1.15, 1.17, 1.21, 1.25, 1.40, 1.50, 1.60, 1.67; substitute `Inter`.
- **GT Planar**: 400, 500, 700, 10px, 11px, 13px, 14px, 16px, 18px, 20px, 1.00, 1.15, 1.25, 1.29, 1.60; substitute `Montserrat`.
- **Font Awesome 5 Pro**: 300, 18px, 1.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 16px, inputs: 1.67772e+07px, buttons: 50px, general: 4px, imagery: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background, primary content sections, elevated cards.
- **Off White Clay** `#f5f4f1`: Secondary background for sections, subtle distinction between content blocks.

## Component cues
- **Primary Filled Button**: Calls to action, form submissions.
- **Ghost Button (Header Nav)**: Secondary navigation in header.
- **Pill Accent Button**: Information tags, small labels, sale indicators.
- **Neutral Rounded Button**: Quantity selectors, small interactive elements.
- **Product Card**: Displaying product items in grids.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
