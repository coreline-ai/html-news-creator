# Aboard - Refero Design MD

- Source: https://styles.refero.design/style/fabacd2a-acb6-46c4-939c-4a464df15440
- Original site: https://aboardhr.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm pastel canvas with cheerful accents

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Ice | `#fafafa` | neutral | Page background or card surface |
| Ink | `#262626` | neutral | Primary text or dark surface |
| Slate | `#757577` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#aeaeaf` | neutral | Border, muted text, or supporting surface |
| Outline Blue | `#008ae8` | brand | Action accent / signal color |
| Ghost Blue | `#e0f2fe` | brand | Action accent / signal color |
| Task Card Pink | `#fbcfe8` | accent | Action accent / signal color |
| Task Card Violet | `#e6dafd` | accent | Action accent / signal color |
| #b6edee | `#b6edee` | accent | Action accent / signal color |
| Task Card Sky | `#afe4ff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-ice: #fafafa;
  --ref-ink: #262626;
  --ref-slate: #757577;
  --ref-whisper-gray: #aeaeaf;
  --ref-outline-blue: #008ae8;
  --ref-ghost-blue: #e0f2fe;
  --ref-task-card-pink: #fbcfe8;
  --ref-task-card-violet: #e6dafd;
}
```

## Typography direction
- **system-ui**: 400, 500, 600, 12px, 15px, 16px, 18px, 20px, 24px, 44px, 56px, 64px, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.56, 1.60, 2.00; substitute `system-ui`.
- **sans-serif**: 400, 12px, 1.20; substitute `Arial, Helvetica`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `cards: 24px, forms: 10px, icons: 10px, buttons: 99px`

## Component cues
- **Ghost Primary Button**: Primary Call to Action
- **Filled Mild Button**: Secondary Call to Action
- **Tag Button**: Informational Tags
- **Feature Card (Pink)**: Colored Content Container
- **Feature Card (Teal)**: Colored Content Container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
