# Relate - Refero Design MD

- Source: https://styles.refero.design/style/337ade6a-4bae-49ba-b4aa-8994ac805a81
- Original site: https://www.relate.so
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Blueprint on frosted linen — Inter headlines with tight negative tracking over a pale blue-white canvas, product UI surfacing as quiet white cards, the single vivid blue accent used like a highlighter pen rather than…

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Linen Canvas | `#fcfcfc` | neutral | Page background or card surface |
| Sky Wash | `#f0f4fe` | neutral | Page background or card surface |
| Midnight Ink | `#020520` | neutral | Primary text or dark surface |
| Graphite | `#14141e` | neutral | Primary text or dark surface |
| Slate | `#374151` | neutral | Border, muted text, or supporting surface |
| Ash | `#696a72` | neutral | Border, muted text, or supporting surface |
| Fog | `#95959b` | neutral | Border, muted text, or supporting surface |
| Steel | `#6b7280` | neutral | Border, muted text, or supporting surface |
| Signal Blue | `#145aff` | brand | Action accent / signal color |
| Periwinkle Glow | `#b6cbfd` | accent | Action accent / signal color |

```css
:root {
  --ref-linen-canvas: #fcfcfc;
  --ref-sky-wash: #f0f4fe;
  --ref-midnight-ink: #020520;
  --ref-graphite: #14141e;
  --ref-slate: #374151;
  --ref-ash: #696a72;
  --ref-fog: #95959b;
  --ref-steel: #6b7280;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Inter**: 400, 500, 600, 10px, 12px, 14px, 15px, 16px, 18px, 20px, 22px, 40px, 56px, 80px, 1.00–1.50 (tighter at display, looser at body); substitute `Inter (Google Fonts)`.
- **Pretendard**: 400 (Regular, Medium, Bold variants), 12px, 14px, 15px, 16px, 18px, 1.00–1.71; substitute `Noto Sans KR, SUIT`.

## Spacing / shape
- Section Gap: `80px`
- Element Gap: `8-12px`
- Page Max Width: `1200px`
- Radius: `pill: 100px, cards: 8px, badges: 4px, images: 16px, inputs: 12px, modals: 32px, buttons: 12px, cardLarge: 40px`

## Surface cues
- **Canvas** `#fcfcfc`: Page background — the base layer everything sits on
- **Tinted Wash** `#f0f4fe`: Alternate section backgrounds and hero gradient zone — one step above canvas with a blue tint
- **Card Surface** `#ffffff`: Product UI cards, feature cards, and elevated content containers with subtle shadow
- **Overlay** `#fcfcfc`: Large feature cards with 40px radius (rgba(252,252,252,0.2) for glassmorphic hero overlays)

## Component cues
- **Primary Outlined Button**: Main call-to-action navigation button (Book a demo, Get started free outline variant)
- **Primary Filled Button**: High-emphasis action (Get started free, filled navbar variant)
- **Hero Ghost Button**: Secondary CTA inside the hero gradient zone
- **Compact Product Card**: CRM pipeline deal rows, contact list items, and inbox entries
- **Large Feature Section Card**: Marketing page feature showcase blocks with embedded product screenshot

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
