# Public - Refero Design MD

- Source: https://styles.refero.design/style/9d16aa65-cef7-4bf7-83c8-91837a248cd9
- Original site: https://public.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp Editorial Clarity: a high-contrast financial journal on a pristine, structured page.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Smoke | `#e9edf3` | neutral | Page background or card surface |
| Graphite | `#262626` | neutral | Primary text or dark surface |
| Ash | `#dce2ea` | neutral | Page background or card surface |
| Jet | `#1b2128` | neutral | Primary text or dark surface |
| Slate | `#516880` | neutral | Border, muted text, or supporting surface |
| Cloud | `#a8b4bf` | neutral | Border, muted text, or supporting surface |
| Ultramarine | `#0027b3` | brand | Action accent / signal color |
| Azure Glow | `#95d0ff` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-canvas: #ffffff;
  --ref-smoke: #e9edf3;
  --ref-graphite: #262626;
  --ref-ash: #dce2ea;
  --ref-jet: #1b2128;
  --ref-slate: #516880;
  --ref-cloud: #a8b4bf;
}
```

## Typography direction
- **Denton**: 300, 48px, 52px, 80px, 1.00, 1.11, 1.12, 1.13; substitute `Playfair Display`.
- **Invest Pro**: 400, 500, 12px, 14px, 16px, 20px, 24px, 32px, 1.00, 1.13, 1.14, 1.15, 1.17, 1.20, 1.28, 1.29, 1.31, 1.37, 1.38, 1.50; substitute `IBM Plex Serif`.
- **Invest Pro**: 400, 500, 12px, 14px, 16px, 20px, 24px, 32px, 1.00, 1.13, 1.14, 1.15, 1.17, 1.20, 1.28, 1.29, 1.31, 1.37, 1.38, 1.50; substitute `IBM Plex Serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `tags: 999px, cards: 16px, buttons: 100px, default: 4px, minimal: 1px, partial: 12px, smallInteractive: 8px`

## Surface cues
- **Canvas** `#ffffff`: Dominant page background, base for light sections.
- **Section Card** `#fafa_fafa`: Light background for grouping content segments within the main canvas.
- **Monochrome Elevated Card** `#262626`: Darker, slightly elevated card backgrounds for focused information or interactive elements.

## Component cues
- **Primary Ghost Button**: Call to action
- **Filled Action Button**: Call to action
- **Section Card**: Content container
- **Monochrome Elevated Card**: Accent / Elevated content.
- **Informational Badge**: Metadata / Status

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
