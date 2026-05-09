# Ditto - Refero Design MD

- Source: https://styles.refero.design/style/e9001d5a-504d-47ed-aef0-d0d35fa86418
- Original site: https://trustditto.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Parchment and Ink with Marigold Accents

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#130e30` | brand | Action accent / signal color |
| Marigold Burst | `#ffe228` | accent | Action accent / signal color |
| Frosted Sage | `#eff2e5` | neutral | Page background or card surface |
| Paper White | `#f9fbf2` | neutral | Page background or card surface |
| Graphite | `#222222` | neutral | Primary text or dark surface |
| Subtle Ash | `#5f5c6e` | neutral | Border, muted text, or supporting surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |
| Vivid Shamrock | `#59e25d` | accent | Action accent / signal color |
| Electric Fuchsia | `#e261e5` | accent | Action accent / signal color |
| Sky Blue | `#3a93ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #130e30;
  --ref-marigold-burst: #ffe228;
  --ref-frosted-sage: #eff2e5;
  --ref-paper-white: #f9fbf2;
  --ref-graphite: #222222;
  --ref-subtle-ash: #5f5c6e;
  --ref-pure-black: #000000;
  --ref-vivid-shamrock: #59e25d;
}
```

## Typography direction
- **Hedvig Letters Serif**: 400, 700, 22px, 32px, 48px, 64px, 1.00, 1.10, 1.15, 1.20, 1.25; substitute `Georgia`.
- **Inter**: 400, 500, 600, 10px, 14px, 16px, 18px, 22px, 1.20, 1.25, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `12px`
- Radius: `cards: 24px, images: 24px, avatars: 1440px, buttons: 1440px`

## Surface cues
- **Page Canvas** `#f9fbf2`: The primary background, clean and bright, for the overall layout.
- **Content Card** `#eff2e5`: Slightly darker, warmer background for grouped content like cards and sections, providing subtle visual layering without elevation.
- **Prominent Accent** `#ffe228`: Used for primary interactive elements, standing out as a focal point.
- **Deep Surface** `#130e30`: Used for dark-themed components or sections, providing strong contrast and visual gravity.

## Component cues
- **Primary Action Button**: Call to action
- **Secondary Filled Button**: Alternative action
- **Ghost Button**: Navigation, tertiary actions
- **Content Card**: Information container
- **Input Field**: User input

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
