# Axelar - Refero Design MD

- Source: https://styles.refero.design/style/109e52eb-e70f-493e-9527-84d672b00c7b
- Original site: https://axelar.network
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark Grid Neon Flux

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Apex | `#04070a` | neutral | Primary text or dark surface |
| Obsidian Surface | `#000000` | neutral | Primary text or dark surface |
| Charcoal Panel | `#0f1214` | neutral | Primary text or dark surface |
| Smoke Gray | `#1a1d1f` | neutral | Primary text or dark surface |
| Ash Outline | `#676f7a` | neutral | Border, muted text, or supporting surface |
| Alabaster Text | `#f0f5fa` | neutral | Page background or card surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Amber Thrust | `#ff6314` | brand | Action accent / signal color |
| Jade Glow | `#33ffac` | semantic | Action accent / signal color |
| Amethyst Spark | `#ff2ad4` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-apex: #04070a;
  --ref-obsidian-surface: #000000;
  --ref-charcoal-panel: #0f1214;
  --ref-smoke-gray: #1a1d1f;
  --ref-ash-outline: #676f7a;
  --ref-alabaster-text: #f0f5fa;
  --ref-polar-white: #ffffff;
  --ref-amber-thrust: #ff6314;
}
```

## Typography direction
- **Clashgrotesk**: 500, 600, 14px, 16px, 19px, 21px, 28px, 37px, 56px, 70px, 74px, 1.00, 1.25, 1.50; substitute `Montserrat`.
- **Inter**: 400, 600, 16px, 19px, 21px, 1.25; substitute `Inter`.
- **DM Mono**: 400, 500, 12px, 14px, 16px, 19px, 1.00, 1.25, 1.33; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `24px`
- Element Gap: `24px`
- Page Max Width: `1584px`
- Radius: `cards: 8px, badges: 100px, inputs: 24px, buttons: 24px`

## Surface cues
- **Midnight Apex Canvas** `#04070a`: The foundational dark background for the entire page, providing depth and contrast.
- **Obsidian Surface** `#000000`: Primary interactive or contained surfaces like navigation and hero elements, slightly elevated from the canvas.
- **Charcoal Panel** `#0f1214`: Secondary structured content panels and card backgrounds, offering a subtle visual break within dark sections.
- **Amber highlight** `#ff6314`: High-impact cards or feature blocks that explicitly draw attention against the dark background.

## Component cues
- **Primary Action Button**: Highest priority interaction
- **Outline Ghost Button**: Secondary action or navigation
- **Category Card**: Grouping related content or trusted brands
- **Highlight Card**: Featured content section
- **Neutral Input Field**: User data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
