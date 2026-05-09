# Pipe - Refero Design MD

- Source: https://styles.refero.design/style/ab201ed7-928f-4080-ba95-c3992311e39d
- Original site: https://pipe.com
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Blackrock and Molten Orange. A landscape of dark, solid forms punctuated by sharp, glowing accents.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Core | `#000000` | neutral | Primary text or dark surface |
| Ivory Canvas | `#ffffff` | neutral | Page background or card surface |
| Slate Text | `#808080` | neutral | Border, muted text, or supporting surface |
| Onyx Layer | `#1a1a1a` | neutral | Primary text or dark surface |
| Ghost White | `#f5f5f5` | neutral | Page background or card surface |
| Molten Orange | `#e2572c` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-core: #000000;
  --ref-ivory-canvas: #ffffff;
  --ref-slate-text: #808080;
  --ref-onyx-layer: #1a1a1a;
  --ref-ghost-white: #f5f5f5;
  --ref-molten-orange: #e2572c;
}
```

## Typography direction
- **Suisse Font**: 400, 10px, 12px, 13px, 14px, 16px, 20px, 24px, 32px, 80px, 1.10, 1.24, 1.25, 1.33, 1.37, 1.40, 1.42, 1.43, 1.50, 1.63, 1.90; substitute `Inter`.

## Spacing / shape
- Section Gap: `64-72px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `pill: 9999px, cards: 16px, buttons: 8px`

## Component cues
- **Primary CTA Button Group**: Reference component style.
- **Feature Cards — Dark Surface Grid**: Reference component style.
- **Stat / Metric Block**: Reference component style.
- **Primary Call-to-Action Button**: Interactive element
- **Secondary Ghost Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
