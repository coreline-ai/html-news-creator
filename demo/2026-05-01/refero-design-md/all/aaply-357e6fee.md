# Aaply - Refero Design MD

- Source: https://styles.refero.design/style/357e6fee-72db-40cf-b858-254b802018bd
- Original site: https://aaply.app
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant whiteboard sketch. Bright digital ink on a muted gray canvas, with playful, organic shapes.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Whiteboard Background | `#f2f2f2` | neutral | Page background or card surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Onyx Ink | `#000000` | neutral | Primary text or dark surface |
| Fog | `#e6e6e6` | neutral | Page background or card surface |
| Pebble | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Playful Burst Orange | `#ff8562` | accent | Action accent / signal color |
| Bubblegum Red | `#f34646` | accent | Action accent / signal color |
| Electric Violet | `#466cf3` | accent | Action accent / signal color |
| Sunshine Yellow | `#f5bd50` | accent | Action accent / signal color |
| Neon Yellow | `#fff705` | accent | Action accent / signal color |

```css
:root {
  --ref-whiteboard-background: #f2f2f2;
  --ref-canvas: #ffffff;
  --ref-onyx-ink: #000000;
  --ref-fog: #e6e6e6;
  --ref-pebble: #cccccc;
  --ref-playful-burst-orange: #ff8562;
  --ref-bubblegum-red: #f34646;
  --ref-electric-violet: #466cf3;
}
```

## Typography direction
- **Poppins**: 400, 500, 700, 14px, 27px, 34px, 52px, 57px, 1.00, 1.05, 1.33, 1.35, 1.56, 1.57; substitute `system-ui`.
- **Inter**: 300, 400, 500, 700, 15px, 16px, 18px, 27px, 31px, 1.40, 1.44, 1.53, 1.55, 1.56; substitute `sans-serif`.
- **Times**: 400, 16px, 1.20; substitute `serif`.

## Spacing / shape
- Section Gap: `64px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `pill: 3000px, cards: 30px, large: 36px, buttons: 30px, default: 16px, extraLarge: 40px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Tooltip / Badge Components**: Reference component style.
- **Feature / Stat Cards**: Reference component style.
- **Primary Call-to-Action Button**: Interactive element
- **Secondary Outline Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
