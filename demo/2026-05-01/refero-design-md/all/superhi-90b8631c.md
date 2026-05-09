# SuperHi - Refero Design MD

- Source: https://styles.refero.design/style/90b8631c-4e2c-407e-86a3-d2bff456dc93
- Original site: https://superhi.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant geometry on a clean canvas — a digital workshop buzzing with creative shapes.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Storm Gray | `#111118` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pale Mist | `#f0f6ff` | neutral | Page background or card surface |
| Electric Blue | `#2727e6` | brand | Action accent / signal color |
| Vivid Green | `#16ab59` | accent | Action accent / signal color |
| Lemon Zest | `#ffda00` | accent | Action accent / signal color |
| Sky Tint | `#e1edff` | accent | Action accent / signal color |
| Cool Aqua | `#91d8ec` | accent | Action accent / signal color |
| Coral Glow | `#ffbac4` | accent | Action accent / signal color |
| Sunset Orange | `#ff7715` | accent | Action accent / signal color |

```css
:root {
  --ref-storm-gray: #111118;
  --ref-canvas-white: #ffffff;
  --ref-pale-mist: #f0f6ff;
  --ref-electric-blue: #2727e6;
  --ref-vivid-green: #16ab59;
  --ref-lemon-zest: #ffda00;
  --ref-sky-tint: #e1edff;
  --ref-cool-aqua: #91d8ec;
}
```

## Typography direction
- **Haas Grot Text**: 400, 16px, 20px, 22px, 24px, 1.10, 1.25, 1.35, 1.40; substitute `Inter`.
- **Haas Grot Disp**: 400, 24px, 35px, 42px, 52px, 62px, 72px, 92px, 1.00, 1.10, 1.15, 1.35; substitute `Neue Haas Grotesk Display`.
- **Martian Mono**: 400, 12px, 17px, 1.00, 1.30, 1.35; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `pill: 48px, input: 5000px, buttons: 32px, default: 24px`

## Component cues
- **Hero CTA Button Group**: Reference component style.
- **Promotional Announcement Banner**: Reference component style.
- **Most Popular Section Header with CTA**: Reference component style.
- **Primary Action Button**: Call to action
- **Large Primary Action Button**: Prominent Call to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
