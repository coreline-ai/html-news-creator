# Egstad - Refero Design MD

- Source: https://styles.refero.design/style/ec17bdec-c8fa-4221-abd6-da717bf38d96
- Original site: https://egstad.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type-first Brutalist

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#e2e0d9` | neutral | Page background or card surface |
| Inkwell Black | `#252422` | neutral | Primary text or dark surface |
| Deepest Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-parchment: #e2e0d9;
  --ref-inkwell-black: #252422;
  --ref-deepest-black: #000000;
}
```

## Typography direction
- **Times New Roman**: 400, 16px, 1.20; substitute `Times`.
- **EG Metaphor**: 400, 12px, 15px, 59px, 399px, 0.97, 1.00, 1.33, 1.34.
- **S85**: 400, 12px, 3.00.

## Spacing / shape
- Section Gap: `22px`
- Card Padding: `14px`
- Element Gap: `16px`
- Radius: `tabs: 36px, buttons: 1440px, navigation: 1440px`

## Component cues
- **Navigation Tab Active**: Primary navigation item, active state
- **Navigation Tab Inactive**: Primary navigation item, inactive state
- **Navigation Link Outlined**: Small, outlined navigation link
- **Large Typography Headline**: Main heading text on hero sections
- **Body Text Section**: Paragraphs of body content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
