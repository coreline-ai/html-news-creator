# Fallen Grape - Refero Design MD

- Source: https://styles.refero.design/style/17ce9ad2-f22d-4e48-92de-e28fb8551cc5
- Original site: https://www.fallengrape.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sunset Vineyard Aura

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Desert Sand | `#ece0d2` | neutral | Page background or card surface |
| Warm Clay | `#e1c6ab` | brand | Action accent / signal color |
| Vineyard Mauve | `#7c664d` | neutral | Border, muted text, or supporting surface |
| Terra Cotta | `#e3a36e` | brand | Action accent / signal color |
| Deep Earth | `#573d21` | neutral | Border, muted text, or supporting surface |
| Pale Sage | `#d8deb7` | accent | Action accent / signal color |
| Cloud Cover | `#f3f3f3` | neutral | Page background or card surface |
| Electric Blue | `#007aff` | accent | Action accent / signal color |
| Sunny Glow | `#efa164` | accent | Action accent / signal color |

```css
:root {
  --ref-desert-sand: #ece0d2;
  --ref-warm-clay: #e1c6ab;
  --ref-vineyard-mauve: #7c664d;
  --ref-terra-cotta: #e3a36e;
  --ref-deep-earth: #573d21;
  --ref-pale-sage: #d8deb7;
  --ref-cloud-cover: #f3f3f3;
  --ref-electric-blue: #007aff;
}
```

## Typography direction
- **Romie**: 400, 700, 12px, 15px, 20px, 48px, 64px, 1.20, 1.30, 1.70; substitute `Playfair Display`.
- **Arial Narrow**: 400, 700, 13px, 14px, 16px, 18px, 20px, 24px, 48px, 1.20, 1.30, 1.50, 1.70, 1.80; substitute `Roboto Condensed`.
- **GTStandard-M**: 400, 20px, 1.50; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `36-40px`
- Card Padding: `17px`
- Element Gap: `10px`
- Radius: `none: 0px`

## Surface cues
- **Desert Sand Canvas** `#ece0d2`: Base background for pages and footer sections, a warm and earthy foundation.
- **Cloud Cover Card** `#f3f3f3`: Background for product cards and other elevated content blocks, a subtle lighter neutral.

## Component cues
- **Primary Action Button**: Call to action for key interactions
- **Section Callout Button**: Secondary action within content sections
- **Ghost Navigation Button**: Navigation and subtle interactive elements, often with icons
- **Product Card**: Display individual product listings in grids
- **Elevated Product Card**: Display featured product listings or interactive cards on the homepage

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
