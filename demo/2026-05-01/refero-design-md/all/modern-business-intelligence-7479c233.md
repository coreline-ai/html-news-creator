# Modern Business Intelligence - Refero Design MD

- Source: https://styles.refero.design/style/7479c233-6fee-468b-af95-9169d01a293e
- Original site: https://mode.com
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Forest Data Lab

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Canvas | `#043f2e` | brand | Action accent / signal color |
| Paper White | `#eef2e3` | neutral | Page background or card surface |
| Data Highlight | `#c8f169` | brand | Action accent / signal color |
| Chartreuse Accent | `#78c51c` | brand | Action accent / signal color |
| Deep Green Card | `#2a6f2b` | brand | Action accent / signal color |
| Black Ink | `#000000` | neutral | Primary text or dark surface |
| Pure White | `#fcfcfc` | neutral | Page background or card surface |
| Deep Gray Text | `#242423` | neutral | Primary text or dark surface |
| Rose Tint (Decorative) | `#ffbbbe` | accent | Action accent / signal color |
| Lavender Tint (Decorative) | `#cecafa` | accent | Action accent / signal color |

```css
:root {
  --ref-forest-canvas: #043f2e;
  --ref-paper-white: #eef2e3;
  --ref-data-highlight: #c8f169;
  --ref-chartreuse-accent: #78c51c;
  --ref-deep-green-card: #2a6f2b;
  --ref-black-ink: #000000;
  --ref-pure-white: #fcfcfc;
  --ref-deep-gray-text: #242423;
}
```

## Typography direction
- **Times**: 400, 16px, 1.20; substitute `Times New Roman`.
- **Grenette**: 400, 16px, 36px, 56px, 70px, 72px, 96px, 0.90, 1.10, 1.20, 1.31; substitute `Georgia`.
- **Graphik**: 400, 500, 600, 12px, 14px, 16px, 18px, 22px, 36px, 1.00, 1.03, 1.10, 1.18, 1.20, 1.30, 1.44; substitute `Inter`.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `32px`
- Element Gap: `12px`
- Radius: `cards: 16px, links: 4px, blocks: 16px, buttons: 16px`

## Surface cues
- **Forest Canvas** `#043f2`: Primary page background, providing a deep, rich foundation for the UI.
- **Paper White** `#eef2e3`: Background for secondary containers, navigation, and sections that require higher contrast against text.
- **Data Highlight** `#c8f169`: Elevated background for interactive elements and prominent textual blocks, bringing elements to the foreground with a vibrant pop.

## Component cues
- **Primary Highlight Button**: Call to action button
- **Outlined Text Button**: Secondary action button for ghost controls or minimal interaction
- **Secondary Ghost Button**: Outlined button for less prominent actions
- **Navigation Link Button**: Navigation items within headers
- **Header Highlight Card**: Display critical metrics or features in the hero section

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
