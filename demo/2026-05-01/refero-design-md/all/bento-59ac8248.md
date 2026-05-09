# Bento - Refero Design MD

- Source: https://styles.refero.design/style/59ac8248-1d64-4df3-92f1-919b50e05602
- Original site: https://www.bento.me
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant, playful canvases

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#1e2330` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Marble Fog | `#f3f3f1` | neutral | Page background or card surface |
| Ash Concrete | `#676b5f` | neutral | Border, muted text, or supporting surface |
| Charcoal Grey | `#222222` | neutral | Primary text or dark surface |
| Chartreuse Kick | `#d2e823` | brand | Action accent / signal color |
| Hydrangea Bold | `#2665d6` | brand | Action accent / signal color |
| Lavender Pop | `#e9c0e9` | brand | Action accent / signal color |
| Iris Deep | `#061492` | brand | Action accent / signal color |
| Dahlia Grape | `#502274` | brand | Action accent / signal color |

```css
:root {
  --ref-ink: #1e2330;
  --ref-pure-white: #ffffff;
  --ref-marble-fog: #f3f3f1;
  --ref-ash-concrete: #676b5f;
  --ref-charcoal-grey: #222222;
  --ref-chartreuse-kick: #d2e823;
  --ref-hydrangea-bold: #2665d6;
  --ref-lavender-pop: #e9c0e9;
}
```

## Typography direction
- **Arial**: 400, 16px, 1.50; substitute `Helvetica Neue`.
- **Linksans Linksansvf**: 400, 500, 700, 800, 14px, 16px, 18px, 24px, 28px, 56px, 80px, 1.00, 1.06, 1.07, 1.20, 1.30, 1.50; substitute `Inter`.
- **Linksans**: 400, 500, 700, 12px, 13px, 14px, 15px, 20px, 24px, 25px, 51px, 1.06, 1.20, 1.31, 1.50, 2.32; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `10px`
- Page Max Width: `1504px`
- Radius: `cards: 32px, inputs: 8px, buttons: 99px, pillForms: 1000px, largeCards: 64px, navigation: 8px`

## Component cues
- **Pill Accent Button**: Primary calls to action
- **Filled Square Button**: Secondary action buttons, form submission
- **Ghost Text Button**: Tertiary actions, navigation links
- **Navigation Link**: Top navigation items
- **Hero Section Card**: Decorative content containers

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
