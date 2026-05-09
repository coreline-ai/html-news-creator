# Tailscale - Refero Design MD

- Source: https://styles.refero.design/style/5b679fb6-8d53-402d-a77b-c88bfb397623
- Original site: https://tailscale.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cloud control panel on pristine paper.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Surface Frost | `#f7f5f4` | neutral | Page background or card surface |
| Canvas Pale | `#eeebea` | neutral | Page background or card surface |
| Graphite Black | `#181717` | neutral | Primary text or dark surface |
| Storm Gray | `#2e2d2d` | neutral | Primary text or dark surface |
| Stone Gray | `#575555` | neutral | Border, muted text, or supporting surface |
| Smoke Gray | `#706e6d` | neutral | Border, muted text, or supporting surface |
| Cloud Mist | `#d5d3d2` | neutral | Border, muted text, or supporting surface |
| Border Light | `#232222` | neutral | Primary text or dark surface |
| Action Red | `#d04841` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-surface-frost: #f7f5f4;
  --ref-canvas-pale: #eeebea;
  --ref-graphite-black: #181717;
  --ref-storm-gray: #2e2d2d;
  --ref-stone-gray: #575555;
  --ref-smoke-gray: #706e6d;
  --ref-cloud-mist: #d5d3d2;
}
```

## Typography direction
- **Inter**: 300, 400, 500, 600, 12px, 14px, 16px, 20px, 32px, 48px, 64px, 1.20, 1.43, 1.50; substitute `system-ui, sans-serif`.
- **MDIO**: 500, 12px, 14px, 20px, 1.20, 1.50; substitute `system-ui, monospace`.

## Spacing / shape
- Section Gap: `24-64px`
- Card Padding: `24px`
- Element Gap: `12px`
- Radius: `tags: 9999px, cards: 16px, buttons: 8px, largeElements: 32px`

## Surface cues
- **Canvas Pale** `#eeebea`: Base page background, providing a light, warm foundation.
- **Canvas White** `#ffffff`: Elevated surfaces like cards, panels, and modals, providing contrast against the base canvas.
- **Dark Content Panel** `#2e2d2d`: Specific content blocks requiring a dark background for emphasis or thematic break. Does not typically stack on other elevated elements.

## Component cues
- **Primary Filled Button**: Hero actions, main CTA buttons.
- **Neutral Ghost Button**: Secondary calls to action, text links that behave as buttons.
- **Secondary Ghost Button**: Tertiary actions, usually within a card or alongside a primary button.
- **Status Tag**: Small informational labels, categories, or active state indicators.
- **Feature Card**: Displaying product features or testimonials in a structured grid.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
