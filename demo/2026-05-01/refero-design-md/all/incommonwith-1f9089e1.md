# Incommonwith - Refero Design MD

- Source: https://styles.refero.design/style/1f9089e1-4170-482f-b988-afe1124a70a9
- Original site: https://www.incommonwith.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sun-drenched architectural permanence.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Bone | `#fafaf9` | neutral | Page background or card surface |
| Surface Frost | `#f8f7f1` | neutral | Page background or card surface |
| Clay Brick | `#4a0a05` | brand | Action accent / signal color |
| Clay Stone | `#bcb6a6` | neutral | Border, muted text, or supporting surface |
| Muted Clay | `#a2827f` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-bone: #fafaf9;
  --ref-surface-frost: #f8f7f1;
  --ref-clay-brick: #4a0a05;
  --ref-clay-stone: #bcb6a6;
  --ref-muted-clay: #a2827f;
}
```

## Typography direction
- **Mier A**: 400, 13px, 14px, 18px, 26px, 1.20; substitute `Inter`.
- **Caslon Ionic**: 400, 24px, 1.20; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `12px`
- Page Max Width: `1392px`
- Radius: `cards: 0px, inputs: 0px, avatars: 9999px, buttons: 0px`

## Surface cues
- **Canvas Bone** `#fafaf9`: Base page background, light and expansive.
- **Surface Frost** `#f8f7f1`: Secondary background for card-like elements or subtle section divisions, providing a gentle lift.
- **Clay Stone** `#bcb6a6`: Accent background for distinct UI blocks, offering a more pronounced separation from the lighter surfaces.

## Component cues
- **Ghost Navigation Button**: Navigation links and secondary actions in headers and footers.
- **Outlined Call to Action**: Primary calls to action that draw attention without being filled blocks.
- **Text Input Field**: Standard input fields for forms and search.
- **Product Thumbnail Card**: Displaying product images in grids.
- **Section Divider Line**: Visual separation between content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
