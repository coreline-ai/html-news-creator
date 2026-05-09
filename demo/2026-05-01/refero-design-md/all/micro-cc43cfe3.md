# Micro - Refero Design MD

- Source: https://styles.refero.design/style/cc43cfe3-195b-4081-b586-c42db054a466
- Original site: https://www.micro.so
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
layered productivity canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#221f1c` | neutral | Primary text or dark surface |
| Canvas White | `#f5f5f5` | neutral | Page background or card surface |
| Subtle Gray | `#797267` | neutral | Border, muted text, or supporting surface |
| Deep Gray | `#575452` | neutral | Border, muted text, or supporting surface |
| Lightest Gray | `#ababab` | neutral | Border, muted text, or supporting surface |
| Border Gray | `#c4c4c4` | neutral | Border, muted text, or supporting surface |
| Midnight Blue | `#518bdb` | brand | Action accent / signal color |
| Teal Burst | `#36bab8` | brand | Action accent / signal color |
| Forest Green | `#1a3a12` | accent | Action accent / signal color |
| Lavender Haze | `#bf89cd` | accent | Action accent / signal color |

```css
:root {
  --ref-inkwell: #221f1c;
  --ref-canvas-white: #f5f5f5;
  --ref-subtle-gray: #797267;
  --ref-deep-gray: #575452;
  --ref-lightest-gray: #ababab;
  --ref-border-gray: #c4c4c4;
  --ref-midnight-blue: #518bdb;
  --ref-teal-burst: #36bab8;
}
```

## Typography direction
- **haffer**: 400, 500, 600, 700, 900, 8px, 9px, 10px, 11px, 12px, 14px, 16px, 18px, 20px, 24px, 96px, 1.00, 1.25, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63; substitute `Inter`.
- **ui-monospace**: 400, 500, 8px, 14px, 16px, 1.43, 1.50, 1.71; substitute `JetBrains Mono`.
- **perfectlyNineties**: 400, 700, 800, 900, 14px, 24px, 30px, 36px, 48px, 72px, 1.00, 1.20, 1.25; substitute `Georgia`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `cards: 18px, inputs: 10px, buttons: 8px, default: 8px, taglike: 14px, circular: 9999px, smallElements: 4px`

## Component cues
- **Ghost Button**: Secondary action button with minimal visual hierarchy.
- **Icon Button**: Compact button primarily for icons, often in navigation context.
- **Primary Filled Button**: Prominent action button, main call-to-action.
- **Subtle Filled Button**: Tertiary action, less emphasis than primary but more than ghost.
- **Elevated Card**: Main content containers with significant visual separation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
