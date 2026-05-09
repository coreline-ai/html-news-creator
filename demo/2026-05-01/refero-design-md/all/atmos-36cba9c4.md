# ATMOS - Refero Design MD

- Source: https://styles.refero.design/style/36cba9c4-9852-4f59-a52d-17be741f6ed8
- Original site: https://atmos.leeroy.ca
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Ethereal Sky Gradient

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Gradient | `#0825c6` | brand | Action accent / signal color |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-sky-gradient: #0825c6;
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
}
```

## Typography direction
- **NewYork**: 400, 50px, 200px, 1.15; substitute `Playfair Display`.
- **DM Sans**: 400, 700, 20px, 25px, 30px, 1.15, 1.50; substitute `Inter`.
- **Times**: 400, 10px, 1.15; substitute `Times New Roman`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `30px`
- Element Gap: `20px`
- Radius: `buttons: 9999px`

## Component cues
- **Hero Title**: Dominant text element on the landing page.
- **Circular Subtitle**: Accompanying descriptive text in the hero section.
- **Outlined Explore Button**: Primary call to action with a ghost-like appearance.
- **Introductory Heading**: Section titles after the hero.
- **Body Text**: Standard paragraph text.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
