# Ballpark - Refero Design MD

- Source: https://styles.refero.design/style/9342e89b-c2fe-4acf-9993-53b44e0c13b5
- Original site: https://ballparkhq.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast research tool; like a scientific dashboard with a single, urgent indicator light.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#f9fafb` | neutral | Page background or card surface |
| Graphite | `#111827` | neutral | Primary text or dark surface |
| Slate Blue | `#4b5563` | neutral | Action accent / signal color |
| Medium Gray | `#374151` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#6b7280` | neutral | Border, muted text, or supporting surface |
| Border Gray | `#e5e7eb` | neutral | Page background or card surface |
| Rocket Red | `#fc4a2b` | brand | Action accent / signal color |
| Passion Red | `#e11d48` | brand | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-ghost-white: #ffffff;
  --ref-ash-gray: #f9fafb;
  --ref-graphite: #111827;
  --ref-slate-blue: #4b5563;
  --ref-medium-gray: #374151;
  --ref-light-gray: #6b7280;
  --ref-border-gray: #e5e7eb;
}
```

## Typography direction
- **Inter Display**: 700, 800, 42px, 60px, 96px, 1.00; substitute `system-ui, sans-serif`.
- **Inter**: 400, 500, 600, 700, 10px, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 1.20, 1.33, 1.38, 1.40, 1.43, 1.46, 1.50, 1.60, 1.65; substitute `system-ui, sans-serif`.
- **sans-serif**: 400, 12px, 1.20; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64-96px`
- Card Padding: `14-24px`
- Element Gap: `8px`
- Radius: `pill: 9999px, cards: 10px, images: 6px, inputs: 6px, buttons: 6px, interactive: 100px`

## Component cues
- **Announcement Banner**: Reference component style.
- **Pill Selector / Research Type Tabs**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Navigation Link**: Primary navigation in header
- **Secondary Ghost Button**: Tertiary actions, secondary calls to attention

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
