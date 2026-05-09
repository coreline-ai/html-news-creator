# Magnetism - Refero Design MD

- Source: https://styles.refero.design/style/a8a1e9e6-d252-49c7-b201-91b3055487df
- Original site: https://www.magnetism.fr/en
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-fashion editorial canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Rich Black | `#222222` | neutral | Primary text or dark surface |
| Night Canvas | `#000000` | neutral | Primary text or dark surface |
| Silver Mist | `#e5e7eb` | neutral | Page background or card surface |
| Graphite | `#343434` | neutral | Primary text or dark surface |
| Cool Steel | `#dbdbdb` | neutral | Page background or card surface |
| Pale Ash | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Muted Gray | `#aaaaaa` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-rich-black: #222222;
  --ref-night-canvas: #000000;
  --ref-silver-mist: #e5e7eb;
  --ref-graphite: #343434;
  --ref-cool-steel: #dbdbdb;
  --ref-pale-ash: #cccccc;
  --ref-muted-gray: #aaaaaa;
}
```

## Typography direction
- **TT Hoves Pro Trial**: 300, 400, 500, 8px, 10px, 11px, 14px, 16px, 20px, 1.00, 1.50, 2.00, 2.50; substitute `Montserrat`.
- **NeueMontreal**: 400, 24px, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `0px`
- Element Gap: `12px`
- Radius: `default: 0px`

## Component cues
- **Navigation Link**: Primary navigation element
- **Works Section Header**: Section title and interactive link
- **Project Card**: Showcase individual projects or campaigns
- **Hairline Divider**: Visual separator for content blocks
- **Muted Text Link**: Secondary and footer navigation links

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
