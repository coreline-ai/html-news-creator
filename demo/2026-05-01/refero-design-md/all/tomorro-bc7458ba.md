# Tomorro - Refero Design MD

- Source: https://styles.refero.design/style/bc7458ba-6b81-4f3e-ab5a-4126ee1eaf80
- Original site: https://www.gotomorro.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Forest AI Canvas

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Canopy | `#122314` | brand | Action accent / signal color |
| Deep Moss | `#273f2b` | brand | Action accent / signal color |
| AI Lime | `#68ef3f` | accent | Action accent / signal color |
| Dark Olive | `#7e8371` | neutral | Border, muted text, or supporting surface |
| Light Stone | `#b7bda5` | neutral | Border, muted text, or supporting surface |
| Pale Mint | `#e7f9dd` | brand | Action accent / signal color |
| Soft Gray | `#d9deca` | neutral | Page background or card surface |
| Evergreen Glow | `#26a200` | accent | Action accent / signal color |
| White | `#ffffff` | neutral | Page background or card surface |
| Ink | `#30322a` | neutral | Primary text or dark surface |

```css
:root {
  --ref-forest-canopy: #122314;
  --ref-deep-moss: #273f2b;
  --ref-ai-lime: #68ef3f;
  --ref-dark-olive: #7e8371;
  --ref-light-stone: #b7bda5;
  --ref-pale-mint: #e7f9dd;
  --ref-soft-gray: #d9deca;
  --ref-evergreen-glow: #26a200;
}
```

## Typography direction
- **Aeonik**: 400, 500, 600, 700, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 32px, 40px, 1.00, 1.10, 1.20, 1.33, 1.43, 1.50, 1.67, 1.70, 1.71; substitute `Inter`.
- **Instrument Serif**: 400, 16px, 18px, 32px, 1.25, 1.50, 1.56; substitute `Lora`.
- **Ozik**: 700, 56px, 80px, 0.86, 0.90; substitute `Oswald`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `40px`
- Element Gap: `8px`
- Radius: `cards: 8px, links: 20px, badges: 40px, inputs: 24px, buttons: 28px, containers: 16px`

## Surface cues
- **White Canvas** `#ffffff`: Default page background, provides a clean and open foundation.
- **Light Canvas Card** `#f2f5eb`: Primary card background for content on light sections, secondary background layer.
- **Pale Mint Accent** `#e7f9dd`: Subtle background for smaller elements or badges, slight elevation in color.
- **Mid Gray Surface** `#d6d6d6`: Background for minimal visual separation or subtle information displays.
- **Forest Canopy Base** `#122314`: Deepest background for hero sections or footers, establishes a contrasting dark base.

## Component cues
- **Primary Filled Button**: Main call-to-action button, signaling key interactions.
- **Ghost Button (Dark)**: Secondary action on dark backgrounds, providing emphasis without distraction.
- **Header Navigation Button**: Compact navigation item with minimal styling.
- **Neutral Card**: Information container on light backgrounds.
- **Dark Accented Card**: Elevated information container within dark sections, featuring a subtle highlight.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
