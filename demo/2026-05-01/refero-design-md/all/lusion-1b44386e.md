# Lusion - Refero Design MD

- Source: https://styles.refero.design/style/1b44386e-31a8-40b0-a577-27c088b51264
- Original site: https://lusion.co
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Computational Laboratory Blueprint — high-contrast text on bright surfaces, accented by vivid blue and lime green.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Whisper Off-White | `#f0f1fa` | neutral | Page background or card surface |
| Storm Gray | `#2b2e3a` | neutral | Primary text or dark surface |
| Button White | `#e4e6ef` | neutral | Page background or card surface |
| Dark Surface | `#121416` | neutral | Primary text or dark surface |
| Deep Space Blue | `#1a2ffb` | accent | Action accent / signal color |
| Electric Lime | `#c1ff00` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-whisper-off-white: #f0f1fa;
  --ref-storm-gray: #2b2e3a;
  --ref-button-white: #e4e6ef;
  --ref-dark-surface: #121416;
  --ref-deep-space-blue: #1a2ffb;
  --ref-electric-lime: #c1ff00;
}
```

## Typography direction
- **Aeonik**: 400, 500, 12px, 13px, 14px, 16px, 18px, 20px, 22px, 26px, 36px, 38px, 43px, 49px, 50px, 108px, 115px, 144px, 0.90, 1.00, 1.10, 1.15, 1.20, 1.40, 1.50; substitute `system-ui (sans-serif)`.

## Spacing / shape
- Card Padding: `25px`
- Element Gap: `13px`
- Radius: `cards: 15px, inputs: 18px, buttons: 87.5px, pillForms: 100px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Hero Tagline with Scroll Bar**: Reference component style.
- **Contact Form Input Card**: Reference component style.
- **Primary Action Button**: Primary Call to Action
- **Secondary Action Button**: Secondary Call to Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
