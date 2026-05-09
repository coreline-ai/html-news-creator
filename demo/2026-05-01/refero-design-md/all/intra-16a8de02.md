# Intra - Refero Design MD

- Source: https://styles.refero.design/style/16a8de02-a4c6-4077-9d3a-ef6b5c10db12
- Original site: https://intracbr.com.au
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monolithic concrete gallery

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Gray | `#e4e4e4` | neutral | Page background or card surface |
| Ink Black | `#212529` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Absolute Black | `#000000` | neutral | Primary text or dark surface |
| Vivid Pink | `#f78da7` | accent | Action accent / signal color |
| Vivid Amber | `#fcb900` | accent | Action accent / signal color |
| Vivid Clay | `#dc3545` | accent | Action accent / signal color |
| Vivid Green Cyan | `#00d084` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-gray: #e4e4e4;
  --ref-ink-black: #212529;
  --ref-paper-white: #ffffff;
  --ref-absolute-black: #000000;
  --ref-vivid-pink: #f78da7;
  --ref-vivid-amber: #fcb900;
  --ref-vivid-clay: #dc3545;
  --ref-vivid-green-cyan: #00d084;
}
```

## Typography direction
- **Whyte**: 400, 16px, 18px, 20px, 95px, 1.00, 1.50; substitute `Arial`.
- **-apple-system**: 400, 16px, 20px, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `cards: 0px, badges: 100%, buttons: 0px`

## Surface cues
- **Canvas Gray** `#e4e4e4`: Dominant page background for main content areas.
- **Ink Black Surface** `#212529`: Darker background for prominent cards and reversed UI sections.

## Component cues
- **Ghost Button**: Navigation and secondary actions
- **Product Display Card**: Showcasing individual product items with strong branding
- **Callout Section Card**: Highlighting specific information like cafe description or hours

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
