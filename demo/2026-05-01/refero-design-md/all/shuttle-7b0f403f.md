# Shuttle - Refero Design MD

- Source: https://styles.refero.design/style/7b0f403f-5428-49dc-9ae3-addbe64261ae
- Original site: https://shuttle.zip/about
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp digital canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#f9f9f9` | neutral | Page background or card surface |
| Border Fog | `#e5e7eb` | neutral | Page background or card surface |
| Stroke Silver | `#b8b8b8` | neutral | Border, muted text, or supporting surface |
| Graphite Black | `#000000` | neutral | Primary text or dark surface |
| Muted Ash | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Text Slate | `#525252` | neutral | Border, muted text, or supporting surface |
| Shuttle Blue | `#0077ff` | brand | Action accent / signal color |
| Warning Gold | `#f59e0b` | accent | Action accent / signal color |
| Error Ember | `#ef4444` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-cloud-gray: #f9f9f9;
  --ref-border-fog: #e5e7eb;
  --ref-stroke-silver: #b8b8b8;
  --ref-graphite-black: #000000;
  --ref-muted-ash: #a3a3a3;
  --ref-text-slate: #525252;
  --ref-shuttle-blue: #0077ff;
}
```

## Typography direction
- **InterVariable**: 400, 500, 600, 700, 10px, 11px, 12px, 14px, 15px, 16px, 62px, 1.00, 1.16, 1.25, 1.33, 1.40, 1.43, 1.50, 1.67; substitute `Inter`.

## Spacing / shape
- Section Gap: `128px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `cards: 16px, badges: 9999px, inputs: 8px, avatars: 9999px, buttons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background
- **Cloud Gray** `#f9f9f9`: Grouped element backgrounds

## Component cues
- **Primary Action Button**: Key interactions
- **Ghost Button**: Secondary actions
- **Light Ghost Button**: Contextual actions within cards or other surfaces
- **Elevated Content Card**: Prominent content blocks
- **Subtle Background Card**: Informational panels

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
