# Glow - Refero Design MD

- Source: https://styles.refero.design/style/6d9b6fe6-51f4-4978-82dd-a791c28db5cf
- Original site: https://glow.app
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant crypto gradient on clean canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ghost Ink | `#131517` | neutral | Primary text or dark surface |
| Cloud Canvas | `#f4f5f6` | neutral | Page background or card surface |
| Snowdrift | `#ffffff` | neutral | Page background or card surface |
| Stone Gray | `#737577` | neutral | Border, muted text, or supporting surface |
| Soft Sterling | `#b3b5b7` | neutral | Border, muted text, or supporting surface |
| Carbon | `#333537` | neutral | Primary text or dark surface |
| Solana Grape | `#cc62d5` | brand | Action accent / signal color |
| Alert Red | `#e83b47` | accent | Action accent / signal color |
| Highlight Orange | `#ec660d` | accent | Action accent / signal color |
| Glow Gradient | `#a732d6` | brand | Action accent / signal color |

```css
:root {
  --ref-ghost-ink: #131517;
  --ref-cloud-canvas: #f4f5f6;
  --ref-snowdrift: #ffffff;
  --ref-stone-gray: #737577;
  --ref-soft-sterling: #b3b5b7;
  --ref-carbon: #333537;
  --ref-solana-grape: #cc62d5;
  --ref-alert-red: #e83b47;
}
```

## Typography direction
- **Roobert**: 400, 500, 600, 700, 12px, 13px, 16px, 18px, 24px, 40px, 56px, 1.00, 1.10, 1.17, 1.20, 1.28, 1.50; substitute `Inter`.
- **-apple-system**: 400, 16px, 1.5.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `cards: 40px, icons: 100px, badges: 4px, buttons: 19px`

## Component cues
- **Primary Action Button**: Filled button
- **Secondary Action Button**: Filled button
- **Feature Card**: Informational display
- **Badge (New)**: Status indicator

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
