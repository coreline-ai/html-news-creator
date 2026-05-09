# WRITER - Refero Design MD

- Source: https://styles.refero.design/style/ddd9ffaa-d831-4cb4-a5bf-a1efce421dca
- Original site: https://writer.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
AI-powered clarity on a pristine canvas. Like crisp code on a luminous display.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Slate Gray | `#2d2d2d` | neutral | Primary text or dark surface |
| Cloud White | `#e4e7ed` | neutral | Page background or card surface |
| Fog | `#d2d4d7` | neutral | Border, muted text, or supporting surface |
| Ghost Gray | `#bdbdbd` | neutral | Border, muted text, or supporting surface |
| Lavender Mist | `#e4e9ff` | neutral | Page background or card surface |
| Agent Violet | `#a95ef8` | brand | Action accent / signal color |
| Action Blue | `#5551ff` | accent | Action accent / signal color |
| Electric Blue | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #000000;
  --ref-canvas-white: #ffffff;
  --ref-slate-gray: #2d2d2d;
  --ref-cloud-white: #e4e7ed;
  --ref-fog: #d2d4d7;
  --ref-ghost-gray: #bdbdbd;
  --ref-lavender-mist: #e4e9ff;
  --ref-agent-violet: #a95ef8;
}
```

## Typography direction
- **Poppins**: 400, 500, 600, 700, 11px, 12px, 13px, 14px, 16px, 18px, 20px, 25px, 40px, 44px, 64px, 1.00, 1.15, 1.20, 1.25, 1.40, 1.50, 1.55, 1.60, 1.66, 1.67, 1.75; substitute `system-ui, sans-serif`.
- **CanelaDeck**: 400, 16px, 1.20; substitute `serif`.

## Spacing / shape
- Card Padding: `0px`
- Element Gap: `8-20px`
- Page Max Width: `1136px`
- Radius: `images: 12px, inputs: 72px, buttons: 60px, 82px, general: 50px`

## Component cues
- **Hero Email CTA Form**: Reference component style.
- **Writer Agent Section CTA**: Reference component style.
- **Resources Cards — Dark Section**: Reference component style.
- **Primary Call to Action Button**: Interactive element
- **Search/Email Input Field**: Form Element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
