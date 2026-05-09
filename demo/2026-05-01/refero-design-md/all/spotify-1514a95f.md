# Spotify - Refero Design MD

- Source: https://styles.refero.design/style/1514a95f-878c-4d4d-bb14-99d1b83f6227
- Original site: https://spotify.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight command center, where content glows against a deep, dark stage.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Night | `#121212` | neutral | Primary text or dark surface |
| Surface Charcoal | `#292929` | neutral | Primary text or dark surface |
| Card Base | `#1f1f1f` | neutral | Primary text or dark surface |
| Input Dark | `#333333` | neutral | Primary text or dark surface |
| Overlay Black | `#000000` | neutral | Primary text or dark surface |
| Text Primary White | `#ffffff` | neutral | Page background or card surface |
| Text Secondary Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Text Muted Graphite | `#73777c` | neutral | Border, muted text, or supporting surface |
| Input Placeholder | `#c5c5c5` | neutral | Border, muted text, or supporting surface |
| Content Red | `#b85850` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-night: #121212;
  --ref-surface-charcoal: #292929;
  --ref-card-base: #1f1f1f;
  --ref-input-dark: #333333;
  --ref-overlay-black: #000000;
  --ref-text-primary-white: #ffffff;
  --ref-text-secondary-gray: #b3b3b3;
  --ref-text-muted-graphite: #73777c;
}
```

## Typography direction
- **SpotifyMixUI**: 400, 11px, 12px, 13px, 14px, 16px, 1.20, 1.33, 1.50; substitute `Arial`.
- **SpotifyMixUITitle**: 700, 24px, 1.20; substitute `Arial Black`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `8px`
- Page Max Width: `1085px`
- Radius: `misc: 2px, cards: 6px, image: 6px, input: 500px, buttons: 9999px`

## Component cues
- **Primary Ghost Button**: Interactive Element
- **Text Link Button**: Interactive Element
- **Muted Ghost Button**: Interactive Element
- **Primary Filled Button**: Interactive Element
- **Content Card**: Content Display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
