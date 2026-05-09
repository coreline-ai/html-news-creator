# ARTWORLD - Refero Design MD

- Source: https://styles.refero.design/style/bab94db1-25ec-459d-8c81-5905a0324b65
- Original site: https://artworld.agency
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome gallery canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Black | `#000000` | neutral | Primary text or dark surface |
| Surface White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-black: #000000;
  --ref-surface-white: #ffffff;
}
```

## Typography direction
- **Graphik Light**: 300, 12px, 16px, 20px, 1.20, 1.50, 1.58; substitute `Inter`.
- **Cardinal Fruit**: 300, 18px, 65px, 75px, 1.00, 1.09, 1.20; substitute `Playfair Display`.
- **Cardinal Fruit Italic**: 300, 16px, 65px, 75px, 1.00, 1.09, 1.50; substitute `Playfair Display Italic`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `default: 0px`

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
