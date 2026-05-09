# Giga - Refero Design MD

- Source: https://styles.refero.design/style/607e0dbf-e2fc-45c9-b939-946b8981c156
- Original site: https://giga.ai
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep night, mountain vista – a cosmic, digital calm.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Ghost | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Shadow | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Pebble Gray | `#969696` | neutral | Border, muted text, or supporting surface |
| Night Sky | `#161717` | neutral | Primary text or dark surface |
| Steel Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Cosmic Dust | `#8a8f98` | neutral | Border, muted text, or supporting surface |
| Ember Glow | `#fe2c02` | accent | Action accent / signal color |
| Growth Green | `#49de80` | accent | Action accent / signal color |

```css
:root {
  --ref-obsidian: #000000;
  --ref-ghost: #ffffff;
  --ref-graphite: #cccccc;
  --ref-shadow: #4d4d4d;
  --ref-pebble-gray: #969696;
  --ref-night-sky: #161717;
  --ref-steel-gray: #808080;
  --ref-cosmic-dust: #8a8f98;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20.
- **Inter**: 300, 400, 500, 8px, 9px, 10px, 11px, 12px, 13px, 14px, 16px, 29px, 44px, 1.00, 1.36, 1.50, 1.54, 1.64, 1.70, 1.71, 1.75, 1.85, 1.93, 2.00, 2.22.
- **Geist Mono**: 400, 500, 11px, 12px, 14px, 1.20, 2.00, 2.18.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `cards: 16px, icons: 9999px, buttons: 1000px, default: 10px`

## Surface cues
- **Deep Space** `#000000`: Primary page background, creating a vast, dark canvas.
- **Subtle Nebula** `#cccccc`: Base background for sections and cards, providing a barely-there structural layer.
- **Whisper Card** `#00000033`: Elevated card background with slight transparency, allowing underlying elements to subtly show through.
- **Ghost Panel** `#00000005`: Secondary card backgrounds, an even lighter, more transparent layer.

## Component cues
- **Ghost Pill Button**: Secondary action or navigation with minimal visual weight.
- **Primary Filled Pill Button**: Main call to action, standing out with a solid background.
- **Dark Filled Pill Button**: Call to action on lighter backgrounds, inverted version of the primary.
- **Small Decorative Pill Button**: Informational or tag-like elements with a subtle, dark background.
- **Transparent Card**: Content container with a very subtle, almost ghost-like presence.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
