# Neuralink - Refero Design MD

- Source: https://styles.refero.design/style/7510b18e-63c3-4c2a-97c3-39fa7dfa6ae3
- Original site: https://neuralink.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep void to soft textured canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Soft Linen | `#f5f5f5` | neutral | Page background or card surface |
| Ash Gray | `#bababa` | neutral | Border, muted text, or supporting surface |
| Neural Gradient | `#e486ab` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-canvas-white: #ffffff;
  --ref-soft-linen: #f5f5f5;
  --ref-ash-gray: #bababa;
  --ref-neural-gradient: #e486ab;
}
```

## Typography direction
- **UntitledSans**: 300, 400, 500, 700, 8px, 12px, 14px, 16px, 17px, 18px, 24px, 32px, 44px, 48px, 1.00, 1.15, 1.20, 1.50; substitute `System UI (sans-serif)`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `cards: 20px, buttons: 80px, circular: 50%, navItems: 16px`

## Surface cues
- **Midnight Void Canvas** `#000000`: Base background for hero sections and dark content areas, creating a deep, immersive feel.
- **Soft Linen Canvas** `#f5f5f5`: Secondary background for most content sections, providing a light, slightly textured contrast.
- **Component Surface** `#ffffff`: Background for interactive elements and prominent cards, standing out against the Soft Linen canvas.

## Component cues
- **Primary Call to Action Button**: Informative action button
- **Ghost Button (Dark)**: Secondary action on dark backgrounds
- **Ghost Button (Light)**: Secondary action on light backgrounds
- **Info Banner**: Top-level informational message
- **Navigation Link**: Main navigation item

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
