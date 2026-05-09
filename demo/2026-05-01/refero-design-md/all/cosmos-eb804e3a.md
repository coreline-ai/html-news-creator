# Cosmos - Refero Design MD

- Source: https://styles.refero.design/style/eb804e3a-1b75-446c-8374-114bbabaf0cd
- Original site: https://cosmos.so
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Wall on White Marble. Content is framed by generous whitespace against a pristine, quiet backdrop, emphasizing individual elements.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0d0d0d` | brand | Action accent / signal color |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Fossil | `#f7f5f3` | neutral | Page background or card surface |
| Dusty Ash | `#6e6a69` | neutral | Border, muted text, or supporting surface |
| Pewter | `#9a9796` | neutral | Border, muted text, or supporting surface |
| Harvest Gold | `#eac7a0` | accent | Action accent / signal color |
| Cardinal Red | `#bc361b` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #0d0d0d;
  --ref-paper-white: #ffffff;
  --ref-fossil: #f7f5f3;
  --ref-dusty-ash: #6e6a69;
  --ref-pewter: #9a9796;
  --ref-harvest-gold: #eac7a0;
  --ref-cardinal-red: #bc361b;
}
```

## Typography direction
- **cosmosOracle**: 350, 400, 500, 14px, 15px, 16px, 18px, 24px, 26px, 33px, 38px, 58px, 66px, 74px, 0.80, 1.00, 1.06, 1.08, 1.10, 1.20, 1.25, 1.29, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `100-180px`
- Element Gap: `4px`
- Radius: `buttons: 1.67772e+07px, default: 16px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Search Bar**: Reference component style.
- **AI Content Tooltip Card**: Reference component style.
- **Ghost Button**: Secondary action
- **Subtle Link Button**: Tertiary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
