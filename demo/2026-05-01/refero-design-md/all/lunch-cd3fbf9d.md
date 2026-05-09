# LUNCH - Refero Design MD

- Source: https://styles.refero.design/style/cd3fbf9d-8d35-411b-9e69-89a03018b677
- Original site: https://lunchconcept.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
gallery meets fashion editorial

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon Black | `#000000` | neutral | Primary text or dark surface |
| Pale Parchment | `#fcfaf1` | neutral | Page background or card surface |
| Digital Lavender | `#b8aad0` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-carbon-black: #000000;
  --ref-pale-parchment: #fcfaf1;
  --ref-digital-lavender: #b8aad0;
}
```

## Typography direction
- **Good Sans**: 400, 700, 12px, 16px, 24px, 32px, 1.00, 1.80; substitute `Inter`.
- **Redaction**: 700, 72px, 1.80; substitute `OCR A Extended`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `0px`
- Element Gap: `20px`
- Radius: `cards: 0px, badges: 0px`

## Component cues
- **Navigation Link**: Primary navigation items and in-content links
- **Product Card**: Displaying product items in grids
- **Footer Announcement Bar**: Global informational messages, typically at the top or bottom of the page.
- **Cookie Consent Banner**: Legal compliance notice
- **Ghost Button/Link**: Secondary calls to action or informational links

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
