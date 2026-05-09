# Convex - Refero Design MD

- Source: https://styles.refero.design/style/f71e92b0-d7a5-4203-b975-394f185218c2
- Original site: https://convex.dev
- Theme: `mixed`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm charcoal workbench with code syntax highlights. The core experience is dark and functional, highlighted by colorful code snippets.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#141414` | neutral | Primary text or dark surface |
| Cloud | `#ffffff` | neutral | Page background or card surface |
| Ash | `#f6f6f6` | neutral | Page background or card surface |
| Parchment | `#fdefd2` | neutral | Page background or card surface |
| Slate | `#292929` | neutral | Primary text or dark surface |
| Stone | `#d7d7d7` | neutral | Border, muted text, or supporting surface |
| Whisper | `#e5e5e5` | neutral | Page background or card surface |
| Code Violet | `#948ae3` | accent | Action accent / signal color |
| Code Pink | `#fc618d` | accent | Action accent / signal color |
| Code Green | `#7bd88f` | accent | Action accent / signal color |

```css
:root {
  --ref-carbon: #141414;
  --ref-cloud: #ffffff;
  --ref-ash: #f6f6f6;
  --ref-parchment: #fdefd2;
  --ref-slate: #292929;
  --ref-stone: #d7d7d7;
  --ref-whisper: #e5e5e5;
  --ref-code-violet: #948ae3;
}
```

## Typography direction
- **GT America**: 400, 500, 700, 10px, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 36px, 40px, 56px, 1.00, 1.25, 1.38, 1.50; substitute `system-ui`.
- **ui-monospace**: 400, 13px, 1.40; substitute `monospace`.

## Spacing / shape
- Card Padding: `12px`
- Element Gap: `4-16px`
- Page Max Width: `1200px`
- Radius: `nav: 8px, cards: 12px, buttons: 0px, general: 4px`

## Component cues
- **Button Group — Primary + Ghost**: Reference component style.
- **Feature List — Everything is code**: Reference component style.
- **Product Section Banner — Not just a database**: Reference component style.
- **Primary Action Button - Dark BG**: Primary call to action on dark backgrounds.
- **Outline Ghost Button - Dark BG**: Secondary action or navigation on dark themed sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
