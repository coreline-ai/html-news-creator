# Uniswap - Refero Design MD

- Source: https://styles.refero.design/style/e5b95270-9148-417a-89c6-32138d83a251
- Original site: https://uniswap.org
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Fuzzy Neon Playground. Crisp white UI elements float above a swirling background of blurred, vibrant color.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#131313` | neutral | Primary text or dark surface |
| Dim Gray | `#222222` | neutral | Primary text or dark surface |
| Ash Gray | `#6a6a6a` | neutral | Border, muted text, or supporting surface |
| Silver Tone | `#acacac` | neutral | Border, muted text, or supporting surface |
| Off White | `#f2f2f2` | neutral | Page background or card surface |
| Techno Pink | `#ff37c7` | brand | Action accent / signal color |
| Amethyst Glow | `#8251fb` | accent | Action accent / signal color |
| Ember Spark | `#ff4d00` | accent | Action accent / signal color |
| Hot Magenta | `#f50db4` | accent | Action accent / signal color |

```css
:root {
  --ref-cloud-white: #ffffff;
  --ref-ink-black: #131313;
  --ref-dim-gray: #222222;
  --ref-ash-gray: #6a6a6a;
  --ref-silver-tone: #acacac;
  --ref-off-white: #f2f2f2;
  --ref-techno-pink: #ff37c7;
  --ref-amethyst-glow: #8251fb;
}
```

## Typography direction
- **Basel**: 400, 485, 500, 535, 12px, 13px, 14px, 16px, 18px, 24px, 36px, 52px, 64px, 0.96, 1.00, 1.11, 1.15, 1.19, 1.20, 1.25, 1.30, 1.33, 1.49; substitute `Inter`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 20px, input: 0px, buttons: 999999px, default: 12px`

## Component cues
- **Swap Interface Card**: Reference component style.
- **Protocol Stats Card**: Reference component style.
- **Button Group Showcase**: Reference component style.
- **Primary Action Button**: Filled button
- **Secondary Ghost Button**: Outlined/Ghost button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
