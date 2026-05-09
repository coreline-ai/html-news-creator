# San Rita - Refero Design MD

- Source: https://styles.refero.design/style/f6b396e6-0ad6-402e-9ab9-0034df0d204d
- Original site: https://sanrita.ca/about
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Field Notes & Radio Signals — a minimalist topographic map combined with stark, technical typography.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Canopy | `#161b13` | neutral | Primary text or dark surface |
| Terrain Shadow | `#2d3329` | neutral | Primary text or dark surface |
| Paper White | `#dde2e4` | neutral | Page background or card surface |
| Earth Gray | `#84907f` | brand | Action accent / signal color |
| Adventure Chartreuse | `#e2ffcc` | accent | Action accent / signal color |
| Headline Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-forest-canopy: #161b13;
  --ref-terrain-shadow: #2d3329;
  --ref-paper-white: #dde2e4;
  --ref-earth-gray: #84907f;
  --ref-adventure-chartreuse: #e2ffcc;
  --ref-headline-black: #000000;
}
```

## Typography direction
- **F37stout**: 400, 40px, 48px, 366px, 0.90; substitute `Bebas Neue`.
- **mono**: 400, 700, 10px, 12px, 16px, 1.20; substitute `Space Mono`.
- **Times New Roman**: 400, 16px, 1.20; substitute `Times New Roman`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `12px`
- Radius: `default: 0px`

## Component cues
- **Navigation Button**: Reference component style.
- **Origin Stat Block**: Reference component style.
- **Photo Scrapbook Cards**: Reference component style.
- **Navigation Button**: Primary Call to Action in header
- **Inline Link**: Interactive text link

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
