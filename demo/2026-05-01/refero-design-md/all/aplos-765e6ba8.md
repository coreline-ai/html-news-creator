# Aplós - Refero Design MD

- Source: https://styles.refero.design/style/765e6ba8-af87-4519-afb7-774ceedc463d
- Original site: https://aplos.world
- Theme: `mixed`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome elegance with botanical whispers

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Desert Sand | `#f2f1ed` | neutral | Page background or card surface |
| Slate Gray | `#646464` | neutral | Border, muted text, or supporting surface |
| Shadow Tint | `#b4aeac` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-desert-sand: #f2f1ed;
  --ref-slate-gray: #646464;
  --ref-shadow-tint: #b4aeac;
}
```

## Typography direction
- **Goudy Old Style**: 400, 26px, 40px, 1.05, 1.08; substitute `Palatino Linotype, Georgia`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `default: 5px`

## Component cues
- **Ghost Header Button (Light)**: Navigation and secondary actions in header.
- **Ghost Header Button (Dark)**: Navigation and secondary actions.
- **Primary Ghost Button**: Prominent calls to action.
- **Frosted Primary Button**: Secondary calls to action or interactive elements requiring slight visual weight.
- **Light Section Button**: Action buttons within the light-themed content sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
