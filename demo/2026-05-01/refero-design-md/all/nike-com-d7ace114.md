# Nike.com - Refero Design MD

- Source: https://styles.refero.design/style/d7ace114-0548-41f5-a2ff-2afbf32be94d
- Original site: https://nike.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast arena with athletic curves.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#111111` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Alloy Gray | `#e5e5e5` | neutral | Page background or card surface |
| Feather Gray | `#f5f5f5` | neutral | Page background or card surface |
| Steel Gray | `#707072` | neutral | Border, muted text, or supporting surface |
| Pewter Gray | `#9e9ea0` | neutral | Border, muted text, or supporting surface |
| Ignite Red | `#ee0005` | brand | Action accent / signal color |
| Blaze Orange | `#ff5000` | brand | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #111111;
  --ref-cloud-white: #ffffff;
  --ref-alloy-gray: #e5e5e5;
  --ref-feather-gray: #f5f5f5;
  --ref-steel-gray: #707072;
  --ref-pewter-gray: #9e9ea0;
  --ref-ignite-red: #ee0005;
  --ref-blaze-orange: #ff5000;
}
```

## Typography direction
- **Helvetica Now Text**: 400, 500, 16px, 20px, 1.50, 1.75; substitute `Arial, Helvetica, sans-serif`.
- **Helvetica Now Display**: 500, 20px, 24px, 1.20, 1.50; substitute `Arial, Helvetica, sans-serif`.
- **Nike Futura ND**: 500, 76px, 1.00; substitute `Arial, Helvetica, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `cards: 0px, buttons: 30px, default: 8px, navItems: 30px`

## Component cues
- **Primary Filled Button**: Call to Action
- **Ghost Button**: Secondary Action
- **Circular Icon Button**: Navigation/Utility
- **Feature Card**: Content Display
- **Product Tile**: Product Listing

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
