# Rows - Refero Design MD

- Source: https://styles.refero.design/style/8d4a4e15-31f1-4509-8d13-7746f85c20d7
- Original site: https://rows.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist worksheet with warm accents

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon Black | `#1a1a1a` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#f7f7f7` | neutral | Page background or card surface |
| Parchment Tan | `#eaeaea` | neutral | Page background or card surface |
| Stone Gray | `#e1e1e1` | neutral | Page background or card surface |
| Ash Gray | `#989898` | neutral | Border, muted text, or supporting surface |
| Charcoal Gray | `#6f6f6f` | neutral | Border, muted text, or supporting surface |
| Zinc Gray | `#c2c2c2` | neutral | Border, muted text, or supporting surface |
| Muted Gold | `#fff6d4` | accent | Action accent / signal color |
| Sunset Gradient | `#ffb84d` | accent | Action accent / signal color |

```css
:root {
  --ref-carbon-black: #1a1a1a;
  --ref-canvas-white: #ffffff;
  --ref-whisper-gray: #f7f7f7;
  --ref-parchment-tan: #eaeaea;
  --ref-stone-gray: #e1e1e1;
  --ref-ash-gray: #989898;
  --ref-charcoal-gray: #6f6f6f;
  --ref-zinc-gray: #c2c2c2;
}
```

## Typography direction
- **Output Sans**: 400, 700, 10px, 14px, 18px, 24px, 1.00, 1.33, 1.43, 1.45; substitute `Inter`.
- **Output Sans**: 400, 700, 10px, 14px, 18px, 24px, 1.00, 1.33, 1.43, 1.45; substitute `Inter`.

## Spacing / shape
- Section Gap: `24px`
- Element Gap: `4px`
- Radius: `buttons: 8px, default: 4px`

## Component cues
- **Search Input Field**: Reference component style.
- **Quick Action Category Buttons**: Reference component style.
- **Footer Link Bar with Start from Blank CTA**: Reference component style.
- **Primary Navigation Link**: Top right navigation items like 'Log in' and 'Free sign up'.
- **Primary Page Title**: Main heading that frames the interaction, e.g., 'Hi, what do you want to build?'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
