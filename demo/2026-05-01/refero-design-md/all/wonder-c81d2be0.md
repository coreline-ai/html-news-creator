# Wonder - Refero Design MD

- Source: https://styles.refero.design/style/c81d2be0-05b7-4755-8046-f2d19fbc448c
- Original site: https://wonder.design
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep canvas, fuchsia accent

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Plum | `#0f0217` | neutral | Primary text or dark surface |
| Ghost Ink | `#0b0211` | neutral | Primary text or dark surface |
| Off-Black | `#111111` | neutral | Primary text or dark surface |
| Bright Snow | `#ffffff` | neutral | Page background or card surface |
| Silver Mist | `#e1e4e8` | neutral | Page background or card surface |
| Border Violet | `#44374a` | neutral | Action accent / signal color |
| Muted Ash | `#6f6774` | neutral | Border, muted text, or supporting surface |
| Charcoal Grey | `#737373` | neutral | Border, muted text, or supporting surface |
| Fuchsia Burst | `#d262ff` | brand | Action accent / signal color |
| Deep Orchid | `#6a1791` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-plum: #0f0217;
  --ref-ghost-ink: #0b0211;
  --ref-off-black: #111111;
  --ref-bright-snow: #ffffff;
  --ref-silver-mist: #e1e4e8;
  --ref-border-violet: #44374a;
  --ref-muted-ash: #6f6774;
  --ref-charcoal-grey: #737373;
}
```

## Typography direction
- **Uncut Sans Variable**: 400, 500, 600, 14px, 15px, 16px, 18px, 24px, 38px, 50px, 1.10, 1.12, 1.33, 1.43, 1.45, 1.50, 1.56; substitute `system-ui, sans-serif`.
- **Inter**: 400, 500, 600, 700, 8px, 10px, 11px, 12px, 14px, 15px, 16px, 24px, 28px, 1.20, 1.25, 1.33, 1.43, 1.50, 1.60, 1.63; substitute `Inter, sans-serif`.
- **Martian Mono**: 400, 10px, 11px, 12px, 1.50, 1.63; substitute `monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `cards: 14px, badges: 9999px, inputs: 9999px, buttons: 8px, navItems: 8px`

## Surface cues
- **Base Canvas** `#0f0217`: Dominant background for the entire application and main page sections.
- **Card Surface** `#0b0211`: Background for contained interface blocks like cards and slightly elevated components.
- **Input Background** `#2b1a12`: Background for interactive input fields and controls, offering a slight visual distinction.

## Component cues
- **Primary Action Button**: Filled action button
- **Ghost Outline Button**: Secondary action button
- **Navigation Link**: Navigation links and subtle interactive text
- **Transparent Card**: Informational display card
- **Elevated Content Card**: Important content display card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
