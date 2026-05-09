# Mesh - Refero Design MD

- Source: https://styles.refero.design/style/1a03b8d7-9204-4c16-ad3c-16306f99fba9
- Original site: https://clay.earth
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight archive behind frosted glass

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Night | `#0f0f10` | neutral | Primary text or dark surface |
| Graphite | `#1d1d1f` | neutral | Primary text or dark surface |
| Moonless Ink | `#000000` | neutral | Primary text or dark surface |
| Silver Whisper | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Cloud White | `#fefef7` | neutral | Page background or card surface |
| Warm Mist | `#868f97` | neutral | Border, muted text, or supporting surface |
| Pale Stone | `#86868b` | neutral | Border, muted text, or supporting surface |
| Amber Glow | `#f2b98b` | brand | Action accent / signal color |
| Sunset Blush | `#ffaf7c` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-night: #0f0f10;
  --ref-graphite: #1d1d1f;
  --ref-moonless-ink: #000000;
  --ref-silver-whisper: #b3b3b3;
  --ref-ash-gray: #666666;
  --ref-cloud-white: #fefef7;
  --ref-warm-mist: #868f97;
  --ref-pale-stone: #86868b;
}
```

## Typography direction
- **Verlag**: 400, 600, 700, 9px, 10px, 12px, 14px, 16px, 18px, 20px, 1.00, 1.10, 1.33, 1.35, 1.38, 1.40, 1.50, 1.69, 2.25, 2.70, 3.00; substitute `Inter`.
- **VerlagCondensed**: 700, 900, 48px, 64px, 1.00; substitute `Oswald`.
- **ChronicleTextG1Roman**: 400, 22px, 1.55; substitute `Lora`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `cards: 16px, badges: 12px, images: 36px, buttons: 6px`

## Surface cues
- **Deep Night** `#0f0f10`: Base page background, deepest layer.
- **Graphite** `#1d1d1f`: Primary interactive surfaces, content containers within the page, eg. sidebars, lists not in cards.
- **Floating Card Surface** `#ffffff`: Elevated cards or modals, with 70% opacity and a distinct shadow for depth.

## Component cues
- **Ghost Navigation Button**: Header navigation and secondary actions
- **Outline Action Button**: Primary calls to action with an understated, interactive glow.
- **Floating Card**: Content groupings that gently rise above the dark background.
- **Subtle Badge**: Informational tags or status indicators within content.
- **Elevated Badge**: Highlighted tags or active filters

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
