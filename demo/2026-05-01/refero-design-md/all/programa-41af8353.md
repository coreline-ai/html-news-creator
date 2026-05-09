# Programa - Refero Design MD

- Source: https://styles.refero.design/style/41af8353-6a8f-416d-947b-57932f591497
- Original site: https://programa.design
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Storm Graphite | `#1a1a1a` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Midas Yellow | `#fbff2b` | brand | Action accent / signal color |

```css
:root {
  --ref-storm-graphite: #1a1a1a;
  --ref-canvas-white: #ffffff;
  --ref-ash-gray: #a3a3a3;
  --ref-midas-yellow: #fbff2b;
}
```

## Typography direction
- **neueHaasGroteskText**: 400, 500, 14px, 16px, 17px, 20px, 24px, 42px, 1.10, 1.20, 1.40; substitute `Helvetica Neue`.
- **neue-haas-grotesk-text**: 400, 20px, 1.4.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `cards: 16px, inputs: 10px, buttons: 10px, navigation: 10px`

## Component cues
- **Neutral Ghost Button**: Secondary action or navigation item
- **Primary Action Button**: Main call to action
- **Dark Filled Button**: Alternative primary action or prominent secondary action on light backgrounds
- **Light Input Field**: Standard input field on dark backgrounds
- **Dark Input Field**: Standard input field on light backgrounds

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
