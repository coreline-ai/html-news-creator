# Paradigm - Refero Design MD

- Source: https://styles.refero.design/style/73cd9a6a-f861-4376-a3e1-e12f83c8960e
- Original site: https://www.paradigmai.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Strategic Intelligence Platform: dark obsidian meets stark white

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#080b12` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Gridline Gray | `#d9d9d9` | neutral | Page background or card surface |
| Subtle Ash | `#4f535e` | neutral | Border, muted text, or supporting surface |
| Surface Off-White | `#f6f7f8` | neutral | Page background or card surface |
| Cool Stone | `#b5b9c4` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Dark Overlay | `#35373e` | neutral | Primary text or dark surface |
| Border Haze | `#edeef1` | neutral | Page background or card surface |
| Cerulean Accent | `#0a33ff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #080b12;
  --ref-canvas-white: #ffffff;
  --ref-gridline-gray: #d9d9d9;
  --ref-subtle-ash: #4f535e;
  --ref-surface-off-white: #f6f7f8;
  --ref-cool-stone: #b5b9c4;
  --ref-steel-gray: #808080;
  --ref-dark-overlay: #35373e;
}
```

## Typography direction
- **PP Neue Montreal**: 400, 450, 500, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 21px, 22px, 160px, 1.00, 1.10, 1.20, 1.28, 1.30, 1.40, 1.50, 1.60, 1.80; substitute `System UI (e.g. SF Pro Text, Roboto, Noto Sans)`.
- **Inter**: 400, 500, 600, 700, 9px, 10px, 11px, 12px, 13px, 14px, 15px, 1.20, 1.40, 1.60; substitute `Roboto, Noto Sans`.
- **Atacama VAR**: 317, 370, 400, 44px, 48px, 54px, 1.00, 1.10, 1.15, 1.20; substitute `Montserrat, Open Sans Light`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `14px`
- Radius: `pill: 100px, cards: 4px, input: 4px, badges: 4px, buttons: 4px, largeCard: 16px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default layer for content.
- **Surface Off-White** `#f6f7f8`: Slightly elevated background for distinct sections or very light card variations.
- **Card Surface** `#ffffff`: Default background for UI cards, typically with a subtle shadow for definition.
- **Modal/Elevated Content** `#ffffff`: Higher Z-index elements like modals or dropdowns, with a more pronounced shadow.

## Component cues
- **Primary Ghost Button**: Main call to action for the hero section and prominent interactions.
- **Secondary Ghost Button**: Auxiliary calls to action, less prominent than the primary.
- **Filled Action Button**: Interactive button for discrete actions, like 'Enrich'.
- **Navigation Link**: Top-level navigation items and in-page links.
- **Simple Card**: Standard container for content, features, or data blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
