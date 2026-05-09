# Palette Supply - Refero Design MD

- Source: https://styles.refero.design/style/542453bb-1895-45fe-95c9-66dbacbf1b08
- Original site: https://palette.supply
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, creative toolkit

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#f2f0e9` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#141212` | neutral | Primary text or dark surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#a1a0a0` | neutral | Border, muted text, or supporting surface |
| Sage Mist | `#d7d7c8` | brand | Action accent / signal color |
| Deep Forest | `#3f593d` | brand | Action accent / signal color |
| Indigo Punch | `#3051a8` | brand | Action accent / signal color |
| Desert Rose | `#e0b9b1` | brand | Action accent / signal color |
| Terracotta | `#863a29` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas: #f2f0e9;
  --ref-paper-white: #ffffff;
  --ref-graphite: #141212;
  --ref-ink-black: #000000;
  --ref-ash-gray: #a1a0a0;
  --ref-sage-mist: #d7d7c8;
  --ref-deep-forest: #3f593d;
  --ref-indigo-punch: #3051a8;
}
```

## Typography direction
- **ui-sans-serif**: 400, 16px, 1.20, 1.50; substitute `system-ui, sans-serif`.
- **ppsupply**: 100, 300, 400, 13px, 15px, 16px, 18px, 1.00, 1.20, 1.22, 1.25, 1.54; substitute `Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif`.
- **esbuild**: 400, 64px, 0.94; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `tags: 1000px, cards: 12px, images: 12px, inputs: 100px, buttons: 100px`

## Surface cues
- **Canvas** `#f2f0e9`: Base page background
- **Paper White** `#ffffff`: Primary card and elevated component background
- **Sage Mist** `#d7d7c8`: Secondary card and decorative section background

## Component cues
- **Ghost Button - Dark**: Secondary action control
- **Ghost Button - Light**: Secondary action control for dark backgrounds
- **Primary Filled Button - Indigo Punch**: Primary call to action
- **Soft Filled Button - Off-white background**: Tertiary action or decorative button
- **Content Card - Deep Forest**: Container for featured content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
