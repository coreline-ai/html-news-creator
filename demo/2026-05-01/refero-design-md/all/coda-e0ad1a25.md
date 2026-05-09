# Coda - Refero Design MD

- Source: https://styles.refero.design/style/e0ad1a25-5609-45e6-a355-9bdeec86c5ae
- Original site: https://www.coda.co
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
digital-first canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Creme | `#f8f9eb` | neutral | Page background or card surface |
| Carbon Black | `#000000` | neutral | Primary text or dark surface |
| Obsidian Gray | `#202020` | neutral | Primary text or dark surface |
| Forest Green | `#003d21` | brand | Action accent / signal color |
| Sage Mist | `#c0c2a9` | neutral | Border, muted text, or supporting surface |
| Mid-tone Gray | `#5a5a4f` | neutral | Border, muted text, or supporting surface |
| Light Taupe | `#7c7d76` | neutral | Border, muted text, or supporting surface |
| Pale Ash | `#edeee1` | neutral | Page background or card surface |
| Aura Green | `#aafdc0` | accent | Action accent / signal color |
| Soft Teal | `#b0f4ff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-creme: #f8f9eb;
  --ref-carbon-black: #000000;
  --ref-obsidian-gray: #202020;
  --ref-forest-green: #003d21;
  --ref-sage-mist: #c0c2a9;
  --ref-mid-tone-gray: #5a5a4f;
  --ref-light-taupe: #7c7d76;
  --ref-pale-ash: #edeee1;
}
```

## Typography direction
- **abcMonumentGrotesk**: 400, 500, 800, 16px, 18px, 21px, 22px, 25px, 34px, 45px, 54px, 63px, 72px, 134px, 0.90, 1.00, 1.02, 1.13, 1.30, 1.43, 1.50, 1.71; substitute `system-ui`.
- **ui-sans-serif**: 400, 16px, 1.50; substitute `sans-serif`.
- **jetBrainsMono**: 400, 10px, 12px, 14px, 16px, 0.90, 1.00, 1.20, 1.37; substitute `monospace`.

## Spacing / shape
- Section Gap: `63px`
- Card Padding: `13px`
- Element Gap: `9px`
- Radius: `cards: 22.3625px, large: 26.835px, badges: 9999px, buttons: 8.94498px, default: 13.4175px, extraLarge: 44.725px`

## Surface cues
- **Canvas Creme** `#f8f9eb`: Base page background, light and warm.
- **Carbon Black** `#000000`: Contrasting background for specific sections and the primary navigation bar.
- **Forest Green** `#003d21`: Prominent background for large, organic decorative elements, and specific card surfaces.

## Component cues
- **Ghost Header Navigation Link**: Navigation item within the header.
- **Pill Button with Outline**: Secondary action button, often for 'Learn More' or 'Go' actions.
- **Filled Primary Button**: Primary call to action.
- **Ghost Button with Light Text**: Action button on dark backgrounds.
- **Transparent Card**: Informational card with no background fill.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
