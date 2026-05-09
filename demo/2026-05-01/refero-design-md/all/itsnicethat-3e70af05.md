# Itsnicethat - Refero Design MD

- Source: https://styles.refero.design/style/3e70af05-a07f-4c11-98ca-6ecb4765e967
- Original site: https://itsnicethat.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Artist's sketchbook, bursting with vibrant scraps and precise typography.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Black Ink | `#2b2b2b` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Frost Gray | `#f0efef` | neutral | Page background or card surface |
| Medium Gray | `#676767` | neutral | Border, muted text, or supporting surface |
| Muted Taupe | `#faead9` | neutral | Page background or card surface |
| Electric Purple | `#8147ff` | brand | Action accent / signal color |
| Sunshine Yellow | `#ffd519` | accent | Action accent / signal color |
| Deep Indigo | `#6219ff` | accent | Action accent / signal color |
| Risograph Gradient | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-black-ink: #2b2b2b;
  --ref-pure-white: #ffffff;
  --ref-frost-gray: #f0efef;
  --ref-medium-gray: #676767;
  --ref-muted-taupe: #faead9;
  --ref-electric-purple: #8147ff;
  --ref-sunshine-yellow: #ffd519;
  --ref-deep-indigo: #6219ff;
}
```

## Typography direction
- **Bradford**: 400, 500, 11px, 15px, 17px, 1.15, 1.47, 1.53, 2.27; substitute `Georgia`.
- **LabilVariable**: 400, 11px, 13px, 15px, 18px, 25px, 40px, 1.20, 1.28, 1.40, 1.45, 1.46, 1.73; substitute `Open Sans`.
- **Labil**: 400, 500, 11px, 13px, 17px, 1.40, 1.45, 1.47; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `10px`
- Page Max Width: `1200px`
- Radius: `buttons: 75px, default: 0px`

## Component cues
- **The Nice Feed — Article Feed Strip**: Reference component style.
- **Article Card with Tags**: Reference component style.
- **Floating Navigation Bar**: Reference component style.
- **Primary Ghost Button**: Call to action, navigation
- **Category Label Button**: Informational grouping, filtering

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
