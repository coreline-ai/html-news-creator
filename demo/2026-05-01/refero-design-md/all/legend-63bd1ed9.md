# Legend - Refero Design MD

- Source: https://styles.refero.design/style/63bd1ed9-b161-45fd-8734-85282bd945ec
- Original site: https://legend.xyz
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ededed` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Deep Gray | `#131313` | neutral | Primary text or dark surface |
| Medium Gray | `#949494` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#b2b2b2` | neutral | Border, muted text, or supporting surface |
| Muted Gray | `#6c6c6c` | neutral | Border, muted text, or supporting surface |
| Outline Gray | `#474747` | neutral | Border, muted text, or supporting surface |
| Button Gray | `#2d2d2d` | neutral | Primary text or dark surface |
| Background Gray | `#dedddc` | neutral | Page background or card surface |
| Accent Violet | `#8931c4` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ededed;
  --ref-ink-black: #000000;
  --ref-deep-gray: #131313;
  --ref-medium-gray: #949494;
  --ref-light-gray: #b2b2b2;
  --ref-muted-gray: #6c6c6c;
  --ref-outline-gray: #474747;
  --ref-button-gray: #2d2d2d;
}
```

## Typography direction
- **knapp**: 400, 500, 12px, 16px, 20px, 22px, 44px, 56px, 1.00, 1.10, 1.25, 1.30, 1.40, 1.50; substitute `Inter`.
- **diatypeMono**: 400, 11px, 13px, 1.00, 1.35; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `68px`
- Card Padding: `20px`
- Element Gap: `20px`
- Page Max Width: `1416px`
- Radius: `cards: 32px, buttons: 4px, general: 4px, navItems: 12px`

## Surface cues
- **Canvas White** `#ededed`: Primary page background providing a clean, bright foundation.
- **Background Gray** `#dedddc`: Subtle background panels or alternative light surfaces for layering content.
- **Deep Gray** `#131313`: Elevated card backgrounds and containers for darker content sections.
- **Button Gray** `#2d2d2d`: Used for filled interactive elements, providing a clear visual affordance.

## Component cues
- **Navigation Item**: Text link within the primary navigation bar.
- **Primary Ghost Button**: Text-only button with a transparent background.
- **Secondary Filled Button**: Contained button for secondary actions.
- **Navigation Utility Button**: Button within the utility navigation area (e.g. download button, menu icon).
- **Product Display Card**: Showcases key data or features, like a phone screen rendering.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
