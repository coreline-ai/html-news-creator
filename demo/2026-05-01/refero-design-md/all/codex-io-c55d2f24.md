# Codex.io - Refero Design MD

- Source: https://styles.refero.design/style/c55d2f24-deb1-44c1-9846-66a3523beb29
- Original site: https://www.codex.io
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric green on midnight grid

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#111111` | neutral | Primary text or dark surface |
| Electric Lime | `#e5ff5d` | brand | Action accent / signal color |
| Ghost Ash | `#f9f9f9` | neutral | Page background or card surface |
| Deep Graphite | `#2b2b2b` | neutral | Primary text or dark surface |
| Muted Stone | `#b7b3a2` | neutral | Border, muted text, or supporting surface |
| Light Grayscale | `#eeeeee` | neutral | Page background or card surface |
| Shadow Ink | `#000000` | neutral | Primary text or dark surface |
| Subtle Gray | `#d6d6d6` | neutral | Border, muted text, or supporting surface |
| Midtone Gray | `#6e6e6e` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#9c9c9c` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #111111;
  --ref-electric-lime: #e5ff5d;
  --ref-ghost-ash: #f9f9f9;
  --ref-deep-graphite: #2b2b2b;
  --ref-muted-stone: #b7b3a2;
  --ref-light-grayscale: #eeeeee;
  --ref-shadow-ink: #000000;
  --ref-subtle-gray: #d6d6d6;
}
```

## Typography direction
- **Neue Haas Grotesk Text**: 400, 500, 10px, 12px, 16px, 20px, 24px, 80px, 0.90, 1.00, 1.20, 1.30, 1.50, 1.73, 2.08; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `32px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `nav: 4px, cards: 12px, buttons: 4px, decorative: 20px`

## Component cues
- **Primary Action Button - Filled**: Calls to action and key interactive elements.
- **Secondary Action Button - Ghost**: Less prominent actions, often next to a primary button.
- **Navigation Link**: Main navigation items and secondary links.
- **Default Card**: Content grouping, feature display, or information containers.
- **Minimal Card**: Small information blocks, often in grids.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
