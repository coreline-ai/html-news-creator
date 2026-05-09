# Morflax - Refero Design MD

- Source: https://styles.refero.design/style/2e24c0ca-dd46-4519-b66e-cc03701d3b8c
- Original site: https://morflax.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprints on frosted glass.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#000000` | neutral | Primary text or dark surface |
| Storm Gray | `#25282b` | neutral | Primary text or dark surface |
| Neutral Canvas | `#ffffff` | neutral | Page background or card surface |
| Light Pearl | `#f5f5f7` | neutral | Page background or card surface |
| Border Silver | `#e5e7eb` | neutral | Page background or card surface |
| Ash Cloud | `#bfbfbf` | neutral | Border, muted text, or supporting surface |
| Header Slate | `#333333` | neutral | Primary text or dark surface |
| Link Gray | `#7c7e83` | neutral | Border, muted text, or supporting surface |
| Icon Mist | `#a3a7ad` | neutral | Border, muted text, or supporting surface |
| Skybound Blue | `#298ef5` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #000000;
  --ref-storm-gray: #25282b;
  --ref-neutral-canvas: #ffffff;
  --ref-light-pearl: #f5f5f7;
  --ref-border-silver: #e5e7eb;
  --ref-ash-cloud: #bfbfbf;
  --ref-header-slate: #333333;
  --ref-link-gray: #7c7e83;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 12px, 14px, 16px, 18px, 20px, 24px, 36px, 48px, 60px, 72px, 1.00, 1.11, 1.33, 1.40, 1.43, 1.50, 1.56; substitute `system-ui, sans-serif`.
- **rogan**: 500, 16px, 24px, 1.33, 1.50.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `tags: 9999px, cards: 24px, avatar: 9999px, inputs: 12px, buttons: 9999px`

## Surface cues
- **Neutral Canvas** `#ffffff`: Base page background
- **Light Pearl** `#f5f5f7`: Elevated card backgrounds, ghost secondary buttons
- **Midnight Graphite** `#000000`: Dark section backgrounds, prominent specialized cards

## Component cues
- **Pill Button - Default**: Secondary action button, often paired with primary blue button or for navigation.
- **Pill Button - Light Secondary**: Subtly elevated secondary button for less emphasis than default.
- **Primary Action Button - Filled**: Call to action, high prominence.
- **Neutral Card - Light**: Standard content container on light backgrounds.
- **Neutral Card - Shadowed**: Elevated white card for key content sections or hover states.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
