# IDHEAL - Refero Design MD

- Source: https://styles.refero.design/style/8d8d5861-dee0-431b-826d-56f3fa4e1f84
- Original site: https://idheal.fr
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochromatic academic blueprint

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Subtle Gray | `#e5e5e5` | neutral | Page background or card surface |
| Shadow Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Brick Red | `#bc5346` | brand | Action accent / signal color |
| Fuchsia Pink | `#ff00bc` | accent | Action accent / signal color |
| Moss Green | `#51633c` | accent | Action accent / signal color |

```css
:root {
  --ref-ink-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-subtle-gray: #e5e5e5;
  --ref-shadow-gray: #cccccc;
  --ref-brick-red: #bc5346;
  --ref-fuchsia-pink: #ff00bc;
  --ref-moss-green: #51633c;
}
```

## Typography direction
- **sans-serif**: 400, 15px, 67px, 1.00, 1.20.
- **Helvetica Neue LT Pro**: 400, 12px, 18px, 21px, 105px, 0.80, 0.95, 1.00, 1.17, 1.20; substitute `Arial, Helvetica, sans-serif`.
- **Helvetica Neue LT Pro**: 400, 12px, 1.20; substitute `Arial, Helvetica, sans-serif`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `cards: 0px, buttons: 15px, navigationItems: 37.5px, generalRoundedElements: 9.999px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background
- **Subtle Gray** `#e5e5e5`: Secondary background for content sections or cards

## Component cues
- **Circular Ghost Button**: Tertiary action button, decorative element with text
- **Rounded Corner Ghost Button**: Outlined button for secondary actions or links
- **Borderless Content Card**: Container for content, particularly news items or listings
- **Navigation Link**: Primary navigation items
- **Headline Link with Accent**: Clickable headlines, leading to detailed content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
