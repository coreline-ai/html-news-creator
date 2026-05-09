# AI Product Generation - Refero Design MD

- Source: https://styles.refero.design/style/186775da-7568-49e5-8110-4fd0bbc7bbe3
- Original site: https://fourmula.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White canvas, sharp shadows, and a burst of sunset.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Coal | `#020108` | brand | Action accent / signal color |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Ash Grey | `#333333` | neutral | Primary text or dark surface |
| Canvas Fog | `#f7f7f7` | neutral | Page background or card surface |
| Stone Whisper | `#d7d7d6` | neutral | Border, muted text, or supporting surface |
| Muted Slate | `#818084` | neutral | Border, muted text, or supporting surface |
| Deep Plum | `#5d5c61` | neutral | Border, muted text, or supporting surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Sunset Orange | `#f94a00` | accent | Action accent / signal color |
| Desert Gold | `#fd7b03` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-coal: #020108;
  --ref-cloud-white: #ffffff;
  --ref-ash-grey: #333333;
  --ref-canvas-fog: #f7f7f7;
  --ref-stone-whisper: #d7d7d6;
  --ref-muted-slate: #818084;
  --ref-deep-plum: #5d5c61;
  --ref-ink-black: #000000;
}
```

## Typography direction
- **SF Pro Display**: 400, 500, 8px, 10px, 11px, 12px, 13px, 14px, 15px, 17px, 20px, 27px, 43px, 53px, 73px, 100px, 0.94, 1.00, 1.05, 1.15, 1.20, 1.25, 1.50; substitute `system-ui`.
- **Arial**: 400, 14px, 1.39; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `27px`
- Element Gap: `20px`
- Radius: `badges: 1.33px, images: 26.62px, buttons: 1317.53px, cards-lg: 19.96px, cards-sm: 6.65px, promo-cards: 39.93px, footer-elements: 119.78px`

## Surface cues
- **Main Canvas** `#ffffff`: Primary page background, base for all content.
- **Subtle Card** `#f7f7f7`: Secondary background for card-like elements, creating slight elevation.
- **Prominent Card** `#d7d7d6`: Used for bordered elements or as a subtle background for complex sections.
- **Dark Overlay / Panel** `#020108`: Background for darker sections or prominent UI elements needing high contrast.

## Component cues
- **Primary Filled Button**: Call to action button for key interactions.
- **Outline Ghost Button**: Secondary call to action, less prominent than filled.
- **Default Content Card**: Container for content blocks.
- **Accent Content Card (Large Radius)**: Prominent content container, drawing more attention.
- **Product Image Card**: Container for product images or visual assets.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
