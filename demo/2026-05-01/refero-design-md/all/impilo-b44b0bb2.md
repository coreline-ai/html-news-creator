# Impilo - Refero Design MD

- Source: https://styles.refero.design/style/b44b0bb2-4ba3-4599-9706-3c3e0c8c2522
- Original site: https://impilo.health
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep violet command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Indigo | `#16165c` | neutral | Primary text or dark surface |
| Ghost Frost | `#f4f4f6` | neutral | Page background or card surface |
| Bright Blue | `#00b1ff` | accent | Action accent / signal color |
| Vivid Green | `#00ffaa` | accent | Action accent / signal color |
| Action Violet | `#5350cc` | brand | Action accent / signal color |
| White | `#ffffff` | neutral | Page background or card surface |
| Muted Violet | `#b1a6f6` | accent | Action accent / signal color |
| Deep Violet Surface | `#232269` | neutral | Action accent / signal color |
| Rich Violet | `#403cd5` | brand | Action accent / signal color |
| Interactive Violet | `#524fe1` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-indigo: #16165c;
  --ref-ghost-frost: #f4f4f6;
  --ref-bright-blue: #00b1ff;
  --ref-vivid-green: #00ffaa;
  --ref-action-violet: #5350cc;
  --ref-white: #ffffff;
  --ref-muted-violet: #b1a6f6;
  --ref-deep-violet-surface: #232269;
}
```

## Typography direction
- **Gilroy**: 500, 600, 12px, 13px, 14px, 17px, 18px, 24px, 46px, 54px, 66px, 92px, 124px, 0.92, 1.00, 1.44; substitute `system-ui`.

## Spacing / shape
- Section Gap: `34px`
- Card Padding: `43px`
- Element Gap: `8px`
- Radius: `cards: 24.0048px, icons: 6.9984px, buttons: 1425.6px, largeCards: 31.9968px, smallCards: 15.9984px`

## Component cues
- **Primary Action Button**: Major calls to action
- **Ghost Header Button**: Navigation and secondary actions in header
- **White Ghost Button**: Secondary calls to action on dark backgrounds
- **Hero Section Card**: Information containers within the hero
- **Feature Card**: Displaying product features or service benefits

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
