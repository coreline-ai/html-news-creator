# Spécialiste Belge - Refero Design MD

- Source: https://styles.refero.design/style/a6729614-4079-4275-ad22-cee04d90ba0c
- Original site: https://misuko.be
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Organic minimalism, gentle contrast.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Almond | `#fcf9ee` | neutral | Page background or card surface |
| Soft Vanilla | `#f2efe3` | neutral | Page background or card surface |
| Deep Licorice | `#000000` | neutral | Primary text or dark surface |
| Light Pebble | `#bcbab2` | neutral | Border, muted text, or supporting surface |
| Charcoal Gray | `#6a6965` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-almond: #fcf9ee;
  --ref-soft-vanilla: #f2efe3;
  --ref-deep-licorice: #000000;
  --ref-light-pebble: #bcbab2;
  --ref-charcoal-gray: #6a6965;
}
```

## Typography direction
- **Beausite**: 400, 500, 14px, 21px, 30px, 34px, 48px, 0.97, 1.08, 1.12, 1.20, 1.29, 1.36, 1.79, 2.86; substitute `Inter`.

## Spacing / shape
- Section Gap: `20px`
- Card Padding: `34px`
- Element Gap: `17px`
- Radius: `links: 20px`

## Surface cues
- **Canvas Almond** `#fcf9ee`: Base page background
- **Soft Vanilla** `#f2efe3`: Card backgrounds, section dividers

## Component cues
- **Ghost Button**: Interactive element
- **Outlined Call-to-Action Button**: Primary interactive element
- **Content Card**: Information grouping and display
- **Informational Card (Padded)**: Detailed content display
- **Text Input Field**: User data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
