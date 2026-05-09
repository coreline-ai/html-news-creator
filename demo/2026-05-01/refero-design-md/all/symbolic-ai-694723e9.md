# Symbolic.ai - Refero Design MD

- Source: https://styles.refero.design/style/694723e9-0df7-4b9f-ba07-83fc598532d6
- Original site: https://symbolic.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Paper-white canvas, ink-on-page UI.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#fdfcf5` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Grey | `#4c4c4a` | neutral | Border, muted text, or supporting surface |
| Mid Grey | `#7f7e7b` | neutral | Border, muted text, or supporting surface |
| Faded Stone | `#d5d0b8` | neutral | Border, muted text, or supporting surface |
| Accent Red | `#f42c2b` | brand | Action accent / signal color |
| Electric Violet | `#6938ef` | accent | Action accent / signal color |
| Subtle Teal | `#10756a` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-parchment: #fdfcf5;
  --ref-paper-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-charcoal-grey: #4c4c4a;
  --ref-mid-grey: #7f7e7b;
  --ref-faded-stone: #d5d0b8;
  --ref-accent-red: #f42c2b;
  --ref-electric-violet: #6938ef;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `system-ui`.
- **Open Runde**: 400, 500, 600, 700, 900, 12px, 14px, 16px, 1.50, 1.60, 1.63, 1.71; substitute `Inter`.
- **Open Runde**: use as primary family; substitute `Inter SemiBold`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `pill: 2000px, tags: 13px, cards: 24px, icons: 8px, buttons: 16px`

## Surface cues
- **Canvas Parchment** `#fdfcf5`: The primary page background, a warm off-white.
- **Paper White** `#ffffff`: Base layer for cards and embedded components, slightly brighter than the canvas.
- **Subtle Border Card Background** `#d5d0b8`: A very light, near-transparent background for less prominent cards, suggesting a layer below Paper White.

## Component cues
- **Pill Button, Outlined**: Ghost buttons for secondary actions or navigation.
- **Filled Button, Subtle Corners**: Primary Call-to-actions, signaling key user interactions.
- **Elevated Card**: Content containers for features, articles, or testimonials.
- **Subtle Border Card**: Informational panels or meta-content displays with low prominence.
- **Accent Red Card**: Highlight cards for urgent messages or prominent features.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
