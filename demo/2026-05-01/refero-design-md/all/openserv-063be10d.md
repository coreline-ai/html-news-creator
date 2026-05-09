# OpenServ - Refero Design MD

- Source: https://styles.refero.design/style/063be10d-593d-4c81-a99e-a7543737b9db
- Original site: https://openserv.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White space innovation laboratory

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Fog Gray | `#f5f5f5` | neutral | Page background or card surface |
| Steel Gray | `#a6a6a6` | neutral | Border, muted text, or supporting surface |
| Graphite | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Deep Blue | `#5f79ff` | brand | Action accent / signal color |
| Electric Green | `#01fe93` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-fog-gray: #f5f5f5;
  --ref-steel-gray: #a6a6a6;
  --ref-graphite: #4d4d4d;
  --ref-deep-blue: #5f79ff;
  --ref-electric-green: #01fe93;
}
```

## Typography direction
- **OS Studio Grotesk**: 400, 12px, 13px, 15px, 20px, 22px, 24px, 30px, 40px, 72px, 0.90, 1.00, 1.10, 1.14, 1.18, 1.25, 1.40.
- **OS Chronik**: 300, 18px, 24px, 34px, 72px, 0.90, 1.00, 1.10, 1.20.
- **sans-serif**: 400, 12px, 1.20.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `card: 16px, pill: 100px, buttons: 12px, default: 16px, heroElement: 40px, interactiveElements: 12px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background
- **Fog Gray** `#f5f5f5`: Secondary card surfaces and subtle content block backgrounds
- **Elevated Navigation** `#ffffffcc`: Floating navigation bar with blur effect

## Component cues
- **Filled Primary Button**: Main call to action
- **Pill Primary Button**: Prominent action with soft, rounded aesthetics
- **Ghost Card Button**: Secondary action within cards, transparent and subtle
- **Subtle Dark Button**: Call to action on dark backgrounds, minimal visual weight
- **Hero Feature Card**: Displays key features or content blocks with a clean appearance.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
