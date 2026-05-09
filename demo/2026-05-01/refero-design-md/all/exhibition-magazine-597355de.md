# Exhibition Magazine - Refero Design MD

- Source: https://styles.refero.design/style/597355de-6167-4f37-8f14-b3897919a94c
- Original site: https://exhibition-magazine.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome editorial canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Divider Gray | `#e5e7eb` | neutral | Page background or card surface |
| Muted Surface | `#a9a9a9` | neutral | Border, muted text, or supporting surface |
| Blush Card Back | `#fff5fa` | neutral | Page background or card surface |
| Swiper Accent | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-divider-gray: #e5e7eb;
  --ref-muted-surface: #a9a9a9;
  --ref-blush-card-back: #fff5fa;
  --ref-swiper-accent: #007aff;
}
```

## Typography direction
- **Cochin**: 400, 16px, 46px, 1.20, 1.50; substitute `Georgia`.
- **DIN**: 400, 25px, 36px, 40px, 50px, 52px, 90px, 100px, 0.75, 0.80, 1.00, 1.20; substitute `Inter`.
- **forma-djr-display**: 500, 13px, 1.60; substitute `Roboto Mono`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `24px`
- Element Gap: `12px`
- Radius: `cards: 0px, buttons: 100%`

## Component cues
- **Carousel Navigation Button**: Interactive element to navigate image carousels
- **Load More Button**: Expands content using a prominent call to action.
- **Image Card Default**: Displays articles or features prominently with large imagery.
- **Blush Content Card**: Highlights specific curated content or editorial picks.
- **Hero Section Header**: Primary visual for articles, featuring a large image and overlaid title.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
