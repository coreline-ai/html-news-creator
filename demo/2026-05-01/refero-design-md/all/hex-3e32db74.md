# Hex - Refero Design MD

- Source: https://styles.refero.design/style/3e32db74-a61d-4e72-93b8-1fb949af2c00
- Original site: https://hex.tech
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Analytical Clarity on Canvas: A pristine digital workspace where data takes center stage, framed by muted sophistication and precise typography.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fffcfc` | neutral | Page background or card surface |
| Obsidian Ink | `#01011b` | neutral | Primary text or dark surface |
| Eggplant Gray | `#31263b` | neutral | Primary text or dark surface |
| Charcoal Grey | `#14141c` | neutral | Primary text or dark surface |
| Cement Gray | `#717a94` | neutral | Border, muted text, or supporting surface |
| Dusk Violet | `#43394c` | neutral | Action accent / signal color |
| Platinum Mist | `#ecedf2` | neutral | Page background or card surface |
| Slate Cloud | `#dbd7da` | neutral | Border, muted text, or supporting surface |
| Minsk Violet | `#473982` | brand | Action accent / signal color |
| Indigo Punch | `#6f63b7` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #fffcfc;
  --ref-obsidian-ink: #01011b;
  --ref-eggplant-gray: #31263b;
  --ref-charcoal-grey: #14141c;
  --ref-cement-gray: #717a94;
  --ref-dusk-violet: #43394c;
  --ref-platinum-mist: #ecedf2;
  --ref-slate-cloud: #dbd7da;
}
```

## Typography direction
- **PP Editorial New**: 200, 78px, 1.30; substitute `Playfair Display`.
- **PP Formula SemiExtended**: 700, 60px, 1.30; substitute `Archivo Expanded`.
- **PP Formula**: 800, 28px, 1.30; substitute `Archivo Black`.

## Spacing / shape
- Section Gap: `70px`
- Card Padding: `12px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `cards: 6px, badges: 9999px, inputs: 6px, buttons: 3px, default: 3px`

## Surface cues
- **Canvas White** `#fffcfc`: Primary page background, base surface for the entire application.
- **Platinum Mist** `#ecedf2`: Secondary background for sections, tables, and subtle content blocks, providing a slight elevation from the main canvas.
- **Frost Card** `#fffcfc`: Component surfaces, cards, and interactive elements, distinguished by subtle shadow elevation rather than color change.

## Component cues
- **Ghost Button**: Action button
- **Standard Card**: Information container
- **Modal Card**: Interactive container
- **Text Input**: Data entry
- **Nav Button**: Navigation link

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
