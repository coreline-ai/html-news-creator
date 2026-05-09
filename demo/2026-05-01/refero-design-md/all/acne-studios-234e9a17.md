# Acne Studios - Refero Design MD

- Source: https://styles.refero.design/style/234e9a17-236d-4446-9d58-f83f6806d012
- Original site: https://acnestudios.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery space, stark and bold.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Text Black | `#000000` | neutral | Primary text or dark surface |
| Background White | `#ffffff` | neutral | Page background or card surface |
| Form Surface | `#f7f7f7` | neutral | Page background or card surface |
| Secondary Text Gray | `#6b6b6b` | neutral | Border, muted text, or supporting surface |
| Action Violet | `#0018a8` | accent | Action accent / signal color |

```css
:root {
  --ref-text-black: #000000;
  --ref-background-white: #ffffff;
  --ref-form-surface: #f7f7f7;
  --ref-secondary-text-gray: #6b6b6b;
  --ref-action-violet: #0018a8;
}
```

## Typography direction
- **Helvetica Monospaced Pro**: 400, 9px, 1.15; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `60px`
- Element Gap: `4px`
- Radius: `all: 0px`

## Component cues
- **Navigation Bar**: Reference component style.
- **Product Category Grid**: Reference component style.
- **Search Input with Action Buttons**: Reference component style.
- **Primary Navigation Link**: Top navigation items
- **Ghost Button**: Primary action triggers, navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
