# Ventriloc - Refero Design MD

- Source: https://styles.refero.design/style/f99aca3e-5289-4595-a7cc-77a72052f4b8
- Original site: https://ventriloc.ca/en
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Analytical architecture on a clean canvas

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#202020` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Slate Mist | `#efefef` | neutral | Page background or card surface |
| Cloud Whisper | `#f5f5f5` | neutral | Page background or card surface |
| Warm Ivory | `#ebe6dd` | neutral | Page background or card surface |
| Dark Shale | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Silver Ash | `#828282` | neutral | Border, muted text, or supporting surface |
| Light Pearl | `#e8e8e8` | neutral | Page background or card surface |
| Sunset Orange | `#ff682c` | accent | Action accent / signal color |
| Data Gold | `#816729` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #202020;
  --ref-canvas-white: #ffffff;
  --ref-slate-mist: #efefef;
  --ref-cloud-whisper: #f5f5f5;
  --ref-warm-ivory: #ebe6dd;
  --ref-dark-shale: #4d4d4d;
  --ref-silver-ash: #828282;
  --ref-light-pearl: #e8e8e8;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 12px, 13px, 14px, 15px, 16px, 18px, 1.15, 1.20, 1.25, 1.33, 1.38, 1.43, 1.50; substitute `system-ui`.
- **PolySans**: 400, 12px, 13px, 16px, 32px, 40px, 66px, 0.91, 1.00, 1.13, 1.19, 1.20, 1.38; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `40px`
- Element Gap: `20px`
- Radius: `cards: 8px, large: 20px, inputs: 20px, avatars: 200px, buttons: 20px, default: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Cloud Whisper** `#f5f5f5`: Lightest card backgrounds, very subtle background shifts
- **Slate Mist** `#efefef`: Primary card backgrounds, distinct content containers
- **Warm Ivory** `#ebe6dd`: Alternative subtle background for visual separation

## Component cues
- **Standard Nav Link**: Navigation item within headers and footers.
- **Muted Nav Link**: Navigation item, typically for less prominent sections or inactive states.
- **Primary Ghost Button**: Call to action, typically in sections with high visual contrast.
- **Secondary Ghost Button**: Discreet calls to action or secondary actions.
- **Highlight Card**: Information display, often for data visualizations or key summaries.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
