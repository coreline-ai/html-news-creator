# Pietrastudio - Refero Design MD

- Source: https://styles.refero.design/style/577eb7d8-3555-4378-83df-0cebebc4782f
- Original site: https://www.pietrastudio.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm digital canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Stone Grey | `#f8f6f2` | neutral | Page background or card surface |
| Midnight Ink | `#1f2026` | neutral | Primary text or dark surface |
| Ink Wash | `#141414` | neutral | Primary text or dark surface |
| Slate Text | `#6b6b6b` | neutral | Border, muted text, or supporting surface |
| Silver Link | `#c4c4c4` | neutral | Border, muted text, or supporting surface |
| Input Border Gray | `#e8e8ea` | neutral | Page background or card surface |
| Action Orange | `#ff5c3c` | brand | Action accent / signal color |
| Slightly Yellowed | `#fffbe7` | accent | Action accent / signal color |
| Amber Dot | `#f9e070` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-stone-grey: #f8f6f2;
  --ref-midnight-ink: #1f2026;
  --ref-ink-wash: #141414;
  --ref-slate-text: #6b6b6b;
  --ref-silver-link: #c4c4c4;
  --ref-input-border-gray: #e8e8ea;
  --ref-action-orange: #ff5c3c;
}
```

## Typography direction
- **Labil Grotesk**: 400, 500, 700, 12px, 14px, 15px, 16px, 20px, 24px, 1.00, 1.20, 1.57; substitute `Inter`.
- **Labil-Regular**: 300, 400, 12px, 14px, 16px, 18px, 20px, 24px, 1.00, 1.13, 1.20, 1.50; substitute `Inter`.
- **Labil-Bold**: 400, 14px, 16px, 20px, 48px, 1.00, 1.13, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `120px`
- Card Padding: `12px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `cards: 12px, inputs: 8px, buttons: 8px, largeElements: 20px`

## Surface cues
- **Canvas White** `#ffffff`: Default page background.
- **Default Card Surface** `#ffffffe6`: Main content cards, slightly translucent.
- **Subtle Elevated Surface** `#f8f6f2`: Background for secondary sections or subtly elevated container groups.

## Component cues
- **Primary Filled Button**: The main call-to-action button, signaling key interactions.
- **Secondary Filled Button (Dark)**: Alternative action button, often for less critical actions.
- **Outline Ghost Button (Light Text)**: Subtle button for secondary actions or links where a filled button is too heavy.
- **Outlined Ghost Button (Yellow Accent)**: Contextual action button with a hint of accent color.
- **Default Card**: General content container for features, information blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
