# Miranda - Refero Design MD

- Source: https://styles.refero.design/style/3f6e3076-e77f-487e-b212-3b5946a34e87
- Original site: https://www.niccolomiranda.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vintage newsprint, bold headlines.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1d1d1b` | neutral | Primary text or dark surface |
| Aged Paper | `#cdc6be` | neutral | Border, muted text, or supporting surface |
| Deep Shadow | `#000000` | neutral | Primary text or dark surface |
| Bleached Canvas | `#e2dedb` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #1d1d1b;
  --ref-aged-paper: #cdc6be;
  --ref-deep-shadow: #000000;
  --ref-bleached-canvas: #e2dedb;
}
```

## Typography direction
- **Editorial New**: 300, 16px, 17px, 19px, 20px, 24px, 29px, 31px, 32px, 37px, 86px, 0.93, 1.08, 1.11, 1.15, 1.16, 1.18, 1.20, 1.25, 1.27, 1.33, 1.36; substitute `Playfair Display`.
- **Canopee**: 400, 17px, 20px, 22px, 23px, 32px, 43px, 65px, 72px, 86px, 109px, 112px, 118px, 122px, 202px, 212px, 366px, 432px, 446px, 533px, 0.71, 0.73, 0.77, 0.78, 0.79, 0.81, 0.91, 1.00, 1.25; substitute `Anton`.
- **Domaine Display**: 500, 20px, 22px, 32px, 65px, 72px, 86px, 109px, 118px, 122px, 446px, 0.73, 0.78, 0.79, 0.91, 1.00; substitute `Staatliches`.

## Spacing / shape
- Section Gap: `43px`
- Element Gap: `14px`
- Radius: `misc: 2.88px, cards: 11.52px, buttons: 0px`

## Surface cues
- **Canvas (Midnight Ink)** `#1d1d1b`: Dominant background for the entire page, creating a deep, immersive environment.
- **Paper Surface (Aged Paper)** `#cdc6be`: Primary surface for cards and content blocks, providing a warm, contrasting layer against the dark canvas.
- **Image Canvas (Bleached Canvas)** `#e2dedb`: Specific background for images, offering a very light, almost white base to make visuals pop.

## Component cues
- **Filled Button (Email Me)**: Primary action button.
- **Feature Card**: Content container for showcased work or information blocks.
- **Callout Badge**: Small, contextual label for showcasing new content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
