# Gumroad - Refero Design MD

- Source: https://styles.refero.design/style/d67e1407-6d16-47e8-89cf-22f5c5f2dd88
- Original site: https://gumroad.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital playground. A stark black and white digital canvas splashed with vivid, almost neon, color accents.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Light Linen | `#ffffff` | neutral | Page background or card surface |
| Marketplace Gray | `#f4f4f0` | neutral | Page background or card surface |
| Graphite Border | `#242423` | neutral | Primary text or dark surface |
| Subtle Ash | `#d1d5dc` | neutral | Border, muted text, or supporting surface |
| Creator Pink | `#ff90e8` | brand | Action accent / signal color |
| Sunshine Yellow | `#ffc900` | accent | Action accent / signal color |
| Lime Glow | `#f1f333` | accent | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-light-linen: #ffffff;
  --ref-marketplace-gray: #f4f4f0;
  --ref-graphite-border: #242423;
  --ref-subtle-ash: #d1d5dc;
  --ref-creator-pink: #ff90e8;
  --ref-sunshine-yellow: #ffc900;
  --ref-lime-glow: #f1f333;
}
```

## Typography direction
- **ABC Favorit**: 400, 500, 700, 14px, 16px, 18px, 20px, 24px, 30px, 36px, 48px, 72px, 96px, 192px, 0.90, 1.00, 1.11, 1.20, 1.25, 1.33, 1.38, 1.40, 1.43, 1.50, 1.56, 1.63; substitute `Inter, Arial`.

## Spacing / shape
- Section Gap: `48px`
- Element Gap: `8px`
- Radius: `cards: 16px, buttons: 1.67772e+07px, default: 4px, largeElements: 24px`

## Component cues
- **Button Group**: Reference component style.
- **Search Input Field**: Reference component style.
- **Feature Cards**: Reference component style.
- **Primary Black Button**: Critical CTAs
- **Ghost Header Button**: Navigation links, secondary actions in headers

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
