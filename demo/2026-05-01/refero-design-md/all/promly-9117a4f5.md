# Promly - Refero Design MD

- Source: https://styles.refero.design/style/9117a4f5-6171-44ad-aa85-a387a5d80620
- Original site: https://promlyapp.com
- Theme: `dark`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight gradient with neon accents.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Deep | `#000000` | neutral | Primary text or dark surface |
| Midnight Indigo | `#040723` | neutral | Primary text or dark surface |
| Ghost Shadow Indigo | `#140f33` | neutral | Primary text or dark surface |
| Primary Blue Neon | `#3898ec` | brand | Action accent / signal color |
| Accent Violet Neon | `#755eff` | accent | Action accent / signal color |
| Highlight Violet | `#aa57ff` | accent | Action accent / signal color |
| Content White | `#ffffff` | neutral | Page background or card surface |
| Muted Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Secondary Text Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Input Text Dark | `#333333` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-deep: #000000;
  --ref-midnight-indigo: #040723;
  --ref-ghost-shadow-indigo: #140f33;
  --ref-primary-blue-neon: #3898ec;
  --ref-accent-violet-neon: #755eff;
  --ref-highlight-violet: #aa57ff;
  --ref-content-white: #ffffff;
  --ref-muted-gray: #808080;
}
```

## Typography direction
- **Avenir**: 300, 400, 700, 14px, 16px, 18px, 20px, 25px, 28px, 35px, 45px, 59px, 60px, 64px, 1.07, 1.11, 1.17, 1.25, 1.36, 1.39, 1.40, 1.43, 1.50, 1.57, 1.69; substitute `Avenir Next, Lato`.
- **Poppins**: 700, 18px, 1.50; substitute `Montserrat, Open Sans`.

## Spacing / shape
- Section Gap: `88px`
- Card Padding: `20px`
- Element Gap: `20px`
- Page Max Width: `1196px`
- Radius: `cards: 25px, images: 20px, inputs: 12px, buttons: 12px`

## Surface cues
- **Canvas Deep** `#000000`: Base page background
- **Midnight Indigo** `#040723`: Elevated card and section backgrounds

## Component cues
- **Primary Filled Button**: Main call to action.
- **Ghost Navigation Button**: Navigation links or secondary actions that sit directly on the dark canvas.
- **Violet Outline Button**: Accentuating secondary actions on dark backgrounds.
- **Highlight Outline Button**: Tertiary interactive elements, often within cards.
- **Floating Card**: Container for content sections, featuring subtle elevation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
