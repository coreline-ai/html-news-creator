# Vanmoof - Refero Design MD

- Source: https://styles.refero.design/style/4887c681-d4e6-41d3-b83c-5650cf925ee9
- Original site: https://www.vanmoof.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome canvas, functional red accents

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#e5e7eb` | neutral | Page background or card surface |
| Carbon Black | `#222222` | neutral | Primary text or dark surface |
| Inkwell | `#000000` | neutral | Primary text or dark surface |
| Deep Slate | `#313131` | neutral | Primary text or dark surface |
| Light Gray | `#e0e0e0` | neutral | Page background or card surface |
| Ignition Red | `#ff0000` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ghost-gray: #e5e7eb;
  --ref-carbon-black: #222222;
  --ref-inkwell: #000000;
  --ref-deep-slate: #313131;
  --ref-light-gray: #e0e0e0;
  --ref-ignition-red: #ff0000;
}
```

## Typography direction
- **Unica77LLWeb**: 400, 600, 700, 12px, 14px, 16px, 18px, 24px, 32px, 48px, 80px, 280px, 1.00, 1.10, 1.33, 1.43, 1.50, 1.56; substitute `Helvetica Neue`.
- **Unica77Mono**: 400, 14px, 1.20; substitute `Roboto Mono`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `8px`
- Element Gap: `8px`
- Radius: `cards: 8px, default: 2px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default content areas.
- **Ghost Gray** `#e5e7eb`: Secondary background areas, subtle panels, and content blocks (e.g., feature cards).
- **Carbon Black** `#222222`: Accentuated section backgrounds, especially in hero areas, and primary button fills.

## Component cues
- **Ghost Outline Button (Light)**: Secondary action button
- **Ghost Outline Button (Dark)**: Secondary action button on dark sections
- **Primary Filled Button**: Primary action button
- **Product Feature Card**: Informational display
- **Navigation Link**: Primary navigation item

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
