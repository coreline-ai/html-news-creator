# Letters - Refero Design MD

- Source: https://styles.refero.design/style/04109c48-f591-4110-9739-622243d4ecc2
- Original site: https://letters.app
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Blue Sky Productivity

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud Canvas | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#f5f5f5` | neutral | Page background or card surface |
| Deep Sea Blue | `#2597d0` | brand | Action accent / signal color |
| Sky Wash | `#c0eaff` | accent | Action accent / signal color |
| Coal Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Action | `#070709` | neutral | Primary text or dark surface |
| Slate Text | `#60606c` | neutral | Border, muted text, or supporting surface |
| Mid-Gray Text | `#8b8b8b` | neutral | Border, muted text, or supporting surface |
| Light Gray Text | `#bebecc` | neutral | Border, muted text, or supporting surface |
| Cool Steel | `#99a0ae` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-cloud-canvas: #ffffff;
  --ref-ghost-gray: #f5f5f5;
  --ref-deep-sea-blue: #2597d0;
  --ref-sky-wash: #c0eaff;
  --ref-coal-black: #000000;
  --ref-charcoal-action: #070709;
  --ref-slate-text: #60606c;
  --ref-mid-gray-text: #8b8b8b;
}
```

## Typography direction
- **sans-serif**: 400, 700, 12px, 1.2.
- **Open Runde**: 400, 500, 600, 700, 900, 10px, 12px, 14px, 16px, 17px, 18px, 20px, 28px, 44px, 80px, 0.90, 1.10, 1.20, 1.40, 1.49, 1.50; substitute `Source Sans Pro`.
- **Inter**: 400, 500, 14px, 1.20, 1.40, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `tags: 100px, cards: 48px, inputs: 18px, buttons: 100px`

## Surface cues
- **Cloud Canvas** `#ffffff`: Base page background and default content surfaces
- **Ghost Gray** `#f5f5f5`: Secondary background for card groups or subtle content sections
- **Sky Wash** `#c0eaff`: Lightly tinted background for specific, non-critical elevated content

## Component cues
- **Primary Action Button**: The main call to action on the page.
- **Ghost Button**: Secondary action or link, visually minimal.
- **Subtle Accent Button**: Tertiary actions or interactive tags.
- **Elevated Card**: Primary content container, creating visual separation.
- **Flat Card**: Secondary content containers, less emphasis than Elevated Card.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
