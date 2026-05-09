# Hatch - Refero Design MD

- Source: https://styles.refero.design/style/e1afed53-6854-40dd-8157-dfc1dd3505f0
- Original site: https://www.hatch.fm
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Bouncy Typographic Playground

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Creme | `#f5f4f0` | neutral | Page background or card surface |
| Surface White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Charcoal Text | `#222222` | neutral | Primary text or dark surface |
| Muted Slate | `#333333` | neutral | Primary text or dark surface |
| Border Ash | `#dddfe2` | neutral | Page background or card surface |
| Mint Accent | `#99ffcc` | brand | Action accent / signal color |
| Sky Blue | `#7bbbff` | accent | Action accent / signal color |
| Orchid Pink | `#ff99cc` | accent | Action accent / signal color |
| Sunset Orange | `#ffcc99` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-creme: #f5f4f0;
  --ref-surface-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-charcoal-text: #222222;
  --ref-muted-slate: #333333;
  --ref-border-ash: #dddfe2;
  --ref-mint-accent: #99ffcc;
  --ref-sky-blue: #7bbbff;
}
```

## Typography direction
- **Recoleta**: 700, 18px, 24px, 32px, 48px, 64px, 72px, 84px, 151px, 1.00; substitute `Playfair Display`.
- **Lota Grotes Que Alt**: 400, 14px, 18px, 24px, 1.50; substitute `Inter`.
- **Lota Grotes Que Alt**: 700, 14px, 18px, 24px, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `28px`
- Element Gap: `24px`
- Page Max Width: `1200px`
- Radius: `cards: 16px, pills: 1440px, small: 4px, buttons: 12px, heroElement: 40px`

## Component cues
- **Primary Filled Button**: Main call to action
- **Secondary Outlined Button**: Alternative call to action
- **Pill Ghost Button**: Compact, subtle interaction
- **Default Card**: Content grouping, feature display
- **Hero Feature Card**: Prominent content showcase

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
