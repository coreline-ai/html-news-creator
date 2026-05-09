# Spotify - Refero Design MD

- Source: https://styles.refero.design/style/cc59e195-fed0-4928-96d1-303752786073
- Original site: https://www.spotify.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Ebony Canvas, Spotlight Content

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ebony Canvas | `#000000` | neutral | Primary text or dark surface |
| Iron Accent | `#121212` | neutral | Primary text or dark surface |
| Charcoal Surface | `#1f1f1f` | neutral | Primary text or dark surface |
| Graphite Text | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Pure White Text | `#ffffff` | neutral | Page background or card surface |
| Muted Grey | `#767676` | neutral | Border, muted text, or supporting surface |
| Spotify Green | `#1ed760` | brand | Action accent / signal color |
| Signal Purple | `#6f74a4` | accent | Action accent / signal color |
| Deep Space Blue | `#1078a8` | accent | Action accent / signal color |
| Sunset Red | `#dc392b` | accent | Action accent / signal color |

```css
:root {
  --ref-ebony-canvas: #000000;
  --ref-iron-accent: #121212;
  --ref-charcoal-surface: #1f1f1f;
  --ref-graphite-text: #b3b3b3;
  --ref-pure-white-text: #ffffff;
  --ref-muted-grey: #767676;
  --ref-spotify-green: #1ed760;
  --ref-signal-purple: #6f74a4;
}
```

## Typography direction
- **SpotifyMixUI**: 400, 600, 700, 11px, 12px, 13px, 14px, 16px, 1.20, 1.33, 1.50; substitute `Inter`.
- **SpotifyMixUITitle**: 700, 24px, 1.20; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `12px`
- Page Max Width: `1085px`
- Radius: `input: 500px, buttons: 9999px, default: 6px, circular: 50%`

## Surface cues
- **Ebony Canvas** `#000000`: Base page background, deepest layer.
- **Iron Accent** `#121212`: Secondary background layer, cards, sidebar.
- **Charcoal Surface** `#1f1f1f`: Interactive elements, input fields, and active states.

## Component cues
- **Filled Button**: Primary action
- **Ghost Button**: Secondary action
- **High-Visibility Ghost Button**: Prominent secondary action
- **Media Content Card**: Content display
- **Container Card**: Grouped content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
