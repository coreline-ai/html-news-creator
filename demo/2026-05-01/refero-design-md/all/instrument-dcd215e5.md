# Instrument - Refero Design MD

- Source: https://styles.refero.design/style/dcd215e5-3511-4e40-87ff-95c095f44ad6
- Original site: https://www.instrument.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast typographic canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#070708` | neutral | Primary text or dark surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Midtone Gray | `#808080` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #070708;
  --ref-white-canvas: #ffffff;
  --ref-midtone-gray: #808080;
}
```

## Typography direction
- **Instrument-Sans**: 400, 11px, 12px, 14px, 15px, 16px, 18px, 19px, 23px, 28px, 36px, 352px, 0.85, 1.00, 1.11, 1.14, 1.22, 1.26, 1.33, 1.43, 1.45, 1.56, 1.60; substitute `Inter`.
- **Instrument-Serif**: 400, 64px, 352px, 0.85, 1.13; substitute `Playfair Display`.
- **Instrument-Serif-Italic**: 400, 352px, 0.85; substitute `Playfair Display Italic`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `tags: 999px, cards: 24px, inputs: 8px, buttons: 999px, minimal: 0px`

## Surface cues
- **White Canvas** `#ffffff`: Dominant background for pages and sections, creating a spacious, clean feel.
- **Midnight Ink** `#070708`: Background for bold, immersive sections, video players, and header/footer blocks, providing strong contrast.

## Component cues
- **Pill Ghost Button**: Primary navigation and filter controls.
- **Outline Text Button**: Secondary actions and category filters.
- **Soft Rectangular Button**: Filter controls on darker backgrounds or for a slightly more defined appearance.
- **Filled Square Button**: Interactive elements requiring strong visual presence on white backgrounds.
- **Transparent Card**: Content presentation where the background provides context.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
