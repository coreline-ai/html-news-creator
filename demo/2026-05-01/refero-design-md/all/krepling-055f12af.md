# Krepling - Refero Design MD

- Source: https://styles.refero.design/style/055f12af-b7b9-46af-81b7-93e0ed6d5ce2
- Original site: https://www.krepling.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural fluid canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Midnight Text | `#000000` | neutral | Primary text or dark surface |
| Soft Gray | `#f1f1f1` | neutral | Page background or card surface |
| Muted Ash | `#6c6b6b` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Deep Midnight | `#171717` | neutral | Primary text or dark surface |
| Krepling Violet | `#b154f9` | brand | Action accent / signal color |
| Rose Bloom | `#f9c2cf` | accent | Action accent / signal color |
| Luminous Grape | `#635bff` | accent | Action accent / signal color |
| Sunburst Yellow | `#ffe01b` | accent | Action accent / signal color |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-midnight-text: #000000;
  --ref-soft-gray: #f1f1f1;
  --ref-muted-ash: #6c6b6b;
  --ref-steel-gray: #b3b3b3;
  --ref-deep-midnight: #171717;
  --ref-krepling-violet: #b154f9;
  --ref-rose-bloom: #f9c2cf;
}
```

## Typography direction
- **Regular**: 400, 16px, 18px, 24px, 32px, 48px, 64px, 80px, 1.1, 1.2, 1.3.
- **Inter**: use as primary family; substitute `system-ui`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `20px`
- Element Gap: `8px`
- Page Max Width: `733px`
- Radius: `cards: 14px, large: 30px, buttons: 10px, default: 8px`

## Surface cues
- **White Canvas** `#ffffff`: Primary page background and default surface for most content.
- **Soft Gray** `#f1f1f1`: Secondary background for sections or subtle elevation of content blocks.
- **Deep Midnight** `#171717`: Used for specific high-contrast areas like footers.

## Component cues
- **Primary Action Button**: Call-to-action button for critical actions
- **Ghost Button**: Secondary or textual actions within a flow
- **White Card**: Content container for features or information blocks
- **FAQ Accordion Item**: Interactive list item for expandable content
- **Navigation Link**: Interactive elements within the main navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
