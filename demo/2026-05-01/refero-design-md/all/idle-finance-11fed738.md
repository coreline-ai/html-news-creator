# Idle Finance - Refero Design MD

- Source: https://styles.refero.design/style/11fed738-a5b5-4509-b4e2-3295ceab3604
- Original site: https://idle.finance
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep-space command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#17202e` | neutral | Primary text or dark surface |
| Astral Gray | `#202a3e` | neutral | Primary text or dark surface |
| Star Dust | `#cdd0d6` | neutral | Border, muted text, or supporting surface |
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Cyber Cyan | `#6ae4ff` | accent | Action accent / signal color |
| Deep Ocean Gradient | `#2d3748` | brand | Action accent / signal color |
| Nebula Core Gradient | `#08218f` | brand | Action accent / signal color |
| Emerald Vapor Gradient | `#34edb3` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #17202e;
  --ref-astral-gray: #202a3e;
  --ref-star-dust: #cdd0d6;
  --ref-void-black: #000000;
  --ref-polar-white: #ffffff;
  --ref-cyber-cyan: #6ae4ff;
  --ref-deep-ocean-gradient: #2d3748;
  --ref-nebula-core-gradient: #08218f;
}
```

## Typography direction
- **Open Sans**: 400, 600, 700, 12px, 14px, 18px, 20px, 22px, 28px, 36px, 56px, 100px, 1.00, 1.20, 1.33, 1.36, 1.43, 1.57, 1.60, 1.96, 2.14; substitute `system-ui`.
- **Source Sans Pro**: 400, 500, 600, 700, 12px, 14px, 15px, 16px, 1.00, 1.17, 1.50, 1.71, 2.00, 2.13, 2.29, 2.33; substitute `system-ui`.
- **Arial**: 400, 13px, 1.20; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `66px`
- Element Gap: `16px`
- Radius: `misc: 24px, cards: 15px, links: 8px, buttons: 80px, smallButtons: 4px`

## Component cues
- **Filled Primary Button**: Primary call to action.
- **Outlined Accent Button**: Call to action with secondary emphasis or promoting brand color.
- **Ghost Bordered Button**: Minimal call to action, often for navigation or secondary actions.
- **Data Card**: Display financial metrics or product features.
- **Nested Dark Card**: Sub-element within a larger card or section, like badges within data cards.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
