# Caldera - Refero Design MD

- Source: https://styles.refero.design/style/fe8cdcf9-c850-4d52-be07-5ad269bf9ebf
- Original site: https://caldera.xyz
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Pixelated Cyber-Playground

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Basalt Canvas | `#e2e2df` | neutral | Page background or card surface |
| Ash White | `#f7f6f2` | neutral | Page background or card surface |
| Abyssal Ink | `#070607` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Digital Orange | `#fc5000` | brand | Action accent / signal color |
| Cyber Violet | `#524ae9` | accent | Action accent / signal color |
| Pixel Glare | `#f5f28e` | accent | Action accent / signal color |

```css
:root {
  --ref-basalt-canvas: #e2e2df;
  --ref-ash-white: #f7f6f2;
  --ref-abyssal-ink: #070607;
  --ref-pure-white: #ffffff;
  --ref-digital-orange: #fc5000;
  --ref-cyber-violet: #524ae9;
  --ref-pixel-glare: #f5f28e;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **PP Neue Corp Compact Ultrabold**: 400, 26px, 32px, 40px, 48px, 56px, 64px, 80px, 96px, 189px, 0.94, 0.95, 1.00, 1.10, 1.20; substitute `Bebas Neue`.
- **DM Sans**: 500, 14px, 16px, 18px, 30px, 1.11, 1.20, 1.25, 1.50, 1.55; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `40px`
- Element Gap: `10px`
- Page Max Width: `1200px`
- Radius: `cards: 40px, inputs: 100px, buttons: 800px, default: 40px`

## Surface cues
- **Basalt Canvas** `#e2e2df`: Base page background, subtle dividers
- **Ash White** `#f7f6f2`: Primary card backgrounds, navigation containers
- **Digital Orange Accent** `#fc5000`: Prominent feature cards, primary button fills

## Component cues
- **Primary Action Button**: Call-to-action
- **Ghost Button**: Secondary action
- **Navigation Link Button**: Navigation, internal links
- **Stats Card - Orange**: Informational display
- **Stats Card - Ash White**: Informational display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
