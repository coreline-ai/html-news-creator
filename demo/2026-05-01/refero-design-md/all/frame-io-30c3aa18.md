# Frame.io - Refero Design MD

- Source: https://styles.refero.design/style/30c3aa18-4323-4448-8ddd-3ca933fe5780
- Original site: https://frame.io
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight control panel, glowing with purpose.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Void Black | `#0a0a13` | neutral | Primary text or dark surface |
| Dark Nebula | `#08080c` | neutral | Primary text or dark surface |
| Twilight Graphite | `#757580` | neutral | Border, muted text, or supporting surface |
| Cloud Whisper | `#fcfcfc` | neutral | Page background or card surface |
| Pale Ash | `#a3a3b3` | neutral | Border, muted text, or supporting surface |
| Frost Gleam | `#dedfee` | neutral | Page background or card surface |
| Electric Indigo | `#6199f6` | accent | Action accent / signal color |
| Cosmic Violet | `#5b53ff` | accent | Action accent / signal color |
| Peripheral Haze Gradient | `#000b35` | brand | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-void-black: #0a0a13;
  --ref-dark-nebula: #08080c;
  --ref-twilight-graphite: #757580;
  --ref-cloud-whisper: #fcfcfc;
  --ref-pale-ash: #a3a3b3;
  --ref-frost-gleam: #dedfee;
  --ref-electric-indigo: #6199f6;
}
```

## Typography direction
- **FrameGothic**: 400, 500, 600, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 24px, 30px, 38px, 48px, 80px, 0.96, 1.00, 1.02, 1.04, 1.16, 1.20, 1.25, 1.30, 1.45, 1.50; substitute `Inter`.
- **NeueMachinaInktrap**: 400, 12px, 0.90; substitute `IBM Plex Mono`.
- **Times**: 400, 10px, 1.00; substitute `Lora`.

## Spacing / shape
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `cards: 24px, buttons: 100px, small-elements: 10px`

## Surface cues
- **Void Black** `#0a0a13`: Base page background, the deepest layer.
- **Dark Nebula** `#08080c`: Primary card and content block background, slightly raised from the base.
- **Nested UI Card Background** `#10101780`: Overlay for interactive or highlighted content, creating significant visual separation and depth.

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Cards Grid**: Reference component style.
- **Announcement Banner + Section Label**: Reference component style.
- **Primary Ghost Button**: Default interactive element for secondary actions.
- **Tertiary Ghost Button (Dark Text)**: Subtle interactive elements on lighter backgrounds or when contrast to white text needs adjustment.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
