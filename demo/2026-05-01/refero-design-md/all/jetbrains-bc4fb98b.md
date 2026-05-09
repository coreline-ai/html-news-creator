# JetBrains - Refero Design MD

- Source: https://styles.refero.design/style/bc4fb98b-37ec-480a-b7a9-acd197cbebb9
- Original site: https://jetbrains.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neon nebula on obsidian — a black-ground page where violet-blue gradients bloom upward like deep-space imagery, punctuated by hot-pink neon and per-product chromatic icon light.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian Ground | `#000000` | neutral | Primary text or dark surface |
| Deep Charcoal | `#19191c` | neutral | Primary text or dark surface |
| Graphite | `#343434` | neutral | Primary text or dark surface |
| Iron | `#474749` | neutral | Border, muted text, or supporting surface |
| Ash | `#757577` | neutral | Border, muted text, or supporting surface |
| Silver | `#a3a3a4` | neutral | Border, muted text, or supporting surface |
| Fog | `#bababb` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Electric Blue | `#18a3fa` | brand | Action accent / signal color |
| Violet Pulse | `#7b61ff` | brand | Action accent / signal color |

```css
:root {
  --ref-obsidian-ground: #000000;
  --ref-deep-charcoal: #19191c;
  --ref-graphite: #343434;
  --ref-iron: #474749;
  --ref-ash: #757577;
  --ref-silver: #a3a3a4;
  --ref-fog: #bababb;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **JetBrains Sans**: 300, 400, 500, 600, 13px, 16px, 20px, 29px, 35px, 43px, 72px, 79px, 0.90–1.54 (tighter at larger sizes: 0.90 at display, 1.50–1.54 at body); substitute `Inter, Plus Jakarta Sans`.

## Spacing / shape
- Section Gap: `80-120px`
- Card Padding: `24px`
- Element Gap: `8-16px`
- Page Max Width: `1280px`
- Radius: `cards: 24px, badges: 4-6px, images: 16px, modals: 24px, buttons: 20-26px`

## Surface cues
- **Void** `#000000`: Absolute page background — the black base from which all gradients emerge
- **Deep Charcoal** `#19191c`: Navigation bar, footer — surfaces that need to sit above the background but below content cards
- **Violet Glass** `#2e106a`: Translucent violet card fills (rgba(90,31,208,0.3)) — feature announcement cards, business section panels
- **Pink Glass** `#45173a`: Translucent pink card fills (rgba(243,17,180,0.2)) — highlight feature cards for specific products

## Component cues
- **Audience Segmentation Tab Row + Business Feature Card**: Reference component style.
- **Feature Announcement Card with IDE Grid**: Reference component style.
- **Button Group — Primary, Violet Deep, and Ghost**: Reference component style.
- **Hero CTA Button — Primary Dark**: Main call-to-action on hero sections
- **CTA Button — Violet Deep**: Secondary prominent CTA on feature cards

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
