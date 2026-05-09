# Overflow - Refero Design MD

- Source: https://styles.refero.design/style/6845a075-8573-4bdc-9346-58cb09b83547
- Original site: https://overflow.io
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant digital canvas. A bright, expansive white canvas animated by soft, flowing color gradients.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#fafafc` | neutral | Page background or card surface |
| Slate Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Light Ash | `#dadce0` | neutral | Page background or card surface |
| Cloud Gray | `#f0f0f2` | neutral | Page background or card surface |
| Deep Violet | `#161637` | brand | Action accent / signal color |
| Overflow Blue | `#0085e4` | accent | Action accent / signal color |
| Gradient Sky | `#7272fb` | brand | Action accent / signal color |
| Gradient Ocean | `#007bff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #000000;
  --ref-ghost-white: #fafafc;
  --ref-slate-gray: #666666;
  --ref-light-ash: #dadce0;
  --ref-cloud-gray: #f0f0f2;
  --ref-deep-violet: #161637;
  --ref-overflow-blue: #0085e4;
  --ref-gradient-sky: #7272fb;
}
```

## Typography direction
- **Inter**: 400, 500, 550, 600, 700, 800, 12px, 14px, 15px, 16px, 20px, 24px, 26px, 32px, 48px, 56px, 1.00, 1.07, 1.14, 1.15, 1.16, 1.20, 1.25, 1.33, 1.42, 1.43, 1.50, 1.57, 1.58, 1.60, 1.67, 1.75; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Page Max Width: `1288px`
- Radius: `cards: 8px, 24px, 0px, inputs: 8px, buttons: 8px, 22px, 50%, navElements: 12px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Cards Grid**: Reference component style.
- **Social Proof Banner**: Reference component style.
- **Primary Dark Button**: Main calls to action.
- **Circular Icon Button**: Small, contained actions like 'play video' or 'more info'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
