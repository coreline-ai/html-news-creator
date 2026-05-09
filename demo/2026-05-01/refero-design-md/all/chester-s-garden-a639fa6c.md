# Chester's Garden - Refero Design MD

- Source: https://styles.refero.design/style/a639fa6c-1705-47c2-b452-d4479469a734
- Original site: https://chester.how
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital garden journal: crisp pages, intimate handwriting, and colorful bookmarks.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Paper Gray | `#e5e7eb` | neutral | Page background or card surface |
| Charcoal Text | `#171717` | neutral | Primary text or dark surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Subtle Gray | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Accent Orange | `#7c2d12` | brand | Action accent / signal color |
| Highlight Orange | `#fdd3b1` | brand | Action accent / signal color |
| Accent Violet | `#581c87` | brand | Action accent / signal color |
| Highlight Violet | `#e6cefe` | brand | Action accent / signal color |
| Highlight Blue | `#afe5fc` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #fafafa;
  --ref-paper-gray: #e5e7eb;
  --ref-charcoal-text: #171717;
  --ref-ink-black: #000000;
  --ref-subtle-gray: #a3a3a3;
  --ref-accent-orange: #7c2d12;
  --ref-highlight-orange: #fdd3b1;
  --ref-accent-violet: #581c87;
}
```

## Typography direction
- **Inter**: 400, 14px, 16px, 1.43, 1.50, 1.63; substitute `system-ui, sans-serif`.
- **Fraunces**: 300, 30px, 36px, 60px, 1.00, 1.11, 1.20, 1.25; substitute `Georgia, serif`.
- **ui-monospace**: 400, 14px, 1.43; substitute `monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1536px`
- Radius: `tags: 4px, cards: 8px, images: 4px, buttons: 9999px`

## Component cues
- **Content Tag Collection**: Reference component style.
- **Book Card — Reading**: Reference component style.
- **Coffee Brew Card — Hobbies**: Reference component style.
- **Primary Navigation Link**: Top-level navigation items
- **Navigation Tab Active**: Currently active category indicator

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
