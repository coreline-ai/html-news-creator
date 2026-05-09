# HeroKit - Refero Design MD

- Source: https://styles.refero.design/style/b3f7b44d-6564-4015-902a-259b4790b9de
- Original site: https://herokit.design
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark mode canvas with vivid yellow punctuation

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Pearl | `#ffffff` | neutral | Page background or card surface |
| Gunmetal | `#333333` | neutral | Primary text or dark surface |
| Steel Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Electric Yellow | `#ffffa7` | brand | Action accent / signal color |
| Vivid Canary | `#fddd05` | brand | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-pearl: #ffffff;
  --ref-gunmetal: #333333;
  --ref-steel-gray: #999999;
  --ref-medium-gray: #808080;
  --ref-electric-yellow: #ffffa7;
  --ref-vivid-canary: #fddd05;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **PP Neue Montreal**: 400, 16px, 20px, 30px, 32px, 50px, 120px, 144px, 1.00, 1.08, 1.20, 1.30, 1.40; substitute `system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`.
- **ABC Monument Grotesk**: 400, 120px, 1.00; substitute `system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `14px`
- Element Gap: `10px`
- Radius: `large: 16px, default: 8px`

## Surface cues
- **Canvas** `#000000`: Dominant page background, deepest layer.
- **Card Base** `#000000`: Cards and content blocks, visually distinct from page background by content, not color.

## Component cues
- **Navigation Link**: Standard navigation item for top bar
- **Primary Action Button**: Main call-to-action button, visually prominent
- **Secondary Action Button**: Less prominent action button, typically ghost or outlined style
- **Product Card**: Container for showcasing individual product items or components

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
