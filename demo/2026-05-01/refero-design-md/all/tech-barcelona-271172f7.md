# Tech Barcelona - Refero Design MD

- Source: https://styles.refero.design/style/271172f7-9f6d-4d6f-9baa-91a41648d8be
- Original site: https://techbarcelona.com/en
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast geometric blueprint

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Text | `#212529` | neutral | Primary text or dark surface |
| Light Gray Divider | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Headline Black | `#090707` | neutral | Primary text or dark surface |
| Ice Blue Accent | `#0075ff` | brand | Action accent / signal color |
| Shadow White | `#eeeeee` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-ink-text: #212529;
  --ref-light-gray-divider: #cccccc;
  --ref-headline-black: #090707;
  --ref-ice-blue-accent: #0075ff;
  --ref-shadow-white: #eeeeee;
}
```

## Typography direction
- **FavoritPro-Light**: 400, 10px, 12px, 13px, 14px, 16px, 18px, 20px, 22px, 50px, 80px, 1.00, 1.14, 1.15, 1.20, 1.30, 1.33, 1.50, 1.59; substitute `Open Sans, Arial`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `default: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and light surface areas.
- **Content Black** `#000000`: Dominant background for main content blocks, high-contrast sections.

## Component cues
- **Primary Action Button**: Filled button for main calls to action.
- **Ghost Bordered Button**: Secondary action button with a border and transparent background.
- **Text Link Button**: Tertiary action or navigational link styled as a button.
- **White Text Link Button**: Text link for navigation or small actions on dark backgrounds.
- **Muted Card**: Container for content, particularly news items.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
