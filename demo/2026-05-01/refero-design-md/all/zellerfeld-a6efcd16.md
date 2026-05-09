# Zellerfeld - Refero Design MD

- Source: https://styles.refero.design/style/a6efcd16-dcd8-435b-9bd6-8c590589b424
- Original site: https://www.zellerfeld.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sculpted forms, digital canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#111111` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Shadow | `#000000` | neutral | Primary text or dark surface |
| Stone Gray | `#a1a4aa` | neutral | Border, muted text, or supporting surface |
| Fog | `#d7d7d7` | neutral | Border, muted text, or supporting surface |
| Surface Gray | `#ecedee` | neutral | Page background or card surface |
| Stonewash | `#444955` | neutral | Border, muted text, or supporting surface |
| Sky Tint | `#e5e7ff` | neutral | Page background or card surface |
| Subtle Slate | `#737780` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#000aff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #111111;
  --ref-canvas-white: #ffffff;
  --ref-shadow: #000000;
  --ref-stone-gray: #a1a4aa;
  --ref-fog: #d7d7d7;
  --ref-surface-gray: #ecedee;
  --ref-stonewash: #444955;
  --ref-sky-tint: #e5e7ff;
}
```

## Typography direction
- **Roobert**: 400, 500, 600, 700, 13px, 14px, 15px, 16px, 20px, 32px, 40px, 64px, 128px, 1.00, 1.15, 1.20, 1.35, 1.40, 1.50; substitute `system-ui`.
- **Space Mono**: 400, 600, 12px, 14px, 1.00, 1.35, 1.50; substitute `monospace`.
- **Arial**: 400, 13px, 1.2.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1440px`
- Radius: `cards: 10px, badges: 30px, images: 10px, inputs: 10px, buttons: 10px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background layer, underlying most content.
- **Surface Gray** `#ecedee`: Subtle secondary background for alternating sections and UI elements, providing a slight elevation from the canvas.
- **Fog** `#d7d7d7`: Used for specific background sections to create a distinct, slightly darker block.
- **Neutral Product Card Base** `#ffffff80`: Semi-transparent card backgrounds, creating a frosted glass effect over underlying content.
- **Dark Overlay** `#111111`: Background for prominent, isolated content blocks or sections requiring high contrast.

## Component cues
- **Primary Action Button**: Main call-to-action button
- **Ghost Button (Dark)**: Secondary action on dark backgrounds
- **Ghost Button (Light)**: Secondary actions on light backgrounds
- **Faded Button**: Tertiary or disabled button states
- **Light Opaque Button**: Standard button on neutral backgrounds

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
