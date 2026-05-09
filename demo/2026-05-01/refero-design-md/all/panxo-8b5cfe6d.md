# Panxo - Refero Design MD

- Source: https://styles.refero.design/style/8b5cfe6d-a2bd-4edb-854e-9185cec46c09
- Original site: https://panxo.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Data terminal in warm ink — every surface echoes ledger paper, every accent reads like a highlighted cell.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Coal Ink | `#1c1a17` | neutral | Primary text or dark surface |
| Ledger White | `#fafafa` | neutral | Page background or card surface |
| Parchment | `#f7f3eb` | neutral | Page background or card surface |
| Ash | `#f1f1f1` | neutral | Page background or card surface |
| Slate Mid | `#7e7d7b` | neutral | Border, muted text, or supporting surface |
| Graphite | `#5a5957` | neutral | Border, muted text, or supporting surface |
| Stone | `#969594` | neutral | Border, muted text, or supporting surface |
| Fossil | `#bab9b8` | neutral | Border, muted text, or supporting surface |
| Smolder | `#ff6020` | brand | Action accent / signal color |
| Signal Violet | `#777eff` | accent | Action accent / signal color |

```css
:root {
  --ref-coal-ink: #1c1a17;
  --ref-ledger-white: #fafafa;
  --ref-parchment: #f7f3eb;
  --ref-ash: #f1f1f1;
  --ref-slate-mid: #7e7d7b;
  --ref-graphite: #5a5957;
  --ref-stone: #969594;
  --ref-fossil: #bab9b8;
}
```

## Typography direction
- **Mona Sans**: 500, 700, 24px, 32px, 40px, 48px, 56px, 1.00–1.20; substitute `Plus Jakarta Sans or Geist`.
- **Inter**: 400, 500, 600, 700, 8px, 9px, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 1.20–1.67; substitute `Inter (freely available on Google Fonts)`.
- **sans-serif**: 400, 12px, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `80-120px`
- Card Padding: `24px`
- Element Gap: `8-12px`
- Page Max Width: `1200px`
- Radius: `cards: 10px, badges: 6-8px, images: 8px, buttons: 48px (filled primary), 999px (outlined/ghost), 20px (filter chips), demoPanels: 12-20px, inputFields: 12px`

## Surface cues
- **Page Base** `#f7f3eb`: Hero section and large atmospheric backgrounds — warmest surface
- **App Surface** `#fafafa`: Default page background and card fills
- **Elevated Card** `#ffffff`: Interactive cards and demo UI panels with micro-shadow
- **Inverse Surface** `#1c1a17`: Dark stat card and primary CTA button fill

## Component cues
- **Button Group (Primary + Ghost + Filter Pills)**: Reference component style.
- **Stat Metric Cards Grid**: Reference component style.
- **Publisher Directory Card**: Reference component style.
- **Primary Filled CTA Button**: Highest-priority action: 'Get Started', 'Try Free'
- **Outlined Ghost Button**: Secondary actions: 'Explore Marketplace', 'Sign In'

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
