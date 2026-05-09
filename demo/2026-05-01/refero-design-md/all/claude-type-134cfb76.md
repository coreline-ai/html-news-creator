# Claude Type - Refero Design MD

- Source: https://styles.refero.design/style/134cfb76-12e0-4e2e-9995-5a1617190c56
- Original site: https://claudetype.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery of Arched Voids

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fcfbf7` | neutral | Page background or card surface |
| Paper Gray | `#e7e4e0` | neutral | Page background or card surface |
| Midnight Ink | `#0d0d0f` | neutral | Primary text or dark surface |
| Deep Charcoal | `#2b1b1b` | neutral | Primary text or dark surface |
| Ghost Fill | `#100401` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Success Green | `#99ff66` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #fcfbf7;
  --ref-paper-gray: #e7e4e0;
  --ref-midnight-ink: #0d0d0f;
  --ref-deep-charcoal: #2b1b1b;
  --ref-ghost-fill: #100401;
  --ref-pure-white: #ffffff;
  --ref-success-green: #99ff66;
}
```

## Typography direction
- **MagicUIPro**: 400, 11px, 12px, 14px, 15px, 18px, 1.00, 1.40, 1.60, 1.67, 2.00; substitute `serif font with good ligature support, such as Optima or ITC Garamond`.

## Spacing / shape
- Section Gap: `180px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 32px, buttons: 100px, imagery: 900px, elements: 10px`

## Surface cues
- **Canvas White** `#fcfbf7`: Primary overall background for the majority of page content, providing a warm, clean base.
- **Paper Gray** `#e7e4e0`: Used for background of specific sections or subtle containers, offering a slight visual shift from the main canvas.
- **Ghost Fill** `#100401`: A very faint background tint on prominent image cards, providing a barely perceptible surface without strong visual weight.

## Component cues
- **Navigation Link**: Top navigation items and footer links.
- **Ghost Button - Light Outline**: Secondary action buttons, typically against light backgrounds.
- **Ghost Button - Dark Outline (variant)**: Secondary action buttons against dark backgrounds.
- **Filled Button - Dark Background**: Primary action button within dark sections or against images.
- **Filled Button - Light Background (variant)**: Primary action button within light sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
