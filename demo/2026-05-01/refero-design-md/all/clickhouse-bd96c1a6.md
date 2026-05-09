# ClickHouse - Refero Design MD

- Source: https://styles.refero.design/style/bd96c1a6-32ba-42e0-bd5c-23c70a23142c
- Original site: https://clickhouse.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Terminal Console with Chartreuse Zap — a focused dark UI with high-contrast, almost neon, interactive highlights.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Oil | `#151515` | neutral | Primary text or dark surface |
| Smokey Carbon | `#1f1f1c` | neutral | Primary text or dark surface |
| Deep Graphite | `#282828` | neutral | Primary text or dark surface |
| Iron Oxide | `#343434` | neutral | Primary text or dark surface |
| Cool Stone | `#3a3a3a` | neutral | Primary text or dark surface |
| Muted Ash | `#414141` | neutral | Border, muted text, or supporting surface |
| Shadow White | `#a0a0a0` | neutral | Border, muted text, or supporting surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Highlight Silver | `#dfdfdf` | neutral | Page background or card surface |
| Silken Whisper | `#bcbcbb` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-oil: #151515;
  --ref-smokey-carbon: #1f1f1c;
  --ref-deep-graphite: #282828;
  --ref-iron-oxide: #343434;
  --ref-cool-stone: #3a3a3a;
  --ref-muted-ash: #414141;
  --ref-shadow-white: #a0a0a0;
  --ref-cloud-white: #ffffff;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 900, 12px, 14px, 16px, 18px, 20px, 24px, 72px, 96px, 1.00, 1.33, 1.38, 1.40, 1.43, 1.50, 1.56; substitute `system-ui, sans-serif`.
- **Basier**: 600, 20px, 24px, 36px, 1.17, 1.30, 1.40; substitute `system-ui, sans-serif`.
- **Inconsolata**: 600, 16px, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `tags: 4px, cards: 8px, buttons: 9999px, inputField: 4px`

## Component cues
- **Use Case Feature Cards**: Reference component style.
- **FAQ Accordion**: Reference component style.
- **Install Code Block & CTA**: Reference component style.
- **Primary Action Button**: Main call to action
- **Secondary Outline Button**: Alternative actions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
