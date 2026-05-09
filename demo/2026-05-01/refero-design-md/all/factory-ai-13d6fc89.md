# Factory.ai - Refero Design MD

- Source: https://styles.refero.design/style/13d6fc89-eba2-4724-ac37-20f4f2e5efec
- Original site: https://factory.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble. Lines are crisp, colors are limited, and every element serves a clear, functional purpose.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Factory Black | `#020202` | neutral | Primary text or dark surface |
| Factory Light Gray | `#eeeeee` | neutral | Page background or card surface |
| Faded Silver | `#fafafa` | neutral | Page background or card surface |
| Cool Gray | `#b8b3b0` | neutral | Border, muted text, or supporting surface |
| Graphite | `#3d3a39` | neutral | Primary text or dark surface |
| Ash Gray | `#a49d9a` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-factory-black: #020202;
  --ref-factory-light-gray: #eeeeee;
  --ref-faded-silver: #fafafa;
  --ref-cool-gray: #b8b3b0;
  --ref-graphite: #3d3a39;
  --ref-ash-gray: #a49d9a;
}
```

## Typography direction
- **Geist**: 400, 14px, 16px, 18px, 24px, 48px, 60px, 1.00, 1.20, 1.50; substitute `Inter`.
- **Geist Mono**: 400, 12px, 14px, 16px, 18px, 1.00, 1.20, 1.38, 1.50; substitute `JetBrains Mono`.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `cards: 6px, header: 0px, buttons: 4px, default: 4px`

## Component cues
- **CLI Install Block**: Reference component style.
- **News Article Cards**: Reference component style.
- **Product Section Nav**: Reference component style.
- **Text Link**: Navigation, inline links, 'Learn More' buttons
- **Navigation Link**: Top navigation menu items

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
