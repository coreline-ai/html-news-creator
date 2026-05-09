# Numbered - Refero Design MD

- Source: https://styles.refero.design/style/50f0b6d5-9e96-42a1-9564-a6e99c289f98
- Original site: https://numbered.studio
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shadowy Gallery Canvas

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Black | `#111111` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Muted Ash | `#4f4f4f` | neutral | Border, muted text, or supporting surface |
| Desert Sand | `#bc9873` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-black: #111111;
  --ref-ghost-white: #ffffff;
  --ref-muted-ash: #4f4f4f;
  --ref-desert-sand: #bc9873;
}
```

## Typography direction
- **aktiv-web**: 400, 700, 12px, 13px, 15px, 25px, 54px, 74px, 1.00, 1.20, 1.50, 2.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `99px`
- Card Padding: `0px`
- Element Gap: `20px`
- Radius: `cards: 0px, buttons: 0px`

## Surface cues
- **Canvas Black** `#111111`: Dominant background for the entire site, creating a deep, immersive dark theme.
- **Desert Sand Accent** `#bc9873`: A secondary, subtle accent surface for specific content blocks or cards, providing a mild contrast without disrupting the dark theme.

## Component cues
- **Ghost Border Button**: Call to action or navigation links.
- **Content Card**: Displaying featured work or case studies.
- **Navigation Link**: Top-level navigation items or footer links.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
