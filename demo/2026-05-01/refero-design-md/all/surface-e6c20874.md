# Surface - Refero Design MD

- Source: https://styles.refero.design/style/e6c20874-c6f9-4c31-b6b2-2cb27cbf15f2
- Original site: https://surface.arcticvolume.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist gallery canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Arctic Snow | `#f7f7f7` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-arctic-snow: #f7f7f7;
  --ref-midnight-ink: #000000;
}
```

## Typography direction
- **Munken Sans Web**: 400, 700, 900, 16px, 20px, 30px, 40px, 230px, 1.00, 1.20, 1.35, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `none: 0px`

## Component cues
- **Ghost Button**: Secondary actions and navigation links
- **Filled Primary Button**: Primary calls to action
- **Content Card (Image/Text)**: Displaying images and associated text in a grid or collage layout

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
