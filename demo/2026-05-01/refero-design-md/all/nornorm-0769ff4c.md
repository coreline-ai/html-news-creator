# Nornorm - Refero Design MD

- Source: https://styles.refero.design/style/0769ff4c-f719-4865-98df-de2f44c694a6
- Original site: https://nornorm.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint on White

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Storm Gray | `#6a6a6a` | neutral | Border, muted text, or supporting surface |
| Light Ash | `#f1efe9` | neutral | Page background or card surface |
| Frost | `#ececec` | neutral | Page background or card surface |
| Command Violet | `#1e37a0` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-storm-gray: #6a6a6a;
  --ref-light-ash: #f1efe9;
  --ref-frost: #ececec;
  --ref-command-violet: #1e37a0;
}
```

## Typography direction
- **Lunar**: 400, 500, 700, 14px, 16px, 20px, 24px, 32px, 48px, 64px, 80px, 112px, 1.00, 1.30; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `links: 8px, others: 8px, buttons: 1440px, navigation: 8px`

## Component cues
- **Ghost Navigation Button**: Primary navigation links and interactive textual buttons that blend into the background.
- **Subtle Gray Button**: Secondary action buttons with a soft visual emphasis.
- **Command Violet Filled Button**: Primary call-to-action buttons, indicating strongest interactive focus.
- **Feature Card**: Informational cards presenting key selling points or content blocks.
- **Header Navigation Item**: Top-level navigation links.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
