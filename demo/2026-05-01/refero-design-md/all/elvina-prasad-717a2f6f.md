# Elvina Prasad - Refero Design MD

- Source: https://styles.refero.design/style/717a2f6f-bc7d-4f9a-adcb-1465fdf77c9a
- Original site: https://www.elvinaprasad.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Academic monograph with confident typography.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Text Graphite | `#333333` | neutral | Primary text or dark surface |
| Surface Frost | `#f7f7f7` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-text-graphite: #333333;
  --ref-surface-frost: #f7f7f7;
}
```

## Typography direction
- **Neue Montreal**: 300, 400, 500, 11px, 18px, 27px, 178px, 1.00, 1.10, 1.30, 1.40.
- **Neue Montreal Variable**: 400, 14px, 32px, 38px, 40px, 1.00, 1.43.
- **Arial**: 400, 14px, 1.43; substitute `System Sans-serif`.

## Spacing / shape
- Section Gap: `85px`
- Card Padding: `21px`
- Element Gap: `16px`
- Radius: `default: 0px`

## Component cues
- **Ghost Navigation Link**: Primary navigation element
- **Body Text Block**: Standard paragraph content
- **Hero Headline**: Main page headline
- **Scroll Indicator Text**: Directional UI helper
- **Minimal Call to Action Button**: Secondary action button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
