# Dollar Shave Club - Refero Design MD

- Source: https://styles.refero.design/style/6d72f05e-dce6-43ad-9532-f61bf211ed46
- Original site: https://www.dollarshaveclub.com
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Bold utility, clear guidance

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Blue | `#142978` | brand | Action accent / signal color |
| Mahogany Red | `#82163f` | brand | Action accent / signal color |
| Action Orange | `#fe5000` | brand | Action accent / signal color |
| Deep Space Blue | `#0a153c` | brand | Action accent / signal color |
| Crisp White | `#ffffff` | neutral | Page background or card surface |
| Slate Gray | `#404040` | neutral | Border, muted text, or supporting surface |
| Powder Blue | `#dbebf5` | neutral | Action accent / signal color |
| Warm Cream | `#f5ecdf` | neutral | Page background or card surface |
| Light Gray | `#eeeeee` | neutral | Page background or card surface |
| Platinum Gray | `#e3e3e3` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-blue: #142978;
  --ref-mahogany-red: #82163f;
  --ref-action-orange: #fe5000;
  --ref-deep-space-blue: #0a153c;
  --ref-crisp-white: #ffffff;
  --ref-slate-gray: #404040;
  --ref-powder-blue: #dbebf5;
  --ref-warm-cream: #f5ecdf;
}
```

## Typography direction
- **DSC Specter**: 400, 600, 700, 800, 900, 12px, 14px, 15px, 16px, 18px, 20px, 24px, 32px, 40px, 52px, 0.80, 1.00, 1.19, 1.20, 1.25, 1.29, 1.30, 1.33, 1.36, 1.50, 1.57, 1.80, 1.86; substitute `Montserrat, Open Sans`.
- **Gelica**: 400, 700, 800, 12px, 14px, 16px, 1.20, 1.40, 1.50, 1.80; substitute `Roboto, Lato`.
- **GTStandard-M**: 400, 16px, 1.5.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `25px`
- Element Gap: `10px`
- Radius: `cards: 4px, buttons: 5px 10px, default: 4px`

## Surface cues
- **Deep Space Blue Canvas** `#0a153c`: Base page background or subtle alternative for dark sections.
- **Midnight Blue Section** `#142978`: Standard background for prominent content blocks and main areas.
- **Powder Blue Card** `#dbebf5`: Background for product or information cards, providing visual separation.

## Component cues
- **Primary Action Button**: Main call-to-action
- **Ghost Button**: Secondary action that needs less emphasis
- **Navigation Button**: Top-level navigation items
- **Information Card (Powder Blue)**: Presenting product features or bundles
- **Plain Card (Transparent)**: Flexible content container without visual emphasis

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
