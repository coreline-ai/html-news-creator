# Fabric - Refero Design MD

- Source: https://styles.refero.design/style/67cdbe0a-a9d5-4a41-91a6-5b26550efc69
- Original site: https://fabric.so
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp digital canvas with thoughtful ink

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#0a0a0a` | neutral | Primary text or dark surface |
| Deep Graphite | `#000000` | neutral | Primary text or dark surface |
| Light Pearl | `#f3f3f3` | neutral | Page background or card surface |
| Ash Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Slate Text | `#333333` | neutral | Primary text or dark surface |
| Dark Charcoal | `#404040` | neutral | Border, muted text, or supporting surface |
| Soft Stone | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Regal Violet | `#1100ff` | brand | Action accent / signal color |
| Outline Violet | `#19154e` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #0a0a0a;
  --ref-deep-graphite: #000000;
  --ref-light-pearl: #f3f3f3;
  --ref-ash-gray: #666666;
  --ref-slate-text: #333333;
  --ref-dark-charcoal: #404040;
  --ref-soft-stone: #b3b3b3;
}
```

## Typography direction
- **GT Alpina Light**: 300, 400, 32px, 52px, 80px, 1.08, 1.40; substitute `Sans-serif serif`.
- **Inter**: 400, 500, 600, 11px, 15px, 16px, 17px, 18px, 26px, 28px, 1.20, 1.30, 1.40, 1.45, 1.50, 1.60, 2.00; substitute `system-ui, sans-serif`.
- **Manrope**: 700, 900, 18px, 1.40; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `10px`
- Radius: `cards: 24px, images: 16px, buttons: 8px, inner-cards: 16px, pill-buttons: 40px, small-elements: 4px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background
- **Default Card Background** `#fafafa`: Standard card surfaces and elevated content blocks
- **Inner UI Card Background** `#f2f2f580`: Subtle, slightly translucent background typically for nested UI or side panels, indicating a secondary surface within a card.

## Component cues
- **Primary Filled Button**: Call to action button for primary actions
- **Transparent Pill Button**: Filter or category selection buttons with a softer presence
- **Outline Button**: Secondary actions or navigation-style buttons
- **Subtle Filled Button**: Tertiary actions or subtle interactive elements
- **Default Card**: Container for content, features, or UI elements

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
