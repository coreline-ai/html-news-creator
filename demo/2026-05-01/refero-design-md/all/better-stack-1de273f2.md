# Better Stack - Refero Design MD

- Source: https://styles.refero.design/style/1de273f2-166f-4526-8442-16cc39fc7fd5
- Original site: https://betterstack.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep space console

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Abyss | `#0f101a` | neutral | Primary text or dark surface |
| Graphite Panel | `#151621` | neutral | Primary text or dark surface |
| Steel Overlay | `#1f2433` | neutral | Primary text or dark surface |
| Faded Steel | `#262935` | neutral | Primary text or dark surface |
| Muted Ash | `#646e87` | neutral | Border, muted text, or supporting surface |
| Ash Text | `#939db8` | neutral | Border, muted text, or supporting surface |
| Cloud Whisper | `#c9d3ee` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Zero Black | `#000000` | neutral | Primary text or dark surface |
| Focus Violet | `#98a4f7` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-abyss: #0f101a;
  --ref-graphite-panel: #151621;
  --ref-steel-overlay: #1f2433;
  --ref-faded-steel: #262935;
  --ref-muted-ash: #646e87;
  --ref-ash-text: #939db8;
  --ref-cloud-whisper: #c9d3ee;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **Helvetica Now Text**: 400, 500, 700, 10px, 12px, 13px, 14px, 16px, 20px, 28px, 36px, 1.00, 1.08, 1.17, 1.20, 1.45, 1.50, 1.55, 1.60, 1.85; substitute `Inter`.
- **Helvetica Now Display**: 500, 700, 40px, 53px, 1.08, 1.10; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `20px`
- Page Max Width: `1320px`
- Radius: `cards: 16px, inputs: 10px, buttons: 9999px, dialogs: 16px, general: 10px`

## Surface cues
- **Midnight Abyss** `#0f101a`: Base page and deepest background surface
- **Graphite Panel** `#151621`: Default background for cards and interactive components, slightly elevated from the base
- **Steel Overlay** `#1f2433`: Input field borders, providing subtle depth and separation for interactive elements

## Component cues
- **Primary Filled Button**: Button
- **Ghost Button**: Button
- **Small Pill Button**: Button
- **Accent Outlined Button**: Button
- **Informative Card**: Card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
