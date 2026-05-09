# Safepal - Refero Design MD

- Source: https://styles.refero.design/style/a74d60e1-0a09-48a1-8721-13f1f45727f1
- Original site: https://www.safepal.com
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cosmic digital frontier

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#0d0b33` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#f7f6ff` | neutral | Page background or card surface |
| Slate | `#666666` | neutral | Border, muted text, or supporting surface |
| Twilight Indigo | `#4a21ef` | brand | Action accent / signal color |
| Emerald Growth | `#79efbd` | accent | Action accent / signal color |
| Jade Outline | `#18d26e` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-space: #0d0b33;
  --ref-cloud-white: #ffffff;
  --ref-ash-gray: #f7f6ff;
  --ref-slate: #666666;
  --ref-twilight-indigo: #4a21ef;
  --ref-emerald-growth: #79efbd;
  --ref-jade-outline: #18d26e;
}
```

## Typography direction
- **AlibabaPuHuiTi-2**: 400, 700, 800, 900, 1000, 12px, 14px, 16px, 18px, 24px, 32px, 48px, 80px, 137px, 1.00, 1.17, 1.20, 1.50, 1.56, 1.57, 1.60; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `113px`
- Card Padding: `53px`
- Element Gap: `12px`
- Page Max Width: `1200px`
- Radius: `cards: 24px, buttons: 100px, largeElements: 48px, navigationItems: 12px`

## Component cues
- **Primary Action Button (Emerald)**: Call to action button for key conversions.
- **Secondary Ghost Button (White)**: Alternative call to action, offering less visual prominence.
- **Tertiary Outline Button (Dark)**: Low-prominence action button, often for secondary functions.
- **Info Card**: Container for testimonials, features, or content blocks.
- **Header Navigation Item**: Top-level navigation link.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
