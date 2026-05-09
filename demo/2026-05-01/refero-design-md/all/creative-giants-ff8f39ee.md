# Creative Giants - Refero Design MD

- Source: https://styles.refero.design/style/ff8f39ee-a10e-4a9d-a94d-6993c6084060
- Original site: https://www.creativegiants.art
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sculpted Minimalism on Canvas. An off-white backdrop frames strong typography and vibrant multimedia like exhibits in a pristine gallery.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fffef7` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Medium Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#aaaaaa` | neutral | Border, muted text, or supporting surface |
| Charcoal Gradient | `#4d4c4a` | neutral | Border, muted text, or supporting surface |
| Vivid Orchid | `#ffacea` | accent | Action accent / signal color |
| Muted Teal | `#a5ebd6` | accent | Action accent / signal color |
| Deep Plum | `#101731` | accent | Action accent / signal color |
| Sunburst Yellow | `#ffd001` | accent | Action accent / signal color |
| Sky Blue | `#009fff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #fffef7;
  --ref-ink-black: #000000;
  --ref-medium-gray: #666666;
  --ref-light-gray: #aaaaaa;
  --ref-charcoal-gradient: #4d4c4a;
  --ref-vivid-orchid: #ffacea;
  --ref-muted-teal: #a5ebd6;
  --ref-deep-plum: #101731;
}
```

## Typography direction
- **Switzer**: 300, 400, 12px, 14px, 16px, 18px, 20px, 34px, 54px, 64px, 84px, 1.00, 1.25, 1.40, 1.43; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `48px`
- Element Gap: `8px`
- Radius: `other: 1440px, buttons: 1440px`

## Component cues
- **Menu Button + Nav Badge**: Reference component style.
- **What We Do — Section Block**: Reference component style.
- **News & Opinion — Article Cards**: Reference component style.
- **Ghost Navigation Button**: Navigation, secondary actions
- **Pill Accent Button (Black)**: Primary calls to action in dark contexts

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
