# Martin Laxenaire - Refero Design MD

- Source: https://styles.refero.design/style/0e8db8d0-4d8f-48ac-a8e7-aaea9601e3ce
- Original site: https://www.martin-laxenaire.fr
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant canvas, bold typography

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#121212` | neutral | Primary text or dark surface |
| Candy Pink | `#f9d9f7` | accent | Action accent / signal color |
| Playful Blue | `#3430ee` | accent | Action accent / signal color |
| Electric Purple | `#8000ff` | accent | Action accent / signal color |
| Teal Wave | `#008170` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #121212;
  --ref-candy-pink: #f9d9f7;
  --ref-playful-blue: #3430ee;
  --ref-electric-purple: #8000ff;
  --ref-teal-wave: #008170;
}
```

## Typography direction
- **MonumentExtended UltraBold**: 400, 700, 18px, 21px, 63px, 94px, 105px, 167px, 419px, 0.75, 0.85, 1.20; substitute `Bebas Neue`.
- **MonumentExtended Regular**: 400, 16px, 21px, 26px, 0.85, 1.20; substitute `Bebas Neue`.
- **Swiss**: 400, 16px, 17px, 19px, 21px, 31px, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `42px`
- Card Padding: `19px`
- Element Gap: `21px`
- Page Max Width: `1440px`
- Radius: `buttons: 16.22px, 20.93px, default: 20.93px, elements: 20.93px`

## Surface cues
- **Canvas Background** `#ffffff`: The foundational background for the entire page and default surface.
- **Accent Section Background** `#f9d9f7`: Used to create alternating background sections, adding visual interest and breaking up the page content.

## Component cues
- **Header Navigation Link**: Text-based navigation link in the header.
- **Ghost Button**: Minimal interactive button, often for secondary actions or decorative information displays.
- **Pill Button (Filled)**: Primary Call-to-action button or interactive element.
- **Pill Button (Ghost)**: Secondary action or interactive label with a distinct rounded shape.
- **Progress Meter (Horizontal)**: Interactive element indicating progress or state.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
