# Structured - Refero Design MD

- Source: https://styles.refero.design/style/6c0b77d3-71f9-469d-98aa-4ce1d6d76ac8
- Original site: https://structured.money
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Classical art gallery

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Greige Canvas | `#ebebeb` | neutral | Page background or card surface |
| Black Ink | `#000000` | neutral | Primary text or dark surface |
| Off-White Text | `#dfdcd5` | neutral | Page background or card surface |
| Slate Surface | `#c4c3b6` | neutral | Border, muted text, or supporting surface |
| Smoke Grey | `#e7e5e4` | neutral | Page background or card surface |
| Warm Accent Grey | `#595855` | neutral | Border, muted text, or supporting surface |
| White Highlight | `#ffffff` | neutral | Page background or card surface |
| Midtone Image Grey | `#808080` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-greige-canvas: #ebebeb;
  --ref-black-ink: #000000;
  --ref-off-white-text: #dfdcd5;
  --ref-slate-surface: #c4c3b6;
  --ref-smoke-grey: #e7e5e4;
  --ref-warm-accent-grey: #595855;
  --ref-white-highlight: #ffffff;
  --ref-midtone-image-grey: #808080;
}
```

## Typography direction
- **Davinci**: 400, 500, 16px, 24px, 34px, 52px, 94px, 374px, 0.84, 1.00, 1.10, 1.33, 1.50; substitute `Playfair Display or Lora (though Davinci's sharp serifs and specific tracking are key)`.
- **Helvetica Now**: 400, 500, 9px, 12px, 15px, 16px, 22px, 24px, 26px, 43px, 1.25, 1.50; substitute `Inter or Helvetica Neue`.

## Spacing / shape
- Section Gap: `25px`
- Card Padding: `18px`
- Element Gap: `6px`
- Radius: `cards: 9px, buttons: 0px, inlineElements: 2px, decorativeElements: 28.8px`

## Surface cues
- **Greige Canvas** `#ebebeb`: Dominant page and footer background
- **Slate Surface** `#c4c3b6`: Secondary background layer for cards and subtle content blocks
- **Black Ink Recess** `#000000`: Background for visually distinct components like the 'mint maxBTC' button, creating a moment of focus

## Component cues
- **Ghost Navigation Link**: Primary navigation elements in header/footer
- **Action Button Dark**: Call to action button, ghost style
- **Action Button Light**: Call to action button, ghost style for light backgrounds
- **Subtle Action Tag**: Small, interactive information tags
- **Feature Card**: Display individual features or content blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
