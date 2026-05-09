# Datalands - Refero Design MD

- Source: https://styles.refero.design/style/a7530405-e523-4268-bba5-ef13549fd61c
- Original site: https://datalands.co
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochromatic Canvas, Vivid Punctuation

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Storm Gray | `#111212` | neutral | Primary text or dark surface |
| Mist | `#f3f3ef` | neutral | Page background or card surface |
| Charcoal | `#3d3d3d` | neutral | Primary text or dark surface |
| Light Gray | `#d9d9d9` | neutral | Page background or card surface |
| Twilight Black | `#1d1a1a` | neutral | Primary text or dark surface |
| Deep Space Blue | `#122d8b` | brand | Action accent / signal color |
| Cyan Sky | `#94bcee` | brand | Action accent / signal color |
| Fuchsia Pulse | `#fc74dd` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-ghost-white: #ffffff;
  --ref-storm-gray: #111212;
  --ref-mist: #f3f3ef;
  --ref-charcoal: #3d3d3d;
  --ref-light-gray: #d9d9d9;
  --ref-twilight-black: #1d1a1a;
  --ref-deep-space-blue: #122d8b;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **OZIK Black**: 400, 358px, 0.83, 1.50; substitute `Black Ops One`.
- **Basis Grotesque Pro**: 400, 14px, 18px, 22px, 35px, 38px, 42px, 60px, 80px, 1.00, 1.10, 1.20, 1.25, 1.45.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `48px`
- Element Gap: `10px`
- Radius: `cards: 30px, links: 30px, inputs: 96px, buttons: 96px, decorativeElements: 300px`

## Surface cues
- **Base Canvas** `#000000`: Dominant background for the entire application, creating a deep, immersive dark mode.
- **Input Surface** `#f3f3ef`: Background for interactive input fields, providing clear contrast against the dark canvas.
- **Actionable Surface** `#1d1a1a`: Background for certain interactive elements or cards, offering a slight visual elevation from the canvas.

## Component cues
- **Ghost Navigation Button**: Navigation and secondary actions.
- **Primary Action Button**: Key interaction calls to action.
- **Dark Overlay Button**: Interactive elements within dark sections, often containing media.
- **Circular Link Button**: Decorative and functional links, often with icons.
- **Pill Input Field**: Data entry fields requiring user input.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
