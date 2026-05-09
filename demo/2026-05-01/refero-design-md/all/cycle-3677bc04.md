# Cycle - Refero Design MD

- Source: https://styles.refero.design/style/3677bc04-7461-4aa4-aec7-5291bac41b0b
- Original site: https://cycle.app
- Theme: `light`
- Industry: `other`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Sandbox with Soft Precision. Elements feel like organized, approachable blocks, gently elevated within a bright, open space.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Black | `#171618` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#727578` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#f7f7f7` | neutral | Page background or card surface |
| Silver Mist | `#efefef` | neutral | Page background or card surface |
| Slate Border | `#dadada` | neutral | Page background or card surface |
| Feedback Violet | `#38296c` | brand | Action accent / signal color |
| Agent Blue | `#004d60` | brand | Action accent / signal color |
| Insight Amber | `#6c4800` | brand | Action accent / signal color |
| Pale Lilac | `#f5f0ff` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-black: #171618;
  --ref-paper-white: #ffffff;
  --ref-graphite: #727578;
  --ref-light-gray: #f7f7f7;
  --ref-silver-mist: #efefef;
  --ref-slate-border: #dadada;
  --ref-feedback-violet: #38296c;
  --ref-agent-blue: #004d60;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 12px, 13px, 14px, 15px, 16px, 21px, 27px, 0.94, 1.00, 1.18, 1.20, 1.40, 1.62, 1.74; substitute `system-ui, sans-serif`.
- **Eudoxus Sans**: 700, 800, 21px, 23px, 32px, 48px, 58px, 1.00, 1.05, 1.20, 1.27, 1.40; substitute `Arial, sans-serif`.
- **Karla**: 400, 21px, 1.40; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `22px`
- Element Gap: `16px`
- Page Max Width: `1447px`
- Radius: `cards: 20px, badges: 100px, inputs: 8px, buttons: 10px`

## Component cues
- **Button Group**: Reference component style.
- **Product Agent Cards**: Reference component style.
- **Feedback Quote Card**: Reference component style.
- **Primary Action Button**: Call to action
- **Secondary Action Button**: Call to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
