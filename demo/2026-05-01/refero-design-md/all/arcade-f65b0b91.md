# Arcade - Refero Design MD

- Source: https://styles.refero.design/style/f65b0b91-bdd1-458d-8775-2f6fa8a9d4b1
- Original site: https://arcade.software
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp Blueprint on White Canvas. Clean surfaces frame sharp typography and a singular, vibrant blue, like a detailed architectural plan on a clear white sheet, accented by a distinct highlight.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#f9fafb` | neutral | Page background or card surface |
| Outline Ash | `#e5e7eb` | neutral | Page background or card surface |
| Graphite Text | `#111827` | neutral | Primary text or dark surface |
| Slate Text | `#4b5563` | neutral | Border, muted text, or supporting surface |
| Silver Text | `#374151` | neutral | Border, muted text, or supporting surface |
| Steel Accent | `#70747d` | neutral | Border, muted text, or supporting surface |
| Arcade Blue | `#2142e7` | brand | Action accent / signal color |
| Deep Blue Shadow | `#182fa5` | brand | Action accent / signal color |
| Dark Gradient Base | `#111827` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-whisper-gray: #f9fafb;
  --ref-outline-ash: #e5e7eb;
  --ref-graphite-text: #111827;
  --ref-slate-text: #4b5563;
  --ref-silver-text: #374151;
  --ref-steel-accent: #70747d;
  --ref-arcade-blue: #2142e7;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 24px, 28px, 30px, 36px, 40px, 48px, 64px, 1.00, 1.06, 1.07, 1.14, 1.17, 1.22, 1.25, 1.29, 1.30, 1.33, 1.38, 1.40, 1.43, 1.50, 1.56, 1.67, 1.71; substitute `system-ui, sans-serif`.
- **Balig Script**: 400, 40px, 1.00; substitute `cursive`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `48px`
- Element Gap: `8px`
- Page Max Width: `1304px`
- Radius: `cards: 16px, inputs: 16px, buttons: 12px, decorative: 24px, large-actions: 72px`

## Component cues
- **Hero URL Input with Tab Selector**: Reference component style.
- **Team Tab Selector with Feature List**: Reference component style.
- **CTA Button Group**: Reference component style.
- **Secondary Outlined Button**: Secondary Action
- **Ghost Button**: Navigation & Tertiary Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
