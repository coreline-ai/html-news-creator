# Slingshot - Refero Design MD

- Source: https://styles.refero.design/style/e683efcd-b005-4a35-a5ea-d25bcf3de5c0
- Original site: https://www.useslingshot.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp canvas, vivid action.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#241f37` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Sky Blue | `#ecf2ff` | neutral | Action accent / signal color |
| Pale Peach | `#fff4ec` | neutral | Page background or card surface |
| Mint Glaze | `#edf9f5` | neutral | Page background or card surface |
| Action Blue | `#1a5fff` | brand | Action accent / signal color |
| Accent Orange | `#ff7a1a` | accent | Action accent / signal color |
| Accent Green | `#359774` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #241f37;
  --ref-canvas-white: #ffffff;
  --ref-sky-blue: #ecf2ff;
  --ref-pale-peach: #fff4ec;
  --ref-mint-glaze: #edf9f5;
  --ref-action-blue: #1a5fff;
  --ref-accent-orange: #ff7a1a;
  --ref-accent-green: #359774;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Gopher**: 400, 500, 24px, 32px, 56px, 1.00; substitute `Open Sans`.
- **Inter**: 400, 12px, 14px, 16px, 1.14, 1.20, 1.33; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `pill: 43px, cards: 24px, buttons: 6px, default: 12px`

## Component cues
- **Secondary Ghost Button**: Navigational or secondary actions where visual prominence is low.
- **Outline Action Button (Nav)**: Navigation or login actions, indicating an interactive element without being primary.
- **Ghost Accent Button**: Lightweight, secondary actions or internal links within content.
- **Primary Filled Button**: Main calls to action on the page, highly visible and interactive.
- **Testimonial Card**: Showcasing client feedback, a floating element with subtle visual depth.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
