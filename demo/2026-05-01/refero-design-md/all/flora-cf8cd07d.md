# FLORA - Refero Design MD

- Source: https://styles.refero.design/style/cf8cd07d-bff0-41dc-ab70-fa85750f6168
- Original site: https://www.florafauna.ai
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Deep Charcoal | `#191919` | neutral | Primary text or dark surface |
| Off White | `#eeeeee` | neutral | Page background or card surface |
| Medium Gray | `#606060` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#b4b4b4` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#7b7b7b` | neutral | Border, muted text, or supporting surface |
| Dark Charcoal Outline | `#303030` | neutral | Primary text or dark surface |
| Soft Gray | `#bfbfbf` | neutral | Border, muted text, or supporting surface |
| Onyx Faint | `#050505` | neutral | Primary text or dark surface |
| Vivid Green | `#71d083` | brand | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-deep-charcoal: #191919;
  --ref-off-white: #eeeeee;
  --ref-medium-gray: #606060;
  --ref-light-gray: #b4b4b4;
  --ref-ash-gray: #7b7b7b;
  --ref-dark-charcoal-outline: #303030;
  --ref-soft-gray: #bfbfbf;
}
```

## Typography direction
- **Geist**: 400, 500, 600, 8px, 11px, 12px, 14px, 15px, 16px, 20px, 22px, 30px, 60px, 80px, 1.00, 1.10, 1.20, 1.37, 1.40, 1.50; substitute `Inter`.
- **Geist Variable**: 400, 700, 14px, 1.00; substitute `Inter`.
- **Satoshi**: 700, 22px, 1.15; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `4px`
- Page Max Width: `1200px`
- Radius: `pill: 999px, cards: 10px, input: 12px, buttons: 9999px, default: 10px`

## Surface cues
- **Canvas** `#000000`: The foundational background for the entire page, providing a deep, immersive dark theme.
- **Base Card** `#191919`: Used for standard cards and major content blocks, offering a slightly lighter dark surface for visual hierarchy.
- **Elevated Card** `#303030`: For cards requiring more distinction or visual lift, creating a subtle third dimension without shadows.

## Component cues
- **Ghost Navigation Button**: Navigational elements in the header and sub-menus.
- **Outlined Pill Button (Dense)**: Compact secondary actions and filters.
- **Outlined Rounded Button (Compact)**: Informational or tertiary actions.
- **Primary CTA Button**: Main call to action, stand-alone buttons for key interactions.
- **Default Card**: Content containers for features, showcases, or related information.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
