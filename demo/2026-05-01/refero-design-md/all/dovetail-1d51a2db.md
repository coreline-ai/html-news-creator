# Dovetail - Refero Design MD

- Source: https://styles.refero.design/style/1d51a2db-18fc-4de3-bff7-d1e73ace8b6e
- Original site: https://dovetail.no
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm parchment, sharp ink — a trusted signature.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment | `#fef9f3` | neutral | Page background or card surface |
| Charcoal Ink | `#1d1e21` | neutral | Primary text or dark surface |
| Haze Gray | `#e5e7eb` | neutral | Page background or card surface |
| Midnight | `#000000` | neutral | Primary text or dark surface |
| Sunkissed Ochre | `#f9e5b1` | brand | Action accent / signal color |

```css
:root {
  --ref-parchment: #fef9f3;
  --ref-charcoal-ink: #1d1e21;
  --ref-haze-gray: #e5e7eb;
  --ref-midnight: #000000;
  --ref-sunkissed-ochre: #f9e5b1;
}
```

## Typography direction
- **Lausanne**: 400, 600, 700, 20px, 22px, 28px, 32px, 48px, 72px, 1.00, 1.17, 1.36, 1.40, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `32px`
- Element Gap: `24px`
- Radius: `tags: 9999px, cards: 16px, lists: 91px, images: 16px, buttons: 24px, navItems: 16px`

## Surface cues
- **Parchment Canvas** `#fef9f3`: Dominant page background, providing a warm, inviting foundation.
- **Haze Gray Surface** `#e5e7eb`: Muted background for secondary content areas or subtle dividers for internal separation.
- **Sunkissed Ochre Card** `#f9e5b1`: Highlighting specific content blocks or cards, adding warmth and visual distinction from the canvas.

## Component cues
- **Filled Primary Button**: Call to action button
- **Ghost Navigation Button**: Secondary call to action or navigation item
- **Primary Card**: Group related content, feature sections
- **Navigation Link**: Site navigation item
- **Image Card**: Display images within content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
