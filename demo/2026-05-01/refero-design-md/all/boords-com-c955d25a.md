# boords.com - Refero Design MD

- Source: https://styles.refero.design/style/c955d25a-b32a-441d-9f07-a260d1df897b
- Original site: https://boords.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
organized workshop on creamy paper

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#000000` | neutral | Primary text or dark surface |
| Charcoal | `#121212` | neutral | Primary text or dark surface |
| Alabaster | `#fafaf5` | neutral | Page background or card surface |
| White | `#ffffff` | neutral | Page background or card surface |
| Parchment | `#e9e9e7` | neutral | Page background or card surface |
| Slate | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Ash | `#cecdca` | neutral | Border, muted text, or supporting surface |
| Dusk Grey | `#7d7d7d` | neutral | Border, muted text, or supporting surface |
| Faded Stone | `#898989` | neutral | Border, muted text, or supporting surface |
| Peach | `#eb6c00` | brand | Action accent / signal color |

```css
:root {
  --ref-carbon: #000000;
  --ref-charcoal: #121212;
  --ref-alabaster: #fafaf5;
  --ref-white: #ffffff;
  --ref-parchment: #e9e9e7;
  --ref-slate: #4d4d4d;
  --ref-ash: #cecdca;
  --ref-dusk-grey: #7d7d7d;
}
```

## Typography direction
- **Matter**: 400, 500, 600, 700, 10px, 11px, 12px, 14px, 16px, 17px, 19px, 20px, 24px, 32px, 40px, 60px, 1.10, 1.15, 1.20, 1.25, 1.45, 1.50, 1.70; substitute `Inter`.
- **ui-monospace**: 400, 500, 600, 9px, 11px, 16px, 1.50; substitute `SF Mono`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `8px`
- Element Gap: `8px`
- Radius: `tags: 9999px, cards: 12px, input: 6px, buttons: 9999px, default: 6px`

## Surface cues
- **Alabaster** `#fafaf5`: Primary page canvas and base background for most content areas.
- **White** `#ffffff`: Elevated cards, modals, and interactive components that require a brighter focus.
- **Sky Mist** `#daeef8`: Subtle background for specific informational blocks or sections needing visual separation without high contrast.
- **Parchment** `#e9e9e7`: Secondary background for footer or less prominent sections, acting as a gentle divider.
- **Ash** `#cecdca`: Tertiary backgrounds or subtle borders within UI components, providing minimal depth.

## Component cues
- **CTA Button Group**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **API & Webhooks Dark Feature Cards**: Reference component style.
- **Primary Navigation Link**: Clickable text in the main navigation.
- **Ghost Outline Button**: Secondary action button, often grouped with a primary button.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
