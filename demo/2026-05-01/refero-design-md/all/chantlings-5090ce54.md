# Chantlings - Refero Design MD

- Source: https://styles.refero.design/style/5090ce54-9097-4d29-a741-2847dbacc419
- Original site: https://www.iorama.studio/chantlings
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Moonlit Forest Floor: glowing forms in the deep dark

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Noir | `#000000` | neutral | Primary text or dark surface |
| Ghostly Gray | `#333333` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Shadow Tint | `#222222` | neutral | Primary text or dark surface |
| Active Fire | `#ff8800` | brand | Action accent / signal color |
| Subtle Glow | `#ffaa20` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-noir: #000000;
  --ref-ghostly-gray: #333333;
  --ref-canvas-white: #ffffff;
  --ref-shadow-tint: #222222;
  --ref-active-fire: #ff8800;
  --ref-subtle-glow: #ffaa20;
}
```

## Typography direction
- **Mija webfont**: 100, 300, 14px, 20px, 24px, 25px, 32px, 0.80, 0.83, 1.00, 1.06, 1.33, 1.42, 1.43, 1.50; substitute `Lora, Playfair Display`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `18px`
- Element Gap: `10px`
- Radius: `buttons: 50px, default: 0px`

## Surface cues
- **Midnight Noir Canvas** `#000000`: Dominant page background, providing a deep, immersive context

## Component cues
- **Ghost Navigation Button**: Header navigation, secondary actions
- **Primary Action Button**: Main calls to action
- **Outlined Accent Link**: Secondary links with visual emphasis
- **App Store Download Button**: Directing users to download the app

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
