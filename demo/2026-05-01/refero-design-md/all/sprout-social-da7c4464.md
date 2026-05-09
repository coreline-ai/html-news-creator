# Sprout Social - Refero Design MD

- Source: https://styles.refero.design/style/da7c4464-f135-41fc-b635-99c6f4dc58e6
- Original site: https://sproutsocial.com
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Ordered command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Core | `#040404` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#d9d9d9` | neutral | Page background or card surface |
| Focus Silver | `#cbcece` | neutral | Border, muted text, or supporting surface |
| Slate Text | `#162020` | neutral | Primary text or dark surface |
| Olive Accent | `#98e58e` | brand | Action accent / signal color |
| Sky Spectrum Fade | `#59cb59` | neutral | Border, muted text, or supporting surface |
| Magenta Mist Fade | `#ac44a8` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-core: #040404;
  --ref-canvas-white: #ffffff;
  --ref-ghost-gray: #d9d9d9;
  --ref-focus-silver: #cbcece;
  --ref-slate-text: #162020;
  --ref-olive-accent: #98e58e;
  --ref-sky-spectrum-fade: #59cb59;
  --ref-magenta-mist-fade: #ac44a8;
}
```

## Typography direction
- **Proxima Nova**: 400, 700, 800, 13px, 16px, 18px, 21px, 24px, 32px, 43px, 57px, 76px, 1.05, 1.12, 1.18, 1.25, 1.33, 1.40, 1.48, 1.50, 1.64; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 16px, badges: 24px, inputs: 6px, buttons: 6px, largeElements: 64px`

## Surface cues
- **Midnight Core Canvas** `#040404`: Primary page background for main content areas and deep sections.
- **Canvas White Panel** `#ffffff`: Card backgrounds, main navigation, and prominent content blocks appearing on the Midnight Core Canvas.

## Component cues
- **Primary Action Button (Filled)**: Call to action
- **Ghost Button (Dark)**: Secondary action
- **Ghost Button (Light)**: Secondary action
- **White Information Card**: Content container
- **Dark Feature Card**: Feature showcase

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
