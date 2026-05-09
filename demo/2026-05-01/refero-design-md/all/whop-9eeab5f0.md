# Whop - Refero Design MD

- Source: https://styles.refero.design/style/9eeab5f0-eece-4898-a1d2-2db48ac2bc7d
- Original site: https://whop.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Clean, bold, and energetic.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Dark Graphite | `#202020` | neutral | Primary text or dark surface |
| Medium Gray | `#646464` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#838383` | neutral | Border, muted text, or supporting surface |
| Border Silver | `#bbbbbb` | neutral | Border, muted text, or supporting surface |
| Very Light Gray | `#e1e4e8` | neutral | Page background or card surface |
| Dark Surface | `#0a0a0a` | neutral | Primary text or dark surface |
| Whop Orange | `#fa4616` | brand | Action accent / signal color |
| Orange Shadow | `#b62600` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-dark-graphite: #202020;
  --ref-medium-gray: #646464;
  --ref-light-gray: #838383;
  --ref-border-silver: #bbbbbb;
  --ref-very-light-gray: #e1e4e8;
  --ref-dark-surface: #0a0a0a;
  --ref-whop-orange: #fa4616;
}
```

## Typography direction
- **acidGroteskFont**: 700, 56px, 128px, 1.00; substitute `Arial Black, sans-serif`.
- **Inter**: 400, 500, 600, 700, 13px, 14px, 16px, 20px, 1.40, 1.43, 1.50; substitute `system-ui, sans-serif`.
- **Geist Mono**: 500, 600, 12px, 13px, 14px, 16px, 1.50, 1.70; substitute `SF Mono, Menlo, monospace`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `misc: 16px, tags: 8px, cards: 24px, forms: 8px, buttons: 8px`

## Component cues
- **Primary Action Button**: Main call-to-action
- **Ghost Secondary Button**: Alternative action, navigation
- **Tab Button**: Category filtering, sub-navigation
- **Feature Card**: Information display, product showcases
- **Subtle Background Card**: Grouped content section

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
