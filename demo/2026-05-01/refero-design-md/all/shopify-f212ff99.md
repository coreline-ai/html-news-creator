# Shopify - Refero Design MD

- Source: https://styles.refero.design/style/f212ff99-24fa-4646-a0f2-46a815736ecd
- Original site: https://www.shopify.com
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center: A sophisticated dark interface, both precise and dynamically lit.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Deep Ocean | `#02090a` | neutral | Primary text or dark surface |
| Charcoal Grey | `#061a1c` | neutral | Primary text or dark surface |
| Steel Gaze | `#1e2c31` | neutral | Primary text or dark surface |
| Twilight Indigo | `#000a10` | neutral | Primary text or dark surface |
| Abyssal Violet | `#010624` | neutral | Action accent / signal color |
| Dark Forest | `#072720` | neutral | Primary text or dark surface |
| Snowdrift | `#ffffff` | neutral | Page background or card surface |
| Ash Grey | `#a1a1aa` | neutral | Border, muted text, or supporting surface |
| Cloud Mist | `#e5e7eb` | neutral | Page background or card surface |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-deep-ocean: #02090a;
  --ref-charcoal-grey: #061a1c;
  --ref-steel-gaze: #1e2c31;
  --ref-twilight-indigo: #000a10;
  --ref-abyssal-violet: #010624;
  --ref-dark-forest: #072720;
  --ref-snowdrift: #ffffff;
}
```

## Typography direction
- **NeueHaasGrotesk**: 330, 400, 500, 550, 600, 14px, 16px, 18px, 20px, 24px, 28px, 48px, 55px, 70px, 96px, 0.83, 0.96, 1.00, 1.14, 1.16, 1.25, 1.28, 1.40, 1.49, 1.50; substitute `Helvetica Neue, Aktiv Grotesk`.
- **Inter-Variable**: 400, 420, 450, 550, 12px, 14px, 16px, 18px, 20px, 1.00, 1.20, 1.29, 1.43, 1.50, 1.56; substitute `Inter`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `13px`
- Element Gap: `12px`
- Radius: `cards: 12px, media: 8px, inputs: 4px, avatars: 340px, buttons: 9999px`

## Surface cues
- **Deep Ocean Canvas** `#02090a`: Primary page background and base layer.
- **Charcoal Grey Card** `#061a1c`: Standard card backgrounds and elevated content blocks.
- **Twilight Indigo Elevated** `#000a1`: Secondary elevated background for distinct panels or deeper content isolation.
- **Snowdrift Overlay** `#ffffff`: Light-themed elements, modals, or contextual pop-ups that stand out from the dark theme.

## Component cues
- **Primary Filled Button**: Interactive element
- **Ghost Button (Subtle)**: Interactive element
- **Ghost Button (Outlined)**: Interactive element
- **Hero Card (Dark Elevated)**: Information display
- **Interactive Card (Light Border)**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
