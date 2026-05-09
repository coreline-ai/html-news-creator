# Hims App - Refero Design MD

- Source: https://styles.refero.design/style/0a489bce-4f93-4b38-b612-d87b1d00999e
- Original site: https://app.forhims.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Rounded digital canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| App Brand Violet | `#5d48db` | brand | Action accent / signal color |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Subtle Gray | `#f0f0f0` | neutral | Page background or card surface |
| Deep Charcoal | `#2e2e2e` | neutral | Primary text or dark surface |
| Border Light Gray | `#e0e0e0` | neutral | Page background or card surface |
| Muted Text Gray | `#8f8f8f` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-app-brand-violet: #5d48db;
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-subtle-gray: #f0f0f0;
  --ref-deep-charcoal: #2e2e2e;
  --ref-border-light-gray: #e0e0e0;
  --ref-muted-text-gray: #8f8f8f;
}
```

## Typography direction
- **sofia**: 400, 500, 14px, 16px, 18px, 20px, 24px, 32px, 35px, 37px, 39px, 44px, 81px, 84px, 85px, 141px, 220px, 280px, 1.00, 1.04, 1.10, 1.15, 1.18, 1.20, 1.25, 1.33, 1.43, 1.67, 2.44, 2.50, 2.78; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `90px`
- Card Padding: `32px`
- Element Gap: `20px`
- Radius: `cards: 45px, navigation: 52px, genericComponent: 30px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and base for all major content areas.
- **Informational Card Background** `#ffffff`: Background for general content cards, distinguished by soft shadows and radius.
- **List Item Background** `#f0f0f0`: Background for secondary content blocks like list items or feature details, offering a slight visual break.

## Component cues
- **Primary Header**: Top navigation bar
- **Download Now Button**: Primary Call to Action in header
- **Hero Section Card**: Prominent content container for hero sections
- **Feature Section Heading**: Large, descriptive titles for major sections
- **Informational Card**: General purpose content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
