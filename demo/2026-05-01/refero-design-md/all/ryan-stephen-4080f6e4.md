# Ryan Stephen - Refero Design MD

- Source: https://styles.refero.design/style/4080f6e4-e61c-4d3c-ab93-de74a1b5dfc2
- Original site: https://www.ryanstephen.co
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid on White Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Graphite Text | `#404040` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#8b8b94` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite-text: #404040;
  --ref-ash-gray: #8b8b94;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `Arial, Helvetica, 'sans-serif'`.
- **system-ui**: 500, 16px, 1.20; substitute `Segoe UI, Roboto, Ubuntu, Cantarell, 'Noto Sans', sans-serif`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `40px`
- Element Gap: `20px`
- Radius: `images: 10px, components: 10px`

## Component cues
- **Profile Description Block**: Informational text block
- **Image Gallery Grid Item**: Displaying visual work
- **Interactive Link**: Navigational or actionable text

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
