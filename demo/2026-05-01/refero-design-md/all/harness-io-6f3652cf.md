# Harness.io - Refero Design MD

- Source: https://styles.refero.design/style/6f3652cf-583f-411d-a117-3a03f6342917
- Original site: https://gitness.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Console. A digital workspace with data streams under soft, diffused light against a dark, technical expanse.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#070707` | neutral | Primary text or dark surface |
| Deep Space | `#0d0e12` | neutral | Primary text or dark surface |
| Ash Grey | `#141418` | neutral | Primary text or dark surface |
| Graphite | `#2e3038` | neutral | Primary text or dark surface |
| Light Ghost | `#ffffff` | neutral | Page background or card surface |
| Cool Mist | `#f0f0f0` | neutral | Page background or card surface |
| Smokey Quartz | `#d9dae5` | neutral | Page background or card surface |
| Storm Cloud | `#aeaeb7` | neutral | Border, muted text, or supporting surface |
| Slate | `#22222a` | neutral | Primary text or dark surface |
| Ice Blue Highlight | `#effbff` | neutral | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #070707;
  --ref-deep-space: #0d0e12;
  --ref-ash-grey: #141418;
  --ref-graphite: #2e3038;
  --ref-light-ghost: #ffffff;
  --ref-cool-mist: #f0f0f0;
  --ref-smokey-quartz: #d9dae5;
  --ref-storm-cloud: #aeaeb7;
}
```

## Typography direction
- **Geist**: 300, 400, 500, 600, 8px, 10px, 12px, 14px, 15px, 16px, 18px, 20px, 22px, 24px, 40px, 0.88, 1.00, 1.13, 1.20, 1.22, 1.37, 1.38, 1.44, 1.50, 1.57; substitute `Inter`.
- **Calsans**: 300, 600, 18px, 24px, 32px, 34px, 56px, 64px, 72px, 88px, 0.96, 1.00, 1.10, 1.15, 1.20, 1.37; substitute `Montserrat`.
- **Helvetica**: 400, 600, 13px, 1.69; substitute `Arial`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `base: 20px, tags: 40px, cards: 20px, input: 5px, buttons: 800px`

## Surface cues
- **Absolute Zero Canvas** `#070707`: Dominant background for the entire application and main content areas.
- **Deep Space Card** `#0d0e12`: First layer of elevated surfaces, typically for cards or content blocks.
- **Ash Grey Elevated** `#141418`: Secondary elevated surfaces, often for nested cards or modals, providing further visual separation.
- **Cyan Sparkle Feature** `#70dcd3`: Specialized elevated surfaces for highlighted features or informational blocks, introducing a distinct color accent.

## Component cues
- **Ghost Navigation Link**: Main navigation items and secondary actions.
- **Primary Pill Button**: Prominent calls to action.
- **Subtle Tag Button**: Informational tags or small interactive elements.
- **Transparent Card**: Container for content with no distinct background.
- **Elevated Dark Card**: Content container with subtle elevation from the background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
