# Dovetail - Refero Design MD

- Source: https://styles.refero.design/style/6f9452a4-3b64-4c6f-a05e-528d7a586f24
- Original site: https://dovetailapp.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Night | `#0a0a0a` | neutral | Primary text or dark surface |
| Graphite | `#1e1e1e` | neutral | Primary text or dark surface |
| Abyssal Plane | `#141414` | neutral | Primary text or dark surface |
| Ghost | `#313131` | neutral | Primary text or dark surface |
| Ash | `#454545` | neutral | Border, muted text, or supporting surface |
| Skybound Violet | `#6798ff` | brand | Action accent / signal color |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Silver Pine | `#a7a7a7` | neutral | Border, muted text, or supporting surface |
| Stone Dust | `#7c7c7c` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-deep-night: #0a0a0a;
  --ref-graphite: #1e1e1e;
  --ref-abyssal-plane: #141414;
  --ref-ghost: #313131;
  --ref-ash: #454545;
  --ref-skybound-violet: #6798ff;
  --ref-pure-white: #ffffff;
  --ref-silver-pine: #a7a7a7;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 14px, 16px, 20px, 24px, 40px, 56px, 64px, 1.13, 1.14, 1.20, 1.29, 1.33, 1.40, 1.50, 1.57; substitute `system-ui`.
- **JetBrains Mono**: 400, 12px, 14px, 1.00, 1.40; substitute `monospace`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `tags: 4px, cards: 8px, buttons: 8px, prominent-card: 66px`

## Surface cues
- **Absolute Canvas** `#0a0a0a`: Primary HTML body and large section backgrounds, lowest visual plane.
- **Card Surface** `#141414`: Standard content cards and containers, slightly elevated from the canvas.
- **Interactive Surface** `#1e1e1`: Backgrounds for interactive components like buttons and certain UI controls, visually distinct.

## Component cues
- **Ghost Navigation Button**: Primary navigation and subtle actions in headers
- **Subtle Nav Button**: Secondary navigation items, subtly interactive elements
- **Standard Button**: General purpose call-to-action buttons
- **Outlined Elevated Button**: Secondary call-to-action, ghost buttons with higher prominence
- **Prominent Spotlight Card**: Highlighted content panels, visual breaks with strong presence

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
