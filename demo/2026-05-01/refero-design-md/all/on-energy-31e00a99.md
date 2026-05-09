# ON.energy - Refero Design MD

- Source: https://styles.refero.design/style/31e00a99-6946-4f07-829a-b0904a39a20d
- Original site: https://www.on.energy
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Industrial Luxe on a Dark Stage. The UI feels like a high-tech data center interior, where essential information is presented with precision and a focused burst of energy.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Steel | `#000000` | neutral | Primary text or dark surface |
| Data Center Graphite | `#202020` | neutral | Primary text or dark surface |
| Industrial Silver | `#afafaf` | neutral | Border, muted text, or supporting surface |
| Screen White | `#eeeeee` | neutral | Page background or card surface |
| Electric Yellow | `#fff313` | brand | Action accent / signal color |
| Asphalt Gray | `#4b4b4b` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-steel: #000000;
  --ref-data-center-graphite: #202020;
  --ref-industrial-silver: #afafaf;
  --ref-screen-white: #eeeeee;
  --ref-electric-yellow: #fff313;
  --ref-asphalt-gray: #4b4b4b;
}
```

## Typography direction
- **Univers Next Pro**: 300, 400, 10px, 12px, 14px, 16px, 24px, 36px, 64px, 1.00, 1.13, 1.17, 1.20, 1.38; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Element Gap: `16px`
- Page Max Width: `1350px`
- Radius: `cards: 9px, buttons: 6px, default: 6px, specialButton: 16px`

## Component cues
- **Electric CTA Button Group**: Reference component style.
- **Discover AI UPS — Overlay Card**: Reference component style.
- **Latest News Cards**: Reference component style.
- **Dark Ghost Button**: Secondary interactive elements within dark sections.
- **Electric CTA Button**: Primary calls to action.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
