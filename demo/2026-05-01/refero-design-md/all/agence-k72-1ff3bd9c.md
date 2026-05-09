# Agence K72 - Refero Design MD

- Source: https://styles.refero.design/style/1ff3bd9c-827d-450a-a382-300839768d66
- Original site: https://k72.ca
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight graphic stage

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Pewter | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Electric Lime | `#d3fd50` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-ghost-white: #ffffff;
  --ref-pewter: #4d4d4d;
  --ref-electric-lime: #d3fd50;
}
```

## Typography direction
- **Lausanne**: 300, 400, 11px, 14px, 16px, 20px, 35px, 94px, 115px, 137px, 0.70, 0.75, 0.87, 1.20, 1.30, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `28px`
- Element Gap: `10px`
- Radius: `buttons: 93506.4px, navBadges: 34965px`

## Component cues
- **Ghost Button Thin Border**: Action button
- **Ghost Button Thick Border Rounded**: Primary action button
- **Nav Item**: Navigation link

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
