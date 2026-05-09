# entire studios - Refero Design MD

- Source: https://styles.refero.design/style/cef25151-078c-4631-8f02-4f204f071b8b
- Original site: https://entirestudios.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery White Box – stark, unadorned surfaces presenting content with minimalist precision.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Pale Slate | `#e7ecea` | neutral | Page background or card surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-pale-slate: #e7ecea;
  --ref-arctic-white: #ffffff;
}
```

## Typography direction
- **Space Mono**: 400, 12px, 16px, 1.33, 1.50; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `6px`
- Radius: `all: 0px`

## Component cues
- **Announcement Banner**: Reference component style.
- **Ghost Navigation Button Group**: Reference component style.
- **Product Card Grid**: Reference component style.
- **Ghost Navigation Button**: Interactive element (e.g. navigation, filters)

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
