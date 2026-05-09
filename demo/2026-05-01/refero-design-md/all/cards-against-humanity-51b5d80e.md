# Cards Against Humanity - Refero Design MD

- Source: https://styles.refero.design/style/51b5d80e-d898-4d70-bd16-9e50406e014c
- Original site: https://www.cardsagainsthumanity.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast midnight game board

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Stinger Red | `#fe2f2f` | accent | Action accent / signal color |
| Jester Violet | `#7333f1` | accent | Action accent / signal color |
| Mischief Yellow | `#d7b73b` | accent | Action accent / signal color |
| Neon Yellow | `#fffe5b` | accent | Action accent / signal color |
| Ghostly Violet | `#ede5ff` | neutral | Action accent / signal color |
| Electric Blue | `#1b5bff` | accent | Action accent / signal color |
| Sky Blue | `#a0e9ff` | accent | Action accent / signal color |
| Vivid Pink | `#ffa0f0` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-stinger-red: #fe2f2f;
  --ref-jester-violet: #7333f1;
  --ref-mischief-yellow: #d7b73b;
  --ref-neon-yellow: #fffe5b;
  --ref-ghostly-violet: #ede5ff;
  --ref-electric-blue: #1b5bff;
}
```

## Typography direction
- **Helvetica Neue LT**: 400, 800, 12px, 14px, 16px, 20px, 24px, 28px, 40px, 55px, 65px, 80px, normal; substitute `Arial`.
- **Helvetica Neue**: 700, 21px, 1.38.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 13px, badges: 38px, buttons: 64px, default: 0px, largeCards: 20px, smallButtons: 28px, mediumButtons: 32px`

## Surface cues
- **Base Canvas** `#000000`: Dominant background for the entire application, providing a deep, dark foundation.
- **Featured Card White** `#ffffff`: Primary surface for interactive cards or content blocks, providing strong contrast on the dark canvas.
- **Featured Card Dark** `#000000`: Used for card-like elements on sections that might already be dark, maintaining the card structure.
- **Accent Card Yellow** `#fffe5b`: Highlight cards with vibrant color, drawing immediate attention to featured content.

## Component cues
- **Ghost Button (Text)**: Invisible buttons with text only, used for secondary actions or navigation.
- **Ghost Button (Outlined)**: Secondary action buttons with a border, minimal visual weight.
- **Pill Button (Filled)**: Primary global action buttons, high contrast.
- **Pill Button (Outlined)**: Distinct secondary action buttons, visually rounded.
- **Base Card**: Background for product information or content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
