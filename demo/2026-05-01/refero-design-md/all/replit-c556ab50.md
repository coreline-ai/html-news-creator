# replit - Refero Design MD

- Source: https://styles.refero.design/style/c556ab50-a242-4854-9395-450c0004bac5
- Original site: https://replit.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, creative studio. Like paper and clay in a sunlit workbench, punctuated by a streak of vibrant orange.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#faf6f1` | neutral | Page background or card surface |
| Ghost | `#ffffff` | neutral | Page background or card surface |
| Carbon | `#0e0e0f` | neutral | Primary text or dark surface |
| Lead | `#36373b` | neutral | Primary text or dark surface |
| Ash | `#898c94` | neutral | Border, muted text, or supporting surface |
| Stone | `#dfddd8` | neutral | Page background or card surface |
| Off-White Accent | `#cbc7c3` | neutral | Border, muted text, or supporting surface |
| Slate | `#52545a` | neutral | Border, muted text, or supporting surface |
| Black | `#000000` | neutral | Primary text or dark surface |
| Signal Orange | `#ff3c00` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas: #faf6f1;
  --ref-ghost: #ffffff;
  --ref-carbon: #0e0e0f;
  --ref-lead: #36373b;
  --ref-ash: #898c94;
  --ref-stone: #dfddd8;
  --ref-off-white-accent: #cbc7c3;
  --ref-slate: #52545a;
}
```

## Typography direction
- **ABC Diatype**: 400, 500, 12px, 13px, 14px, 16px, 32px, 1.20, 1.25, 1.38, 1.50, 1.60; substitute `Inter`.
- **ABC Diatype Plus Variable**: 400, 500, 600, 700, 8px, 10px, 11px, 12px, 14px, 15px, 16px, 17px, 18px, 20px, 24px, 26px, 28px, 32px, 42px, 48px, 60px, 64px, 69px, 0.80, 0.83, 0.89, 1.00, 1.05, 1.10, 1.20, 1.40, 1.60; substitute `Inter Variable`.
- **IBM Plex Sans**: 400, 14px, 1.00, 1.20, 1.57; substitute `IBM Plex Sans`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `lg: 20px, md: 16px, sm: 6px, xl: 40px, 2xl: 60px, none: 0px, pill: 90px`

## Surface cues
- **Page Canvas** `#faf6f1`: The foundational background for the entire page, providing a warm, slightly textured base.
- **Floating Card** `#ffffff`: Used for distinct content cards and interactive components, appearing crisp and elevated above the canvas.
- **Muted Content Card** `#faf6f1`: A surface that subtly blends with the page canvas but has distinct borders or is part of a different section.

## Component cues
- **Primary Action Button**: Call to action
- **Ghost Border Button**: Secondary action
- **Muted Border Button**: Tertiary action or filter tag
- **Feature Card**: Product feature display
- **Decorative Section Card**: Visual content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
