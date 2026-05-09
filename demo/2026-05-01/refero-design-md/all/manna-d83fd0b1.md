# MANNA - Refero Design MD

- Source: https://styles.refero.design/style/d83fd0b1-afde-41ff-b970-c622bfed9f59
- Original site: https://www.mannaarchitects.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Earthy Gallery Canvas

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Earthy Ochre | `#af6446` | brand | Action accent / signal color |
| Pale Linen | `#f2edde` | neutral | Page background or card surface |
| Charcoal Ink | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-earthy-ochre: #af6446;
  --ref-pale-linen: #f2edde;
  --ref-charcoal-ink: #000000;
}
```

## Typography direction
- **Scto Grotesk A**: 300, 500, 14px, 60px, 1.29; substitute `Inter`.
- **Merlo**: 400, 16px, 26px, 1.23, 1.50; substitute `Georgia`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `10-20px`
- Radius: `images: 0px`

## Component cues
- **Image Card with Caption**: Primary content display for portfolio pieces or architectural photography.
- **Footer Section**: Global brand and contact information.
- **Prominent Brand Heading**: Major section titles and brand identity.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
