# Deta Surf - Refero Design MD

- Source: https://styles.refero.design/style/51752cfb-4fd4-464f-8b78-ecbc813830e1
- Original site: https://deta.surf
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sky-bound clarity

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Canvas | `#a8d5ff` | brand | Action accent / signal color |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#f3f4f6` | neutral | Page background or card surface |
| Deep Space Blue | `#009afc` | brand | Action accent / signal color |
| Ocean Shadow | `#006dc8` | brand | Action accent / signal color |
| Graphite Text | `#000000` | neutral | Primary text or dark surface |
| Slate Text | `#5b6882` | neutral | Border, muted text, or supporting surface |
| Light Steel Border | `#e5e7eb` | neutral | Page background or card surface |
| Faint Blue Border | `#cfe9fd` | neutral | Action accent / signal color |
| Ash Gray | `#808080` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-sky-canvas: #a8d5ff;
  --ref-cloud-white: #ffffff;
  --ref-fog-gray: #f3f4f6;
  --ref-deep-space-blue: #009afc;
  --ref-ocean-shadow: #006dc8;
  --ref-graphite-text: #000000;
  --ref-slate-text: #5b6882;
  --ref-light-steel-border: #e5e7eb;
}
```

## Typography direction
- **Switzer**: 400, 500, 12px, 14px, 15px, 16px, 17px, 18px, 20px, 60px, 1.00, 1.11, 1.20, 1.40, 1.43, 1.45, 1.50, 1.56, 1.60; substitute `Inter`.
- **Gambarino**: 400, 500, 16px, 18px, 20px, 36px, 40px, 48px, 60px, 1.00, 1.11, 1.20, 1.40, 1.50, 1.56; substitute `Georgia`.
- **Tanker**: 400, 16px, 19px, 1.30, 1.50; substitute `Monospace`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 12px, buttons: 9999px, general: 8px, inputField: 16.2px`

## Surface cues
- **Sky Canvas** `#a8d5ff`: Dominant background for the page, setting the atmospheric tone with its gradient.
- **Fog Gray** `#f3f4f6`: Subtle background for less prominent cards, providing a soft contrast to the primary canvas.
- **Cloud White** `#ffffff`: Primary surface for interactive elements, content cards, and input fields, offering high contrast and perceived cleanliness.

## Component cues
- **Primary Filled Button**: Main call-to-action
- **Ghost Open Source Button**: Secondary action or status indicator
- **Search/Notebook Input**: Interactive input field
- **Standard Card**: Content container
- **Muted Card Background**: Secondary content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
