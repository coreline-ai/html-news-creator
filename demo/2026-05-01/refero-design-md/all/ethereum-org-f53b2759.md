# ethereum.org - Refero Design MD

- Source: https://styles.refero.design/style/f53b2759-5b4a-4509-9311-51ab74238326
- Original site: https://ethereum.org
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Abstract digital canvas, illuminated.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#121212` | neutral | Primary text or dark surface |
| Ash Gray | `#616161` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#cfcfcf` | neutral | Border, muted text, or supporting surface |
| Ghost White | `#f7f7f7` | neutral | Page background or card surface |
| Lavender Bloom | `#ece0ff` | brand | Action accent / signal color |
| Electric Violet | `#6c24e0` | brand | Action accent / signal color |
| Fuchsia Burst | `#f60e9d` | accent | Action accent / signal color |
| Indigo Orb | `#3d4ceb` | accent | Action accent / signal color |
| Emerald Spark | `#0f9972` | accent | Action accent / signal color |

```css
:root {
  --ref-cloud-white: #ffffff;
  --ref-graphite: #121212;
  --ref-ash-gray: #616161;
  --ref-silver-mist: #cfcfcf;
  --ref-ghost-white: #f7f7f7;
  --ref-lavender-bloom: #ece0ff;
  --ref-electric-violet: #6c24e0;
  --ref-fuchsia-burst: #f60e9d;
}
```

## Typography direction
- **Inter**: 400, 700, 900, 10px, 14px, 16px, 18px, 20px, 24px, 30px, 35px, 36px, 48px, 60px, 64px, 1.00, 1.10, 1.20, 1.30, 1.40, 1.60, 2.00; substitute `system-ui, sans-serif`.
- **IBM Plex Mono**: 400, 14px, 16px, 1.60; substitute `Menlo, Consolas, monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `pill: 9999px, cards: 0px, large: 32px, links: 16px, buttons: 8px, default: 4px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Popular Topics Cards**: Reference component style.
- **Feature Section Card — Network Badge**: Reference component style.
- **Ghost Button - Default**: Interactive element
- **Ghost Button - Secondary**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
