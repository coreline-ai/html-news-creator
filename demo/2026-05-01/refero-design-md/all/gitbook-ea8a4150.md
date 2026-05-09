# Gitbook - Refero Design MD

- Source: https://styles.refero.design/style/ea8a4150-e062-4c0e-94ca-668a3033eb63
- Original site: https://www.gitbook.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on bright white

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Ink | `#1c1917` | neutral | Primary text or dark surface |
| Ash | `#57534d` | neutral | Border, muted text, or supporting surface |
| Stone | `#79716b` | neutral | Border, muted text, or supporting surface |
| Parchment | `#fafaf9` | neutral | Page background or card surface |
| Whisper Gray | `#efeeed` | neutral | Page background or card surface |
| Outline Gray | `#e5e5e5` | neutral | Page background or card surface |
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Sunset Orange | `#fe551b` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas: #ffffff;
  --ref-ink: #1c1917;
  --ref-ash: #57534d;
  --ref-stone: #79716b;
  --ref-parchment: #fafaf9;
  --ref-whisper-gray: #efeeed;
  --ref-outline-gray: #e5e5e5;
  --ref-obsidian: #000000;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 16px, 1.2.
- **General Sans Variable**: 700, 12px, 14px, 16px, 20px, 24px, 30px, 32px, 38px, 45px, 55px, 1.00, 1.20, 1.30, 1.40, 1.50, 1.60; substitute `system-ui, sans-serif`.
- **Inter**: 400, 500, 600, 10px, 11px, 12px, 14px, 15px, 16px, 20px, 1.08, 1.18, 1.20, 1.30, 1.40, 1.60; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `10px`
- Radius: `full: 9999px, tags: 4px, cards: 16px, buttons: 99px, default: 8px`

## Surface cues
- **Canvas** `#ffffff`: Primary page and main card backgrounds, providing a bright and spacious base.
- **Parchment** `#fafaf9`: Secondary card backgrounds, slightly differentiated to indicate grouping or a subtle layer.
- **Whisper Gray** `#efeeed`: Subtle background washes, hover states, and lighter secondary card variants.

## Component cues
- **Primary Filled Button**: Call to action
- **Ghost Button**: Secondary action
- **Text Link Button**: Tertiary action, inline link
- **Text Link Button (Transparent)**: Inline navigation, minimal action
- **Feature Card (Parchment)**: Informational display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
