# Sanity.io - Refero Design MD

- Source: https://styles.refero.design/style/a3af7369-b61c-4923-a628-931861c8097f
- Original site: https://sanity.io
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Data grid, pulsing with neon light. A clean terminal-like layout where vibrant color accents pinpoint critical information within structured data.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Black | `#0b0b0b` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#212121` | neutral | Primary text or dark surface |
| Medium Gray | `#b9b9b9` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#797979` | neutral | Border, muted text, or supporting surface |
| Pumpkin Spill | `#ff4100` | brand | Action accent / signal color |
| Electric Blue | `#0052ef` | brand | Action accent / signal color |
| Neon Green | `#45ff00` | accent | Action accent / signal color |
| Terminal Green | `#19d600` | accent | Action accent / signal color |
| Future Violet | `#f500ff` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-black: #0b0b0b;
  --ref-canvas-white: #ffffff;
  --ref-graphite: #212121;
  --ref-medium-gray: #b9b9b9;
  --ref-silver-mist: #797979;
  --ref-pumpkin-spill: #ff4100;
  --ref-electric-blue: #0052ef;
  --ref-neon-green: #45ff00;
}
```

## Typography direction
- **Waldenburg Normal**: 400, 425, 500, 600, 11px, 12px, 13px, 15px, 16px, 18px, 20px, 24px, 32px, 38px, 48px, 60px, 72px, 112px, 0.80, 1.00, 1.05, 1.08, 1.10, 1.13, 1.20, 1.24, 1.30, 1.50; substitute `system-ui, sans-serif`.
- **IBM Plex Mono**: 400, 500, 10px, 12px, 13px, 15px, 1.30, 1.40, 1.50, 1.70; substitute `SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `12px`
- Radius: `cards: 12px, buttons: 99999px, default: 0px, input-sm: 3px, buttons-sm: 6px`

## Component cues
- **Button Group**: Reference component style.
- **Feature Tab Selector**: Reference component style.
- **Announcement Banner + Stats Block**: Reference component style.
- **Primary Ghost Button (Dark)**: Primary calls to action on dark backgrounds
- **Pill Ghost Button (Dark)**: Secondary actions on dark backgrounds, navigation elements

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
