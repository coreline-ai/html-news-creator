# Eight Sleep - Refero Design MD

- Source: https://styles.refero.design/style/e4e8fe86-47ed-4ddd-a6c6-2c28eae9aabe
- Original site: https://eightsleep.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center // A dark, immersive interface with pin-prick bright accents, like illuminated controls in a premium device.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#121212` | neutral | Primary text or dark surface |
| Porcelain White | `#ffffff` | neutral | Page background or card surface |
| Silver Thread | `#808080` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#8e8d92` | neutral | Border, muted text, or supporting surface |
| Graphite | `#363636` | neutral | Primary text or dark surface |
| Winter Frost | `#f9f8f7` | neutral | Page background or card surface |
| Ghost Gray | `#f1f2f4` | neutral | Page background or card surface |
| Electric Violet | `#4158ee` | accent | Action accent / signal color |
| Sky Blue | `#1862ff` | accent | Action accent / signal color |
| Nightfall Gradient | `#1b263b` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #121212;
  --ref-porcelain-white: #ffffff;
  --ref-silver-thread: #808080;
  --ref-ash-gray: #8e8d92;
  --ref-graphite: #363636;
  --ref-winter-frost: #f9f8f7;
  --ref-ghost-gray: #f1f2f4;
  --ref-electric-violet: #4158ee;
}
```

## Typography direction
- **NeueMontreal**: 300, 400, 500, 700, 10px, 12px, 14px, 15px, 16px, 17px, 18px, 20px, 22px, 28px, 36px, 44px, 56px, 64px, 115px, 0.94, 1.00, 1.09, 1.10, 1.20, 1.27, 1.31, 1.33, 1.40, 1.50, 1.70, 1.92; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Element Gap: `16px`
- Radius: `cards: 12px, chips: 9999px, inputs: 0px, buttons: 4px, default: 8px`

## Component cues
- **Region Selector Modal**: Reference component style.
- **Sleep Challenge Quiz Panel**: Reference component style.
- **Announcement Banner + CTA Buttons**: Reference component style.
- **Ghost Navigation Link**: Primary navigation, secondary CTAs
- **Primary Navigation Product Link**: Top-level navigation items

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
