# Odin's Crow - Refero Design MD

- Source: https://styles.refero.design/style/65c01b0f-7ae5-42ff-ad5b-162bbdce8e01
- Original site: https://odins-crow.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist ledger, sharp lines

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Bone | `#e5e7eb` | neutral | Page background or card surface |
| Carbon Ink | `#2b2b2b` | neutral | Primary text or dark surface |
| Faded Stone | `#e5d5c3` | neutral | Border, muted text, or supporting surface |
| Pale Driftwood | `#cdc0b1` | neutral | Border, muted text, or supporting surface |
| Cloud Gray | `#c9c8c9` | neutral | Border, muted text, or supporting surface |
| Muted Ash | `#afa7a2` | neutral | Border, muted text, or supporting surface |
| Graphite Line | `#535251` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-bone: #e5e7eb;
  --ref-carbon-ink: #2b2b2b;
  --ref-faded-stone: #e5d5c3;
  --ref-pale-driftwood: #cdc0b1;
  --ref-cloud-gray: #c9c8c9;
  --ref-muted-ash: #afa7a2;
  --ref-graphite-line: #535251;
}
```

## Typography direction
- **Plain**: 400, 700, 10px, 16px, 20px, 27px, 34px, 36px, 42px, 60px, 187px, 190px, 1.00, 1.08, 1.11, 1.25, 1.40, 1.50, 2.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `22px`
- Element Gap: `20px`
- Radius: `none: 0px`

## Component cues
- **Ghost Button**: Interactive element
- **Underlined Input Field**: Form input
- **Minimal Badge**: Decorative/Informational Tag

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
