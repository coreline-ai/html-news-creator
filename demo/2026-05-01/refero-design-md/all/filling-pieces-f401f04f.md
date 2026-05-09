# Filling Pieces - Refero Design MD

- Source: https://styles.refero.design/style/f401f04f-c45b-4261-9441-f502c6569a29
- Original site: https://www.fillingpieces.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochromatic gallery, precise typography

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Ice | `#e5e7eb` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Fog Gray | `#efefef` | neutral | Page background or card surface |
| Steel Gray | `#6b7280` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-ice: #e5e7eb;
  --ref-pure-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-fog-gray: #efefef;
  --ref-steel-gray: #6b7280;
}
```

## Typography direction
- **Favorit**: 400, 600, 8px, 10px, 11px, 12px, 14px, 16px, 18px, 35px, 50px, 100px, 0.90, 1.00, 1.20, 1.50, 1.78; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `all: 8px`

## Surface cues
- **Canvas Ice** `#e5e7eb`: Dominant background for the overall page, providing a light, neutral base.
- **Pure White** `#ffffff`: Primary surface for interactive components, cards, and modal dialogs, offering high contrast against text.
- **Fog Gray** `#efefef`: Secondary background sections, creating a subtle contrast to the primary canvas for content grouping.

## Component cues
- **Primary Filled Button**: Main call to action
- **Ghost Button**: Secondary action or discrete navigation
- **Surface Button**: Navigational elements or filters within a light context
- **Text Input (Default)**: Standard form field for user input
- **Text Input (Light Background)**: Standard form field for user input on white surfaces

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
