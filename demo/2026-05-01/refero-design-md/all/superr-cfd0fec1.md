# Superr - Refero Design MD

- Source: https://styles.refero.design/style/cfd0fec1-f25a-4b9b-9bd0-d5b66960f2f2
- Original site: https://www.superr.ai
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Child's Animated Sketchbook. This system feels like looking into a favorite, well-loved school notebook where every element has personality.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#fdfbf9` | neutral | Page background or card surface |
| Deep Graphite | `#171717` | neutral | Primary text or dark surface |
| Soft Black | `#2b1a07` | neutral | Primary text or dark surface |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Warm Gray Shadow | `#bebcbb` | neutral | Border, muted text, or supporting surface |
| Cheeky Orange | `#ff6f1e` | brand | Action accent / signal color |
| Playful Red | `#ce500a` | brand | Action accent / signal color |
| Sky Blue | `#3b82f6` | brand | Action accent / signal color |
| Bubblegum Pink | `#ff66cf` | brand | Action accent / signal color |
| Grass Green | `#22c55e` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-parchment: #fdfbf9;
  --ref-deep-graphite: #171717;
  --ref-soft-black: #2b1a07;
  --ref-jet-black: #000000;
  --ref-warm-gray-shadow: #bebcbb;
  --ref-cheeky-orange: #ff6f1e;
  --ref-playful-red: #ce500a;
  --ref-sky-blue: #3b82f6;
}
```

## Typography direction
- **gelica**: 400, 500, 600, 16px, 20px, 24px, 28px, 32px, 36px, 40px, 46px, 104px, 1.08, 1.20, 1.40, 1.50; substitute `Comic Sans MS (as a last resort), or a custom script font like 'Caveat' or 'Gochi Hand' if 'gelica' is unavailable.`.
- **Geist**: 400, 500, 18px, 20px, 32px, 1.50; substitute `Inter, Figtree, or General Sans.`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `12px`
- Radius: `tags: 56px, cards: 12px, avatar: 9999px, fields: 8px, buttons: 20px, default: 8px`

## Component cues
- **Ghost Button**: Interactive element, secondary action
- **Pill Ghost Button**: Call to action, primary interaction
- **Elevated Card**: Content container, feature display
- **Navigation Link**: Primary navigation item

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
