# Mage - Refero Design MD

- Source: https://styles.refero.design/style/ba07accb-b2cc-4ad9-a25f-c50b0f90f34e
- Original site: https://www.mage.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Greige Canvas | `#f7f7f1` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Storm Gray | `#2b2b2b` | neutral | Primary text or dark surface |
| Silver Mist | `#b0b0b0` | neutral | Border, muted text, or supporting surface |
| Ocean Blue | `#244cff` | brand | Action accent / signal color |
| Sky Tint | `#e8f8ff` | accent | Action accent / signal color |
| Pale Aqua | `#d6f2ff` | accent | Action accent / signal color |
| Lavender Haze | `#c3aeff` | accent | Action accent / signal color |
| Soft Yellow | `#ffffbd` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-greige-canvas: #f7f7f1;
  --ref-ink-black: #000000;
  --ref-storm-gray: #2b2b2b;
  --ref-silver-mist: #b0b0b0;
  --ref-ocean-blue: #244cff;
  --ref-sky-tint: #e8f8ff;
  --ref-pale-aqua: #d6f2ff;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Inter**: 400, 500, 600, 700, 12px, 13px, 15px, 16px, 17px, 18px, 21px, 22px, 24px, 1.20, 1.30, 1.40, 1.50, 1.65; substitute `system-ui, sans-serif`.
- **Inter Variable**: 400, 20px, 22px, 30px, 38px, 60px, 1.30, 1.40; substitute `Inter, system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `40px`
- Element Gap: `10px`
- Radius: `cards: 6px, pills: 100px, buttons: 17px, default: 6px, smallComponents: 16px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default card surface.
- **Greige Canvas** `#f7f7f1`: Secondary page and section backgrounds, subtly differentiating content blocks.
- **Sky Tint** `#e8f8ff`: Highlight backgrounds for specific informational cards or feature areas.
- **Accent Card Colors** `#d6f2ff`: Varied background for unique card variants or decorative elements within content.

## Component cues
- **Primary Action Button**: Call-to-action button for initiating key user flows.
- **Ghost Secondary Button**: Secondary action button, providing a less prominent option.
- **Default Content Card**: General purpose card for grouping content and features.
- **Compact Info Card**: Smaller card for lists or minor content blocks.
- **Highlight Card**: Card with a subtle accent colored background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
