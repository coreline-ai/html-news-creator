# Redis Agency - Refero Design MD

- Source: https://styles.refero.design/style/4406799b-1586-4d84-aac9-e6acdee0f679
- Original site: https://www.redis.agency
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dramatic Midnight Sculpture

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Canvas | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Slate Text | `#808080` | neutral | Border, muted text, or supporting surface |
| Dark Stone | `#333333` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-canvas: #000000;
  --ref-ghost-white: #ffffff;
  --ref-slate-text: #808080;
  --ref-dark-stone: #333333;
}
```

## Typography direction
- **Times New Roman**: 400, 32px, 90px, 0.82, 1.05; substitute `serif`.
- **Suisseintl WebM**: 400, 14px, 16px, 18px, 24px, 36px, 38px, 1.16, 1.20, 1.40; substitute `Arial`.
- **Editorialnew**: 100, 14px, 1.20; substitute `Georgia`.

## Spacing / shape
- Section Gap: `70px`
- Card Padding: `25px`
- Element Gap: `22px`
- Radius: `links: 24px, buttons: 40px, default: 44px`

## Component cues
- **Filled Primary Button**: Action button
- **Ghost Outline Link**: Navigation or secondary action link
- **Zero-Padding Card**: Content card/container for case studies

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
