# Helloivy - Refero Design MD

- Source: https://styles.refero.design/style/5af6b791-6cad-4497-9e94-ace28e4fbd51
- Original site: https://helloivy.co
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on creamy paper. Black lines precisely segment content on a soft background.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Greige Canvas | `#faf6f0` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Soft Graphite | `#5e697f` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-greige-canvas: #faf6f0;
  --ref-midnight-ink: #000000;
  --ref-soft-graphite: #5e697f;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **Unbounded**: 400, 500, 20px, 34px, 62px, 82px, 1.10, 1.20, 1.40; substitute `Montserrat, Poppins`.
- **Inter**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 24px, 27px, 32px, 1.20, 1.40, 1.50, 1.57, 1.60; substitute `Inter`.
- **system-ui (sans-serif fallback)**: 400, 12px, 1.20; substitute `inherit`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `10px`
- Page Max Width: `1200px`
- Radius: `buttons: 8px, generic: 8px, pillButtons: 9999px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Highlight Card**: Reference component style.
- **Social Proof / Client Logo Grid**: Reference component style.
- **Primary Navigation Link**: Main navigation items
- **Hero Headline**: Main page title

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
