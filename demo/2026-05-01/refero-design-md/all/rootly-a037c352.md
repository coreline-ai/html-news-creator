# Rootly - Refero Design MD

- Source: https://styles.refero.design/style/a037c352-4315-4650-a16c-08392ffca597
- Original site: https://rootly.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Violet-tinged command center behind frosted glass.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#100f12` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Haze White | `#fbfaff` | neutral | Page background or card surface |
| Cadet Violet | `#d9cffa` | brand | Action accent / signal color |
| Deep Space Violet | `#8d6fde` | brand | Action accent / signal color |
| Lavender Mist | `#ebe5ff` | brand | Action accent / signal color |
| Graphite Feather | `#787685` | neutral | Border, muted text, or supporting surface |
| Nightfall Violet | `#4a3e8a` | brand | Action accent / signal color |
| Ash Grey | `#65646e` | neutral | Border, muted text, or supporting surface |
| Faded Stone | `#aaa9ae` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #100f12;
  --ref-canvas-white: #ffffff;
  --ref-haze-white: #fbfaff;
  --ref-cadet-violet: #d9cffa;
  --ref-deep-space-violet: #8d6fde;
  --ref-lavender-mist: #ebe5ff;
  --ref-graphite-feather: #787685;
  --ref-nightfall-violet: #4a3e8a;
}
```

## Typography direction
- **Ppmori**: 200, 500, 600, 10px, 12px, 14px, 16px, 17px, 31px, 52px, 1.00, 1.03, 1.20, 1.30, 1.40, 1.43, 1.45, 1.46; substitute `Inter`.

## Spacing / shape
- Section Gap: `42px`
- Card Padding: `14px`
- Element Gap: `7px`
- Page Max Width: `1600px`
- Radius: `full: 1440px, large: 34.6px, small: 13.84px, medium: 17.3px, xsmall: 6.92px`

## Surface cues
- **Haze White Canvas** `#fbfaff`: Base page background, providing a soft, almost imperceptible off-white foundation.
- **Lavender Mist Card** `#ebe5ff`: Background for secondary content cards or sections, offering a gentle visual lift from the canvas.
- **Canvas White Element** `#ffffff`: Background for primary interactive elements like buttons, header, and active states, creating distinct contrast and visual hierarchy.

## Component cues
- **Primary Filled Button**: Main call to action button.
- **Secondary Filled Button (Canvas)**: Secondary call to action, often paired with primary button.
- **Ghost Button**: Tertiary action or navigational button within text.
- **Light Card**: Content container with a soft background.
- **Accent Card**: Highlighted content container.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
