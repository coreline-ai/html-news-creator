# Pixso - Refero Design MD

- Source: https://styles.refero.design/style/155dbf6e-1187-424e-9ce8-59ffecff7e6b
- Original site: https://pixso.net
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint on White Marble. This system feels like designs precisely laid out in a brightly lit, expansive modern studio.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Warm Mist | `#f9f9fa` | neutral | Page background or card surface |
| Slate Border | `#eaebee` | neutral | Page background or card surface |
| Deep Graphite | `#121212` | neutral | Primary text or dark surface |
| Cloud Whisper | `#faf8fd` | neutral | Page background or card surface |
| Cool Teal | `#cfe7ed` | accent | Action accent / signal color |
| Skybound Blue | `#336fff` | brand | Action accent / signal color |
| Skybound Blue Hover | `#4381ff` | brand | Action accent / signal color |
| Cosmic Drift Gradient | `#bfbfbf` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-canvas-white: #ffffff;
  --ref-warm-mist: #f9f9fa;
  --ref-slate-border: #eaebee;
  --ref-deep-graphite: #121212;
  --ref-cloud-whisper: #faf8fd;
  --ref-cool-teal: #cfe7ed;
  --ref-skybound-blue: #336fff;
}
```

## Typography direction
- **Figtree**: 400, 500, 600, 700, 12px, 13px, 14px, 16px, 18px, 24px, 28px, 30px, 34px, 48px, 50px, 60px, 1.10, 1.15, 1.17, 1.20, 1.21, 1.29, 1.30, 1.38, 1.40, 1.50, 1.55, 1.60, 1.61; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `0px`
- Element Gap: `6px`
- Radius: `cards: 8px, input: 0px, buttons: 8px, largeButtons: 12px, decorativeRound: 18px`

## Component cues
- **Hero CTA Button Group**: Reference component style.
- **Design Resource Cards Grid**: Reference component style.
- **Value Proposition Text Block**: Reference component style.
- **Primary Action Button**: Core CTA for user actions
- **Secondary Action Button**: Alternative or less prominent actions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
