# Travelperk - Refero Design MD

- Source: https://styles.refero.design/style/75c06591-34d2-493a-bd49-70551b5e4a53
- Original site: https://travelperk.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Lime spark on warm parchment — electric CTA green against aged-paper cream, zero shadows, everything rounded at exactly 26px.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Electric Lime | `#beff50` | brand | Action accent / signal color |
| Near Black | `#14140f` | neutral | Primary text or dark surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Warm Cream | `#f5f5eb` | neutral | Page background or card surface |
| Parchment Card | `#fafaf5` | neutral | Page background or card surface |
| Stone | `#d2d2c8` | neutral | Border, muted text, or supporting surface |
| Graphite | `#6e6e64` | neutral | Border, muted text, or supporting surface |
| Charcoal | `#30302a` | neutral | Primary text or dark surface |
| Slate Border | `#919183` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-electric-lime: #beff50;
  --ref-near-black: #14140f;
  --ref-pure-black: #000000;
  --ref-pure-white: #ffffff;
  --ref-warm-cream: #f5f5eb;
  --ref-parchment-card: #fafaf5;
  --ref-stone: #d2d2c8;
  --ref-graphite: #6e6e64;
}
```

## Typography direction
- **OTSono**: 400, 500, 10px, 12px, 13px, 14px, 16px, 17px, 18px, 20px, 22px, 24px, 30px, 32px, 40px, 64px, 80px, 90px, 200px, 0.89–1.50 (display: 0.89–0.90, body: 1.40–1.50, headings: 1.00–1.20); substitute `Cabinet Grotesk, Geist, or General Sans (rounded terminals, high x-height grotesque)`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `24-40px`
- Element Gap: `8-16px`
- Page Max Width: `1200px`
- Radius: `cards: 26px, badges: 8px, images: 26px, buttons: 26px, pillTabs: 26px, iconButtons: 50%`

## Surface cues
- **Page Ground** `#f5f5eb`: Hero background and primary page fill — warm cream that makes lime feel organic not neon
- **Section Surface** `#fafaf5`: Feature cards and alternating section backgrounds — one step brighter than page ground
- **Elevated Card** `#ffffff`: White cards floating over cream backgrounds — the contrast provides the 'elevation' without shadow
- **Dark Surface** `#14140f`: Dark feature cards and announcement strip — maximum contrast against all light surfaces

## Component cues
- **Button Group**: Reference component style.
- **Tab Pill Selector with Feature Cards**: Reference component style.
- **Flight Info Card + Status Badges**: Reference component style.
- **Primary CTA Button**: Main conversion action — 'Book a demo', 'Get started'
- **Ghost Button — Dark**: Secondary actions on light backgrounds

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
