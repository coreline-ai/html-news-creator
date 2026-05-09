# Contrast - Refero Design MD

- Source: https://styles.refero.design/style/effca480-81fb-4b8f-ab9c-3aa8c219c82a
- Original site: https://www.getcontrast.io
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid pulse on a static canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Red Action | `#ff5065` | brand | Action accent / signal color |
| Orange Highlight | `#ff7a59` | accent | Action accent / signal color |
| Amber Detail | `#ff5c35` | accent | Action accent / signal color |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ebony Text | `#0e0f10` | neutral | Primary text or dark surface |
| Slate Gray | `#2f3133` | neutral | Primary text or dark surface |
| Whisper Gray | `#f4f4f8` | neutral | Page background or card surface |
| Dark Neutral Button | `#1c1d1e` | neutral | Primary text or dark surface |
| Stone Text | `#7a7b7c` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-red-action: #ff5065;
  --ref-orange-highlight: #ff7a59;
  --ref-amber-detail: #ff5c35;
  --ref-jet-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-ebony-text: #0e0f10;
  --ref-slate-gray: #2f3133;
  --ref-whisper-gray: #f4f4f8;
}
```

## Typography direction
- **Gilroy**: 500, 600, 700, 14px, 16px, 18px, 20px, 48px, 56px, 0.80, 1.00, 1.11, 1.17, 1.20, 1.25, 1.33, 1.43, 1.50, 1.56, 1.60, 1.78, 1.80, 1.88, 1.90; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `32px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `tags: 100px, cards: 24px, small: 4px, buttons: 100px`

## Component cues
- **Primary Action Button**: High-priority call to action
- **Dark Secondary Button**: Secondary action or ghost button
- **Light Outlined Button**: Tertiary action button or subtly interactive element
- **Elevated Card**: Content container that stands out
- **Ghost Card**: Content container with minimal visual impact

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
