# UY Studio - Refero Design MD

- Source: https://styles.refero.design/style/b376d42c-b2cb-4a52-8cec-ebf19cf1883f
- Original site: https://www.uy-studio.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Canvas, Monochromatic Depth

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#24241f` | neutral | Primary text or dark surface |
| Fog Canvas | `#d1d3cf` | neutral | Border, muted text, or supporting surface |
| Ghost White | `#e5e5e5` | neutral | Page background or card surface |
| Obsidian | `#333333` | neutral | Primary text or dark surface |

```css
:root {
  --ref-carbon: #24241f;
  --ref-fog-canvas: #d1d3cf;
  --ref-ghost-white: #e5e5e5;
  --ref-obsidian: #333333;
}
```

## Typography direction
- **GP**: 400, 13px, 15px, 16px, 30px, 48px, 1.10, 1.13, 1.20, 1.37, 1.38, 1.41, 1.50, 1.77; substitute `Arial`.
- **GTStandard-M**: 400, 15px, 1.50; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `143px`
- Card Padding: `13px`
- Element Gap: `13px`
- Radius: `input: 3px`

## Component cues
- **Ghost Header Button**: Navigation and secondary actions in the header
- **Filled Action Button**: Primary call to action button
- **Product Input Field**: Standard text input field
- **Footer Input Field**: Input field in the footer for subscribing
- **Search Input Field**: Search or filter input field within product listings

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
