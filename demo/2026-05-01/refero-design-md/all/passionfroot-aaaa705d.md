# Passionfroot - Refero Design MD

- Source: https://styles.refero.design/style/aaaa705d-3042-4355-ad30-13360f04e403
- Original site: https://www.passionfroot.me
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whimsical data observatory

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#1d1d1c` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Surface Frost | `#f8f7f2` | neutral | Page background or card surface |
| Ash Gray | `#43423e` | neutral | Border, muted text, or supporting surface |
| Subtle Stone | `#d8d6ce` | neutral | Border, muted text, or supporting surface |
| Lilac Dream | `#b26bf5` | accent | Action accent / signal color |
| Cherry Blossom | `#f788d2` | accent | Action accent / signal color |
| Sunset Orange | `#ff9147` | accent | Action accent / signal color |
| Sky Teal | `#4ad5e8` | accent | Action accent / signal color |
| Ocean Blue | `#51b1fb` | accent | Action accent / signal color |

```css
:root {
  --ref-ink-black: #1d1d1c;
  --ref-canvas-white: #ffffff;
  --ref-surface-frost: #f8f7f2;
  --ref-ash-gray: #43423e;
  --ref-subtle-stone: #d8d6ce;
  --ref-lilac-dream: #b26bf5;
  --ref-cherry-blossom: #f788d2;
  --ref-sunset-orange: #ff9147;
}
```

## Typography direction
- **new-kansas**: 400, 500, 16px, 20px, 28px, 48px, 64px, 1.00, 1.20, 1.25, 1.35, 1.45, 1.50; substitute `Georgia or Libre Baskerville`.
- **Nunito Sans**: 400, 500, 600, 700, 10px, 12px, 14px, 15px, 16px, 18px, 20px, 1.00, 1.25, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63; substitute `Open Sans or Lato`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `pill: 9999px, large: 16px, default: 12px, extraLarge: 24px`

## Surface cues
- **Page Background** `#f8f7f2`: The foundational canvas for the entire page, providing a subtle off-white base.
- **Primary Card Surface** `#ffffff`: Used for most interactive cards, buttons, and content blocks, offering a crisp, clean background.
- **Elevated Component Surface** `#f3e8ff`: A very light, almost white accent surface primarily seen on pill-shaped buttons and subtle interactive elements.

## Component cues
- **Primary Filled Button**: Call to action, primary interaction.
- **Ghost Button (Header)**: Secondary actions in navigation.
- **Text Button**: Tertiary actions, inline links within controls.
- **Pill Button**: Categorization, filters, small contextual actions.
- **Feature Card (Achromatic)**: Content presentation, informational blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
