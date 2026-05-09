# Sleeve - Refero Design MD

- Source: https://styles.refero.design/style/2b49d4b2-8461-4985-b7ee-cf9517e19803
- Original site: https://replay.software/sleeve
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Macintosh desktop app on white marble. The design system feels like a carefully crafted macOS application brought to a website, with crisp, clean elements resting on a bright, uncluttered surface.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Marble | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#f9fafb` | neutral | Page background or card surface |
| Border Fog | `#e5e7eb` | neutral | Page background or card surface |
| Ash Text | `#000000` | neutral | Primary text or dark surface |
| Slate Text | `#333333` | neutral | Primary text or dark surface |
| Steel Accent | `#374151` | neutral | Border, muted text, or supporting surface |
| Deep Sea Gradient | `#0e95ee` | brand | Action accent / signal color |
| Success Leaf | `#53bc2a` | semantic | Action accent / signal color |
| Error Ember | `#750d0d` | semantic | Action accent / signal color |
| Accent Violet | `#783af5` | accent | Action accent / signal color |

```css
:root {
  --ref-white-marble: #ffffff;
  --ref-cloud-gray: #f9fafb;
  --ref-border-fog: #e5e7eb;
  --ref-ash-text: #000000;
  --ref-slate-text: #333333;
  --ref-steel-accent: #374151;
  --ref-deep-sea-gradient: #0e95ee;
  --ref-success-leaf: #53bc2a;
}
```

## Typography direction
- **ui-sans-serif**: 400, 500, 600, 700, 900, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 24px, 48px, 96px, 1.00, 1.33, 1.40, 1.43, 1.50, 1.56; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `96px`
- Element Gap: `8px`
- Page Max Width: `1264px`
- Radius: `cards: 24px, buttons: 12px, elements: 12px, pillButtons: 9999px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Cards Grid**: Reference component style.
- **Product Tab Selector**: Reference component style.
- **Ghost Navigation Button**: Primary navigation and selection in header.
- **Bordered Pill Button**: Secondary navigation and filtering tags.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
