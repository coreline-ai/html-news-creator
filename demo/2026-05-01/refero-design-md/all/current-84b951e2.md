# Current - Refero Design MD

- Source: https://styles.refero.design/style/84b951e2-eaae-4f56-8f3f-d90407517a56
- Original site: https://current.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White Canvas Precision

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Storm Anthracite | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Skyline Gray | `#737582` | neutral | Border, muted text, or supporting surface |
| Faded Steel | `#dfe5ec` | neutral | Page background or card surface |
| Ghost Fill | `#ebeff2` | neutral | Page background or card surface |
| Deep Space | `#4e525e` | neutral | Border, muted text, or supporting surface |
| Current Gradient | `#f4cb45` | brand | Action accent / signal color |

```css
:root {
  --ref-storm-anthracite: #000000;
  --ref-cloud-white: #ffffff;
  --ref-skyline-gray: #737582;
  --ref-faded-steel: #dfe5ec;
  --ref-ghost-fill: #ebeff2;
  --ref-deep-space: #4e525e;
  --ref-current-gradient: #f4cb45;
}
```

## Typography direction
- **soehne**: 100, 300, 400, 700, 12px, 16px, 18px, 20px, 21px, 24px, 48px, 72px, 90px, 1.00, 1.10, 1.20, 1.25, 1.40, 1.50, 1.60; substitute `system-ui, sans-serif`.
- **proxima-nova**: 400, 700, 16px, 43px, 1.40; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `cards: 30px, buttons: 9999px, input-text: 0px, square-components: 0px`

## Surface cues
- **Desktop Canvas** `#ffffff`: Primary background for the entire page.
- **Input Field Background** `#ebeff2`: Background for form input elements, offering a subtle visual distinction from the canvas.

## Component cues
- **Filled Primary Button**: Action button with dark background.
- **Outlined Secondary Button**: Secondary action button with light background.
- **Ghost Action Button**: Minimalist interactive element, often for 'Learn More' or informational actions.
- **Mobile Number Input Field**: User input for contact information.
- **Information Icon Button**: Small, interactive icon for tooltips or additional context.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
