# Partiful - Refero Design MD

- Source: https://styles.refero.design/style/6db1057d-3457-4173-9184-df160415f060
- Original site: https://partiful.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
confetti landing on white marble — the page stays quiet and light while the content explodes with color and celebration.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | brand | Action accent / signal color |
| Pure Canvas | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#333333` | neutral | Primary text or dark surface |
| Slate | `#666666` | neutral | Border, muted text, or supporting surface |
| Ash | `#999999` | neutral | Border, muted text, or supporting surface |
| Fog | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Silver | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Warm Sand | `#d9c58b` | accent | Action accent / signal color |
| Party Pink | `#f8c4ff` | accent | Action accent / signal color |
| Sky Periwinkle | `#96c4ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-pure-canvas: #ffffff;
  --ref-graphite: #333333;
  --ref-slate: #666666;
  --ref-ash: #999999;
  --ref-fog: #b3b3b3;
  --ref-silver: #cccccc;
  --ref-warm-sand: #d9c58b;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Partiful Display Medium**: 400, 500, 26px, 40px, 42px, 48px, 1.00–1.20; substitute `Cabinet Grotesk, Satoshi`.
- **TWK Lausanne Pan**: 400, 500, 550, 600, 650, 700, 825, 12px, 14px, 16px, 18px, 20px, 22px, 24px, 36px, 112px, 1.20–1.40; substitute `Neue Haas Grotesk, Inter`.

## Spacing / shape
- Section Gap: `80px`
- Element Gap: `10px`
- Page Max Width: `1200px`
- Radius: `cards: 12px, badges: 960px, images: 12px, inputs: 8px, modals: 16px, buttons: 8px, navPills: 4px`

## Surface cues
- **Canvas** `#ffffff`: Base page background for all feature and content sections
- **Card Surface** `#ffffff`: White card with shadow separation (rgba(0,0,0,0.1) 0px 0px 6px 0px) — floats above canvas via shadow, not color difference
- **Gradient Wash** `#96c4ff`: Section backgrounds using periwinkle-to-white or pink-to-mauve gradients — the only non-white surface level, used for hero and alternating feature…
- **Overlay Ink** `#000000`: Dark overlay for hero photography — photography sections use black with gradient overlay and backdrop blur for legible white text

## Component cues
- **Announcement Banner**: Reference component style.
- **Feature Tab Selector**: Reference component style.
- **RSVP Response Buttons**: Reference component style.
- **Primary Filled Button**: Main page CTAs — Create invite, Create event
- **Ghost Nav Button**: Login / secondary header action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
