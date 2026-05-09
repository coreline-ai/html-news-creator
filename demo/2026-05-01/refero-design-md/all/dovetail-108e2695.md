# Dovetail - Refero Design MD

- Source: https://styles.refero.design/style/108e2695-6970-47d5-b5b0-eea8fc34e048
- Original site: https://dovetail.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#0a0a0a` | neutral | Primary text or dark surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Off-Black | `#141414` | neutral | Primary text or dark surface |
| Dark Frost | `#1e1e1e` | neutral | Primary text or dark surface |
| Medium Gray | `#313131` | neutral | Primary text or dark surface |
| Light Gray | `#454545` | neutral | Border, muted text, or supporting surface |
| Dim Gray | `#7c7c7c` | neutral | Border, muted text, or supporting surface |
| Silver Dust | `#a7a7a7` | neutral | Border, muted text, or supporting surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Data Blue | `#6798ff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-charcoal: #0a0a0a;
  --ref-pitch-black: #000000;
  --ref-off-black: #141414;
  --ref-dark-frost: #1e1e1e;
  --ref-medium-gray: #313131;
  --ref-light-gray: #454545;
  --ref-dim-gray: #7c7c7c;
  --ref-silver-dust: #a7a7a7;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 14px, 16px, 20px, 24px, 40px, 56px, 64px, 1.13, 1.14, 1.20, 1.29, 1.33, 1.40, 1.50, 1.57; substitute `System UI`.
- **JetBrains Mono**: 400, 12px, 14px, 1.00, 1.40; substitute `Fira Code`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 8px, images: 8px, buttons: 8px, circularElements: 66px`

## Surface cues
- **Midnight Charcoal** `#0a0a0a`: Primary page background and recessed areas.
- **Off-Black** `#141414`: Background for main content blocks and slightly-raised sections.
- **Dark Frost** `#1e1e1`: Background for interactive elements, secondary buttons, and some data cards.

## Component cues
- **Ghost Navigation Button**: Main navigation and secondary actions in headers/footers.
- **Filled Secondary Button**: Standard secondary call-to-action or functional button within dark UIs.
- **Filled Primary Button**: Key call-to-action button, often guiding user flow.
- **Outlined Tertiary Button**: Less prominent interactive elements, often in data displays or advanced controls.
- **Circular Card Background**: Used as a distinctive visual element or container, possibly for testimonials or key metrics.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
