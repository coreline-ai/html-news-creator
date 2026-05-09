# Daniela and Moe Wedding 2019 - Refero Design MD

- Source: https://styles.refero.design/style/0f1b3cd0-de5a-4418-8711-0e1afe04707c
- Original site: https://danielaandmoe.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whimsical Botanical Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Petal | `#fef1ec` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#11223f` | neutral | Primary text or dark surface |
| Sunset Blush | `#ff5734` | brand | Action accent / signal color |
| Mossy Green | `#7e813c` | accent | Action accent / signal color |
| Deep Forest | `#193c35` | accent | Action accent / signal color |
| Coral Haze | `#f6bba4` | accent | Action accent / signal color |
| Dusty Sage | `#c6d7d0` | accent | Action accent / signal color |
| Azure Whisper | `#092a49` | accent | Action accent / signal color |
| Sunbeam Gold | `#e5ba2b` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-petal: #fef1ec;
  --ref-paper-white: #ffffff;
  --ref-midnight-ink: #11223f;
  --ref-sunset-blush: #ff5734;
  --ref-mossy-green: #7e813c;
  --ref-deep-forest: #193c35;
  --ref-coral-haze: #f6bba4;
  --ref-dusty-sage: #c6d7d0;
}
```

## Typography direction
- **Canela Web**: 100, 400, 500, 24px, 28px, 32px, 48px, 120px, 0.85, 1.00, 1.20, 1.30, 1.40, 1.60, 2.00; substitute `serif`.
- **calibre**: 300, 400, 500, 12px, 16px, 20px, 24px, 36px, 48px, 1.20, 1.40, 1.60, 2.00; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 0px, other: 200px, buttons: 0px`

## Component cues
- **Primary Action Button**: Call to action button
- **Transparent Content Card**: Content container for detailed information
- **White Content Card**: Elevated content container
- **Text Input Field**: Form input element
- **Navigation Link**: Global navigation item

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
