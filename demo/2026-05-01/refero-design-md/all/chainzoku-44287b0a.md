# Chainzoku - Refero Design MD

- Source: https://styles.refero.design/style/44287b0a-8709-406d-8ba3-8765ecb19a1f
- Original site: https://chainzoku.io
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neon Cyberpunk Nightscape – A high-contrast world of dark urban realism punctuated by electric neon accents.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#fffff7` | neutral | Page background or card surface |
| Deep Shadow | `#1c1616` | neutral | Primary text or dark surface |
| Faded Concrete | `#c4c1c6` | neutral | Border, muted text, or supporting surface |
| Electric Lime | `#cdfb52` | accent | Action accent / signal color |
| Sky Blue | `#5c97ce` | accent | Action accent / signal color |
| Cyber Pink | `#f24ac7` | accent | Action accent / signal color |
| Olive Drab | `#485229` | accent | Action accent / signal color |
| Forest Fern | `#8c9b57` | accent | Action accent / signal color |
| Crimson Glare | `#ab0000` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-ghost-white: #fffff7;
  --ref-deep-shadow: #1c1616;
  --ref-faded-concrete: #c4c1c6;
  --ref-electric-lime: #cdfb52;
  --ref-sky-blue: #5c97ce;
  --ref-cyber-pink: #f24ac7;
  --ref-olive-drab: #485229;
}
```

## Typography direction
- **NeueHaasGrotDisp**: 400, 500, 900, 16px, 18px, 23px, 26px, 40px, 57px, 90px, 100px, 1.00, 1.19, 1.20, 1.39; substitute `Helvetica Neue`.
- **Helvetica Neue**: 400, 700, 26px, 30px, 0.78.
- **Druk Heavy**: 400, 100px, 177px, 301px, 0.80; substitute `Bebas Neue`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `40px`
- Element Gap: `8px`
- Radius: `cards: 10px, navigation: 15px`

## Surface cues
- **Canvas Base** `#fffff7`: Primary page background, light sections, often serves as the base for high-contrast text.
- **Subtle Dark Card** `#1c1616`: Background for self-contained content cards or distinct sections that require a darker context.
- **Footer Canvas** `#c4c1c6`: Background for the footer and other low-priority information areas, offering minimal contrast against the primary white.

## Component cues
- **Ghost Navigation Link: Dark**: Primary header navigation and sidebar links.
- **Ghost Navigation Link: Light**: Primary header navigation and sidebar links.
- **Pill Accent Button**: Primary calls to action for key interactions.
- **Outline Sidebar Button**: Interactive elements within the left sidebar navigation.
- **Base Card**: Structural container for content sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
