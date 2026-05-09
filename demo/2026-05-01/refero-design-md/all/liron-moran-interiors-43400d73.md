# Liron Moran Interiors - Refero Design MD

- Source: https://styles.refero.design/style/43400d73-ca89-4750-8fa6-78cd2c661943
- Original site: https://www.lironmoran-interiors.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery backdrop with monumental typography

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Greyscale Canvas | `#41443e` | neutral | Border, muted text, or supporting surface |
| Overlaid Paper | `#f2f0ed` | neutral | Page background or card surface |
| Text and Accent Light | `#eeeeee` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Deepest Black | `#050505` | neutral | Primary text or dark surface |

```css
:root {
  --ref-greyscale-canvas: #41443e;
  --ref-overlaid-paper: #f2f0ed;
  --ref-text-and-accent-light: #eeeeee;
  --ref-midnight-ink: #000000;
  --ref-deepest-black: #050505;
}
```

## Typography direction
- **Lausanne-300**: 400, 12px, 13px, 14px, 20px, 23px, 30px, 75px, 93px, 185px, 0.80, 1.00; substitute `Inter`.
- **cardinalfruit-regular**: 400, 260px, 1.00; substitute `Playfair Display`.
- **Metropolis**: 500, 14px, 1.14; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `89px`
- Element Gap: `5px`
- Radius: `buttons: 50%, navigation: 0px`

## Component cues
- **Ghost Circular Button**: Interactive element (e.g., menu toggle, accessibility toggle)
- **Dark Circular Button**: Interactive element (e.g., close button on overlay)
- **Ghost Rectangular Button**: Text link or secondary action
- **Main Navigation Link**: Top-level navigation items

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
