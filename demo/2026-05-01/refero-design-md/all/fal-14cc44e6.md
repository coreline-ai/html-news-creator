# Fal - Refero Design MD

- Source: https://styles.refero.design/style/14cc44e6-41bf-4178-b834-fc61bfeed4ae
- Original site: https://fal.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Pixelated digital playground

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1b1b1d` | neutral | Primary text or dark surface |
| Carbon | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Stone Gray | `#383a42` | neutral | Primary text or dark surface |
| Soft Mist | `#e5e7eb` | neutral | Page background or card surface |
| Silver Dust | `#f4f4f5` | neutral | Page background or card surface |
| Deep Plum | `#252527` | neutral | Primary text or dark surface |
| Sky Aqua | `#99ecff` | accent | Action accent / signal color |
| Vivid Violet | `#4a17b0` | accent | Action accent / signal color |
| Lime Spritz | `#f1ffd2` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #1b1b1d;
  --ref-carbon: #000000;
  --ref-cloud-white: #ffffff;
  --ref-stone-gray: #383a42;
  --ref-soft-mist: #e5e7eb;
  --ref-silver-dust: #f4f4f5;
  --ref-deep-plum: #252527;
  --ref-sky-aqua: #99ecff;
}
```

## Typography direction
- **focal**: 400, 500, 600, 700, 10px, 12px, 14px, 16px, 18px, 24px, 30px, 36px, 40px, 48px, 60px, 80px, 120px, 0.83, 0.88, 0.90, 1.00, 1.11, 1.20, 1.33, 1.40, 1.43, 1.50, 1.56, 1.60; substitute `Inter`.
- **Chivo Mono**: 400, 14px, 1.14, 1.43, 1.50; substitute `Space Mono`.
- **publicSansRounded**: 400, 600, 700, 14px, 16px, 24px, 1.00, 1.43, 1.50; substitute `Public Sans`.

## Spacing / shape
- Section Gap: `113px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1440px`
- Radius: `cards: 12px, buttons: 4px, default: 4px`

## Component cues
- **Primary Filled Button**: Call to action button
- **Ghost Button**: Secondary action button
- **Standard Card**: Content container
- **Accent Card - Lime Spritz**: Highlighted content container
- **Accent Card - Lavender Haze**: Highlighted content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
