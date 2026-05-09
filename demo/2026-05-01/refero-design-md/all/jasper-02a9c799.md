# Jasper - Refero Design MD

- Source: https://styles.refero.design/style/02a9c799-eb91-425b-8d68-3776b5e84229
- Original site: https://jasper.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Marketing billboard meets data dashboard. Bold headlines and vibrant accents punctuate a clean, analytical canvas.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Smoke Gray | `#f9f9f9` | neutral | Page background or card surface |
| Graphite | `#5e5d5f` | neutral | Border, muted text, or supporting surface |
| Jasper Indigo | `#00063d` | brand | Action accent / signal color |
| Jasper Flame | `#fa4028` | brand | Action accent / signal color |
| System Red | `#fa7560` | semantic | Action accent / signal color |
| System Green | `#103a00` | semantic | Action accent / signal color |
| Research Green | `#e6ffd9` | accent | Action accent / signal color |
| Highlight Blue | `#0095ff` | accent | Action accent / signal color |
| Highlight Pink | `#5a003c` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-smoke-gray: #f9f9f9;
  --ref-graphite: #5e5d5f;
  --ref-jasper-indigo: #00063d;
  --ref-jasper-flame: #fa4028;
  --ref-system-red: #fa7560;
  --ref-system-green: #103a00;
  --ref-research-green: #e6ffd9;
}
```

## Typography direction
- **Feature**: 450, 20px, 24px, 28px, 38px, 54px, 80px, 1.00, 1.05, 1.10; substitute `Georgia`.
- **ABC ROM**: 450, 500, 700, 14px, 16px, 18px, 28px, 1.00, 1.20, 1.40; substitute `Graphik`.
- **ABC ROM Mono**: 450, 14px, 16px, 1.00, 1.20, 1.40; substitute `DM Mono`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `badge: 4px, default: 0px`

## Component cues
- **Announcement Banner + CTA Buttons**: Reference component style.
- **Platform Section Block**: Reference component style.
- **Metric Stat Card**: Reference component style.
- **Primary CTA Button**: Call to action
- **Secondary CTA Button**: Secondary call to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
