# Healthy Together - Refero Design MD

- Source: https://styles.refero.design/style/d577e44e-bc63-4cbe-b759-25262d089b95
- Original site: https://www.healthytogether.co
- Theme: `mixed`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
midnight gradient horizon

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#101722` | neutral | Primary text or dark surface |
| Canvas Ice | `#f9f0ff` | neutral | Page background or card surface |
| Plasma Violet | `#4541fe` | brand | Action accent / signal color |
| Soft Lavender | `#d9c6ff` | neutral | Border, muted text, or supporting surface |
| Pale Stone | `#6c6c7a` | neutral | Border, muted text, or supporting surface |
| Snow White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #101722;
  --ref-canvas-ice: #f9f0ff;
  --ref-plasma-violet: #4541fe;
  --ref-soft-lavender: #d9c6ff;
  --ref-pale-stone: #6c6c7a;
  --ref-snow-white: #ffffff;
}
```

## Typography direction
- **Inter**: 400, 600, 700, 14px, 16px, 24px, 36px, 64px, 72px, 92px, 0.88, 0.90, 1.00, 1.10, 1.15, 1.30, 1.40; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `cards: 42px, badges: 9999px, buttons: 16000px`

## Component cues
- **Primary Action Button**: Call to action button
- **Ghost Button**: Secondary action or subtle navigation
- **Cream Background Button**: Tertiary action or alternative prompt
- **Standard Content Card**: Information container, testimonial display
- **Gradient Hero Card**: Prominent feature or call to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
