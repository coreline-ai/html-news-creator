# Sana Agents - Refero Design MD

- Source: https://styles.refero.design/style/5bfbe8b0-de0e-470f-b130-929f50437160
- Original site: https://sana.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble. Sharp, expansive white spaces frame meticulously placed elements, with occasional flashes of neon green illuminating key interactions.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Tarmac | `#0a1217` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Limestone | `#e4eff7` | neutral | Page background or card surface |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#85898b` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#6c7174` | neutral | Border, muted text, or supporting surface |
| Bio-Luminescent Green | `#cdfe00` | accent | Action accent / signal color |

```css
:root {
  --ref-tarmac: #0a1217;
  --ref-canvas-white: #ffffff;
  --ref-limestone: #e4eff7;
  --ref-jet-black: #000000;
  --ref-cloud-gray: #85898b;
  --ref-steel-gray: #6c7174;
  --ref-bio-luminescent-green: #cdfe00;
}
```

## Typography direction
- **Sana Serif**: 400, 72px, 1.10; substitute `Playfair Display`.
- **Sana Sans**: 400, 450, 500, 13px, 14px, 16px, 20px, 1.20, 1.40, 1.43, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `62px`
- Element Gap: `8px`
- Page Max Width: `1305px`
- Radius: `pill: 9999px, input: 24px, buttons: 24px`

## Component cues
- **Product Cards — Sana Agents & Sana Learn**: Reference component style.
- **Sign Up Form — Try for free with your work email**: Reference component style.
- **Button Group — Primary, Secondary & Outline variants**: Reference component style.
- **Pill Outline Button**: Secondary action button, often for navigation or subtle interactions.
- **Dark Filled Button**: Primary action button within dark contexts or for prominent interactions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
