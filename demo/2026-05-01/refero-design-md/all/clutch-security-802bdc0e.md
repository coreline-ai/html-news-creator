# Clutch Security - Refero Design MD

- Source: https://styles.refero.design/style/802bdc0e-ec2e-4d2d-bf5d-de98c0899f66
- Original site: https://www.clutch.security
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist digital blueprint

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Storm Gray | `#e5e7eb` | neutral | Page background or card surface |
| Muted Gray | `#dfdfdf` | neutral | Page background or card surface |
| Whisper Gray | `#c9c9c9` | neutral | Border, muted text, or supporting surface |
| Dim Gray | `#6e6e6e` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#004dff` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-storm-gray: #e5e7eb;
  --ref-muted-gray: #dfdfdf;
  --ref-whisper-gray: #c9c9c9;
  --ref-dim-gray: #6e6e6e;
  --ref-electric-blue: #004dff;
}
```

## Typography direction
- **Inter**: 400, 500, 700, 12px, 14px, 15px, 16px, 17px, 1.30, 1.40, 1.50; substitute `system-ui`.
- **PP Radio Grotesk**: 400, 500, 600, 10px, 12px, 13px, 14px, 20px, 24px, 26px, 32px, 38px, 56px, 68px, 1.10, 1.20, 1.30, 1.40, 1.50; substitute `sans-serif`.
- **Times**: 400, 16px, 1.2.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 6px, pills: 80px, buttons: 6px, default: 6px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for most content.
- **Muted Gray** `#dfdfdf`: Subtle background for UI elements like cards or sections, providing minimal visual separation.

## Component cues
- **Primary Action Button**: Filled call to action
- **Ghost Button**: Call to action variant
- **Navigation Link**: Header and footer navigation
- **Detail Card**: Informational container
- **Input Field**: User entry fields

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
