# Tuple - Refero Design MD

- Source: https://styles.refero.design/style/1003d7c5-536c-485d-b191-a34178415eac
- Original site: https://tuple.app
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp developer canvas.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Canvas Fog | `#f4f4f5` | neutral | Page background or card surface |
| Border Ash | `#e4e4e7` | neutral | Page background or card surface |
| Content Graphite | `#71717a` | neutral | Border, muted text, or supporting surface |
| Text Slate | `#27272a` | neutral | Primary text or dark surface |
| Dark Border Zinc | `#52525b` | neutral | Border, muted text, or supporting surface |
| Dark Accent Charcoal | `#3f3f46` | neutral | Primary text or dark surface |
| Grape Action | `#6a5ed9` | brand | Action accent / signal color |
| Sky Brand | `#3f71d4` | brand | Action accent / signal color |
| Sunset Orange | `#db5434` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-canvas-fog: #f4f4f5;
  --ref-border-ash: #e4e4e7;
  --ref-content-graphite: #71717a;
  --ref-text-slate: #27272a;
  --ref-dark-border-zinc: #52525b;
  --ref-dark-accent-charcoal: #3f3f46;
  --ref-grape-action: #6a5ed9;
}
```

## Typography direction
- **Inter Variable**: 400, 500, 600, 700, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 36px, 48px, 60px, 1.00, 1.11, 1.14, 1.20, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63; substitute `Inter`.
- **DM Mono**: 400, 500, 11px, 12px, 13px, 14px, 16px, 1.33, 1.43, 1.50, 1.63; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `32px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `tags: 9999px, cards: 12px, input: 8px, large: 24px, small: 8px, buttons: 12px, default: 12px, navItem: 4px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background and default layer for most content and components.
- **Canvas Fog** `#f4f4f5`: Secondary background for distinct sections or subtle card surfaces, differentiating from the base canvas.
- **Dark Surface** `#27272a`: Background for dedicated dark mode sections or elevated components within a dark context, creating strong contrast.

## Component cues
- **Primary Action Button**: Main call-to-action
- **Default Card**: Content container
- **Subtle Card**: Secondary content container
- **Dark Elevated Card**: Content container in dark sections
- **Alert Banner**: Prominent announcements

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
