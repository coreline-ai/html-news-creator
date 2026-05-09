# CHRISTOPHER IRELAND CREATIVE - Refero Design MD

- Source: https://styles.refero.design/style/295beab5-cd8a-473b-ab7d-3df6cda30231
- Original site: https://christopherireland.net
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Wall Typography – Elegant serifs on a vast, pale canvas.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#f2f1ec` | neutral | Page background or card surface |
| Charcoal Ink | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#333332` | neutral | Primary text or dark surface |
| Subtle Ash | `#5d5b5b` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-parchment: #f2f1ec;
  --ref-charcoal-ink: #000000;
  --ref-deep-graphite: #333332;
  --ref-subtle-ash: #5d5b5b;
}
```

## Typography direction
- **Playfair Display**: 400, 63px, 94px, 1.00, 1.16, 1.20; substitute `Playfair Display`.
- **Rubik**: 400, 16px, 94px, 1.50; substitute `Rubik`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `11px`
- Radius: `none: 0px`

## Component cues
- **Service Category List**: Reference component style.
- **Brand Identity Header**: Reference component style.
- **Portfolio Image Card with Caption**: Reference component style.
- **Service Category Button**: Interactive text link for portfolio sections.
- **Sub-heading Link**: Descriptive role for the brand.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
