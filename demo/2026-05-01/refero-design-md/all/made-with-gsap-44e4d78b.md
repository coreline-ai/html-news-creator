# Made With Gsap - Refero Design MD

- Source: https://styles.refero.design/style/44e4d78b-d78a-4d00-bd10-94b14ac083c9
- Original site: https://madewithgsap.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital canvas.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f1f1f1` | neutral | Page background or card surface |
| Midnight Ink | `#121212` | neutral | Primary text or dark surface |
| Accent Green | `#c9fe6e` | brand | Action accent / signal color |
| Deep Gray | `#252525` | neutral | Primary text or dark surface |
| Muted Ash | `#777777` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #f1f1f1;
  --ref-midnight-ink: #121212;
  --ref-accent-green: #c9fe6e;
  --ref-deep-gray: #252525;
  --ref-muted-ash: #777777;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **LayGrotesk**: 500, 700, 12px, 18px, 22px, 40px, 44px, 65px, 100px, 114px, 250px, 0.80, 0.88, 0.90, 1.00, 1.08, 1.11, 1.20, 1.30, 2.28; substitute `Inter`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `25px`
- Element Gap: `15px`
- Radius: `cards: 12px, links: 2px, buttons: 2px`

## Component cues
- **Primary Action Button**: Call to action button
- **Hero Outline Button**: Secondary action button/ghost button
- **Navigation Link Button**: Navigation link
- **Dark Card**: Content container for features or examples
- **Content Input**: User input field

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
