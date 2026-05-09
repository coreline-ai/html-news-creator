# Apple - Refero Design MD

- Source: https://styles.refero.design/style/aecac5da-f397-4ddf-b71f-de1efc434cb8
- Original site: https://www.apple.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery White Precision

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Porcelain | `#f5f5f7` | neutral | Page background or card surface |
| Graphite | `#1d1d1f` | neutral | Primary text or dark surface |
| Cool Gray | `#707070` | neutral | Border, muted text, or supporting surface |
| Charcoal Black | `#000000` | neutral | Primary text or dark surface |
| Subtle Frost | `#f4f8fb` | neutral | Page background or card surface |
| Border Gray | `#e2e2e5` | neutral | Page background or card surface |
| Electric Blue | `#0071e3` | brand | Action accent / signal color |
| Link Blue | `#0066cc` | accent | Action accent / signal color |
| Highlight Blue | `#2997ff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-porcelain: #f5f5f7;
  --ref-graphite: #1d1d1f;
  --ref-cool-gray: #707070;
  --ref-charcoal-black: #000000;
  --ref-subtle-frost: #f4f8fb;
  --ref-border-gray: #e2e2e5;
  --ref-electric-blue: #0071e3;
}
```

## Typography direction
- **SF Pro Display**: 700, 21px, 28px, 40px, 56px, 1.07, 1.10, 1.14, 1.19; substitute `system-ui`.
- **SF Pro Display**: 400, 21px, 28px, 40px, 56px, 1.07, 1.10, 1.14, 1.19; substitute `system-ui`.
- **SF Pro Text**: 600, 12px, 14px, 17px, 18px, 24px, 26px, 34px, 44px, 1.00, 1.18, 1.24, 1.29, 1.33, 1.47, 1.50, 2.12, 2.41; substitute `system-ui`.

## Spacing / shape
- Section Gap: `70-114px`
- Card Padding: `15px`
- Element Gap: `10px`
- Radius: `tags: 999px, cards: 0px, buttons: 980px, formElements: 11px`

## Component cues
- **Primary Filled Button**: Call to action button
- **Ghost Button - Blue Text**: Secondary action button
- **Default Header Button**: Navigation button
- **Region Selector Button**: Informational button
- **Standard Content Card**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
