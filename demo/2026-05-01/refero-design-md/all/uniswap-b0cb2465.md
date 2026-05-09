# Uniswap - Refero Design MD

- Source: https://styles.refero.design/style/b0cb2465-ad7b-4657-a2e4-b8c793355cd3
- Original site: https://app.uniswap.org
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neon accent on white canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Surface Frost | `#f9f9f9` | neutral | Page background or card surface |
| Action Pink | `#ff37c7` | brand | Action accent / signal color |
| Action Pink Light | `#fef4ff` | brand | Action accent / signal color |
| Text Primary | `#131313` | neutral | Primary text or dark surface |
| Text Secondary | `#222222` | neutral | Primary text or dark surface |
| Text Muted | `#6a6a6a` | neutral | Border, muted text, or supporting surface |
| Text Placeholder | `#acacac` | neutral | Border, muted text, or supporting surface |
| Border Grey | `#f2f2f2` | neutral | Page background or card surface |
| Icon Violet | `#8251fb` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-surface-frost: #f9f9f9;
  --ref-action-pink: #ff37c7;
  --ref-action-pink-light: #fef4ff;
  --ref-text-primary: #131313;
  --ref-text-secondary: #222222;
  --ref-text-muted: #6a6a6a;
  --ref-text-placeholder: #acacac;
}
```

## Typography direction
- **Basel**: 400, 485, 500, 535, 11px, 12px, 13px, 14px, 16px, 18px, 24px, 36px, 52px, 64px, 0.75, 0.96, 1.00, 1.11, 1.15, 1.19, 1.20, 1.25, 1.30, 1.33, 1.49, 3.00; substitute `system-ui`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `8px`
- Element Gap: `8px`
- Radius: `lg: 20px, md: 12px, sm: 8px, xl: 24px, none: 0px, pill: 999999px, circle: 50%`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, providing a bright, expansive base.
- **Surface Frost** `#f9f9f9`: Background for secondary containers and inputs, indicating a slight lift or contained area.
- **Elevated Card** `#ffffff`: Prominent cards or interactive components, standing out on the Surface Frost layer; uses the same color as the canvas but distinct by radius.

## Component cues
- **Primary Action Button**: Filled button for main calls to action
- **Ghost Button**: Secondary and tertiary actions that need less emphasis
- **Filled Secondary Button**: Secondary action button with a subtle fill
- **Input Card**: Container for user inputs and content blocks
- **Elevated Content Card**: Prominent content card, often used for interactive tools or feature showcases

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
