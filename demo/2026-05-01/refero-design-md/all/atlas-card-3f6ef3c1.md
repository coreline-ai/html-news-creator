# Atlas Card - Refero Design MD

- Source: https://styles.refero.design/style/3f6ef3c1-f98f-4cd9-bdf0-545059758705
- Original site: https://atlascard.com
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Velvet Vault – rich, dark surfaces punctuated by a single, deep gem-toned light.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Charcoal Grey | `#272727` | neutral | Primary text or dark surface |
| Dark Slate | `#333333` | neutral | Primary text or dark surface |
| Deep Graphite | `#3d3d3d` | neutral | Primary text or dark surface |
| Bright Silver | `#f8f8f8` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Cadet Grey | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Mid-Grey | `#808080` | neutral | Border, muted text, or supporting surface |
| Atlas Violet | `#001391` | brand | Action accent / signal color |
| Dark Gradient | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-charcoal-grey: #272727;
  --ref-dark-slate: #333333;
  --ref-deep-graphite: #3d3d3d;
  --ref-bright-silver: #f8f8f8;
  --ref-pure-white: #ffffff;
  --ref-cadet-grey: #cccccc;
  --ref-mid-grey: #808080;
}
```

## Typography direction
- **Sequel Sans Headline Book**: 400, 700, 16px, 23px, 24px, 28px, 1.17, 1.30, 1.40; substitute `Inter, sans-serif`.
- **Sequel Sans Book**: 400, 17px, 1.24; substitute `Inter, sans-serif`.
- **ApercuMono Pro Medium**: 400, 12px, 15px, 1.40, 1.67; substitute `IBM Plex Mono, monospace`.

## Spacing / shape
- Section Gap: `48-64px`
- Card Padding: `16px`
- Element Gap: `8-32px`
- Radius: `inputs: 8px, default: 4px, buttons-pill: 128px, buttons-square: 18px, buttons-outline: 24px`

## Component cues
- **Request Invite CTA Block**: Reference component style.
- **Ticker Marquee Banner**: Reference component style.
- **Button Group Showcase**: Reference component style.
- **Primary Action Pill Button**: Call to action
- **Ghost Feature Button**: Secondary action in content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
