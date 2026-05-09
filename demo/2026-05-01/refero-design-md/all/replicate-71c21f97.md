# Replicate - Refero Design MD

- Source: https://styles.refero.design/style/71c21f97-ba85-4439-b259-198a66f4b3d2
- Original site: https://replicate.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neon Gradient Playground. The site feels like an interactive playground built on a fluctuating neon energy field.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#202020` | neutral | Primary text or dark surface |
| Alabaster | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#646464` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#bfbfbf` | neutral | Border, muted text, or supporting surface |
| Whisper White | `#f9f9f9` | neutral | Page background or card surface |
| Outline Gray | `#d9d9d9` | neutral | Page background or card surface |
| Blackhole | `#000000` | neutral | Primary text or dark surface |
| Cosmic Candy | `#ea2804` | brand | Action accent / signal color |
| Deep Space Blue | `#032f62` | brand | Action accent / signal color |
| Sunset Burst | `#dd4425` | brand | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #202020;
  --ref-alabaster: #ffffff;
  --ref-graphite: #646464;
  --ref-silver-mist: #bfbfbf;
  --ref-whisper-white: #f9f9f9;
  --ref-outline-gray: #d9d9d9;
  --ref-blackhole: #000000;
  --ref-cosmic-candy: #ea2804;
}
```

## Typography direction
- **rb-freigeist-neue**: 400, 600, 700, 16px, 30px, 48px, 72px, 128px, 1.00, 1.20, 1.50; substitute `Montserrat`.
- **basier-square**: 400, 600, 12px, 14px, 16px, 18px, 20px, 24px, 29px, 1.11, 1.33, 1.40, 1.43, 1.50, 1.56; substitute `Inter`.
- **jetbrains-mono**: 400, 10px, 11px, 14px, 16px, 1.43, 1.50; substitute `Inconsolata`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 0px, badges: 9999px, buttons: 9999px, defaults: 0px`

## Component cues
- **Category Filter Pills**: Reference component style.
- **Model Cards Grid**: Reference component style.
- **Code Block with Tabs**: Reference component style.
- **Primary Filled Button**: Call to action.
- **Standard Ghost Button**: Secondary navigation and non-critical actions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
