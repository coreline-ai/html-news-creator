# Metalab - Refero Design MD

- Source: https://styles.refero.design/style/da087e69-8832-418a-aa1b-42e1acabb39e
- Original site: https://metalab.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome canvas, serif headlines as art

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Ash Surface | `#252525` | neutral | Primary text or dark surface |
| Elevated Grey | `#bababa` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-void-black: #000000;
  --ref-ash-surface: #252525;
  --ref-elevated-grey: #bababa;
}
```

## Typography direction
- **PP Eiko**: 240, 88px, 0.80; substitute `Playfair Display`.
- **Basis Grotesque Pro**: 350, 400, 12px, 16px, 1.00, 1.20, 1.40, 1.76, 2.00; substitute `Inter`.

## Spacing / shape
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `forms: 50px, buttons: 50px, general: 50px`

## Component cues
- **Ghost Button**: Reference component style.
- **Client Tag Buttons**: Reference component style.
- **Stat / Identity Block**: Reference component style.
- **Ghost Button**: Primary Call to Action
- **Client Tag Button**: Client Logo/Identifier

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
