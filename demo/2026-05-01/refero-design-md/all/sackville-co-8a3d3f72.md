# Sackville & Co. - Refero Design MD

- Source: https://styles.refero.design/style/8a3d3f72-9ef0-466d-adde-77189ddff797
- Original site: https://sackville.co
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric Blue Studio

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Creme | `#f3f4ee` | neutral | Page background or card surface |
| Midnight Ash | `#231f20` | neutral | Primary text or dark surface |
| Deep Space Blue | `#245dc5` | brand | Action accent / signal color |
| Sunset Orange | `#ffc6a6` | brand | Action accent / signal color |
| Crimson Ember | `#f04736` | semantic | Action accent / signal color |
| Jet | `#000000` | neutral | Primary text or dark surface |
| Charcoal Whisper | `#383435` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-creme: #f3f4ee;
  --ref-midnight-ash: #231f20;
  --ref-deep-space-blue: #245dc5;
  --ref-sunset-orange: #ffc6a6;
  --ref-crimson-ember: #f04736;
  --ref-jet: #000000;
  --ref-charcoal-whisper: #383435;
}
```

## Typography direction
- **FoundersGrotesk**: 400, 16px, 22px, 23px, 25px, 26px, 29px, 32px, 34px, 38px, 47px, 50px, 60px, 72px, 85px, 99px, 122px, 130px, 0.80, 0.85, 0.90, 0.94, 1.00, 1.15, 1.30, 1.50, 2.19; substitute `Inter`.
- **TimesNow SemiLight**: 400, 29px, 34px, 60px, 122px, 130px, 0.80, 0.85, 1.00, 1.10, 1.15; substitute `Times New Roman`.

## Spacing / shape
- Section Gap: `43px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 10px 10px 0px 0px, buttons: 50px, ovalButtons: 81px / 39px`

## Component cues
- **Ghost Button**: Minimal interactive elements
- **Text Link Button**: Inline text actions
- **Oval Outline Button - Deep Space**: Primary interaction button
- **Oval Outline Button - Crimson**: Secondary interaction button, often for 'Underage' states
- **Rounded Product Card**: Product display card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
