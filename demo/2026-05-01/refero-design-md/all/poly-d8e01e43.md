# Poly - Refero Design MD

- Source: https://styles.refero.design/style/d8e01e43-d260-4fa3-8f42-ae39e5c6ac84
- Original site: https://poly.app
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Subtle Depth, Focused Accent

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f4f4f4` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Steel Gray | `#292930` | neutral | Primary text or dark surface |
| Shadow Tint | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Poly Gradient | `#f4824d` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #f4f4f4;
  --ref-ink-black: #000000;
  --ref-steel-gray: #292930;
  --ref-shadow-tint: #cccccc;
  --ref-poly-gradient: #f4824d;
}
```

## Typography direction
- **Inter**: 400, 600, 12px, 15px, 24px, 30px, 45px, 1.10, 1.20, 1.50; substitute `system-ui`.
- **Haffer Variable**: 450, 24px, 30px, 45px, 53px, 1.10.
- **Bogue**: 400, 24px, 30px, 45px, 53px, 1.10, 1.50.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `12px`
- Page Max Width: `1280px`
- Radius: `default: 8px`

## Component cues
- **Primary Call-to-Action Button**: Interactive element
- **Secondary Ghost Button**: Interactive element
- **Navigation Link**: Interactive element
- **Info Badge**: Informative label

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
