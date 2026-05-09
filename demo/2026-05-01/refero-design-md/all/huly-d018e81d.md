# Huly - Refero Design MD

- Source: https://styles.refero.design/style/d018e81d-6bb6-4445-86d7-39fd6be7e74d
- Original site: https://huly.io
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#090a0c` | neutral | Primary text or dark surface |
| Charcoal Grey | `#111111` | neutral | Primary text or dark surface |
| Shadow Ink | `#303236` | neutral | Primary text or dark surface |
| Ash Cloud | `#4a4b50` | neutral | Border, muted text, or supporting surface |
| Storm Grey | `#61656b` | neutral | Border, muted text, or supporting surface |
| Battleship Grey | `#95979e` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#a9a9aa` | neutral | Border, muted text, or supporting surface |
| Cloud Burst | `#d1d1d1` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Electric Blue | `#5683da` | brand | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #090a0c;
  --ref-charcoal-grey: #111111;
  --ref-shadow-ink: #303236;
  --ref-ash-cloud: #4a4b50;
  --ref-storm-grey: #61656b;
  --ref-battleship-grey: #95979e;
  --ref-silver-mist: #a9a9aa;
  --ref-cloud-burst: #d1d1d1;
}
```

## Typography direction
- **Esbuild**: 400, 500, 600, 28px, 32px, 80px, 84px, 0.80, 0.90, 1.00; substitute `Montserrat`.
- **Inter**: 300, 400, 500, 600, 700, 10px, 11px, 12px, 14px, 15px, 16px, 18px, 22px, 24px, 1.00, 1.13, 1.25, 1.38, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `73px`
- Card Padding: `12px`
- Element Gap: `12px`
- Page Max Width: `1280px`
- Radius: `tags: 9999px, cards: 12px, lists: 30px, inputs: 4px, buttons: 9999px`

## Surface cues
- **Pitch Black Canvas** `#090a0c`: Base background for the entire application, creating a deep dark mode foundation.
- **Charcoal Grey Card** `#111111`: Primary surface for cards, content blocks, and subtle segmentation within the dark canvas.
- **Ash Cloud Overlay** `#4a4b50`: Used for interactive elements or modal backgrounds that appear on top of cards, indicating a higher interaction layer.
- **Silver Mist Panel** `#d1d1d1`: Ghost button backgrounds and elements that require a stark contrast or highlighted status within the dark UI.

## Component cues
- **Primary Action Button**: Main call-to-action
- **Ghost Primary Button**: Secondary call-to-action
- **Pill Button**: Tertiary action or filter tag
- **Navigation Link**: Top navigation item
- **Standard Card**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
