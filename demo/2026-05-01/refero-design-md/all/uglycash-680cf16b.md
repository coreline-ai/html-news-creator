# UGLYCASH - Refero Design MD

- Source: https://styles.refero.design/style/680cf16b-0093-473b-854f-f1de9af5e698
- Original site: https://ugly.cash
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital pop: Bold black text on bright canvas, punctuated by vivid neons.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Ice | `#f2f2f2` | neutral | Page background or card surface |
| Ghost Gray | `#e6e4e4` | neutral | Page background or card surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Carbon Black | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#3a3a3a` | neutral | Primary text or dark surface |
| Muted Stone | `#6e6e6e` | neutral | Border, muted text, or supporting surface |
| Soft Stone | `#888888` | neutral | Border, muted text, or supporting surface |
| Cream Card | `#e7e3bf` | neutral | Page background or card surface |
| Power Pink | `#fa00ff` | accent | Action accent / signal color |
| Sky Blue | `#02bbff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-ice: #f2f2f2;
  --ref-ghost-gray: #e6e4e4;
  --ref-polar-white: #ffffff;
  --ref-carbon-black: #000000;
  --ref-deep-graphite: #3a3a3a;
  --ref-muted-stone: #6e6e6e;
  --ref-soft-stone: #888888;
  --ref-cream-card: #e7e3bf;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `Arial`.
- **Helvetica Now Display Cn Bold**: 700, 900, 20px, 64px, 85px, 164px, 0.85, 0.94, 1.20; substitute `Montserrat Black`.
- **Inter**: 400, 500, 700, 12px, 14px, 18px, 20px, 24px, 1.17, 1.20, 1.22, 1.29, 1.33, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `pill: 100px, large: 46px, small: 1px, default: 16px`

## Component cues
- **Ghost Button Inverse**: Minimal interactive element for secondary actions or navigation.
- **Pill Accent Button**: Primary Call to Action, visually distinct and inviting interaction.
- **Rounded Accent Button**: Secondary action or featured link, with a soft background.
- **White Information Card**: Standard container for content blocks and feature explanations.
- **Cream Accent Card**: Highlight card for special features, uses a distinct neutral background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
