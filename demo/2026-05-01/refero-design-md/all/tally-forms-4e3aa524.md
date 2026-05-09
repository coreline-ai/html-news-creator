# Tally Forms - Refero Design MD

- Source: https://styles.refero.design/style/4e3aa524-b146-416c-907f-382c079ea80c
- Original site: https://tally.so
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
white canvas, playful ink sketches

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#37352f` | neutral | Primary text or dark surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Soft Mist | `#e0e0df` | neutral | Page background or card surface |
| Ash Gray | `#898884` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#777672` | neutral | Border, muted text, or supporting surface |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Faded Ink | `#45433e` | neutral | Border, muted text, or supporting surface |
| Tally Blue | `#0070d7` | brand | Action accent / signal color |
| Sketch Pink | `#f81ce5` | accent | Action accent / signal color |
| Soft Sketch Pink | `#fcadf6` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-charcoal: #37352f;
  --ref-white-canvas: #ffffff;
  --ref-soft-mist: #e0e0df;
  --ref-ash-gray: #898884;
  --ref-steel-gray: #777672;
  --ref-jet-black: #000000;
  --ref-faded-ink: #45433e;
  --ref-tally-blue: #0070d7;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 800, 13px, 14px, 15px, 16px, 18px, 22px, 26px, 30px, 36px, 64px, 1.00, 1.15, 1.25, 1.50, 1.80; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 10px, input: 7px, buttons: 8px`

## Surface cues
- **Soft Mist** `#e0e0df`: Dominant page background, subtle dividers, canvas for content.
- **White Canvas** `#ffffff`: Standard card backgrounds, primary content blocks, primary page canvas within sections.

## Component cues
- **Primary Action Button**: Button
- **Ghost Navigation Button**: Button
- **Standard Card**: Card
- **Elevated Feature Card**: Card
- **Accent Border Card**: Card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
