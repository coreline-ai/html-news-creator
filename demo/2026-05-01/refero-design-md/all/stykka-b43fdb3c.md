# Stykka - Refero Design MD

- Source: https://styles.refero.design/style/b43fdb3c-85e9-4282-9262-1d3deb4b679d
- Original site: https://stykka.com
- Theme: `light`
- Industry: `design`
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
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#f6f6f6` | neutral | Page background or card surface |
| Medium Gray | `#2e2e20` | neutral | Primary text or dark surface |
| Light Gray | `#c9c9c9` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-canvas-white: #ffffff;
  --ref-ash-gray: #f6f6f6;
  --ref-medium-gray: #2e2e20;
  --ref-light-gray: #c9c9c9;
}
```

## Typography direction
- **Inter**: 400, 500, 11px, 14px, 16px, 22px, 24px, 30px, 46px, 1.00, 1.05, 1.10, 1.20, 1.25, 1.50; substitute `system-ui, sans-serif`.
- **Azeret Mono**: 400, 18px, 1.00; substitute `monospace`.
- **sans-serif**: 400, 12px, 1.20; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `cards: 16px, buttons: 8px, navigation: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background, predominant clean surface
- **Ash Gray** `#f6f6f6`: Subtle secondary background for content cards and distinct sections, creating soft separation.
- **Absolute Zero (Hero Overlay)** `#000000`: Used as a full-bleed background for certain hero or header sections, creating a strong visual anchor and contrast for white text.

## Component cues
- **Ghost Primary Button**: Call to action button for primary user actions, designed to integrate subtly into the layout.
- **Information Card**: Container for showcasing features, testimonials, or short content blocks.
- **Navigation Link**: Standard navigation item in header and footer.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
