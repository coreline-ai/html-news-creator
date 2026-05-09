# Design Full-Time - Refero Design MD

- Source: https://styles.refero.design/style/80b2cc74-62c5-4898-bc2b-12aa94ed2943
- Original site: https://designfulltime.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark mode command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Charcoal Black | `#111111` | neutral | Primary text or dark surface |
| Whisper White | `#ffffff` | neutral | Page background or card surface |
| Slate Gray | `#888888` | neutral | Border, muted text, or supporting surface |
| Cool Steel | `#a0a0a0` | neutral | Border, muted text, or supporting surface |
| Faded Ink | `#2c3e50` | neutral | Primary text or dark surface |
| Midnight Graphite | `#343434` | neutral | Primary text or dark surface |
| Sunset Fire Light | `#ffc840` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-charcoal-black: #111111;
  --ref-whisper-white: #ffffff;
  --ref-slate-gray: #888888;
  --ref-cool-steel: #a0a0a0;
  --ref-faded-ink: #2c3e50;
  --ref-midnight-graphite: #343434;
  --ref-sunset-fire-light: #ffc840;
}
```

## Typography direction
- **Inter**: 400, 600, 700, 800, 15px, 16px, 18px, 20px, 24px, 1.00, 1.33, 1.40, 1.50, 1.56; substitute `system-ui`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `none: 0px`

## Component cues
- **Primary Filled Button**: Interactive element for key actions
- **Coming Soon Tag**: Informational label
- **Promotional Banner**: Highlighting special offers
- **Video Thumbnail Card**: Container for video content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
