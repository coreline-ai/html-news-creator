# Electronic Materials Office® - Refero Design MD

- Source: https://styles.refero.design/style/297f65f7-0fbd-4521-ab91-a5f6e17175d9
- Original site: https://electronicmaterialsoffice.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep charcoal precision

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#202020` | neutral | Primary text or dark surface |
| Vanilla Ice | `#ffffff` | neutral | Page background or card surface |
| Ash | `#9d9d9d` | neutral | Border, muted text, or supporting surface |
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Power Orange | `#f45500` | brand | Action accent / signal color |
| Electric Violet | `#9e9eff` | accent | Action accent / signal color |
| Dark Umber | `#933400` | accent | Action accent / signal color |

```css
:root {
  --ref-carbon: #202020;
  --ref-vanilla-ice: #ffffff;
  --ref-ash: #9d9d9d;
  --ref-obsidian: #000000;
  --ref-power-orange: #f45500;
  --ref-electric-violet: #9e9eff;
  --ref-dark-umber: #933400;
}
```

## Typography direction
- **Times**: 400, 16px, 1.20; substitute `Times New Roman`.
- **GT-Flexa**: 200, 400, 16px, 24px, 26px, 28px, 42px, 68px, 86px, 1.00, 1.06, 1.08, 1.14, 1.20, 1.31, 1.33; substitute `Montserrat`.
- **Tobias-light**: 400, 32px, 42px, 1.20; substitute `Lato`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `4px`
- Radius: `cards: 20px, buttons: 16px, elements: 20px`

## Surface cues
- **Carbon Base** `#202020`: Primary page background and darker card surface.
- **Vanilla Ice Overlay** `#FFFFFF`: Highlight surface for light-themed cards or interactive components, offering stark contrast.

## Component cues
- **Primary Action Button (Pre-order)**: Main call-to-action button, driving conversions.
- **Play Film Button**: Secondary action button, typically embedded in rich media sections.
- **Compact Accent Button**: Small, functional button for specific actions like 'Pre-order' in the header.
- **Product Feature Card**: Displays key features or specifications with an associated visual.
- **Transparent Card**: Used for content overlays or sections that should blend with the background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
