# Walden - Refero Design MD

- Source: https://styles.refero.design/style/31903c2b-99bf-4fa8-8c92-238858f3563c
- Original site: https://walden.us
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Forest floor stillness

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Shadow | `#3f3f3f` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Earth Stone | `#d3cec5` | neutral | Border, muted text, or supporting surface |
| True Black | `#030302` | neutral | Primary text or dark surface |
| Muted Grey | `#686867` | neutral | Border, muted text, or supporting surface |
| Light Stone | `#acacac` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-forest-shadow: #3f3f3f;
  --ref-canvas-white: #ffffff;
  --ref-earth-stone: #d3cec5;
  --ref-true-black: #030302;
  --ref-muted-grey: #686867;
  --ref-light-stone: #acacac;
}
```

## Typography direction
- **Graphik**: 400, 600, 10px, 12px, 14px, 16px, 18px, 20px, 1.00, 1.10, 1.20, 1.30, 1.40, 1.67; substitute `system-ui, sans-serif`.
- **Geist**: 400, 14px, 1.00, 1.10, 1.20, 1.40; substitute `monospace`.
- **GTStandard-M**: 400, 14px, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `cards: 16px, buttons: 2px`

## Surface cues
- **Canvas White** `#ffffff`: Dominant page background, providing a clean, expansive foundation.

## Component cues
- **Ghost Navigation Button (Light)**: Navigation links and secondary actions within light UI sections.
- **Contained Footer Button**: Interactive elements within the footer or compact UI sections.
- **Filled Primary Button**: Main calls to action requiring emphasis.
- **Outlined Text Link**: Links and actions in text-heavy areas, often within product details.
- **Search/Input Field**: Text input areas for search or forms.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
