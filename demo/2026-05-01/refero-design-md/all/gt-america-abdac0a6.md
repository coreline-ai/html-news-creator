# Gt-america - Refero Design MD

- Source: https://styles.refero.design/style/abdac0a6-64f7-46f7-98af-82ce921fe78c
- Original site: https://www.gt-america.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid Pop-Art Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Electric Blue | `#0000ff` | brand | Action accent / signal color |
| Orange Punch | `#ff3500` | brand | Action accent / signal color |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Vivid Indigo | `#0028ff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-electric-blue: #0000ff;
  --ref-orange-punch: #ff3500;
  --ref-ink-black: #000000;
  --ref-vivid-indigo: #0028ff;
}
```

## Typography direction
- **GT America Intl**: 400, 12px, 14px, 16px, 18px, 21px, 22px, 24px, 32px, 36px, 39px, 54px, 58px, 60px, 65px, 79px, 88px, 101px, 108px, 115px, 130px, 135px, 144px, 158px, 171px, 230px, 287px, 338px, 346px, 900px, 0.74, 0.80, 0.95, 1.00, 1.11, 1.12, 1.14, 1.15, 1.17, 1.20, 1.22, 1.23, 1.30, 1.35, 1.45, 1.50, 1.60; substitute `system-ui, sans-serif`.
- **GT America Intl Mono**: 400, 12px, 18px, 60px, 65px, 101px, 255px, 338px, 346px, 0.95, 1.00, 1.12, 1.15, 1.17, 1.22, 1.35; substitute `monospace`.
- **GT America Japanese**: 400, 16px, 32px, 65px, 108px, 130px, 900px, 0.8, 1.11, 1.22, 1.5.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `input: 9999px, buttons: 9999px`

## Component cues
- **Ghost Button - Blue Type**: Interactive controls with minimal visual footprint, often in navigation or secondary actions, emphasized by type color and a hairline border.
- **Ghost Button - Orange Type**: Interactive controls for less critical actions, using the secondary brand color for text and border, maintaining a minimalist appearance.
- **Pill Button - Orange Filled**: Primary call-to-action buttons, highly prominent with a filled brand color and large, playful padding, suggesting interactive delight.
- **Ghost Button - White BG Blue Type**: A subtle interactive control primarily for navigation or utility, used when the background demands a distinct white container.
- **Text Input - White BG Blue Border**: Standard text input field on a light background, outlined with the primary brand blue to maintain visual consistency.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
