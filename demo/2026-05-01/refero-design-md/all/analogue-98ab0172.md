# Analogue - Refero Design MD

- Source: https://styles.refero.design/style/98ab0172-9474-43b5-9055-98cf1a6a2401
- Original site: https://analogue.co
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Matte black precision instrument. A single focused beam of light highlights intricate details against a deep, absorbing dark.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Glacial White | `#ffffff` | neutral | Page background or card surface |
| Frost Gray | `#e5e7eb` | neutral | Page background or card surface |
| Steel Accent | `#bfbfbf` | neutral | Border, muted text, or supporting surface |
| Faded Gray | `#999999` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-obsidian: #000000;
  --ref-glacial-white: #ffffff;
  --ref-frost-gray: #e5e7eb;
  --ref-steel-accent: #bfbfbf;
  --ref-faded-gray: #999999;
}
```

## Typography direction
- **circularXx**: 400, 13px, 15px, 16px, 18px, 19px, 21px, 26px, 35px, 47px, 53px, 0.80, 1.00, 1.11, 1.14, 1.15, 1.20, 1.23, 1.50; substitute `Circular Std`.
- **circularXx**: 450, 13px, 15px, 16px, 18px, 19px, 21px, 26px, 35px, 47px, 53px, 0.80, 1.00, 1.11, 1.14, 1.15, 1.20, 1.23, 1.50; substitute `Circular Std`.
- **circularXx**: 500, 13px, 15px, 16px, 18px, 19px, 21px, 26px, 35px, 47px, 53px, 0.80, 1.00, 1.11, 1.14, 1.15, 1.20, 1.23, 1.50; substitute `Circular Std`.

## Spacing / shape
- Section Gap: `41-103px`
- Card Padding: `26px`
- Element Gap: `3-18px`
- Radius: `cards: 17.6256px, buttons: 16777200px`

## Component cues
- **CTA Block — Available Now**: Reference component style.
- **Review Cards — Analogue 3D Press**: Reference component style.
- **Product Section Header — Analogue 3D Shipping Now**: Reference component style.
- **Primary Button**: Calls to action
- **Secondary Button**: Calls to action (dark mode)

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
