# Boostinsurance - Refero Design MD

- Source: https://styles.refero.design/style/e60c61d3-2657-429e-a581-568aea27a448
- Original site: https://boostinsurance.com
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep ocean current, softly glowing

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Ocean | `#002025` | neutral | Primary text or dark surface |
| Seaweed Green | `#05333a` | neutral | Action accent / signal color |
| Kelp Shadow | `#244348` | neutral | Primary text or dark surface |
| Deep Sea Gray | `#455c60` | neutral | Border, muted text, or supporting surface |
| Slate Echo | `#54696c` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#7d8f92` | neutral | Border, muted text, or supporting surface |
| Pale Mist | `#9eaeb0` | neutral | Border, muted text, or supporting surface |
| Frost White | `#fffffa` | neutral | Page background or card surface |
| Aqua Glow | `#30d7f1` | accent | Action accent / signal color |
| Lime Burst | `#79fa4b` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-ocean: #002025;
  --ref-seaweed-green: #05333a;
  --ref-kelp-shadow: #244348;
  --ref-deep-sea-gray: #455c60;
  --ref-slate-echo: #54696c;
  --ref-silver-mist: #7d8f92;
  --ref-pale-mist: #9eaeb0;
  --ref-frost-white: #fffffa;
}
```

## Typography direction
- **Gellix**: 300, 400, 500, 600, 12px, 13px, 14px, 16px, 18px, 20px, 22px, 26px, 48px, 90px, 120px, 0.85, 1.00, 1.05, 1.10, 1.20, 1.25, 1.30, 1.45; substitute `Inter`.
- **Times**: 400, 16px, 1.20; substitute `serif`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `40px`
- Element Gap: `5px`
- Radius: `cards: 29.9952px, large: 15.9984px, small: 2.9952px, images: 29.9952px, medium: 10px, buttons: 999px`

## Surface cues
- **Deep Ocean Canvas** `#002025`: Primary page background, base layer.
- **Seaweed Green Card** `#05333a`: Elevated card backgrounds, distinct content containers.
- **Kelp Shadow Panel** `#244348`: Secondary elevated surfaces, often used for enclosed components or detailed data displays within cards.

## Component cues
- **Ghost Navigation Button**: Primary navigation links and text-based interactive elements
- **Gradient Call to Action Button**: Main interactive button for primary actions
- **Outlined Accent CTA**: Secondary call to action or link that needs visual emphasis without being a filled button.
- **Soft Card**: Container for content sections, subtly elevated
- **Muted Card Background**: Background for secondary content areas or embedded elements within cards.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
