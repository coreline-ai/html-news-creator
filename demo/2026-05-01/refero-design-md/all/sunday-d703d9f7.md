# sunday - Refero Design MD

- Source: https://styles.refero.design/style/d703d9f7-4821-468e-8fe4-c8b5790b00ed
- Original site: https://sundayapp.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochromatic Precision, Neon Pulse

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Subtle Gray | `#736f7c` | neutral | Border, muted text, or supporting surface |
| Border Ash | `#dedede` | neutral | Page background or card surface |
| Accent Slate | `#7f7f7f` | neutral | Border, muted text, or supporting surface |
| Ghost Shadow | `#8b8893` | neutral | Border, muted text, or supporting surface |
| Divider Silver | `#bdbdbd` | neutral | Border, muted text, or supporting surface |
| Vivid Orchid | `#ff17e9` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-subtle-gray: #736f7c;
  --ref-border-ash: #dedede;
  --ref-accent-slate: #7f7f7f;
  --ref-ghost-shadow: #8b8893;
  --ref-divider-silver: #bdbdbd;
  --ref-vivid-orchid: #ff17e9;
}
```

## Typography direction
- **Helvetica Neue**: 400, 12px, 14px, 16px, 18px, 24px, 32px, 48px, 64px, 200px, 0.80, 0.95, 1.00, 1.13, 1.14, 1.20, 1.25, 1.33, 1.78; substitute `Arial, sans-serif`.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1328px`
- Radius: `cards: 16px, badges: 100px, inputs: 16px, buttons: 64px, large-cards: 48px 0px 0px 48px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background
- **Standard Card Background** `#0e071d0a`: Content cards and feature blocks

## Component cues
- **Primary Filled Button**: Call to action
- **Ghost Link Button**: Secondary action or link
- **Standard Card**: Content container, feature display
- **Asymmetric Section Card**: Prominent content section
- **Text Input Field**: User data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
