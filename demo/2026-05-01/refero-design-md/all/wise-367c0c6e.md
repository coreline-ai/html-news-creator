# Wise - Refero Design MD

- Source: https://styles.refero.design/style/367c0c6e-73a7-441c-a8ff-91d139ac60dc
- Original site: https://wise.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant Fintech Authority; a financial system in bold green and crisp black on a pristine white canvas.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#0e0f0c` | neutral | Primary text or dark surface |
| Slate Text | `#454745` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#e8ebe6` | neutral | Page background or card surface |
| Muted Grey | `#868685` | neutral | Border, muted text, or supporting surface |
| Ghost Gray | `#6a6c6a` | neutral | Border, muted text, or supporting surface |
| Ambient Cyan | `#ecf9f9` | neutral | Page background or card surface |
| Forest Green | `#163300` | brand | Action accent / signal color |
| Lime Accent | `#9fe870` | accent | Action accent / signal color |
| Deep Teal | `#0b4c72` | semantic | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #0e0f0c;
  --ref-slate-text: #454745;
  --ref-ash-gray: #e8ebe6;
  --ref-muted-grey: #868685;
  --ref-ghost-gray: #6a6c6a;
  --ref-ambient-cyan: #ecf9f9;
  --ref-forest-green: #163300;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 22px, 25px, 36px, 45px, 61px, 300px, 0.72, 1.00, 1.10, 1.25, 1.30, 1.40, 1.43, 1.44, 1.50, 1.55, 1.63, 1.71, 1.86, 2.17; substitute `system-ui, sans-serif`.
- **Wise Sans**: 400, 900, 40px, 52px, 59px, 89px, 105px, 300px, 0.85, 1.50.
- **monospace**: 400, 300px.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `28px`
- Element Gap: `8px`
- Radius: `sm: 2px, full: 1000px, none: 0px, pill: 9999px, card-lg: 28.1539px, card-md: 18.7693px, card-xl: 37.5385px, default: 10px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background, primary content sections.
- **Ash Gray** `#e8ebe6`: Subtle background for UI blocks, secondary card surfaces.
- **Ambient Cyan** `#ecf9f9`: Background for informational or celebratory sections, providing a soft color block.

## Component cues
- **Primary Filled Button**: Call to action
- **Secondary Ghost Button**: Secondary action (text only)
- **Outlined Pill Button**: Tertiary action
- **Circular Icon Button**: Decorative/Functional
- **Base Card**: Informational grouping

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
