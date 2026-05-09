# Raw Materials - Refero Design MD

- Source: https://styles.refero.design/style/274e85fb-a34d-4e41-9369-be03065b971b
- Original site: https://therawmaterials.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Color-blocked minimalist architecture. Imagine a de Stijl painting brought to life as interactive digital canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f4e9e1` | neutral | Page background or card surface |
| Charcoal Grey | `#242320` | neutral | Primary text or dark surface |
| Snow White | `#ffffff` | neutral | Page background or card surface |
| Coral Flame | `#ff3d00` | brand | Action accent / signal color |
| Electric Yellow | `#ffff00` | brand | Action accent / signal color |
| Neon Green | `#05ff00` | brand | Action accent / signal color |
| Deep Violet | `#5900cc` | brand | Action accent / signal color |
| Royal Blue | `#2835f8` | brand | Action accent / signal color |
| Alert Red | `#ff003d` | accent | Action accent / signal color |
| Leaf Green | `#20db70` | semantic | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #f4e9e1;
  --ref-charcoal-grey: #242320;
  --ref-snow-white: #ffffff;
  --ref-coral-flame: #ff3d00;
  --ref-electric-yellow: #ffff00;
  --ref-neon-green: #05ff00;
  --ref-deep-violet: #5900cc;
  --ref-royal-blue: #2835f8;
}
```

## Typography direction
- **StabilGrotesk**: 100, 400, 500, 12px, 13px, 14px, 16px, 17px, 18px, 19px, 20px, 22px, 23px, 24px, 28px, 29px, 32px, 40px, 46px, 95px, 99px, 100px, 101px, 140px, 199px, 200px, 0.80, 1.00, 1.03, 1.04, 1.07, 1.08, 1.10, 1.14, 1.17, 1.20, 1.38, 1.69, 2.08; substitute `Inter`.
- **Optimistic Text**: 100, 400, 700, 18px, 23px, 80px, 95px, 193px, 1.00, 1.06, 1.20, 1.38; substitute `Montserrat`.
- **KlarheitKurrent**: 400, 500, 20px, 40px, 79px, 107px, 200px, 259px, 1.00, 1.03, 1.20; substitute `Arial Black`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `badges: 24px, buttons: 44px, default: 16px, largerElements: 99.36px`

## Component cues
- **Navigation Menu - Color Blocked**: Reference component style.
- **Status Bar - Section Indicator**: Reference component style.
- **Button Group - CTA Variants**: Reference component style.
- **Navigation Button - Primary**: Primary navigation interaction
- **Navigation Button - Outline**: Secondary navigation interaction

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
