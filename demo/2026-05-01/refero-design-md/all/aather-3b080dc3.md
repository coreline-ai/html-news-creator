# AATHER - Refero Design MD

- Source: https://styles.refero.design/style/3b080dc3-1992-43fe-91d6-2a721f934435
- Original site: https://aather.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whispered luxury on white linen. A visual system that emphasizes premium product through a muted, spacious, high-contrast, text-dominant interface.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#e8e8e8` | neutral | Page background or card surface |
| Ash Gray | `#808080` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-inkwell: #000000;
  --ref-paper-white: #ffffff;
  --ref-ghost-gray: #e8e8e8;
  --ref-ash-gray: #808080;
}
```

## Typography direction
- **Gestura Text Extra Light**: 100, 200, 14px, 16px, 20px, 1.22, 1.35, 1.38.
- **Gestura Text**: 100, 200, 14px, 16px, 20px, 35px, 1.20, 1.22, 1.35, 1.38; substitute `Montserrat, Raleway Thin`.
- **Untitled Sans**: 100, 200, 400, 9px, 11px, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 0.78, 1.17, 1.20, 1.22, 1.35, 1.38, 1.39; substitute `Inter, Lato`.

## Spacing / shape
- Section Gap: `25px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `inputs: 2px, buttons: 2px`

## Surface cues
- **Paper White** `#ffffff`: Primary page background and untouched content areas.
- **Ghost Gray** `#e8e8e8`: Subtle dividers and secondary background accents.

## Component cues
- **Ghost Button**: Navigation links and secondary actions
- **Outlined Button**: Call to action with minimal visual weight
- **Secondary Outlined Button**: Subtle interactive elements
- **Product Card**: Display individual products within a grid
- **Text Input Field**: Forms and data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
