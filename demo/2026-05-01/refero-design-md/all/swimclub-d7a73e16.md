# SwimClub - Refero Design MD

- Source: https://styles.refero.design/style/d7a73e16-4b3e-4b9d-aef2-2c31a9db7457
- Original site: https://swimclub.co
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Scientific precision, stark contrast

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Atlantic Fog | `#d2dce1` | neutral | Page background or card surface |
| Mid-Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Silver Dust | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Sunset Orange | `#ff9e00` | brand | Action accent / signal color |
| Oceanic Gradient | `#417390` | accent | Action accent / signal color |
| Subtle Surface Gradient | `#d2dce0` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-atlantic-fog: #d2dce1;
  --ref-mid-gray: #666666;
  --ref-silver-dust: #b3b3b3;
  --ref-sunset-orange: #ff9e00;
  --ref-oceanic-gradient: #417390;
  --ref-subtle-surface-gradient: #d2dce0;
}
```

## Typography direction
- **Px Grotesk**: 400, 700, 12px, 15px, 16px, 17px, 21px, 31px, 37px, 52px, 74px, 1.05, 1.10, 1.30, 1.70; substitute `Inter`.
- **Apercu Mono Pro**: 400, 15px, 17px, 1.10, 1.20; substitute `Space Mono`.
- **Swimclub**: 400, 96px, 105px, 1.00; substitute `Pixelify Sans`.

## Spacing / shape
- Section Gap: `120px`
- Card Padding: `32px`
- Element Gap: `4px`
- Radius: `inputs: 0px, buttons: 0px, default: 0px`

## Surface cues
- **Atlantic Fog Canvas** `#d2dce1`: Primary page background, footer background.
- **Canvas White Panel** `#ffffff`: Dominant surface for content blocks, cards, and primary sections.
- **Subtle Accent Surface** `#0000000d`: Slightly elevated or interactive elements, like some button backgrounds.

## Component cues
- **Primary Ghost Button**: Interactive element, calls to action
- **Filled White Button**: Interactive element, calls to action
- **Subtle Accent Button**: Secondary interactive element, filtering, categorization
- **Muted Border Button**: Tertiary interactive element, inactive states
- **Text Input (Default)**: Form element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
