# Lightdash - Refero Design MD

- Source: https://styles.refero.design/style/d0f65d12-a8e6-4631-99f7-bb7cdcd5b6c5
- Original site: https://www.lightdash.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Codebase blueprint on frosted glass

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1a1b25` | neutral | Primary text or dark surface |
| Charcoal Slate | `#272835` | neutral | Primary text or dark surface |
| Deep Indigo | `#36394a` | neutral | Primary text or dark surface |
| Steel Gray | `#666d80` | neutral | Border, muted text, or supporting surface |
| Cloud Gray | `#818898` | neutral | Border, muted text, or supporting surface |
| Stone Wash | `#a4abb8` | neutral | Border, muted text, or supporting surface |
| Off-White | `#f8fafb` | neutral | Page background or card surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Lava Cloud | `#eceff3` | neutral | Page background or card surface |
| Ghost Fill | `#f6f8fa` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #1a1b25;
  --ref-charcoal-slate: #272835;
  --ref-deep-indigo: #36394a;
  --ref-steel-gray: #666d80;
  --ref-cloud-gray: #818898;
  --ref-stone-wash: #a4abb8;
  --ref-off-white: #f8fafb;
  --ref-canvas-white: #ffffff;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Britti Sans Trial Semibold**: 400, 600, 18px, 48px, 56px, 57px, 76px, 0.90, 0.95, 1.00, 1.56; substitute `Montserrat`.
- **Britti Sans Medium**: 400, 500, 14px, 16px, 18px, 20px, 24px, 32px, 1.11, 1.14, 1.20, 1.25, 1.30, 1.80, 2.00; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `40-64px`
- Card Padding: `24-32px`
- Element Gap: `8px`
- Radius: `tags: 999px, cards: 12px, inputs: 0px, buttons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for content.
- **Ghost Fill** `#f6f8fa`: Subtle background for distinct sections, hover states, or input wrappers.
- **Lava Cloud** `#eceff3`: Alternating section backgrounds and more pronounced content dividers.
- **Off-White** `#f8fafb`: Background for specific UI components or elevated informational blocks.

## Component cues
- **Primary Action Button**: Call to action.
- **Secondary Ghost Button**: Secondary action or subtle interaction.
- **Tertiary Filled Button**: Informational actions or less prominent calls to action.
- **Interactive Chip Button**: Filter chips or toggleable options.
- **Elevated Feature Card**: Showcasing product features or key information.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
