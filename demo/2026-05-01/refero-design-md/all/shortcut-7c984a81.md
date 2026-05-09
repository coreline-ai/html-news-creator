# Shortcut - Refero Design MD

- Source: https://styles.refero.design/style/7c984a81-a08f-41a3-b790-8d4a9ed92031
- Original site: https://www.shortcut.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
organized data, muted luminescence

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#08093f` | neutral | Primary text or dark surface |
| Slate Text | `#686878` | neutral | Border, muted text, or supporting surface |
| Shortcut Violet | `#494bcb` | brand | Action accent / signal color |
| Sunshine Yellow | `#ffde87` | semantic | Action accent / signal color |
| Iris Tint | `#9f7ad0` | accent | Action accent / signal color |
| Link Blue | `#8a8ac6` | accent | Action accent / signal color |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pewter Mist | `#f6f6fa` | neutral | Page background or card surface |
| Ash Gray | `#6d737d` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #08093f;
  --ref-slate-text: #686878;
  --ref-shortcut-violet: #494bcb;
  --ref-sunshine-yellow: #ffde87;
  --ref-iris-tint: #9f7ad0;
  --ref-link-blue: #8a8ac6;
  --ref-jet-black: #000000;
  --ref-canvas-white: #ffffff;
}
```

## Typography direction
- **Satoshi**: 500, 700, 10px, 13px, 14px, 15px, 17px, 19px, 21px, 46px, 61px, 1.10, 1.25, 1.27, 1.28, 1.30, 1.50, 1.60, 1.80; substitute `Inter, Arial`.

## Spacing / shape
- Section Gap: `73px`
- Card Padding: `19px`
- Element Gap: `4px`
- Page Max Width: `1200px`
- Radius: `cards: 15.24px, badges: 35.81px, buttons: 7.62px, default: 7.62px`

## Surface cues
- **Page Canvas** `#ffffff`: Dominant background for most page content.
- **Secondary Section** `#f6f6fa`: Alternating background for content sections and subtle card backgrounds.
- **Elevated Card** `#ffffff`: Cards or containers that need slight visual separation and depth.
- **Hero/Footer Wash** `#08093f`: Dark, immersive backgrounds for prominent hero sections and footers.

## Component cues
- **Primary Filled Button**: Main call-to-action.
- **Secondary Ghost Button**: Complementary actions.
- **Text Outline Button**: Minimalist interactive elements.
- **Hero Light Button**: Action for dark hero sections.
- **Feature Card (Subtle Shadow)**: Content modules requiring light elevation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
