# Base - Refero Design MD

- Source: https://styles.refero.design/style/530eb4cf-7e75-4833-95c9-746818050db7
- Original site: https://www.base.org
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital blueprint, on-chain precision.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Haze Gray | `#f2f2f2` | neutral | Page background or card surface |
| Twilight Graphite | `#323232` | neutral | Primary text or dark surface |
| Muted Ash | `#999999` | neutral | Border, muted text, or supporting surface |
| Slate Mist | `#b1b7c3` | neutral | Border, muted text, or supporting surface |
| Vivid Cobalt | `#0000ff` | brand | Action accent / signal color |
| Subtle Granite | `#717886` | accent | Action accent / signal color |
| Emerald Green | `#098551` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-haze-gray: #f2f2f2;
  --ref-twilight-graphite: #323232;
  --ref-muted-ash: #999999;
  --ref-slate-mist: #b1b7c3;
  --ref-vivid-cobalt: #0000ff;
  --ref-subtle-granite: #717886;
}
```

## Typography direction
- **doto**: 400, 700, 16px, 115px, 0.70, 1.50; substitute `Montserrat`.
- **coinbaseSans**: 400, 500, 12px, 14px, 15px, 16px, 32px, 80px, 110px, 0.70, 1.00, 1.13, 1.14, 1.30, 1.33, 1.50; substitute `Inter`.
- **coinbaseDisplay**: 400, 14px, 16px, 1.14, 1.43, 1.50; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `4px`
- Page Max Width: `1128px`
- Radius: `small: 2px, default: 8px`

## Component cues
- **Ghost Navigation Item**: Primary navigation links in the sidebar
- **Filled Primary Button**: Main call-to-action button
- **Outlined Secondary Button**: Secondary or alternative actions
- **Informational Card**: Cards displaying product features or statistics

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
