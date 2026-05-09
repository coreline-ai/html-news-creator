# OpenSea - Refero Design MD

- Source: https://styles.refero.design/style/61f1902f-6da3-4af7-b046-3b08bc1377f6
- Original site: https://opensea.io
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight data console

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#080809` | neutral | Primary text or dark surface |
| Deep Graphite | `#141415` | neutral | Primary text or dark surface |
| Slate Card | `#1b1d1f` | neutral | Primary text or dark surface |
| Steel Border | `#26272d` | neutral | Primary text or dark surface |
| Soft Stone | `#34353c` | neutral | Primary text or dark surface |
| Ghost Fill | `#3c3d40` | neutral | Primary text or dark surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Silver Whisper | `#acadae` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#83c3ff` | accent | Action accent / signal color |
| Success Green | `#47bb64` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #080809;
  --ref-deep-graphite: #141415;
  --ref-slate-card: #1b1d1f;
  --ref-steel-border: #26272d;
  --ref-soft-stone: #34353c;
  --ref-ghost-fill: #3c3d40;
  --ref-white-canvas: #ffffff;
  --ref-silver-whisper: #acadae;
}
```

## Typography direction
- **gtAmerica**: 400, 500, 12px, 14px, 16px, 20px, 32px, 1.25, 1.50; substitute `Inter`.
- **gtAmericaMono**: 400, 500, 12px, 14px, 16px, 1.00, 1.25, 1.50; substitute `JetBrains Mono`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `8px`
- Page Max Width: `1325px`
- Radius: `cards: 8px, buttons: 4px, default: 4px`

## Component cues
- **Ghost Button**: Interactive elements for secondary actions or navigation.
- **Filled Neutral Button**: Tertiary actions or category filters.
- **White Text Button (Ghost)**: Prominent ghost actions or tab activators.
- **Inset Border Card**: Collection or asset display cards.
- **Shadowed Card**: Elevated information or interactive cards.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
