# Affinity - Refero Design MD

- Source: https://styles.refero.design/style/6fd5c4e6-7003-4768-bc62-1b9c0c774054
- Original site: https://www.affinity.studio
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Theatrical design stage, floating artworks

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Black | `#000000` | neutral | Primary text or dark surface |
| Foreground Black | `#0f1015` | neutral | Primary text or dark surface |
| Dark Card Surface | `#211d1d` | neutral | Primary text or dark surface |
| Midtone Gray | `#505050` | neutral | Border, muted text, or supporting surface |
| Light Gray Text | `#707477` | neutral | Border, muted text, or supporting surface |
| Muted White | `#e0dcd6` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Border Silver | `#c4c4c4` | neutral | Border, muted text, or supporting surface |
| Affinity Green | `#a7f175` | brand | Action accent / signal color |
| Ocean Teal | `#83d9e1` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-black: #000000;
  --ref-foreground-black: #0f1015;
  --ref-dark-card-surface: #211d1d;
  --ref-midtone-gray: #505050;
  --ref-light-gray-text: #707477;
  --ref-muted-white: #e0dcd6;
  --ref-paper-white: #ffffff;
  --ref-border-silver: #c4c4c4;
}
```

## Typography direction
- **Affinity Serif Variable**: 400, 700, 48px, 56px, 80px, 112px, 0.96, 0.98, 1.00, 1.10; substitute `Playfair Display or Lora`.
- **Canva Sans**: 400, 401, 500, 600, 700, 10px, 13px, 14px, 16px, 19px, 24px, 32px, 38px, 1.20, 1.25, 1.30, 1.38, 1.40, 1.50, 1.57; substitute `Inter or Lato`.
- **Times**: 400, 10px, 1.20; substitute `Georgia`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `cards: 8px, links: 4px, pills: 9999px, buttons: 8px, default: 8px`

## Component cues
- **Primary Action Button**: Key interaction element
- **Ghost Button (Pill)**: Secondary action control
- **Cookie Action Button**: Tertiary consent action
- **Light-Theme Card**: Content container on dark backgrounds
- **Dark-Theme Card**: Content container on dark backgrounds

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
