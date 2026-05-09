# Moonli - Refero Design MD

- Source: https://styles.refero.design/style/74be1036-f867-4cee-959a-a9a9129111c0
- Original site: https://moonli.me
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant green digital ledger

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Soft Cloud | `#f3f3f3` | neutral | Page background or card surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Light Steel | `#e2e2e2` | neutral | Page background or card surface |
| Muted Stone | `#757575` | neutral | Border, muted text, or supporting surface |
| Vivacious Green | `#b8ff65` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-soft-cloud: #f3f3f3;
  --ref-canvas-white: #ffffff;
  --ref-light-steel: #e2e2e2;
  --ref-muted-stone: #757575;
  --ref-vivacious-green: #b8ff65;
}
```

## Typography direction
- **DM Sans**: 400, 500, 700, 14px, 16px, 24px, 38px, 48px, 58px, 1.08, 1.13, 1.17, 1.26, 1.45, 1.50, 1.75; substitute `system-ui`.

## Spacing / shape
- Section Gap: `25px`
- Card Padding: `20px`
- Element Gap: `20px`
- Page Max Width: `1280px`
- Radius: `tags: 30px, cards: 30px, buttons: 40px`

## Component cues
- **Primary Hero Card**: Main introductory content block
- **Default Card**: General content container
- **Light Surface Card**: Secondary content container, subtle elevation
- **Navigation Link**: Top navigation items
- **Primary Navigation Button**: Call to action in navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
