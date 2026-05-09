# Portrait - Refero Design MD

- Source: https://styles.refero.design/style/6b51388b-d00f-4b22-8297-68fb9fc00bc7
- Original site: https://portrait.so
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Generative digital canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#353535` | neutral | Primary text or dark surface |
| Charcoal | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#eeeeee` | neutral | Page background or card surface |
| Stone Gray | `#797979` | neutral | Border, muted text, or supporting surface |
| Pale Blue Mist | `#e8f1ff` | neutral | Action accent / signal color |
| Ocean Blue | `#08304c` | brand | Action accent / signal color |
| Sky Blue | `#084e72` | brand | Action accent / signal color |
| Rainbow Glow | `#26c0ff` | accent | Action accent / signal color |
| Success Green | `#00cc3d` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #353535;
  --ref-charcoal: #000000;
  --ref-cloud-gray: #eeeeee;
  --ref-stone-gray: #797979;
  --ref-pale-blue-mist: #e8f1ff;
  --ref-ocean-blue: #08304c;
  --ref-sky-blue: #084e72;
}
```

## Typography direction
- **Switzer**: 400, 500, 540, 600, 700, 10px, 11px, 12px, 14px, 16px, 18px, 20px, 24px, 36px, 1.00, 1.11, 1.38, 1.43, 1.45, 1.50; substitute `system-ui, sans-serif`.
- **Basier Circle**: 500, 600, 16px, 18px, 20px, 31px, 39px, 44px, 49px, 76px, 1.00, 1.04, 1.08, 1.10, 1.20, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `cards: 24px, buttons: 28px, containers: 16px, formInputs: 8px, microElements: 12px, imageContainers: 24px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and base layer for all content.
- **Cloud Gray** `#eeeeee`: Secondary background color for subtle section breaks or less prominent cards.
- **Pale Blue Mist** `#e8f1ff`: Elevated background for focal cards or informative sections, adding a soft chromatic highlight.

## Component cues
- **Ghost Button**: Secondary action control
- **Outlined Button**: Primary action button
- **Rainbow Input Field**: Interactive text input
- **Basic Card**: Content container
- **Elevated Tooltip Card**: Informational overlay

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
