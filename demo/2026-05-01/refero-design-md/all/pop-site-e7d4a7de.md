# Pop Site - Refero Design MD

- Source: https://styles.refero.design/style/e7d4a7de-aeaf-4d49-8c0c-0dedd05a8992
- Original site: https://pop.site
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp canvas, bold headlines, electric blue

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Coal Black | `#000000` | neutral | Primary text or dark surface |
| Ink Black | `#171717` | neutral | Primary text or dark surface |
| Slate Gray | `#5e5e5e` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#6e6e73` | neutral | Border, muted text, or supporting surface |
| Fog Gray | `#d2d2d7` | neutral | Border, muted text, or supporting surface |
| Action Blue | `#3b82f6` | brand | Action accent / signal color |
| Outline Blue | `#6ea5ff` | brand | Action accent / signal color |
| Eclipse Gradient | `#363836` | accent | Action accent / signal color |
| Ember Gradient | `#c72b00` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-coal-black: #000000;
  --ref-ink-black: #171717;
  --ref-slate-gray: #5e5e5e;
  --ref-ash-gray: #6e6e73;
  --ref-fog-gray: #d2d2d7;
  --ref-action-blue: #3b82f6;
  --ref-outline-blue: #6ea5ff;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Satoshi**: 400, 500, 700, 12px, 13px, 15px, 21px, 53px, 93px, 120px, 0.90, 1.00, 1.20, 1.30, 1.40; substitute `Inter`.
- **Inter**: 400, 14px, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `pill: 9999px, cards: 10px, image: 8px, buttons: 26px, default: 8px`

## Component cues
- **Primary Action Button**: Filled call to action button
- **Ghost Input Segment Button**: Segmented control component part or input accessory
- **Ghost Link Button**: Outlined or text-only button for secondary actions or navigation
- **Content Card**: Container for features, testimonials, or content blocks
- **Full-Bleed Media Card**: Card container for imagery or full-bleed elements

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
