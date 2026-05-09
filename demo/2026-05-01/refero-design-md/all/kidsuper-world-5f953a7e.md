# KidSuper World - Refero Design MD

- Source: https://styles.refero.design/style/5f953a7e-c8e9-4e71-872f-4e7ffb7e7264
- Original site: https://kidsuper.world
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Sketchbook on Canvas – a raw, hand-drawn aesthetic dominates the visual experience.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
}
```

## Typography direction
- **Abc Diatype Mono**: 400, 500, 12px, 16px, 1.00, 1.15, 1.20, 1.30; substitute `Space Mono`.
- **Neue Haas Grotesk Display**: 800, 60px, 1.00; substitute `Helvetica Neue (Display)`.

## Spacing / shape
- Section Gap: `40px`
- Element Gap: `16px`
- Page Max Width: `64px`
- Radius: `default: 0px`

## Component cues
- **Top Navigation Bar**: Reference component style.
- **Ghost Button Group**: Reference component style.
- **Footer Bar**: Reference component style.
- **Ghost Button**: Interactive Element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
