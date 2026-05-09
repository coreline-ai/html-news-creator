# Blok - Refero Design MD

- Source: https://styles.refero.design/style/7d10f1d6-f2a8-43ce-b055-6ddd74e3c7e1
- Original site: https://blokwatches.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
energetic timepiece on a clean canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0a0d0f` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Haze | `#2e3438` | neutral | Primary text or dark surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |
| Whisper Gray | `#f7f7f7` | neutral | Page background or card surface |
| Footer Gray | `#efefef` | neutral | Page background or card surface |
| Border Ash | `#d5d6d7` | neutral | Border, muted text, or supporting surface |
| Muted Stone | `#656565` | neutral | Border, muted text, or supporting surface |
| Aqua Thrill | `#1dd8e1` | brand | Action accent / signal color |
| Electric Blue | `#2c75d4` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #0a0d0f;
  --ref-canvas-white: #ffffff;
  --ref-charcoal-haze: #2e3438;
  --ref-pure-black: #000000;
  --ref-whisper-gray: #f7f7f7;
  --ref-footer-gray: #efefef;
  --ref-border-ash: #d5d6d7;
  --ref-muted-stone: #656565;
}
```

## Typography direction
- **Poppins**: 400, 500, 14px, 16px, 17px, 21px, 24px, 25px, 1.38, 1.42, 1.50; substitute `system-ui`.
- **Cabin**: 500, 600, 12px, 14px, 17px, 20px, 21px, 68px, 1.00, 1.20, 1.25, 1.50, 1.63; substitute `sans-serif`.
- **Jost**: 700, 23px, 34px, 42px, 51px, 1.25, 1.37, 1.38; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `12px`
- Element Gap: `10px`
- Page Max Width: `1200px`
- Radius: `input: 3px, buttons: 100px, default: 3px`

## Component cues
- **Solid Aqua Button**: Primary Call to Action
- **Pill Ghost Button**: Secondary action/Filter
- **Text Link Button**: Minimal action
- **Circular Pagination Button**: Navigation Control
- **Block Input Field**: Text Input

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
