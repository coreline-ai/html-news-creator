# Penpot - Refero Design MD

- Source: https://styles.refero.design/style/7be94705-3666-4fb1-a389-0cfd7cb223cd
- Original site: https://penpot.app
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#151035` | brand | Action accent / signal color |
| Activation Teal | `#1ccac7` | accent | Action accent / signal color |
| Vivid Violet Accent | `#2f226c` | accent | Action accent / signal color |
| Pure White | `#fafafa` | neutral | Page background or card surface |
| Off-White | `#eeeeee` | neutral | Page background or card surface |
| Subtle Gray | `#d3d3d3` | neutral | Border, muted text, or supporting surface |
| Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #151035;
  --ref-activation-teal: #1ccac7;
  --ref-vivid-violet-accent: #2f226c;
  --ref-pure-white: #fafafa;
  --ref-off-white: #eeeeee;
  --ref-subtle-gray: #d3d3d3;
  --ref-black: #000000;
}
```

## Typography direction
- **Work Sans**: 400, 500, 700, 12px, 14px, 16px, 18px, 24px, 48px, 52px, 72px, 1.10, 1.20, 1.50; substitute `system-ui`.
- **Times**: 400, 16px, 1.2.

## Spacing / shape
- Section Gap: `130px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `tags: 50px, cards: 20px, inputs: 8px, buttons: 8px`

## Surface cues
- **Canvas Midnight** `#151035`: Primary page background, base layer.
- **Card Surface** `#151035`: Background for product display cards and grouped content sections, matching the canvas for a flush look.

## Component cues
- **Ghost Button (Dark)**: Secondary action button with transparent background, used against dark backgrounds.
- **Ghost Button (Light)**: Secondary action button with transparent background, used against light backgrounds.
- **Primary Action Button**: Main call-to-action button.
- **Neutral Button**: Default interactive button for general actions.
- **Product Display Card**: Container for product showcases or feature descriptions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
