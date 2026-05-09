# Chris Biron - Refero Design MD

- Source: https://styles.refero.design/style/68eeb68f-935b-4c14-9369-f3a5c23efedc
- Original site: https://biron.io
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast typographic canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Arctic Mist | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-arctic-mist: #ffffff;
}
```

## Typography direction
- **editorial**: 400, 16px, 32px, 35px, 43px, 1.00, 1.10, 1.15; substitute `Playfair Display`.
- **goodsans**: 400, 10px, 12px, 35px, 1.00, 1.10; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `22px`
- Element Gap: `5px`

## Component cues
- **Primary Navigation Link**: Top-level navigation items
- **Body Text Block**: Main narrative content
- **Section Heading**: Major content section titles
- **Footer Description**: Site-wide descriptive text

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
