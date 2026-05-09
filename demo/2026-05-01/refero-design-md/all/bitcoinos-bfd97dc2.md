# BitcoinOS - Refero Design MD

- Source: https://styles.refero.design/style/bfd97dc2-5c12-483b-9101-ebfaf82ba83e
- Original site: https://bitcoinos.build
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark Command Center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Truffle | `#000000` | neutral | Primary text or dark surface |
| Digital Canvas | `#101010` | neutral | Primary text or dark surface |
| Ash Graphite | `#1a1a1a` | neutral | Primary text or dark surface |
| Slate Steel | `#272727` | neutral | Primary text or dark surface |
| Ghost White | `#fffafa` | neutral | Page background or card surface |
| Muted Silver | `#bababa` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-truffle: #000000;
  --ref-digital-canvas: #101010;
  --ref-ash-graphite: #1a1a1a;
  --ref-slate-steel: #272727;
  --ref-ghost-white: #fffafa;
  --ref-muted-silver: #bababa;
}
```

## Typography direction
- **Times**: 400, 16px, 1.20; substitute `serif`.
- **Kalice**: 400, 12px, 16px, 24px, 1.00, 1.40, 1.60; substitute `monospace`.
- **Review**: 700, 900, 14px, 18px, 32px, 0.75, 0.88, 1.00, 1.10; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `links: 2px, buttons: 8px, default: 16px, decorative: 48px, smallComponents: 8px`

## Component cues
- **Ghost Button**: Interactive elements with minimal visual footprint.
- **Outlined Button**: Secondary action or navigation items.
- **Filled Primary Button**: Main call to action.
- **Ghost Card**: Structural container for content without visual background.
- **Standard Card**: Content presentation with a clear visual boundary.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
