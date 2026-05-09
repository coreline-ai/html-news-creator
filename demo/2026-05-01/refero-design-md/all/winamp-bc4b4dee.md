# Winamp - Refero Design MD

- Source: https://styles.refero.design/style/bc4b4dee-8b32-494c-9a2d-d56fcd450b79
- Original site: https://www.winamp.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp digital canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#18181b` | neutral | Primary text or dark surface |
| Fog | `#f7f7f7` | neutral | Page background or card surface |
| Storm Gray | `#71717a` | neutral | Border, muted text, or supporting surface |
| Midnight Ash | `#09090b` | neutral | Primary text or dark surface |
| Silver Whisper | `#a1a1aa` | neutral | Border, muted text, or supporting surface |
| Cloud Burst | `#d4d4d8` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-arctic-white: #ffffff;
  --ref-graphite: #18181b;
  --ref-fog: #f7f7f7;
  --ref-storm-gray: #71717a;
  --ref-midnight-ash: #09090b;
  --ref-silver-whisper: #a1a1aa;
  --ref-cloud-burst: #d4d4d8;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'`.
- **Poppins**: 400, 500, 600, 700, 12px, 13px, 15px, 19px, 24px, 34px, 69px, 1.13, 1.18, 1.25, 1.26, 1.33, 1.50, 1.60, 1.62; substitute `sans-serif`.
- **Rubik**: 400, 12px, 1.50; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `cards: 16px, buttons: 8px, general: 12px`

## Component cues
- **Primary Filled Button**: Navigational call to action
- **Ghost Button**: Secondary action or subtle navigation
- **Light Card**: Content container
- **Dark Card**: Emphasized content container
- **Navigation Link**: Top-level navigation items

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
