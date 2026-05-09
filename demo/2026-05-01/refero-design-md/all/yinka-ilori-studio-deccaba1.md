# Yinka Ilori Studio - Refero Design MD

- Source: https://styles.refero.design/style/deccaba1-8d53-4a82-b4c7-e2b99a3dc326
- Original site: https://yinkailori.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Joyful maximalism with graphic rhythm

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas Blush | `#f5e5e5` | neutral | Page background or card surface |
| Passion Pink | `#d9698c` | brand | Action accent / signal color |
| Zesty Orange | `#ee6d22` | accent | Action accent / signal color |
| Lush Green | `#1f8029` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-canvas-blush: #f5e5e5;
  --ref-passion-pink: #d9698c;
  --ref-zesty-orange: #ee6d22;
  --ref-lush-green: #1f8029;
}
```

## Typography direction
- **Yinka Sans Ultra**: 400, 500, 120px, 1.10; substitute `Bebas Neue`.
- **Haas Grotesk Display R Web**: 400, 500, 14px, 20px, 120px, 1.00, 1.05, 1.30, 1.50; substitute `Public Sans`.

## Spacing / shape
- Section Gap: `175px`
- Card Padding: `30px`
- Element Gap: `15px`
- Radius: `default: 0px`

## Surface cues
- **Canvas Blush** `#f5e5e5`: Base page background and default surface for content blocks
- **Passion Pink** `#d9698c`: Background for bold, immersive content sections, providing a strong visual shift

## Component cues
- **Primary Navigation Link**: Main site navigation
- **Hero Headline**: Large central title
- **Text Section Divider**: Visual separator for content sections
- **Animated Background Pattern**: Dynamic visual element
- **Sectional Background**: Alternating background fills for distinct content blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
