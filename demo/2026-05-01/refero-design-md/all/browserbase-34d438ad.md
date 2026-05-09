# Browserbase - Refero Design MD

- Source: https://styles.refero.design/style/34d438ad-0647-471e-9a6f-7c1fa29d5df6
- Original site: https://www.browserbase.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Pixelated digital landscape

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#f8fafc` | neutral | Page background or card surface |
| Powder Blue | `#e2e9f3` | neutral | Action accent / signal color |
| Pale Sage | `#fffde6` | neutral | Page background or card surface |
| Charcoal Text | `#686562` | neutral | Border, muted text, or supporting surface |
| Impact Orange | `#ff4500` | brand | Action accent / signal color |
| Sky Tint | `#c4edff` | accent | Action accent / signal color |
| Pixel Mountain | `#c5d3e8` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-cloud-gray: #f8fafc;
  --ref-powder-blue: #e2e9f3;
  --ref-pale-sage: #fffde6;
  --ref-charcoal-text: #686562;
  --ref-impact-orange: #ff4500;
  --ref-sky-tint: #c4edff;
}
```

## Typography direction
- **plain**: 400, 500, 16px, 24px, 1.00, 1.10, 1.16, 1.30, 1.41, 1.50; substitute `Inter`.
- **gtPlanar**: 400, 500, 16px, 24px, 34px, 45px, 189px, 1.00, 1.10, 1.15, 1.50; substitute `DM Sans`.
- **gtStandardMono**: 400, 14px, 1.00, 1.20; substitute `IBM Plex Mono`.

## Spacing / shape
- Section Gap: `75px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `lists: 999px, buttons: 50px, roundedElements: 4px`

## Component cues
- **Primary Action Button**: Call to action button for essential actions
- **Ghost Navigation Button**: Navigation items and secondary actions within headers/menus
- **Accent Pill Button**: Secondary action button with specific highlight
- **Compact Info Button**: Small, information-dense button often used in feature lists
- **Transparent Content Card**: Container for content sections without visual separation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
