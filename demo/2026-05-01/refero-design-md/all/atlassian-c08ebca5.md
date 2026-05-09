# Atlassian - Refero Design MD

- Source: https://styles.refero.design/style/c08ebca5-87d4-4c19-a5d7-ae5e670dae11
- Original site: https://www.atlassian.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
organized digital workspace

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Frost | `#ffffff` | neutral | Page background or card surface |
| Slate 900 | `#000000` | neutral | Primary text or dark surface |
| Graphite Base | `#101214` | neutral | Primary text or dark surface |
| Periwinkle 500 | `#1868db` | brand | Action accent / signal color |
| Steel Grey | `#1c2b42` | neutral | Primary text or dark surface |
| Ash Cloud | `#f0f1f2` | neutral | Page background or card surface |
| Storm Sky | `#42526e` | semantic | Action accent / signal color |
| Harvest Gold | `#fca700` | accent | Action accent / signal color |
| Subtle Mist | `#b7b9be` | neutral | Border, muted text, or supporting surface |
| Sky Haze | `#e9f2fe` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-frost: #ffffff;
  --ref-slate-900: #000000;
  --ref-graphite-base: #101214;
  --ref-periwinkle-500: #1868db;
  --ref-steel-grey: #1c2b42;
  --ref-ash-cloud: #f0f1f2;
  --ref-storm-sky: #42526e;
  --ref-harvest-gold: #fca700;
}
```

## Typography direction
- **Charlie Text**: 400, 500, 700, 13px, 14px, 16px, 20px, 24px, 0.88, 1.00, 1.20, 1.25, 1.29, 1.40, 1.50, 2.29; substitute `Inter`.
- **Charlie Display**: 400, 500, 700, 800, 14px, 24px, 28px, 32px, 40px, 44px, 48px, 70px, 80px, 1.00, 1.10, 1.14, 1.17, 1.19, 1.20, 1.25, 1.43; substitute `Poppins`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `20px`
- Element Gap: `4px`
- Radius: `cards: 20px, buttons: 10000px, general: 2px`

## Surface cues
- **Canvas Frost** `#ffffff`: Primary page background
- **Ash Cloud** `#f0f1f2`: Subtle background for ghost buttons and certain UI components

## Component cues
- **Primary Action Button**: Filled Button
- **Text Link Button**: Ghost Button
- **Pill Ghost Button**: Ghost Button
- **Icon Button**: Round Ghost Button
- **Elevated Content Card**: Informational Card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
