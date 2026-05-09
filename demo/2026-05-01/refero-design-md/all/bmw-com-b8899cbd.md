# BMW.com - Refero Design MD

- Source: https://styles.refero.design/style/b8899cbd-e2ca-4069-83cf-d8f8b0d71100
- Original site: https://bmw.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precision-engineered monochrome luxury; every detail is intentional, nothing is superfluous.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian | `#262626` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Graphite Grey | `#bbbbbb` | neutral | Border, muted text, or supporting surface |
| Frost | `#f1f1f1` | neutral | Page background or card surface |
| Deep Space | `#262626` | neutral | Primary text or dark surface |
| Electric Blue | `#1c69d4` | accent | Action accent / signal color |

```css
:root {
  --ref-obsidian: #262626;
  --ref-canvas-white: #ffffff;
  --ref-graphite-grey: #bbbbbb;
  --ref-frost: #f1f1f1;
  --ref-deep-space: #262626;
  --ref-electric-blue: #1c69d4;
}
```

## Typography direction
- **BMWTypeNextLatin**: 400, 700, 900, 16px, 18px, 1.15, 1.20, 1.30, 1.60, 1.63; substitute `Open Sans`.
- **BMWTypeNextLatin Light**: 300, 60px, 1.30; substitute `Open Sans Light`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `buttons: 0px, default: 0px`

## Component cues
- **CTA Link Button — 'Find your BMW'**: Reference component style.
- **Language Selector Bar**: Reference component style.
- **Footer Link Columns**: Reference component style.
- **Text Link Button**: Primary Call to Action
- **Navigation Link**: Primary Navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
