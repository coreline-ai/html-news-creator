# Shupatto - Refero Design MD

- Source: https://styles.refero.design/style/17824ea8-ac7d-42ca-97e2-9bf92ebea7e1
- Original site: https://www.shupatto.com/en
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Wall Typography

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Text | `#2d2d2d` | neutral | Primary text or dark surface |
| Deepest Ink | `#000000` | neutral | Primary text or dark surface |
| Slate Gray | `#878887` | neutral | Border, muted text, or supporting surface |
| Highlight Violet | `#738ae5` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-charcoal-text: #2d2d2d;
  --ref-deepest-ink: #000000;
  --ref-slate-gray: #878887;
  --ref-highlight-violet: #738ae5;
}
```

## Typography direction
- **Gill Sans Nova Book**: 500, 12px, 16px, 18px, 19px, 21px, 22px, 28px, 1.00, 1.22, 1.25, 1.29, 1.33.
- **Gill Sans Nova Semibold**: 800, 8px, 18px, 21px, 28px, 1.00, 1.22, 1.29, 1.33, 2.50.
- **Yu Gothic**: 18px, 1.00.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `cards: 0px, other: 3px, badges: 0px, buttons: 0px`

## Component cues
- **Ghost Navigation Link**: Interactive element for global navigation and secondary calls-to-action.
- **Highlight Badge**: Small, informative labels indicating status or new content.
- **Monochrome Badge**: Neutral, understated label often used for categories or tags.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
