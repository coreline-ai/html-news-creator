# VEED - Refero Design MD

- Source: https://styles.refero.design/style/fff821ec-a3bf-41a5-aea2-626185bcd227
- Original site: https://www.veed.io
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid green workspace.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Black | `#121212` | neutral | Primary text or dark surface |
| Slate Gray | `#323232` | neutral | Primary text or dark surface |
| Dark Granite | `#292a2e` | neutral | Primary text or dark surface |
| Medium Gray | `#71737a` | neutral | Border, muted text, or supporting surface |
| Light Ash | `#f2f1f0` | neutral | Page background or card surface |
| Electric Green | `#96ff1a` | brand | Action accent / signal color |
| Vivid Leaf | `#d6ffa6` | brand | Action accent / signal color |
| Forest Shade | `#083300` | brand | Action accent / signal color |
| Misty Mint | `#e6ffc8` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-charcoal-black: #121212;
  --ref-slate-gray: #323232;
  --ref-dark-granite: #292a2e;
  --ref-medium-gray: #71737a;
  --ref-light-ash: #f2f1f0;
  --ref-electric-green: #96ff1a;
  --ref-vivid-leaf: #d6ffa6;
}
```

## Typography direction
- **SwissNow**: 400, 11px, 12px, 13px, 14px, 16px, 40px, 44px, 54px, 0.88, 0.90, 1.00, 1.30, 1.36, 1.40, 1.43, 1.50, 1.80; substitute `Inter`.
- **SwissNow**: 500, 11px, 12px, 13px, 14px, 16px, 40px, 44px, 54px, 0.88, 0.90, 1.00, 1.30, 1.36, 1.40, 1.43, 1.50, 1.80; substitute `Inter`.
- **SwissNow**: 600, 11px, 12px, 13px, 14px, 16px, 40px, 44px, 54px, 0.88, 0.90, 1.00, 1.30, 1.36, 1.40, 1.43, 1.50, 1.80; substitute `Inter`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `lg: 16px, md: 10px, sm: 4px, pill: 58px`

## Surface cues
- **Canvas** `#ffffff`: Primary page background, expansive and bright.
- **Card Surface** `#f2f1f0`: Subtle, slightly off-white background for secondary cards and button states, offering a soft contrast.
- **Elevated Panel** `#292a2`: Dark background for distinct sections, providing depth and visual separation.

## Component cues
- **Primary Action Button**: Call to action
- **Secondary Action Button**: Alternative action
- **Ghost Button**: Minimal interaction
- **Dark Elevated Button**: Content container button
- **Promotional Card - Vivid Leaf**: Highlight content block

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
