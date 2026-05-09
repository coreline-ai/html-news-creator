# Kalstore® - Refero Design MD

- Source: https://styles.refero.design/style/e854a4f7-4243-44a7-92e2-e22db22bef1b
- Original site: https://kal-store.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm minimal gallery

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#faf9f7` | neutral | Page background or card surface |
| Surface White | `#ffffff` | neutral | Page background or card surface |
| Text Primary | `#242424` | neutral | Primary text or dark surface |
| Text Secondary | `#585a5a` | neutral | Border, muted text, or supporting surface |
| Text Muted | `#727272` | neutral | Border, muted text, or supporting surface |
| Border Light | `#d3d3d3` | neutral | Border, muted text, or supporting surface |
| Border Pale | `#edecea` | neutral | Page background or card surface |
| Action Gold | `#f1ba35` | brand | Action accent / signal color |
| Info Text | `#30250b` | semantic | Action accent / signal color |
| Card Accent Red | `#6c3c3c` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas: #faf9f7;
  --ref-surface-white: #ffffff;
  --ref-text-primary: #242424;
  --ref-text-secondary: #585a5a;
  --ref-text-muted: #727272;
  --ref-border-light: #d3d3d3;
  --ref-border-pale: #edecea;
  --ref-action-gold: #f1ba35;
}
```

## Typography direction
- **ABCDiatype**: 400, 500, 12px, 14px, 16px, 19px, 21px, 22px, 25px, 71px, 82px, 140px, 0.93, 1.00, 1.20, 1.25, 1.30, 1.35, 1.40; substitute `Inter`.
- **Arial**: 400, 13px, 1.20.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `10px`
- Radius: `badges: 4px, default: 8px, bodyElements: 1px, asymmetricCards: 16px`

## Surface cues
- **Canvas** `#faf9f7`: Base background for the entire page, providing a warm, unobtrusive backdrop.
- **Surface White** `#ffffff`: Background for cards and primary navigational elements, slightly elevating content from the canvas.
- **Border Pale** `#edecea`: Background for subtle highlights, specific card variants (e.g., placeholders), and hover states.

## Component cues
- **Primary Action Button**: Main call to action button.
- **Ghost Button**: Secondary action or navigational link button.
- **Text Button**: Minimal link-style button for secondary actions or navigation within content.
- **Newsletter Input Field (Dark)**: Input element for forms within dark-themed sections (newsletter popup).
- **Product Card (Full Width)**: Card for displaying product images, often full bleeding.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
