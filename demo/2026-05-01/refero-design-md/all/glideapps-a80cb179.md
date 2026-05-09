# Glideapps - Refero Design MD

- Source: https://styles.refero.design/style/a80cb179-2d90-4896-b52d-4e674b421498
- Original site: https://www.glideapps.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Engineering clarity on white canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Fog | `#e4feff` | neutral | Page background or card surface |
| Pale Ash | `#edede8` | neutral | Page background or card surface |
| Warm Mist | `#d9dad3` | neutral | Page background or card surface |
| Steel Gray | `#999991` | neutral | Border, muted text, or supporting surface |
| Charcoal Text | `#303030` | neutral | Primary text or dark surface |
| Dark Graphite | `#5c5c5c` | neutral | Border, muted text, or supporting surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Input Black | `#171715` | neutral | Primary text or dark surface |
| Midnight Black | `#0e0e0d` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ghost-fog: #e4feff;
  --ref-pale-ash: #edede8;
  --ref-warm-mist: #d9dad3;
  --ref-steel-gray: #999991;
  --ref-charcoal-text: #303030;
  --ref-dark-graphite: #5c5c5c;
  --ref-ink-black: #000000;
}
```

## Typography direction
- **bootonFont**: 400, 575, 600, 700, 12px, 14px, 16px, 20px, 22px, 48px, 60px, 85px, 1.00, 1.10, 1.30, 1.40, 1.50; substitute `Inter`.
- **affairsFont**: 400, 36px, 80px, 1.05, 1.20; substitute `Georgia`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `12px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `tags: 6px, cards: 12px, images: 6px, inputs: 0px, buttons: 6px`

## Component cues
- **Primary Action Button**: Filled button for main calls to action.
- **Ghost Accent Button**: Subtle button for secondary actions or information calls.
- **Navigation Link Button**: Text-only button for navigation or tertiary actions.
- **Text Input (Default)**: Standard text entry field.
- **Informational Card**: Container for content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
