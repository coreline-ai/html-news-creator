# Rocc Naturals - Refero Design MD

- Source: https://styles.refero.design/style/254b584a-6fb0-4ebb-8893-fc86ccee5ca3
- Original site: https://roccnaturals.com.au
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
grid on soft sage

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Dusty Sage | `#526e3e` | brand | Action accent / signal color |
| Graphite Text | `#636363` | neutral | Border, muted text, or supporting surface |
| Muted Text | `#6e6e6e` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-dusty-sage: #526e3e;
  --ref-graphite-text: #636363;
  --ref-muted-text: #6e6e6e;
}
```

## Typography direction
- **Suisse**: 300, 500, 13px, 15px, 16px, 1.25, 1.33, 1.54; substitute `system-ui`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `15px`
- Element Gap: `18px`
- Radius: `inputs: 1px, buttons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for most UI elements.

## Component cues
- **Ghost Button**: Secondary action. Low visual priority.
- **Solid Button**: Primary action. High visual priority.
- **Text Input**: User input fields.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
