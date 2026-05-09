# Symbol Audio - Refero Design MD

- Source: https://styles.refero.design/style/3b742f76-25ad-446c-a942-09b09b93f6a3
- Original site: https://www.symbolaudio.com
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sculptural Typography on Forest Canvas: Letterforms as architecture, anchored by a deep green backdrop.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Canvas | `#1c3c27` | brand | Action accent / signal color |
| Arctic Mist | `#dfe2e5` | neutral | Page background or card surface |
| Ink | `#000000` | neutral | Primary text or dark surface |
| Polar White | `#fffffd` | neutral | Page background or card surface |
| Mellow Yellow | `#fffcda` | neutral | Action accent / signal color |
| Link Blue | `#447cf0` | accent | Action accent / signal color |
| Alert Red | `#c72a00` | accent | Action accent / signal color |

```css
:root {
  --ref-forest-canvas: #1c3c27;
  --ref-arctic-mist: #dfe2e5;
  --ref-ink: #000000;
  --ref-polar-white: #fffffd;
  --ref-mellow-yellow: #fffcda;
  --ref-link-blue: #447cf0;
  --ref-alert-red: #c72a00;
}
```

## Typography direction
- **Chalet-LondonSixty**: 400, 13px, 15px, 16px, 1.00, 1.30, 1.31, 1.33, 1.50; substitute `Georgia`.
- **SupremeLL-Bold**: 400, 14px, 20px, 34px, 52px, 80px, 1.00, 1.13, 1.25, 1.26, 1.33; substitute `Roboto Condensed`.
- **Chalet-NewYorkSixty**: 400, 11px, 13px, 15px, 1.00, 1.33; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `buttons: 0px, default: 0px, tagsAndBadges: 9999px`

## Surface cues
- **Forest Canvas Background** `#1c3c27`: Primary page and section background; the foundational layer of the design.
- **Product Display Card** `#fffffd`: Elevated clean surface for showcasing product photography and details.
- **Subtle Cream Background** `#fffcda`: Lightest background for secondary content sections, providing a slight warmth.

## Component cues
- **Bare Text Button**: Navigation and functional buttons
- **Outlined Text Button**: Secondary navigation and ghost actions
- **Product Card**: Display individual product listings
- **Minimal Input Field**: Search and data entry fields
- **Product Tag**: Labels for product features or categories

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
