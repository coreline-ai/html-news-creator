# Essie Wine - Refero Design MD

- Source: https://styles.refero.design/style/07f5281d-2a18-4e12-a8ff-d54d3e03d198
- Original site: https://www.essiewine.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vintage Bookplate Serenity — a quiet, reserved aesthetic like an aged paper with delicate script.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#062d32` | brand | Action accent / signal color |
| Parchment | `#e9e9e2` | neutral | Page background or card surface |
| White Linen | `#ffffff` | neutral | Page background or card surface |
| Old Gold | `#aa9e54` | accent | Action accent / signal color |
| Dusty Rose | `#c9a9b5` | neutral | Border, muted text, or supporting surface |
| Slate Grain | `#767676` | neutral | Border, muted text, or supporting surface |
| Deep Pewter | `#344b52` | neutral | Border, muted text, or supporting surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-inkwell: #062d32;
  --ref-parchment: #e9e9e2;
  --ref-white-linen: #ffffff;
  --ref-old-gold: #aa9e54;
  --ref-dusty-rose: #c9a9b5;
  --ref-slate-grain: #767676;
  --ref-deep-pewter: #344b52;
  --ref-pitch-black: #000000;
}
```

## Typography direction
- **BasicCommercial LT Com Roman**: 300, 400, 19px, 38px, 49px, 1.16, 1.18, 1.20; substitute `Inter`.
- **Adobe Caslon Pro**: 300, 49px, 1.18; substitute `Libre Baskerville`.
- **Elementa**: 300, 400, 16px, 19px, 1.00, 1.16; substitute `Graphik`.

## Spacing / shape
- Section Gap: `136px`
- Card Padding: `27px`
- Element Gap: `23px`
- Radius: `inputs: 0px, buttons: 0px`

## Surface cues
- **Parchment** `#e9e9e2`: Primary content canvas, providing a soft background for text-heavy sections.
- **Old Gold** `#aa9e54`: Elevated background for distinct content blocks, like forms or highlighted features, offering a warm contrast.
- **Dusty Rose** `#c9a9b5`: Background for less textual, more illustrative elements such as the hero or footer, serving a decorative role.
- **White Linen** `#ffffff`: Background for pristine, clean content areas or specific nested components.

## Component cues
- **Ghost Text Button**: Default interactive element for navigation and actions.
- **Underlined Call-to-Action**: Semantic action for submissions or primary interactions.
- **Form Input Field**: Standard input for user data collection.
- **Form Input Field (Active)**: Active state for form inputs.
- **Content Section (Old Gold)**: Distinct background for specific content blocks like forms.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
