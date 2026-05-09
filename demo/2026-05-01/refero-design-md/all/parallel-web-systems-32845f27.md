# Parallel Web Systems - Refero Design MD

- Source: https://styles.refero.design/style/32845f27-6b24-48be-af25-8e664f826b30
- Original site: https://parallel.ai
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint; Grid-based precision with sparse, functional color accents.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Smoke Gray | `#f6f6f6` | neutral | Page background or card surface |
| Whisper Gray | `#eeeeee` | neutral | Page background or card surface |
| Light Concrete | `#e5e5e5` | neutral | Page background or card surface |
| Medium Ash | `#858483` | neutral | Border, muted text, or supporting surface |
| Charcoal Black | `#181818` | neutral | Primary text or dark surface |
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Ignite Orange | `#fb631b` | brand | Action accent / signal color |
| Sky Blueprint | `#0d6ea5` | brand | Action accent / signal color |
| Ocean Tint | `#6fa2e8` | brand | Action accent / signal color |

```css
:root {
  --ref-cloud-white: #ffffff;
  --ref-smoke-gray: #f6f6f6;
  --ref-whisper-gray: #eeeeee;
  --ref-light-concrete: #e5e5e5;
  --ref-medium-ash: #858483;
  --ref-charcoal-black: #181818;
  --ref-obsidian: #000000;
  --ref-ignite-orange: #fb631b;
}
```

## Typography direction
- **gerstnerProgramm**: 400, 500, 11px, 13px, 14px, 16px, 26px, 36px, 1.11, 1.23, 1.50; substitute `Inter`.
- **ftSystemMono**: 400, 500, 10px, 11px, 12px, 13px, 14px, 16px, 1.00, 1.23, 1.33, 1.50; substitute `Roboto Mono`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `8px`
- Element Gap: `8px`
- Page Max Width: `1600px`
- Radius: `buttons: 4px, default: 2px, card_large: 8px, card_small: 4px`

## Component cues
- **Button Group**: Reference component style.
- **Feature Cards Grid**: Reference component style.
- **Announcement Banner + Status Bar**: Reference component style.
- **Secondary Ghost Button**: Interactive element
- **Neutral Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
