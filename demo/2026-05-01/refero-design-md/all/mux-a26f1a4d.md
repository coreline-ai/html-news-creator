# Mux - Refero Design MD

- Source: https://styles.refero.design/style/a26f1a4d-758c-4df0-a61e-88a7ca0931ce
- Original site: https://www.mux.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Parchment Grid, Terminal Cards

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Greige Canvas | `#e2e4dd` | neutral | Page background or card surface |
| Cloud Gray | `#ffffff` | neutral | Page background or card surface |
| Graphite Card | `#242628` | neutral | Primary text or dark surface |
| Subtle Ash | `#f4f6f4` | neutral | Page background or card surface |
| Ghost Border | `#adb9c6` | neutral | Border, muted text, or supporting surface |
| Slate Text | `#565e67` | neutral | Border, muted text, or supporting surface |
| Warm Gray Outline | `#828c97` | neutral | Border, muted text, or supporting surface |
| Action Orange | `#ff6100` | brand | Action accent / signal color |
| Interactive Yellow | `#ffb200` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-greige-canvas: #e2e4dd;
  --ref-cloud-gray: #ffffff;
  --ref-graphite-card: #242628;
  --ref-subtle-ash: #f4f6f4;
  --ref-ghost-border: #adb9c6;
  --ref-slate-text: #565e67;
  --ref-warm-gray-outline: #828c97;
}
```

## Typography direction
- **Aeonik**: 400, 700, 14px, 16px, 18px, 21px, 24px, 50px, 1.15, 1.20, 1.40, 1.50, 2.00; substitute `Inter`.
- **JetBrainsMono**: 400, 12px, 14px, 1.20, 1.50, 1.60; substitute `Fira Code`.
- **Rotonto**: 400, 50px, 66px, 1.15, 1.20; substitute `Chalkboard SE`.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `28px`
- Element Gap: `14px`
- Page Max Width: `1200px`
- Radius: `cards: 28px, images: 112px, buttons: 9999px, input-focus: 2px, inline-elements: 7px`

## Surface cues
- **Greige Canvas** `#e2e4dd`: Dominant page background, grid backdrop
- **Cloud Gray** `#ffffff`: Primary elevated card surfaces, feature backgrounds
- **Graphite Card** `#242628`: Darker, functional card backgrounds for code or content presentation

## Component cues
- **Primary Action Button**: Filled button for main calls to action
- **Ghost Outline Button - Dark Text**: Secondary action or navigation link with neutral text on light backgrounds
- **Ghost Outline Button - Light Text**: Secondary action or navigation link with light text on dark backgrounds
- **Ghost Outline Button - Monospace Text**: Code-focused actions or inline controls
- **Dark Terminal Card**: Main content display for features and examples

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
