# Balsa - Refero Design MD

- Source: https://styles.refero.design/style/ebbfbc6a-988b-4f33-b261-d431b2327545
- Original site: https://www.balsa.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Ice | `#f7f7f7` | neutral | Page background or card surface |
| Surface White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#313131` | neutral | Primary text or dark surface |
| Storm Gray | `#686868` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#bbbbbb` | neutral | Border, muted text, or supporting surface |
| Purple Haze | `#914db2` | accent | Action accent / signal color |
| Goldenrod | `#ffb700` | accent | Action accent / signal color |
| Midnight Ink Blue | `#003399` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-ice: #f7f7f7;
  --ref-surface-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite: #313131;
  --ref-storm-gray: #686868;
  --ref-silver-mist: #bbbbbb;
  --ref-purple-haze: #914db2;
  --ref-goldenrod: #ffb700;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `system-ui`.
- **Van Condensed Pro Bold**: 400, 24px, 32px, 48px, 1.20, 1.50; substitute `Bebas Neue`.
- **Inter**: 400, 600, 700, 11px, 14px, 16px, 1.18, 1.20, 1.29, 1.30, 1.43, 1.50, 1.64, 1.73; substitute `Inter`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `tags: 16px, cards: 12px, buttons: 6px, minimal: 1px`

## Surface cues
- **Canvas Ice** `#f7f7f7`: Base page background
- **Surface White** `#ffffff`: Primary interactive cards, content blocks, and UI elements

## Component cues
- **Primary Filled Button**: Main call-to-action
- **Outline Accent Button (Midnight Ink Blue)**: Secondary call-to-action or informational link
- **Base Card (No Shadow)**: Content grouping, pricing tiers in neutral state
- **Elevated Content Card**: Prominent content blocks, feature descriptions
- **Callout Card (Goldenrod)**: Highlighting key information, warnings, or tips

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
