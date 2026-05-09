# Moffitt.Moffitt. - - Refero Design MD

- Source: https://styles.refero.design/style/4244637b-e27b-4962-b586-cb3ac605e5aa
- Original site: https://moffittmoffitt.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome gallery canvas

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Fog Gray | `#f5f5f5` | neutral | Page background or card surface |
| Charcoal Gray | `#595b60` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#888888` | neutral | Border, muted text, or supporting surface |
| Divider Gray | `#d8d8da` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-fog-gray: #f5f5f5;
  --ref-charcoal-gray: #595b60;
  --ref-stone-gray: #888888;
  --ref-divider-gray: #d8d8da;
}
```

## Typography direction
- **Suisse**: 400, 500, 600, 12px, 16px, 22px, 24px, 40px, 1.00, 1.13, 1.17, 1.20, 1.25, 1.33, 1.39, 2.00; substitute `Helvetica Neue, Arial`.
- **Lyon**: 100, 13px, 1.00; substitute `Georgia, serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `tags: 50px, cards: 0px, images: 5px, inputs: 0px, buttons: 50px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for most content sections.
- **Fog Gray** `#f5f5f5`: Secondary background for alternating content sections, providing a subtle shift in visual texture.
- **Ink Black** `#000000`: Used as an occasional dark surface for highly impactful sections or controls, creating maximum contrast.

## Component cues
- **Pill Button - Light**: Interactive element (button).
- **Pill Button - Dark**: Interactive element (button).
- **Ghost Link**: Interactive text link/button.
- **Muted Ghost Link**: Interactive text link/button (muted).
- **Content Card**: Container for content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
