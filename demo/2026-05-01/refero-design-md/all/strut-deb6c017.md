# Strut - Refero Design MD

- Source: https://styles.refero.design/style/deb6c017-d2d3-4945-aaee-fa3d9ea6de70
- Original site: https://strut.so
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Antique Paper Workspace

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Oatmeal Canvas | `#e5dfd5` | neutral | Page background or card surface |
| Muted Ash | `#73706b` | neutral | Border, muted text, or supporting surface |
| Storm Gray | `#676460` | neutral | Border, muted text, or supporting surface |
| Charcoal Text | `#333333` | neutral | Primary text or dark surface |
| Amber Accent | `#ffb546` | brand | Action accent / signal color |
| Solid Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-oatmeal-canvas: #e5dfd5;
  --ref-muted-ash: #73706b;
  --ref-storm-gray: #676460;
  --ref-charcoal-text: #333333;
  --ref-amber-accent: #ffb546;
  --ref-solid-black: #000000;
}
```

## Typography direction
- **GT Pressura Standard**: 400, 500, 12px, 14px, 48px, 68px, 104px, 136px, 0.92, 1.00, 1.33, 1.43, 1.67; substitute `Montserrat`.
- **Inter**: 400, 600, 10px, 14px, 16px, 20px, 32px, 48px, 1.17, 1.25, 1.40, 1.43, 1.50, 1.60; substitute `Inter`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `cards: 8px, badges: 0px, default: 8px, elements: 24px, containers: 28px`

## Surface cues
- **Oatmeal Canvas** `#e5dfd5`: Base page background and general UI container.
- **Elevated Container** `#e5dfd5`: Internal cards and modular content blocks, distinct via subtle borders and light inset shadow.

## Component cues
- **Interactive Card**: Standard content containers for features and workspace elements.
- **Ghost Button/Link**: Used for secondary actions and text-based interactive elements.
- **Icon Button**: Small, functional buttons identified by an icon.
- **Badge (Neutral Text)**: Indicative labels without a background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
