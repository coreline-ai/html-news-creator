# Glyphy - Refero Design MD

- Source: https://styles.refero.design/style/6ec18fa7-41ff-41e0-8824-94f6fa104a75
- Original site: https://glyphy.io
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Arcade Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Cream | `#fef9e6` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Dark Onyx | `#060606` | neutral | Primary text or dark surface |
| Stone Whisper | `#c7c3b4` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#8d8b80` | neutral | Border, muted text, or supporting surface |
| Sunny Glow | `#fdc331` | accent | Action accent / signal color |
| Sunset Orange | `#fe5722` | accent | Action accent / signal color |
| Vivid Scarlet | `#f0353c` | accent | Action accent / signal color |
| Berry Rouge | `#b4213d` | accent | Action accent / signal color |
| Plum Wine | `#671c3b` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-cream: #fef9e6;
  --ref-midnight-ink: #000000;
  --ref-dark-onyx: #060606;
  --ref-stone-whisper: #c7c3b4;
  --ref-steel-gray: #8d8b80;
  --ref-sunny-glow: #fdc331;
  --ref-sunset-orange: #fe5722;
  --ref-vivid-scarlet: #f0353c;
}
```

## Typography direction
- **Neue Machina**: 400, 700, 800, 21px, 64px, 120px, 0.75, 1.00; substitute `Space Mono`.
- **__system85_8a4f0d**: 400, 700, 14px, 16px, 18px, 24px, 32px, 40px, 1.00, 1.20; substitute `Inter`.
- **__pixelMPlus10_ff679b**: 400, 700, 12px, 14px, 18px, 24px, 64px, 1.00, 1.33; substitute `Press Start 2P`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `cards: 14px, buttons: 28px, callouts: 14px, navigation: 14px`

## Surface cues
- **Canvas Cream** `#fef9e6`: Dominant page and content background.
- **Dark Onyx** `#060606`: Background for primary buttons and specific interactive areas within lighter sections.
- **Vivid Gradient Bands** `#fdc331`: Sequential, distinct background colors for major content sections, creating visual rhythm.

## Component cues
- **Primary Dark Button**: Filled button for main actions on light backgrounds
- **Light Outline Button**: Outlined button for secondary actions on dark backgrounds.
- **Light Fill Button**: Filled button for main actions on dark backgrounds.
- **Muted Outline Button**: Outlined button for secondary actions on light backgrounds.
- **Section Callout Card**: Informational cards within sections, driving to deeper content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
