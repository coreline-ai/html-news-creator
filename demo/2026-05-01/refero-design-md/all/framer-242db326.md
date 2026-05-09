# Framer - Refero Design MD

- Source: https://styles.refero.design/style/242db326-a6f3-482a-b12e-5e7f8af94981
- Original site: https://www.framer.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Space Command

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#080808` | neutral | Primary text or dark surface |
| Rich Coal | `#171717` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Mercury Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#0099ff` | brand | Action accent / signal color |
| Velocity Blue | `#0055ff` | brand | Action accent / signal color |
| Shadow Tint | `#021f33` | brand | Action accent / signal color |
| Interactive Blue Tint | `#0000ee` | neutral | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-deep-graphite: #080808;
  --ref-rich-coal: #171717;
  --ref-cloud-white: #ffffff;
  --ref-mercury-gray: #999999;
  --ref-steel-gray: #666666;
  --ref-electric-blue: #0099ff;
  --ref-velocity-blue: #0055ff;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Inter Variable**: 400, 8px, 12px, 13px, 14px, 15px, 18px, 24px, 0.80, 1.00, 1.07, 1.20, 1.30, 1.40; substitute `Inter`.
- **Inter**: 400, 500, 600, 700, 10px, 12px, 13px, 14px, 20px, 22px, 0.83, 1.00, 1.10, 1.15, 1.20, 1.30, 1.40, 1.60; substitute `Inter`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `40px`
- Element Gap: `10px`
- Radius: `cards: 10px, buttons: 100px, default: 8px, minimal: 1px, decorative: 15px, extra-large: 40px, large-cards: 30px`

## Surface cues
- **Midnight Ink** `#000000`: Base page background, deepest layer.
- **Deep Graphite** `#080808`: Primary card backgrounds, first layer of elevation.
- **Rich Coal** `#171717`: Secondary elevated surfaces, slightly darker than Deep Graphite for further distinction.

## Component cues
- **Primary Ghost Button**: Action button
- **Secondary Button (White)**: Call to action
- **Tertiary Button (Ghost Frosted)**: Secondary action button
- **Text Button / Link**: Navigation or in-line action
- **Default Card**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
