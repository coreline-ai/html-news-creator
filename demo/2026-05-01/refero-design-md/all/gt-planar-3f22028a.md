# Gt-planar - Refero Design MD

- Source: https://styles.refero.design/style/3f22028a-05d4-4648-a6d1-591134af06a4
- Original site: https://gt-planar.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight mainframe with glowing terminals.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Screen White | `#ffffff` | neutral | Page background or card surface |
| Input Dark | `#1a0014` | neutral | Primary text or dark surface |
| Subtle Gray | `#949494` | neutral | Border, muted text, or supporting surface |
| Border Gray | `#606060` | neutral | Border, muted text, or supporting surface |
| Electric Violet | `#6100ff` | brand | Action accent / signal color |
| Fluorescent Green | `#00ff85` | brand | Action accent / signal color |
| Deep Space Violet | `#29006c` | accent | Action accent / signal color |
| Safety Yellow | `#fcff76` | accent | Action accent / signal color |
| Alert Red | `#ff003d` | accent | Action accent / signal color |

```css
:root {
  --ref-void-black: #000000;
  --ref-screen-white: #ffffff;
  --ref-input-dark: #1a0014;
  --ref-subtle-gray: #949494;
  --ref-border-gray: #606060;
  --ref-electric-violet: #6100ff;
  --ref-fluorescent-green: #00ff85;
  --ref-deep-space-violet: #29006c;
}
```

## Typography direction
- **GT Planar**: 300, 400, 700, 11px, 14px, 16px, 17px, 20px, 24px, 25px, 32px, 37px, 58px, 86px, 115px, 146px, 187px, 230px, 274px, 0.80, 0.90, 0.95, 1.00, 1.09, 1.10, 1.14, 1.15, 1.17, 1.19, 1.20, 1.24, 1.43, 1.50, 1.63; substitute `Space Mono, IBM Plex Mono`.

## Spacing / shape
- Section Gap: `25px`
- Card Padding: `25px`
- Element Gap: `5px`
- Radius: `tags: 9999px, buttons: 9999px, default: 0px`

## Surface cues
- **Canvas** `#000000`: Primary page background, deep void for content.
- **Input Surface** `#1a0014`: Input fields and subtly recessed interactive areas.
- **Elevated Violet Surface** `#29006c`: Background for secondary interactive elements or elevated content modules.

## Component cues
- **Primary Action Button (Violet Fill)**: Main interactive element for actions.
- **Outlined Button (Violet Border)**: Secondary action or ghost button.
- **Dark Elevated Button (Violet Border)**: Tertiary action or grouped controls.
- **Fluorescent Action Button**: Prominent, high-contrast call to action.
- **Text Input**: Data entry fields.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
