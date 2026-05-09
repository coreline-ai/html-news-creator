# wix.com - Refero Design MD

- Source: https://styles.refero.design/style/a31f5b99-6e7d-4e13-9b80-cd60e455bd76
- Original site: https://www.wix.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Animated digital canvas – an interactive, slightly playful yet authoritative workspace.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#f1f5f9` | neutral | Page background or card surface |
| Silver Mist | `#d0d0d0` | neutral | Border, muted text, or supporting surface |
| Steel Blue | `#1c1d21` | neutral | Action accent / signal color |
| Sky Blue | `#166aea` | brand | Action accent / signal color |
| Deep Violet | `#101585` | brand | Action accent / signal color |
| Lime Zest | `#dff994` | brand | Action accent / signal color |
| Twilight Indigo | `#2c34af` | brand | Action accent / signal color |
| Ocean Teal | `#024051` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-cloud-gray: #f1f5f9;
  --ref-silver-mist: #d0d0d0;
  --ref-steel-blue: #1c1d21;
  --ref-sky-blue: #166aea;
  --ref-deep-violet: #101585;
  --ref-lime-zest: #dff994;
}
```

## Typography direction
- **madefor-display**: 400, 10px, 13px, 14px, 16px, 21px, 24px, 31px, 48px, 82px, 89px, 104px, 184px, 0.85, 1.00, 1.10, 1.20, 1.30, 1.40, 1.48, 1.50, 1.60; substitute `Arial`.
- **wix-madefor-display-v2**: 400, 500, 20px, 21px, 53px, 1.00, 1.10, 1.20; substitute `Arial`.
- **madefor-text**: 400, 10px, 13px, 14px, 15px, 16px, 18px, 21px, 25px, 1.00, 1.20, 1.29, 1.30, 1.50, 1.60, 1.71; substitute `Arial`.

## Spacing / shape
- Section Gap: `81px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `tags: 50px, cards: 20px, images: 20px, inputs: 999px, buttons: 50px`

## Surface cues
- **Canvas** `#ffffff`: Dominant page background, primary stage for content.
- **Base Card** `#f1f5f9`: Background for secondary content areas or simple cards.
- **Decorative Card** `#dff994`: Specific card backgrounds using brand or accent colors (e.g., Lime Zest, Pale Sage, Amethyst).

## Component cues
- **Primary Filled Button**: Call to action, primary interaction
- **Ghost Button**: Secondary action, navigation
- **Black Rounded Button**: Alternative call to action, often accentuating a dark background.
- **Square Corner Card**: Content container, information display
- **Rounded Corner Card**: Elevated content container, featured information

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
