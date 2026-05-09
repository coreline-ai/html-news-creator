# OpenAI Developers - Refero Design MD

- Source: https://styles.refero.design/style/5c94c49f-0612-4261-842c-e1d501f3e13d
- Original site: https://developers.openai.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprints on frosted glass. A digital space that feels both precise and slightly translucent, built on foundational whites and grays.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#f9f9f9` | neutral | Page background or card surface |
| Whisper Gray | `#ededed` | neutral | Page background or card surface |
| Slate Text | `#282828` | neutral | Primary text or dark surface |
| Graphite Text | `#5d5d5d` | neutral | Border, muted text, or supporting surface |
| Subtle Gray | `#64748b` | neutral | Border, muted text, or supporting surface |
| Shadow | `#000000` | neutral | Primary text or dark surface |
| Input Pale | `#f3f3f3` | neutral | Page background or card surface |
| Dark Overlay | `#181818` | neutral | Primary text or dark surface |
| Accent Black | `#0d0d0d` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-cloud-gray: #f9f9f9;
  --ref-whisper-gray: #ededed;
  --ref-slate-text: #282828;
  --ref-graphite-text: #5d5d5d;
  --ref-subtle-gray: #64748b;
  --ref-shadow: #000000;
  --ref-input-pale: #f3f3f3;
}
```

## Typography direction
- **OpenAI Sans**: 400, 500, 600, 12px, 14px, 16px, 18px, 20px, 30px, 1.00, 1.30, 1.33, 1.38, 1.40, 1.43, 1.50, 1.63, 1.75; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `4px`
- Page Max Width: `1200px`
- Radius: `cards: 8px, banners: 10px, buttons: 9999px, default: 8px, callouts: 10px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background
- **Cloud Gray** `#f9f9f9`: Elevated card and section backgrounds
- **Whisper Gray** `#ededed`: Secondary card backgrounds, active navigation elements

## Component cues
- **Primary Navigation Link**: Navigation item
- **API Dashboard Button**: Call to action button
- **Search Input Field**: Search interface element
- **Info Callout Card**: Informational alert/highlight
- **Feature Card (Default)**: Interactive content display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
