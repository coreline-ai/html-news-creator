# Flying Papers - Refero Design MD

- Source: https://styles.refero.design/style/7d254296-6817-487a-a58c-4d5eca89cbf3
- Original site: https://www.flyingpapers.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Punchy Pulp Comic

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Grape Soda | `#8584bd` | brand | Action accent / signal color |
| Lemon Drop | `#f4ed36` | brand | Action accent / signal color |
| Warm Dough | `#f9cc73` | brand | Action accent / signal color |
| Deep Plum | `#61609a` | brand | Action accent / signal color |
| Rose Blush | `#f8c1ba` | accent | Action accent / signal color |
| Sage Clay | `#b5c995` | accent | Action accent / signal color |
| Forest Floor | `#375027` | brand | Action accent / signal color |
| Orchid Bloom | `#ac4f98` | brand | Action accent / signal color |
| Crimson Pop | `#c94245` | brand | Action accent / signal color |
| Licorice Stick | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-grape-soda: #8584bd;
  --ref-lemon-drop: #f4ed36;
  --ref-warm-dough: #f9cc73;
  --ref-deep-plum: #61609a;
  --ref-rose-blush: #f8c1ba;
  --ref-sage-clay: #b5c995;
  --ref-forest-floor: #375027;
  --ref-orchid-bloom: #ac4f98;
}
```

## Typography direction
- **ObviouslyVariable**: 800, 900, 18px, 20px, 30px, 100px, 113px, 130px, 133px, 149px, 184px, 241px, 244px, 341px, 0.80, 0.90, 1.00.
- **DegularVariable**: 400, 10px, 1.00.
- **DegularDisplay-Bold**: 700, 16px, 1.00.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `17px`
- Element Gap: `17px`
- Radius: `cards: 6px, buttons: 0px, elements: 6px, roundElements: 100px`

## Surface cues
- **Grape Soda Canvas** `#8584bd`: Primary page background and large, immersive sections.
- **Whipped Cream Surface** `#f9f5f2`: Secondary backgrounds, such as for navigation elements or subtle content areas.
- **Deep Plum Card Surface** `#61609a`: Prominent card backgrounds, providing a distinct color block within the layout.

## Component cues
- **Primary Outlined Button**: Main call-to-action button.
- **Secondary Outlined Button (Neutral)**: Secondary action or ghost button.
- **Text Link (Light)**: Interactive text link on dark backgrounds.
- **Text Link (Dark)**: Interactive text link on light backgrounds.
- **Neutral Card**: Basic content container.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
