# Privy - Refero Design MD

- Source: https://styles.refero.design/style/78d9ece2-9033-479a-997a-ede94fc87fda
- Original site: https://www.privy.io
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital architecture.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Deep Midnight | `#010110` | neutral | Primary text or dark surface |
| Carbon Gray | `#111117` | neutral | Primary text or dark surface |
| Steel Gray | `#22222a` | neutral | Primary text or dark surface |
| Muted Stone | `#73737c` | neutral | Border, muted text, or supporting surface |
| Deep Space Violet | `#635bff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-deep-midnight: #010110;
  --ref-carbon-gray: #111117;
  --ref-steel-gray: #22222a;
  --ref-muted-stone: #73737c;
  --ref-deep-space-violet: #635bff;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `system-ui`.
- **Inter**: 400, 500, 700, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 21px, 38px, 1.00, 1.20, 1.26, 1.27, 1.40, 1.50, 1.60, 1.78, 1.90; substitute `Inter`.
- **ABC Favorit Variable Unlicensed Trial**: 400, 16px, 26px, 28px, 52px, 56px, 76px, 1.03, 1.07, 1.13, 1.15, 1.23, 1.29; substitute `IBM Plex Sans`.

## Spacing / shape
- Section Gap: `70px`
- Card Padding: `16px`
- Element Gap: `10px`
- Radius: `cards: 8px, small: 2px, buttons: 100px, extreme: 951px, primary: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default content area.
- **Carbon Gray** `#111117`: First-level elevated surfaces, such as primary content cards.
- **Steel Gray** `#22222a`: Second-level elevated surfaces or emphasized cards, visually distinct from Carbon Gray.

## Component cues
- **Primary Filled Button**: Action button
- **Ghost Button**: Secondary action button
- **Light Card**: Informational container
- **Dark Card**: Emphasized container
- **Navigation Link**: Primary navigation item

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
