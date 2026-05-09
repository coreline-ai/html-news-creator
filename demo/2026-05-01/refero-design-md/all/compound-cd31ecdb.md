# Compound - Refero Design MD

- Source: https://styles.refero.design/style/cd31ecdb-297a-4fc5-a727-05f835ff917f
- Original site: https://withcompound.com/membership
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#171717` | neutral | Primary text or dark surface |
| Ash Gray | `#e5e7eb` | neutral | Page background or card surface |
| Smoke | `#7e7e7e` | neutral | Border, muted text, or supporting surface |
| Boulder | `#6f6f6f` | neutral | Border, muted text, or supporting surface |
| Cloud Gray | `#f3f3f3` | neutral | Page background or card surface |
| Stone Gray | `#8f8f8f` | neutral | Border, muted text, or supporting surface |
| Platinum | `#a0a0a0` | neutral | Border, muted text, or supporting surface |
| Warm Gold | `#ffc838` | accent | Action accent / signal color |
| Deep Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-graphite: #171717;
  --ref-ash-gray: #e5e7eb;
  --ref-smoke: #7e7e7e;
  --ref-boulder: #6f6f6f;
  --ref-cloud-gray: #f3f3f3;
  --ref-stone-gray: #8f8f8f;
  --ref-platinum: #a0a0a0;
}
```

## Typography direction
- **Monument Grotesk**: 400, 12px, 13px, 14px, 16px, 18px, 36px, 48px, 58px, 60px, 72px, 1.00, 1.10, 1.11, 1.25, 1.33, 1.38, 1.43, 1.50, 1.56, 1.71; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `4px`
- Radius: `cards: 20px, icons: 9999px, lists: 28px, images: 9999px, buttons: 9999px`

## Surface cues
- **Canvas Background** `#e5e7eb`: Dominant page background for the site.
- **Base Surface** `#ffffff`: Primary surface for cards, sections, and interactive elements.
- **Subtle Surface** `#f3f3f3`: Slightly recessed or highlighted areas; hover states, subtle background differentiation.
- **Dark Content Surface** `#000000`: Distinct, immersive content containers for media or specific product modules.

## Component cues
- **Text Only Button**: Link-style buttons for navigation and secondary actions.
- **Pill Primary Button**: Main calls to action.
- **Pill Inverted Button**: Secondary action or prominent ghost button.
- **Elevated Content Card**: Container for featured information or interactive content blocks.
- **Dark Embed Card**: Embedded content blocks, often product screenshots or code examples.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
