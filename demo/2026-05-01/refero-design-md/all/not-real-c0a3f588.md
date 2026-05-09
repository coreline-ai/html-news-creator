# Not Real - Refero Design MD

- Source: https://styles.refero.design/style/c0a3f588-74b7-4fad-b557-1fc7cd7bd777
- Original site: https://notreal.tv
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast editorial canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f2f2f2` | neutral | Page background or card surface |
| Ink Black | `#292a2c` | neutral | Primary text or dark surface |
| Deepest Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #f2f2f2;
  --ref-ink-black: #292a2c;
  --ref-deepest-black: #000000;
}
```

## Typography direction
- **Telegraf**: 400, 15px, 18px, 20px, 24px, 25px, 55px, 0.75, 1.00, 1.08, 1.10, 1.25, 1.33, 1.67, 2.00; substitute `Inter`.
- **Ogg**: 400, 24px, 26px, 55px, 1.06, 1.10, 1.50; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `44px`
- Card Padding: `18px`
- Element Gap: `11px`
- Radius: `default: 0px`

## Component cues
- **Primary Navigation Link**: Top-level navigation element
- **Site Logo**: Brand identifier
- **Hero Description Block**: Introductory text for the agency
- **Project Thumbnail Card**: Showcase individual projects
- **Copyright/Status Text**: Informational text in footer or sidebar

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
