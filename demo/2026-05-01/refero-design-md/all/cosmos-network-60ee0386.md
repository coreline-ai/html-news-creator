# Cosmos Network - Refero Design MD

- Source: https://styles.refero.design/style/60ee0386-cfad-409a-8310-762bfc2e4816
- Original site: https://cosmos.network
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Ledger, sharp and precise

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Abyss | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Iron Slate | `#333333` | neutral | Primary text or dark surface |
| Faded Steel | `#807f7f` | neutral | Border, muted text, or supporting surface |
| Card Dark | `#1e1f20` | neutral | Primary text or dark surface |
| Frost | `#f1f4f4` | neutral | Page background or card surface |
| Interface Green | `#22e2a8` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-abyss: #000000;
  --ref-ghost-white: #ffffff;
  --ref-iron-slate: #333333;
  --ref-faded-steel: #807f7f;
  --ref-card-dark: #1e1f20;
  --ref-frost: #f1f4f4;
  --ref-interface-green: #22e2a8;
}
```

## Typography direction
- **The Future**: 400, 12px, 14px, 16px, 24px, 32px, 36px, 60px, 1.13, 1.25, 1.33, 1.43, 1.50, 1.60, 1.63; substitute `Inter, Open Sans`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `20px`
- Element Gap: `16px`
- Radius: `cards: 20px, images: 10px, buttons: 0px, sections: 16px`

## Surface cues
- **Base Canvas** `#000000`: Primary page background for all sections.
- **Content Card** `#1e1f20`: Background for feature cards and secondary content blocks, slightly elevated from the base canvas.

## Component cues
- **Navigation Link**: Primary navigation item
- **Ghost Button**: Secondary action or link
- **Feature Card (Dark)**: Container for secondary content like customer showcases.
- **Header Card (Dark, Large)**: Prominent content container for key sections.
- **Default Input Field**: Standard input for user data.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
