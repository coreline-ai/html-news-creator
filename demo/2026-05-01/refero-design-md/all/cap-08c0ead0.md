# Cap - Refero Design MD

- Source: https://styles.refero.design/style/08c0ead0-1899-47b4-bfdc-865ab459bbe5
- Original site: https://cap.so
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp utility on a bright canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fcfcfc` | neutral | Page background or card surface |
| Ghost Gray | `#e5e7eb` | neutral | Page background or card surface |
| Smoke Gray | `#e0e0e0` | neutral | Page background or card surface |
| Accent Blue | `#2563eb` | brand | Action accent / signal color |
| Focus Blue | `#1e40af` | brand | Action accent / signal color |
| Base Black | `#000000` | neutral | Primary text or dark surface |
| Carbon Text | `#202020` | neutral | Primary text or dark surface |
| Muted Ash | `#838383` | neutral | Border, muted text, or supporting surface |
| Soft Shadow | `#f0f0f0` | neutral | Page background or card surface |
| Subtle Elevation | `#e0ecfc` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #fcfcfc;
  --ref-ghost-gray: #e5e7eb;
  --ref-smoke-gray: #e0e0e0;
  --ref-accent-blue: #2563eb;
  --ref-focus-blue: #1e40af;
  --ref-base-black: #000000;
  --ref-carbon-text: #202020;
  --ref-muted-ash: #838383;
}
```

## Typography direction
- **defaultFont**: 400, 500, 700, 9px, 10px, 11px, 12px, 14px, 15px, 16px, 18px, 20px, 30px, 36px, 52px, 60px, 1.00, 1.07, 1.11, 1.20, 1.25, 1.33, 1.38, 1.40, 1.43, 1.50, 1.56, 1.60, 1.63, 1.71, 2.00, 2.18, 2.40, 2.67; substitute `Inter`.
- **ui-monospace**: 400, 500, 8px, 10px, 1.40, 2.40, 3.00; substitute `Menlo`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `24px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `lg: 12px, md: 6px, sm: 2px, card: 16px, none: 0px, pill: 9999px`

## Surface cues
- **Canvas White** `#fcfcfc`: Base page background and primary content areas.
- **Feature Card Surface** `#fcfcfc`: Elevated cards that contain content, distinguished by subtle shadow.
- **Subtle Elevation** `#e0ecfc`: Hints at interactivity or selection, used for specific control panels or hover effects.

## Component cues
- **Primary Filled Button**: Main call-to-action.
- **Ghost Button**: Secondary actions or navigation items.
- **Navigation Link**: Primary navigation elements.
- **Feature Card**: Content container for features or testimonials.
- **Option Select Card**: Interactive choice element, particularly for mode selection.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
