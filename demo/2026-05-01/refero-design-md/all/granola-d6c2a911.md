# Granola - Refero Design MD

- Source: https://styles.refero.design/style/d6c2a911-45ed-4860-a992-43df22793c2a
- Original site: https://www.granola.ai
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Field notes on warm parchment — Granola reads like a well-worn Moleskine open on a sunlit desk: serifed headlines with editorial gravity, organic green accents like ink from a plant-based pen, and hairline-ruled card…

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment Canvas | `#f7f7f2` | neutral | Page background or card surface |
| Pure Surface | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#0e0f0c` | neutral | Primary text or dark surface |
| Deep Charcoal | `#292929` | neutral | Primary text or dark surface |
| Carbon | `#454745` | neutral | Border, muted text, or supporting surface |
| Slate | `#72726e` | neutral | Border, muted text, or supporting surface |
| Graphite | `#818179` | neutral | Border, muted text, or supporting surface |
| Ash Border | `#e3e3e3` | neutral | Page background or card surface |
| Stone Border | `#d5d5d2` | neutral | Border, muted text, or supporting surface |
| Fog Surface | `#eaebe5` | neutral | Page background or card surface |

```css
:root {
  --ref-parchment-canvas: #f7f7f2;
  --ref-pure-surface: #ffffff;
  --ref-midnight-ink: #0e0f0c;
  --ref-deep-charcoal: #292929;
  --ref-carbon: #454745;
  --ref-slate: #72726e;
  --ref-graphite: #818179;
  --ref-ash-border: #e3e3e3;
}
```

## Typography direction
- **Melange**: 300, 400, 500, 600, 13px, 14px, 15px, 16px, 20px, 24px, 1.00–1.50; substitute `DM Sans, Instrument Sans`.
- **Quadrant**: 400, 16px, 18px, 20px, 24px, 36px, 48px, 68px, 1.00–1.40; substitute `Playfair Display, Lora`.
- **-apple-system / system-ui**: 300, 400, 500, 700, 14px, 15px, 16px, 20px, 1.14–1.50; substitute `Inter, system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `cards: 8px, inputs: 8px, buttons: 9999px, cardsXL: 16px, tooltips: 4px, pillBadge: 9999px, cardsLarge: 12px, decorativeBlobs: 64px`

## Surface cues
- **Canvas** `#f7f7f2`: Page background — warm off-white, never pure white at page level
- **Card** `#ffffff`: White card surfaces, nav background, input fill backgrounds
- **Tinted Surface** `#eaebe5`: Hover fills, soft opaque states, subtle inset surfaces
- **Accent Tint** `#e5eacd`: Sprout-tinted button backgrounds for secondary actions and announcement pills

## Component cues
- **Primary Download Button**: Main CTA for app download actions
- **Announcement Pill Button**: Secondary/news banner linked badge
- **White Surface Button**: Tertiary action on tinted or colored backgrounds
- **Ghost Text Button**: Inline links within social/testimonial content
- **Social Testimonial Card**: Twitter/X embed social proof blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
