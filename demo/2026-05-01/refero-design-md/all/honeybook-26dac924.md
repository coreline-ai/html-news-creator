# HoneyBook - Refero Design MD

- Source: https://styles.refero.design/style/26dac924-d1c8-4097-af0f-0417ccb12128
- Original site: https://www.honeybook.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm productivity with a vibrant hum

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Onyx Black | `#142127` | neutral | Primary text or dark surface |
| Buttermilk Yellow | `#fffa77` | brand | Action accent / signal color |
| Lemon Zest | `#fffa56` | brand | Action accent / signal color |
| Arctic Mist | `#ffffff` | neutral | Page background or card surface |
| Earl Gray | `#c7d5d9` | neutral | Border, muted text, or supporting surface |
| Paper White | `#f4eae0` | neutral | Page background or card surface |
| Charcoal Grey | `#343c40` | neutral | Primary text or dark surface |
| Ink Grey | `#131416` | neutral | Primary text or dark surface |
| Dusk Blue | `#9ab9e8` | accent | Action accent / signal color |
| Jade Green | `#99d3ac` | accent | Action accent / signal color |

```css
:root {
  --ref-onyx-black: #142127;
  --ref-buttermilk-yellow: #fffa77;
  --ref-lemon-zest: #fffa56;
  --ref-arctic-mist: #ffffff;
  --ref-earl-gray: #c7d5d9;
  --ref-paper-white: #f4eae0;
  --ref-charcoal-grey: #343c40;
  --ref-ink-grey: #131416;
}
```

## Typography direction
- **STK Bureau Sans**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 24px, 28px, 32px, 48px, 1.00, 1.20, 1.40, 1.50, 1.80; substitute `Inter`.
- **STK Bureau Serif**: 400, 16px, 28px, 40px, 48px, 56px, 64px, 1.00, 1.20; substitute `Merriweather`.
- **STK Gerhard**: 500, 14px, 1.20, 1.50; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `tags: 30px, cards: 20px, buttons: 159984px, general: 6px`

## Surface cues
- **Buttermilk Yellow Canvas** `#fffa77`: Dominant background for large, impactful sections like the hero and key feature areas, providing a warm, inviting foundation.
- **Arctic Mist Surface** `#ffffff`: Used for card backgrounds, secondary containers, and general content areas that require a clean, bright, and neutral surface.
- **Paper White Soft Surface** `#f4eae0`: A warmer, subtle background alternative for specific sections, offering a slightly softer contrast than pure white.
- **Lemon Zest Accent** `#fffa56`: Applied to prominent cards and interactive elements, bringing a vibrant, active layer on top of other surfaces.

## Component cues
- **Primary Ghost Button**: Call to action button for primary actions, providing a strong visual cue without a solid fill.
- **Secondary Ghost Button**: Call to action button for secondary actions or navigation links, less prominent than primary.
- **Navigation Circle Button**: Round buttons for navigation or specific icon-based actions.
- **Inverted Ghost Button (Dark Background)**: Ghost button for use on darker backgrounds, maintaining brand consistency.
- **Standard Card**: Basic content container for features, information blocks, or testimonials.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
