# Fiasco - Refero Design MD

- Source: https://styles.refero.design/style/ef73c742-1c3b-48b9-a174-de365ecc4691
- Original site: https://fiasco.design
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery canvas, warm minimal.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud Canvas | `#f8f9f3` | neutral | Page background or card surface |
| Soot Black | `#1d1e19` | neutral | Primary text or dark surface |
| Ash Grey | `#e9eae2` | neutral | Page background or card surface |
| Slate Border | `#686e77` | neutral | Border, muted text, or supporting surface |
| Midnight Ink | `#151612` | neutral | Primary text or dark surface |
| Accent Yellow | `#fff714` | accent | Action accent / signal color |
| Candy Pink | `#fbc2d1` | accent | Action accent / signal color |
| Sky Blue | `#84bdff` | accent | Action accent / signal color |
| Vivid Orange | `#fd6b01` | accent | Action accent / signal color |
| Forest Green | `#03ac47` | accent | Action accent / signal color |

```css
:root {
  --ref-cloud-canvas: #f8f9f3;
  --ref-soot-black: #1d1e19;
  --ref-ash-grey: #e9eae2;
  --ref-slate-border: #686e77;
  --ref-midnight-ink: #151612;
  --ref-accent-yellow: #fff714;
  --ref-candy-pink: #fbc2d1;
  --ref-sky-blue: #84bdff;
}
```

## Typography direction
- **Area-Normal**: 400, 500, 600, 12px, 13px, 14px, 18px, 20px, 30px, 60px, 80px, 1.00, 1.10, 1.20, 1.40, 1.43, 1.50, 1.60, 2.71; substitute `Inter`.
- **HAL Timezone**: 100, 400, 500, 12px, 20px, 22px, 34px, 1.20, 1.40, 1.50, 2.00; substitute `IBM Plex Sans`.
- **Gooper**: 400, 500, 700, 16px, 17px, 19px, 40px, 0.80, 1.20, 1.30; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `12px`
- Page Max Width: `1440px`
- Radius: `cards: 8px, links: 44px, inputs: 3px, buttons: 800px, heroContainer: 40px`

## Surface cues
- **Cloud Canvas** `#f8f9f3`: Primary page and hero background
- **Ash Grey** `#e9eae2`: Secondary background for navigation and subtle section breaks
- **Accent Colored Cards** `#fff714`: Elevated card backgrounds, providing visual distinction for content blocks
- **Midnight Ink** `#151612`: Dark mode footer and specific section backgrounds

## Component cues
- **Subtle Ghost Button**: Secondary action or tag
- **Primary Filled Button**: Call to action
- **Navigation Link Button**: Top-level navigation
- **Standard Card**: Content container
- **Hero Section Card**: Prominent content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
