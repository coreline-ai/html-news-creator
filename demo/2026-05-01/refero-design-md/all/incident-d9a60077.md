# Incident - Refero Design MD

- Source: https://styles.refero.design/style/d9a60077-619a-4cb7-95ed-0c428c2b51ed
- Original site: https://incident.io
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Engineering blueprint on stark white

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Platinum Mist | `#efefef` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Deep Graphite | `#161618` | neutral | Primary text or dark surface |
| Desert Sand | `#e4d9c8` | neutral | Page background or card surface |
| Alert Red | `#ff492c` | accent | Action accent / signal color |
| Flamingo Orange | `#f25533` | brand | Action accent / signal color |
| Vivid Hue | `#f1641e` | accent | Action accent / signal color |
| Light Gray Divider | `#dadada` | neutral | Page background or card surface |
| Medium Gray Divider | `#cccccc` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-platinum-mist: #efefef;
  --ref-ink-black: #000000;
  --ref-deep-graphite: #161618;
  --ref-desert-sand: #e4d9c8;
  --ref-alert-red: #ff492c;
  --ref-flamingo-orange: #f25533;
  --ref-vivid-hue: #f1641e;
}
```

## Typography direction
- **Times**: 400, 700, 16px, 19px, 24px, 32px, 1.20; substitute `serif`.
- **Arial**: 400, 13px, 1.20; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `16px`
- Radius: `all: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background
- **Platinum Mist** `#efefef`: Component backgrounds (e.g., buttons), subtle content separators
- **Subtle Background** `#000000`: Highly subtle translucent dark backgrounds for content cards, often used with transparency (rgba(0,0,0,0.15))

## Component cues
- **Default Button**: Interactive element
- **Ghost Card**: Container, content grouping
- **Subtle Background Card**: Container, content grouping

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
