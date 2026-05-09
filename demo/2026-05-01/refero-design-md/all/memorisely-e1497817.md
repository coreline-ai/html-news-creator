# Memorisely - Refero Design MD

- Source: https://styles.refero.design/style/e1497817-b9f1-4d7a-842f-58a08dd9e455
- Original site: https://www.memorisely.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard Clarity, focused on sharp text and understated components.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Black | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#faf9f6` | neutral | Page background or card surface |
| Smoke Gray | `#171717` | neutral | Primary text or dark surface |
| Ghost Ivory | `#f2f0e9` | neutral | Page background or card surface |
| Muted Stone | `#878787` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#6e6e6e` | neutral | Border, muted text, or supporting surface |
| Deep Graphite | `#414141` | neutral | Border, muted text, or supporting surface |
| Ink Black | `#212121` | neutral | Primary text or dark surface |
| Soft Pewter | `#c9c6bd` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-charcoal-black: #000000;
  --ref-paper-white: #faf9f6;
  --ref-smoke-gray: #171717;
  --ref-ghost-ivory: #f2f0e9;
  --ref-muted-stone: #878787;
  --ref-steel-gray: #6e6e6e;
  --ref-deep-graphite: #414141;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 10px, 11px, 13px, 14px, 15px, 16px, 18px, 22px, 32px, 56px, 1.14, 1.23, 1.25, 1.27, 1.33, 1.38, 1.40, 1.43, 1.44, 1.45, 1.50; substitute `system-ui, sans-serif`.
- **sans-serif**: 400, 12px, 1.20; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `10px`
- Radius: `pill: 100px, cards: 12px, small: 4px, medium: 8px, buttons: 24px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background, brightest surface for cards and buttons.
- **Paper White** `#faf9f6`: Secondary page and section backgrounds, providing subtle visual breaks.
- **Ghost Ivory** `#f2f0e9`: Subtle differentiators for borders or very light accents.

## Component cues
- **Primary Filled Button**: Main call-to-action button, dark and commanding.
- **Outline Ghost Button**: Secondary action or subtle interaction button.
- **Standard Card**: Content containers for features or listings.
- **Hero Card**: Prominent card for showcasing key information.
- **Navigation Link**: Interactive text link within navigation menus.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
