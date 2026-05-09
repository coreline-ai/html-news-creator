# basement.studio - Refero Design MD

- Source: https://styles.refero.design/style/e06224b2-6d52-4d06-bbde-115cec719b47
- Original site: https://basement.studio
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Void print shop at 3am — massive compressed type bleeding off a pitch-black canvas, one ember of orange light on the nav, everything else white or ghost-gray.

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ember Signal | `#ff4d00` | accent | Action accent / signal color |
| Void | `#000000` | neutral | Primary text or dark surface |
| Chalk | `#ffffff` | neutral | Page background or card surface |
| Fog | `#e5e7eb` | neutral | Page background or card surface |
| Ash | `#c4c4c4` | neutral | Border, muted text, or supporting surface |
| Graphite | `#757575` | neutral | Border, muted text, or supporting surface |
| Carbon | `#454545` | neutral | Border, muted text, or supporting surface |
| Cinder | `#1a1a1a` | neutral | Primary text or dark surface |
| Smudge | `#666666` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-ember-signal: #ff4d00;
  --ref-void: #000000;
  --ref-chalk: #ffffff;
  --ref-fog: #e5e7eb;
  --ref-ash: #c4c4c4;
  --ref-graphite: #757575;
  --ref-carbon: #454545;
  --ref-cinder: #1a1a1a;
}
```

## Typography direction
- **Geist**: 400, 500, 600, 12px, 13px, 15px, 16px, 20px, 24px, 38px, 76px, 87px, 0.89–1.50 (tightest at largest sizes: 0.89 at 87px, 0.90 at 76px); substitute `Inter, Helvetica Neue`.

## Spacing / shape
- Section Gap: `128px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1280px`
- Radius: `cards: 0px, badges: 0px, global: 0px — zero radius everywhere, no exceptions, inputs: 0px, buttons: 0px`

## Component cues
- **Client Logo Grid**: Reference component style.
- **Display Headline with Body Copy**: Reference component style.
- **Nav Bar Strip**: Reference component style.
- **Ghost Navigation Link**: Primary nav items
- **Contact Us Button**: Primary CTA in nav

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
