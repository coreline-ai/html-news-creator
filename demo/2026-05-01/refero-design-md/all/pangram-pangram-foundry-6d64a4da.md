# Pangram Pangram Foundry - Refero Design MD

- Source: https://styles.refero.design/style/6d64a4da-ef40-453e-86f7-4bfabc0c9051
- Original site: https://pangrampangram.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type foundry's bold canvas: white pages, dark headers, expressive typography, and soft, rounded containers.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas | `#fafafa` | neutral | Page background or card surface |
| Paper | `#ededed` | neutral | Page background or card surface |
| Slate | `#666666` | neutral | Border, muted text, or supporting surface |
| Alert Red | `#ff2f00` | brand | Action accent / signal color |
| Update Yellow | `#ffb700` | accent | Action accent / signal color |
| Early Access Blue | `#bfe0ff` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-canvas: #fafafa;
  --ref-paper: #ededed;
  --ref-slate: #666666;
  --ref-alert-red: #ff2f00;
  --ref-update-yellow: #ffb700;
  --ref-early-access-blue: #bfe0ff;
}
```

## Typography direction
- **Neue Montreal**: 400, 530, 600, 12px, 14px, 16px, 18px, 20px, 22px, 24px, 36px, 48px, 121px, 145px, 1.00, 1.10, 1.17, 1.20, 1.30; substitute `Inter`.
- **neue-montreal-semibold**: 600, 103px, 121px, 1.00; substitute `Inter`.
- **neue-york-normal-bold**: 700, 103px, 1.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `92px`
- Card Padding: `26px`
- Element Gap: `8px`
- Radius: `cards: 20px, badges: 999px, inputs: 20px, buttons: 20px`

## Surface cues
- **Canvas** `#fafafa`: Primary page background and default card background.
- **Paper** `#ededed`: Secondary lightweight surface for cards and some button backgrounds, subtle elevation.

## Component cues
- **Filled Button - Dark**: Primary action button.
- **Filled Button - Light**: Secondary action button.
- **Outlined Button - Light**: Tertiary action button or alternative action.
- **Outlined Button - Accent**: Call-to-action with strong visual emphasis.
- **Font Showcase Card - Filled**: Displays font information within a contained content block.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
