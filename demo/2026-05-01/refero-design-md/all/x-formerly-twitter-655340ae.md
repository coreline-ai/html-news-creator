# X (formerly Twitter) - Refero Design MD

- Source: https://styles.refero.design/style/655340ae-abff-4a90-8545-8feb62411f68
- Original site: https://create.video
- Theme: `light`
- Industry: `media`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast information stream

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Puck Blue | `#1d9bf0` | brand | Action accent / signal color |
| Slate Gray | `#536471` | neutral | Border, muted text, or supporting surface |
| Mist | `#eff3f4` | neutral | Page background or card surface |
| Border Silver | `#cfd9de` | neutral | Border, muted text, or supporting surface |
| Near Black | `#0f1419` | neutral | Primary text or dark surface |
| Whisper Gray | `#e0e4e7` | neutral | Page background or card surface |
| Shadowed Button | `#4b4f53` | neutral | Border, muted text, or supporting surface |
| Muted Navigation Text | `#829aab` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-puck-blue: #1d9bf0;
  --ref-slate-gray: #536471;
  --ref-mist: #eff3f4;
  --ref-border-silver: #cfd9de;
  --ref-near-black: #0f1419;
  --ref-whisper-gray: #e0e4e7;
}
```

## Typography direction
- **Times**: 400, 700, 15px, 1.20; substitute `Georgia`.
- **TwitterChirp**: 400, 500, 700, 800, 11px, 13px, 14px, 15px, 20px, 23px, 0.80, 1.09, 1.14, 1.20, 1.22, 1.23, 1.33; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `4px`
- Page Max Width: `1070px`
- Radius: `cards: 16px, links: 9999px, other: 4px, avatars: 9999px, buttons: 9999px`

## Surface cues
- **Page Canvas** `#ffffff`: Dominant background for the entire application, providing a clean white slate.
- **Card Surface** `#ffffff`: Background for individual content cards and interactive modules, often with a 16px radius.
- **Subtle Background** `#eff3f4`: Used for slight visual breaks, such as background of search inputs or subtle dividers.

## Component cues
- **Text Only Button**: Neutral, interactive text-based button.
- **Subtle Text Button**: Subtly darker text button for secondary actions.
- **Outlined Button**: Ghost button with a neutral border.
- **Primary Action Button**: Calls to action with brand emphasis.
- **Ghost Card**: Content container with minimal visual separation from the background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
