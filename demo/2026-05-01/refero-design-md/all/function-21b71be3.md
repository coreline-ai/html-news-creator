# Function - Refero Design MD

- Source: https://styles.refero.design/style/21b71be3-78a0-4681-a5b9-64cc4b40eb67
- Original site: https://www.functionhealth.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
organic science lab

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Amber Glow | `#b05a36` | brand | Action accent / signal color |
| Night Sky | `#2a2b2f` | neutral | Primary text or dark surface |
| Charcoal Grey | `#333333` | neutral | Primary text or dark surface |
| Faded Stone | `#515151` | neutral | Border, muted text, or supporting surface |
| Parchment White | `#fef9ef` | neutral | Page background or card surface |
| Cream Canvas | `#f5eee1` | neutral | Page background or card surface |
| Warm Mist | `#d1c9bf` | neutral | Border, muted text, or supporting surface |
| Slate Border | `#808988` | neutral | Border, muted text, or supporting surface |
| Off-White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-amber-glow: #b05a36;
  --ref-night-sky: #2a2b2f;
  --ref-charcoal-grey: #333333;
  --ref-faded-stone: #515151;
  --ref-parchment-white: #fef9ef;
  --ref-cream-canvas: #f5eee1;
  --ref-warm-mist: #d1c9bf;
  --ref-slate-border: #808988;
}
```

## Typography direction
- **Ftbase**: 300, 400, 600, 700, 12px, 14px, 16px, 18px, 20px, 24px, 88px, 1.00, 1.10, 1.11, 1.20, 1.25, 1.30, 1.40, 1.43, 1.50; substitute `Inter`.
- **Financier Display**: 300, 400, 34px, 45px, 64px, 80px, 0.90, 1.00, 1.10, 1.15; substitute `Playfair Display`.
- **Fragment mono**: 400, 11px, 1.00; substitute `Fira Code`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `25px`
- Element Gap: `16px`
- Page Max Width: `1434px`
- Radius: `cards: 12px, small: 2px, inputs: 1440px, buttons: 40px`

## Surface cues
- **Parchment White** `#fef9ef`: Primary page background and base canvas.
- **Cream Canvas** `#f5eee1`: Secondary background for sections and cards, creating a subtle lift.
- **Warm Mist** `#d1c9bf`: Tertiary background for slight visual separation or subtle divider elements.
- **Off-White** `#ffffff`: Pure white for focused elements like input fields or specific card backgrounds.

## Component cues
- **Primary Action Button**: Filled button for primary calls to action.
- **Ghost Button**: Outlined button for secondary actions, or when less visual prominence is desired.
- **Text Link Button**: Minimal button styled as a text link.
- **Feature Card**: Card for showcasing key features or information blocks.
- **Elevated Content Card**: Card with subtle shadow for emphasized content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
