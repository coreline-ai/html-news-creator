# Klim - Refero Design MD

- Source: https://styles.refero.design/style/0dad8530-9422-4d9e-8622-1f50ee4bc702
- Original site: https://klim.co.nz
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type specimen on black velvet

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Ghost Gray | `#555555` | neutral | Border, muted text, or supporting surface |
| Input Dark | `#1c1c1c` | neutral | Primary text or dark surface |
| Text White | `#ffffff` | neutral | Page background or card surface |
| Ocean Blue | `#24a7f2` | accent | Action accent / signal color |
| Forest Green | `#3c585f` | accent | Action accent / signal color |
| Fire Orange | `#d33c03` | accent | Action accent / signal color |
| Vivid Red | `#e90702` | accent | Action accent / signal color |
| Neon Teal | `#93ffe6` | accent | Action accent / signal color |
| Muted Peach | `#ffe6d9` | accent | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-ghost-gray: #555555;
  --ref-input-dark: #1c1c1c;
  --ref-text-white: #ffffff;
  --ref-ocean-blue: #24a7f2;
  --ref-forest-green: #3c585f;
  --ref-fire-orange: #d33c03;
  --ref-vivid-red: #e90702;
}
```

## Typography direction
- **SOEHNE**: 400, 700, 16px, 36px, 0.98, 1.19, 1.20, 1.33, 1.50; substitute `Inter`.
- **SOEHNE_IKON**: 400, 16px, 1.20, 1.33, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `69px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `cards: 0px, links: 2px, images: 2px, inputs: 2px, buttons: 2px, navItems: 2px`

## Surface cues
- **Pitch Black Canvas** `#000000`: Primary page background, foundation for all content.
- **Dark Panel** `#101c19`: Used for content sections or background variations on the main canvas.
- **Input Dark Surface** `#1c1c1c`: Background for interactive input fields and similar components, indicating focus.

## Component cues
- **Filled Primary Button**: Call-to-action button for initiating primary actions.
- **Outlined Secondary Button**: Secondary action button, providing a less prominent interactive element.
- **Navigation Link Button**: Interactive text link within navigation areas.
- **Text Input Field**: Form input for user text entry.
- **Transparent Card**: Content container that blends into the background, often for lists of items.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
