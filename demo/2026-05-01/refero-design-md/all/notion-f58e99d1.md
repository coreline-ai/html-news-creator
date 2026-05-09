# Notion - Refero Design MD

- Source: https://styles.refero.design/style/f58e99d1-940d-4254-8822-5d856bba6505
- Original site: https://www.notion.com
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep-space command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Abyss | `#000000` | neutral | Primary text or dark surface |
| Ghostly Gray | `#0b0b0b` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Mist Gray | `#f6f5f4` | neutral | Page background or card surface |
| Slate Text | `#615d59` | neutral | Border, muted text, or supporting surface |
| Dim Gray | `#a39e98` | neutral | Border, muted text, or supporting surface |
| Iron Border | `#dddddd` | neutral | Page background or card surface |
| Deep Space Violet | `#02093a` | brand | Action accent / signal color |
| Cosmic Blue | `#455dd3` | brand | Action accent / signal color |
| Link Ocean | `#0075de` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-abyss: #000000;
  --ref-ghostly-gray: #0b0b0b;
  --ref-canvas-white: #ffffff;
  --ref-mist-gray: #f6f5f4;
  --ref-slate-text: #615d59;
  --ref-dim-gray: #a39e98;
  --ref-iron-border: #dddddd;
  --ref-deep-space-violet: #02093a;
}
```

## Typography direction
- **NotionInter**: 400, 500, 600, 700, 12px, 14px, 15px, 16px, 20px, 22px, 24px, 26px, 40px, 42px, 54px, 64px, 0.83, 1.00, 1.04, 1.14, 1.20, 1.23, 1.27, 1.33, 1.35, 1.40, 1.43, 1.50; substitute `Inter`.
- **Lyon Text**: 400, 32px, 1.25; substitute `Georgia`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `cards: 12px, badges: 9999px, inputs: 4px, buttons: 8px, default: 12px`

## Surface cues
- **Midnight Abyss** `#000000`: Primary page background and deepest UI layer.
- **Deep Space Violet** `#02093a`: Elevated card backgrounds, embedded content frames, and hero sections.
- **Ghostly Gray** `#0b0b0b`: Sub-surfaces within cards or slightly more elevated elements, like embedded app panes within the main UI.

## Component cues
- **Nav Header Button**: Navigation, utility
- **Product Feature Card**: Content container
- **Accent Block Card**: Decorative content housing
- **Call to Action Button (Filled)**: Primary interaction
- **Call to Action Button (Outlined)**: Secondary interaction

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
