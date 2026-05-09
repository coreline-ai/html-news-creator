# Pentagram - Refero Design MD

- Source: https://styles.refero.design/style/86b56f02-57da-48a1-a647-fda9bbdf2c97
- Original site: https://pentagram.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Drafting on Blueprint

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1a1a1a` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Stone Gray | `#8c8c8c` | neutral | Border, muted text, or supporting surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal | `#222222` | neutral | Primary text or dark surface |
| Silver Mist | `#e3e4e5` | neutral | Page background or card surface |
| Deep Graphite | `#333333` | neutral | Primary text or dark surface |
| Soft Stone | `#767676` | neutral | Border, muted text, or supporting surface |
| Pentagram Blue | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #1a1a1a;
  --ref-canvas-white: #ffffff;
  --ref-stone-gray: #8c8c8c;
  --ref-pitch-black: #000000;
  --ref-charcoal: #222222;
  --ref-silver-mist: #e3e4e5;
  --ref-deep-graphite: #333333;
  --ref-soft-stone: #767676;
}
```

## Typography direction
- **Plain**: 400, 500, 13px, 16px, 19px, 27px, 32px, 52px, 1.00, 1.05, 1.19, 1.20, 1.25, 1.32, 1.88; substitute `Arial, Helvetica, sans-serif`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `24px`
- Element Gap: `8px`
- Page Max Width: `1728px`
- Radius: `cards: 8px, buttons: 4px, default: 4px, pillButtons: 9999px`

## Component cues
- **Ghost Button Inverse**: Interactive elements for secondary actions or navigation.
- **Pill Button Inverse**: Small, contained labels or filters.
- **Soft Tag Button**: Categorization or filter tags with a subtle background.
- **Filled Action Button**: Primary calls to action with high visual weight.
- **Clear Card**: Container for content where the background is part of the overall page design.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
