# Custo - Refero Design MD

- Source: https://styles.refero.design/style/3ad131ed-b603-49a3-9491-7407db6cb423
- Original site: https://custo.io
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Industrial product showcase, matte gray

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Platinum Gray | `#d8d8d8` | neutral | Border, muted text, or supporting surface |
| Hero Ash | `#9ea29f` | neutral | Border, muted text, or supporting surface |
| Muted Steel | `#8e9194` | neutral | Border, muted text, or supporting surface |
| Lightest Slate | `#a7aaad` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-graphite: #000000;
  --ref-canvas-white: #ffffff;
  --ref-platinum-gray: #d8d8d8;
  --ref-hero-ash: #9ea29f;
  --ref-muted-steel: #8e9194;
  --ref-lightest-slate: #a7aaad;
}
```

## Typography direction
- **PP Neue Montreal**: 400, 15px, 16px, 19px, 20px, 30px, 38px, 57px, 1.00, 1.05, 1.15, 1.25, 1.38, 1.42, 1.43, 1.62; substitute `system-ui`.

## Spacing / shape
- Section Gap: `110px`
- Card Padding: `20px`
- Element Gap: `24px`
- Radius: `cards: 8px, links: 31.35px, inputs: 8px, buttons: 8px`

## Surface cues
- **Hero Ash Background** `#9ea29f`: Primary background for the main hero section, providing a muted foundation for product display.
- **Canvas White** `#ffffff`: Standard page and content section backgrounds, offering a clean, expansive substrate for information.

## Component cues
- **Outline Accent Button**: Primary Call to Action
- **Contained Small Button**: Secondary Call to Action
- **Input Field**: Standard Data Entry
- **Compact Input Field**: Header Search/Small Field

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
