# Viewport - Refero Design MD

- Source: https://styles.refero.design/style/754ad72f-9abd-43df-ac72-c6abf2036ed4
- Original site: https://viewport.co
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp digital canvas

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#f8f9fa` | neutral | Page background or card surface |
| Stone Gray | `#e3e6ec` | neutral | Page background or card surface |
| Ash Gray | `#c8c9cf` | neutral | Border, muted text, or supporting surface |
| Midnight Graphite | `#333333` | neutral | Primary text or dark surface |
| Muted Silver | `#7f8087` | neutral | Border, muted text, or supporting surface |
| Frost Teal | `#c5fbee` | accent | Action accent / signal color |
| Viewport Violet | `#4d4dff` | brand | Action accent / signal color |
| Aqua Glow | `#66dff7` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-cloud-gray: #f8f9fa;
  --ref-stone-gray: #e3e6ec;
  --ref-ash-gray: #c8c9cf;
  --ref-midnight-graphite: #333333;
  --ref-muted-silver: #7f8087;
  --ref-frost-teal: #c5fbee;
}
```

## Typography direction
- **Silka Medium Italic**: 400, 18px, 1.2.
- **HK Sentiments Bold**: 400, 700, 24px, 28px, 32px, 1.10, 1.20; substitute `Georgia`.
- **Silka**: 400, 500, 14px, 16px, 18px, 1.00, 1.20, 1.30; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `12px`
- Radius: `cards: 16px, pills: 100px, buttons: 12px, controls: 8px`

## Component cues
- **Primary Filled Button**: Call to action with full visual emphasis
- **Ghost Button**: Secondary action or navigation link with minimal visual weight
- **Navigation Link**: Tertiary navigation or inline links
- **Feature Card (Default)**: Container for content blocks, features information
- **Feature Card (Ambient)**: Container for content, with a subtle background color

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
