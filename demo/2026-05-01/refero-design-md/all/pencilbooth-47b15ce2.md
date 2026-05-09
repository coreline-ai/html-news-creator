# PencilBooth - Refero Design MD

- Source: https://styles.refero.design/style/47b15ce2-34c8-46e3-b2de-f7eed0b6a3b9
- Original site: https://www.pencilbooth.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast content blueprint

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper Gray | `#f2f2f2` | neutral | Page background or card surface |
| Border Fog | `#e5e7eb` | neutral | Page background or card surface |
| Muted Stone | `#b2b2b2` | neutral | Border, muted text, or supporting surface |
| Shadow Graphite | `#5a5e62` | neutral | Border, muted text, or supporting surface |
| Sapphire Accent | `#0f1ea1` | brand | Action accent / signal color |
| Horizon Blue | `#cfd2ec` | accent | Action accent / signal color |
| Sky Interactive | `#8fbaff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-whisper-gray: #f2f2f2;
  --ref-border-fog: #e5e7eb;
  --ref-muted-stone: #b2b2b2;
  --ref-shadow-graphite: #5a5e62;
  --ref-sapphire-accent: #0f1ea1;
  --ref-horizon-blue: #cfd2ec;
}
```

## Typography direction
- **Soehne**: 400, 700, 12px, 14px, 16px, 18px, 32px, 96px, 1.00, 1.20; substitute `system-ui`.

## Spacing / shape
- Section Gap: `47px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `cards: 10px, icons: 9999px, links: 2px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Whisper Gray** `#f2f2f2`: Card backgrounds, secondary interactive surface
- **Horizon Blue** `#cfd2ec`: Alternating section backgrounds
- **Sky Interactive** `#8fbaff`: Active states, subtle highlights
- **Sapphire Accent** `#0f1ea1`: Primary active states, brand highlights

## Component cues
- **Feature Card**: Showcasing individual features or content blocks.
- **Interactive List Item**: Navigation or select options within a list.
- **Selected List Item**: Currently active or selected item in a list.
- **Profile Thumbnail**: Representing user profiles or content creators.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
