# Daniel Sun - Refero Design MD

- Source: https://styles.refero.design/style/8d1b6c70-e045-4ce6-891d-aba5d5c00e0d
- Original site: https://danielsun.space
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Solar Flare Canvas. A radiant yellow burst on a clean, stark white backdrop defines the visual energy.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sunbeam Yellow | `#ffd500` | brand | Action accent / signal color |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pale Gray | `#f5f5f5` | neutral | Page background or card surface |
| Ash Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#a6a6a6` | neutral | Border, muted text, or supporting surface |
| Shadow Gradient | `#e6e6e6` | neutral | Page background or card surface |

```css
:root {
  --ref-sunbeam-yellow: #ffd500;
  --ref-pitch-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-pale-gray: #f5f5f5;
  --ref-ash-gray: #808080;
  --ref-silver-mist: #a6a6a6;
  --ref-shadow-gradient: #e6e6e6;
}
```

## Typography direction
- **Reddit Sans Condensed**: 900, 36px, 88px, 246px, 0.90, 0.96, 1.00; substitute `Bebas Neue`.
- **Inter Display**: 500, 18px, 20px, 26px, 30px, 1.10, 1.30, 1.35; substitute `Inter`.
- **Inter**: 500, 14px, 20px, 128px, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Radius: `buttons: 32px, default: 14px, heroElement: 110px, largeImages: 24px`

## Component cues
- **Navigation Bar**: Reference component style.
- **Work Showcase Card**: Reference component style.
- **Button Group & CTA Strip**: Reference component style.
- **Navigation Button**: Interactive element
- **Work Showcase Card**: Content display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
