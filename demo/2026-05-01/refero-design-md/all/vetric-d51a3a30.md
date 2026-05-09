# Vetric - Refero Design MD

- Source: https://styles.refero.design/style/d51a3a30-965c-427e-9e40-ff177786889f
- Original site: https://vetric.io
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crystal clarity, data flow

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#090a1e` | brand | Action accent / signal color |
| Arctic Canvas | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#e0e0e0` | neutral | Page background or card surface |
| Smoke Gray | `#222222` | neutral | Primary text or dark surface |
| Deep Slate | `#444557` | neutral | Border, muted text, or supporting surface |
| Misty Blue | `#c3dae3` | neutral | Action accent / signal color |
| Sky Flow | `#2969ff` | semantic | Action accent / signal color |
| Rose Haze | `#f75cc3` | brand | Action accent / signal color |
| Lime Glow | `#5ab040` | semantic | Action accent / signal color |
| Sunbeam | `#ffd363` | semantic | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #090a1e;
  --ref-arctic-canvas: #ffffff;
  --ref-cloud-gray: #e0e0e0;
  --ref-smoke-gray: #222222;
  --ref-deep-slate: #444557;
  --ref-misty-blue: #c3dae3;
  --ref-sky-flow: #2969ff;
  --ref-rose-haze: #f75cc3;
}
```

## Typography direction
- **Noto Serif**: 400, 500, 26px, 35px, 42px, 49px, 63px, 77px, 1.00, 1.06, 1.20, 1.33, 1.40, 1.43; substitute `Georgia`.
- **Manrope**: 400, 500, 600, 700, 11px, 14px, 16px, 18px, 19px, 23px, 26px, 70px, 0.79, 1.00, 1.10, 1.30, 1.33, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `53px`
- Card Padding: `28px`
- Element Gap: `9px`
- Radius: `cards: 7px, badges: 50%, buttons: 7px, interactive: 7px`

## Component cues
- **Primary Filled Button**: Main call to action, critical interaction.
- **Ghost Button**: Secondary actions, navigation links where no strong call to action is needed.
- **Neutral Outlined Button**: Ghost button with an explicit border. Secondary actions, team/jobs link.
- **Info Card (Frosted Transparency)**: Displaying digestible chunks of information, often featuring subtle contextual data.
- **Themed Data Card - Pink**: Highlighting specific data points or features with a branded context.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
