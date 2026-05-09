# Campsite - Refero Design MD

- Source: https://styles.refero.design/style/5d8ad116-b3d8-4890-a969-5b856b35c678
- Original site: https://www.campsite.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard with sticky notes — clean, organized, and quietly structured.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#171717` | neutral | Primary text or dark surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Pale Gray | `#f5f5f5` | neutral | Page background or card surface |
| Cream Canvas | `#fffdf9` | neutral | Page background or card surface |
| Ash Gray | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Off White | `#f0f0f0` | neutral | Page background or card surface |
| Slate Gray | `#737373` | neutral | Border, muted text, or supporting surface |
| Charcoal Text | `#525252` | neutral | Border, muted text, or supporting surface |
| Forest Green | `#22c55e` | accent | Action accent / signal color |
| Warning Red | `#ef4444` | accent | Action accent / signal color |

```css
:root {
  --ref-ink-black: #171717;
  --ref-arctic-white: #ffffff;
  --ref-pale-gray: #f5f5f5;
  --ref-cream-canvas: #fffdf9;
  --ref-ash-gray: #a3a3a3;
  --ref-off-white: #f0f0f0;
  --ref-slate-gray: #737373;
  --ref-charcoal-text: #525252;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 22px, 29px, 58px, 1.00, 1.20, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63, 1.80; substitute `system-ui, sans-serif`.
- **ui-monospace**: 400, 600, 12px, 1.00; substitute `monospace`.
- **emoji**: 500, 600, 12px, 14px, 1.00; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `lg: 12px, md: 8px, sm: 4px, none: 0px, circular: 9999px`

## Surface cues
- **Cream Canvas** `#fffdf9`: Dominant page background
- **Arctic White** `#ffffff`: Primary card surfaces, base for elevated components
- **Pale Gray** `#f5f5f5`: Secondary card surfaces, feature backgrounds, subtle textural differentiation

## Component cues
- **Ghost Button**: Secondary action control
- **Subtle Gray Button**: Tertiary action control, tag
- **Primary Action Button**: Call to action
- **Interactive Card Shadowed**: Container for actionable content
- **Secondary Surface Card**: Background for feature blocks or secondary content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
