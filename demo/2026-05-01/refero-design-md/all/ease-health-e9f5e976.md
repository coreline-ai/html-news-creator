# Ease Health - Refero Design MD

- Source: https://styles.refero.design/style/e9f5e976-53f7-42f5-a882-4e63b3c2f734
- Original site: https://easehealth.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
calm clinical canvas

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Green | `#0f3e17` | brand | Action accent / signal color |
| Cream Canvas | `#fffefc` | neutral | Page background or card surface |
| Mint Glaze | `#b1dbb8` | accent | Action accent / signal color |
| Slate Mist | `#b6ced5` | accent | Action accent / signal color |
| Keylime Wash | `#e1f4df` | accent | Action accent / signal color |
| Mint Kiss | `#cfe7d3` | accent | Action accent / signal color |
| Border Grey | `#e5e7eb` | neutral | Page background or card surface |
| Ink Text | `#222222` | neutral | Primary text or dark surface |
| Dark Charcoal | `#333333` | neutral | Primary text or dark surface |

```css
:root {
  --ref-forest-green: #0f3e17;
  --ref-cream-canvas: #fffefc;
  --ref-mint-glaze: #b1dbb8;
  --ref-slate-mist: #b6ced5;
  --ref-keylime-wash: #e1f4df;
  --ref-mint-kiss: #cfe7d3;
  --ref-border-grey: #e5e7eb;
  --ref-ink-text: #222222;
}
```

## Typography direction
- **Suisseintl**: 300, 400, 12px, 14px, 18px, 23px, 28px, 56px, 1.00, 1.30, 1.50; substitute `Inter`.
- **Faire Octave**: 300, 40px, 74px, 1.05, 1.35; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `42px`
- Card Padding: `42px`
- Element Gap: `21px`
- Radius: `nav: 7px, cards: 14px, badges: 999px, buttons: 14px`

## Surface cues
- **Canvas Background** `#fffefc`: Dominant page background, providing a clean, bright, and almost textured base for all content.
- **Keylime Wash Card** `#e1f4df`: First layer of elevated content, used for prominent cards or hero sections, offering a subtle green tint.
- **Mint Glaze Card** `#b1dbb8`: Second layer of elevated content, for detailed information cards or feature blocks, slightly more saturated green.
- **Slate Mist Card** `#b6ced5`: Third layer of elevated content, providing clear visual separation for distinct blocks, using a cool desaturated blue-gray.

## Component cues
- **Primary Action Button (Filled)**: Main call-to-action button, conveying primary user interaction.
- **Large Action Button**: Prominent full-block call-to-action for key feature sections.
- **Content Card (Mint Glaze)**: General purpose container for information or features, with a refreshing tint.
- **Content Card (Slate Mist)**: Alternative general purpose container, providing subtle visual distinction.
- **Content Card (Keylime Wash)**: Lightest card background for sub-sections or layered content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
