# Peppermint - Refero Design MD

- Source: https://styles.refero.design/style/c03d3f6f-91f9-4571-9840-7fd4da539322
- Original site: https://paywithpeppermint.com
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight festival, playful neon

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Indigo | `#0a1d4b` | brand | Action accent / signal color |
| Warm Vanilla | `#fcf6ea` | neutral | Page background or card surface |
| Powder Snow | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#474b60` | neutral | Border, muted text, or supporting surface |
| Lavender Bloom | `#9c8bf9` | accent | Action accent / signal color |
| Sugared Almond | `#faedd2` | neutral | Action accent / signal color |
| Mint Glaze | `#68dacb` | accent | Action accent / signal color |
| Azure Haze | `#bcdff0` | accent | Action accent / signal color |
| Starry Night | `#162d67` | brand | Action accent / signal color |
| Coral Pink | `#ffb8d9` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-indigo: #0a1d4b;
  --ref-warm-vanilla: #fcf6ea;
  --ref-powder-snow: #ffffff;
  --ref-ash-gray: #474b60;
  --ref-lavender-bloom: #9c8bf9;
  --ref-sugared-almond: #faedd2;
  --ref-mint-glaze: #68dacb;
  --ref-azure-haze: #bcdff0;
}
```

## Typography direction
- **Excon**: 400, 500, 700, 24px, 25px, 45px, 48px, 50px, 60px, 90px, 128px, 130px, 151px, 274px, 0.87, 0.92, 1.00, 1.09; substitute `Anton, Impact`.
- **Generalsans**: 400, 500, 700, 14px, 16px, 18px, 1.14, 1.22, 1.25, 1.43, 1.50; substitute `Inter, Eina01`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 20px, forms: 16px, accents: 36px, buttons: 48px`

## Component cues
- **Primary Action Button**: Filled button for main calls to action.
- **Hero Action Button**: Large, prominent button for hero sections.
- **FAQ Accordion Card**: Container for frequently asked questions, with interactive state.
- **Feature Card (Blush Rose)**: Highlighting key features with a soft, distinct background.
- **Illustrative Feature Card (Mint Glaze)**: Card acting as a canvas for illustrations or imagery.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
