# MindMarket - Refero Design MD

- Source: https://styles.refero.design/style/9130ad37-bf80-458f-b808-ac0ef6a8d1e9
- Original site: https://mindmarket.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Organic illustrations on calm canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Greige Canvas | `#f5f1e4` | neutral | Page background or card surface |
| Midnight Graphite | `#2c2e2a` | neutral | Primary text or dark surface |
| Clean White | `#ffffff` | neutral | Page background or card surface |
| Muted Stone | `#e0dbce` | neutral | Page background or card surface |
| Darkest Night | `#000000` | neutral | Primary text or dark surface |
| Ash Whisper | `#80827f` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#d5d5d4` | neutral | Border, muted text, or supporting surface |
| Market Green | `#8ed462` | brand | Action accent / signal color |
| Vibrant Yellow | `#f5e211` | brand | Action accent / signal color |
| Insight Blue | `#2ba0ff` | brand | Action accent / signal color |

```css
:root {
  --ref-greige-canvas: #f5f1e4;
  --ref-midnight-graphite: #2c2e2a;
  --ref-clean-white: #ffffff;
  --ref-muted-stone: #e0dbce;
  --ref-darkest-night: #000000;
  --ref-ash-whisper: #80827f;
  --ref-light-steel: #d5d5d4;
  --ref-market-green: #8ed462;
}
```

## Typography direction
- **Inter**: 400, 500, 9px, 15px, 17px, 18px, 20px, 30px, 53px, 81px, 140px, 144px, 0.95, 1.15, 1.20, 1.25, 1.50, 2.00; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `85px`
- Card Padding: `21px`
- Element Gap: `21px`
- Radius: `cards: 63.75px, badges: 50px, inputs: 10px, buttons: 50px, containers: 25.5px`

## Surface cues
- **Greige Canvas** `#f5f1e4`: Base page background and default large content areas
- **Clean White** `#ffffff`: Elevated card backgrounds and focused content blocks

## Component cues
- **Primary Ghost Button**: Interactive element
- **Quote Button**: Call to action
- **Navigation Menu Button**: UI control
- **Rounded Info Card**: Content container
- **Section Highlight Card**: Content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
