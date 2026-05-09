# Phantom - Refero Design MD

- Source: https://styles.refero.design/style/80028bf5-0c05-43a4-8c9e-b98750d610bd
- Original site: https://phantom.app
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Soft Violet Dreamscape: A calming digital space where gentle curves meet understated color, feeling secure and approachable.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Phantom Violet | `#3c315b` | brand | Action accent / signal color |
| Lavender Mist | `#e2dffe` | brand | Action accent / signal color |
| Grape Glow | `#ab9ff2` | accent | Action accent / signal color |
| Success Green | `#2ec08b` | semantic | Action accent / signal color |
| Paper White | `#fdfcfe` | neutral | Page background or card surface |
| Charcoal Black | `#1c1c1c` | neutral | Primary text or dark surface |
| Silver Ash | `#e9e8ea` | neutral | Page background or card surface |
| Fog Gray | `#f4f2f4` | neutral | Page background or card surface |
| Stone Gray | `#86848d` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-phantom-violet: #3c315b;
  --ref-lavender-mist: #e2dffe;
  --ref-grape-glow: #ab9ff2;
  --ref-success-green: #2ec08b;
  --ref-paper-white: #fdfcfe;
  --ref-charcoal-black: #1c1c1c;
  --ref-silver-ash: #e9e8ea;
  --ref-fog-gray: #f4f2f4;
}
```

## Typography direction
- **Phantom**: 350, 400, 13px, 15px, 16px, 20px, 24px, 30px, 64px, 80px, 96px, 1.00, 1.10, 1.20, 1.21, 1.25, 1.35, 1.40.

## Spacing / shape
- Card Padding: `24px`
- Radius: `pill: 100px, cards: 24px, input: 0px, buttons: 32px`

## Component cues
- **Download CTA Button Group**: Reference component style.
- **Feature Section Card — Trading Tools**: Reference component style.
- **Security Feature Card — Dark**: Reference component style.
- **Primary Action Button**: Main call to action
- **Inverted Dark Button**: Secondary action or featured button on dark backgrounds

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
