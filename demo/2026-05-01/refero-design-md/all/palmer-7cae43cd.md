# Palmer - Refero Design MD

- Source: https://styles.refero.design/style/7cae43cd-dd0e-4658-86e6-d66935cfb213
- Original site: https://www.palmer-dinnerware.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm gallery space

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Creme | `#f5f6ee` | neutral | Page background or card surface |
| Inkwell | `#222222` | neutral | Primary text or dark surface |
| Chalk White | `#ffffff` | neutral | Page background or card surface |
| Shadow Grey | `#a1a19c` | neutral | Border, muted text, or supporting surface |
| Deep Licorice | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-creme: #f5f6ee;
  --ref-inkwell: #222222;
  --ref-chalk-white: #ffffff;
  --ref-shadow-grey: #a1a19c;
  --ref-deep-licorice: #000000;
}
```

## Typography direction
- **TWK Lausanne**: 300, 400, 500, 600, 700, 11px, 12px, 14px, 16px, 18px, 120px, 0.90, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `12px`
- Radius: `nav: 3px, tags: 100px, cards: 9px, buttons: 0px`

## Surface cues
- **Base Canvas** `#f5f6ee`: The primary background for the entire application, creating an open and airy foundation.
- **Product Card Surface** `#f5f6ee`: These surfaces are transparent, blending into the Base Canvas. Elevation is implied solely by product imagery and its soft shadows.
- **Navigation Bar** `#000000`: A solid opaque surface used for the bottom navigation, providing a strong, contrasting anchor for interactive controls.

## Component cues
- **Ghost Button**: Default interactive element, secondary actions
- **Dark Overlay Button**: Navigation and primary controls
- **Product Card**: Displaying individual dinnerware pieces
- **Circular Tag**: Filters and categorization

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
