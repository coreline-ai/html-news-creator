# Flim - Refero Design MD

- Source: https://styles.refero.design/style/94ed6ce8-c2e5-45bf-83bd-e5d1daf63efc
- Original site: https://flim.ai
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Grid-paper studio, bold blocks.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#141414` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#f5f5f5` | neutral | Page background or card surface |
| Ash Gray | `#e9e9e9` | neutral | Page background or card surface |
| Stone Grout | `#d9d9d9` | neutral | Page background or card surface |
| Vivid Green | `#30a81d` | brand | Action accent / signal color |
| Sunburst Orange | `#ff8400` | brand | Action accent / signal color |
| Forest Green | `#21935b` | accent | Action accent / signal color |
| Lemon Zest | `#fecc33` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #141414;
  --ref-canvas-white: #ffffff;
  --ref-pure-black: #000000;
  --ref-paper-white: #f5f5f5;
  --ref-ash-gray: #e9e9e9;
  --ref-stone-grout: #d9d9d9;
  --ref-vivid-green: #30a81d;
  --ref-sunburst-orange: #ff8400;
}
```

## Typography direction
- **Swizzy**: 500, 21px, 27px, 47px, 125px, 0.86, 1.00, 1.10; substitute `Montserrat, Raleway Bold`.
- **Arial**: 400, 700, 16px, 32px, 1.00, 1.13; substitute `Helvetica Neue`.
- **PP Neue Montreal Mono**: 400, 12px, 15px, 1.00; substitute `Space Mono, Fira Code`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `24px`
- Radius: `cards: 16px, chips: 160px, icons: 16px, links: 4px, images: 16px, buttons: 8px, specialHeading: 25.04px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and outermost containers.
- **Paper White** `#f5f5f5`: Slightly elevated content areas like cards and forms, provides subtle visual separation.
- **Ash Gray** `#e9e9e9`: Secondary background for card-like elements or subtle banding, deeper contrast against the Canvas White.

## Component cues
- **Ghost Button**: Secondary action. Low visual hierarchy, relies on border for delineation.
- **Filled Button (Accent)**: Primary action. High visual hierarchy, black background for strong call to action.
- **Media Card**: Content container for visual assets.
- **Circular Card (Accent)**: Decorative or small content container.
- **Callout Card (Orange)**: Promotional or highlighted content block.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
