# Basic.Space - Refero Design MD

- Source: https://styles.refero.design/style/d7096101-d33c-43b8-8b0b-d9dfff802db2
- Original site: https://basic.space
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid Monochrome.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Fog | `#ebebeb` | neutral | Page background or card surface |
| Inkwell | `#000000` | neutral | Primary text or dark surface |
| Surface Frost | `#cecccc` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Subtle Ash | `#f7f7f7` | neutral | Page background or card surface |
| Placeholder Gray | `#b5b5b5` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-fog: #ebebeb;
  --ref-inkwell: #000000;
  --ref-surface-frost: #cecccc;
  --ref-pure-white: #ffffff;
  --ref-subtle-ash: #f7f7f7;
  --ref-placeholder-gray: #b5b5b5;
  --ref-electric-blue: #007aff;
}
```

## Typography direction
- **FTBasicSpace**: 400, 500, 600, 14px, 16px, 18px, 20px, 38px, 39px, 40px, 1.12, 1.13, 1.20, 1.22, 1.38, 1.43, 1.71; substitute `Arial`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `0px`
- Element Gap: `4px`
- Radius: `cards: 2px, inputs: 16px, buttons: 9999px`

## Surface cues
- **Canvas Fog** `#ebebeb`: Base page background and default dividing lines.
- **Subtle Ash** `#f7f7f7`: Background for secondary sections or specific content blocks.
- **Pure White** `#ffffff`: Background for prominent content, such as certain inputs or temporary contextual elements.
- **Surface Frost** `#cecccc`: Distinct background for elevated content areas, often wider sections.

## Component cues
- **Outlined Pill Button**: Secondary action button, often used for navigation or filtering.
- **Ghost Link Button**: Minimal interactive text link or navigation item.
- **Product Card (Minimal)**: Default display for product listings with no visible border or shadow.
- **Product Card (Hover)**: Product display with a subtle radius, likely for interactive states.
- **Search Input (Filled)**: Primary search input field.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
