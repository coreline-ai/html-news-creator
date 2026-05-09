# Katherine Pihl - Refero Design MD

- Source: https://styles.refero.design/style/a6b2d6dc-7d71-4d2d-af3e-b34a8b665744
- Original site: https://katherinepihl.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint on Carbon

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Carbon | `#000000` | neutral | Primary text or dark surface |
| Graphite Filter | `#999999` | neutral | Border, muted text, or supporting surface |
| Pewter Mist | `#b3b3b3` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-carbon: #000000;
  --ref-graphite-filter: #999999;
  --ref-pewter-mist: #b3b3b3;
}
```

## Typography direction
- **Neue Montreal**: 300, 400, 500, 16px, 1.20, 1.50; substitute `Inter`.
- **Ryhmes**: 300, 32px, 1.10; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `12px`
- Radius: `none: 0px`

## Component cues
- **Main Navigation Link**: Top-level navigation items and secondary links.
- **Project Gallery Grid Item**: Thumbnail container for showcasing individual projects.
- **Project Title**: Displaying the name of individual projects within the gallery or on project pages.
- **Project Category/Sub-Text**: Descriptive text below project titles, indicating category or additional detail.
- **Footer Links**: Contact information or secondary navigation in the footer.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
