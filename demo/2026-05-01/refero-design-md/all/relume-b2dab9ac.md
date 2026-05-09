# Relume - Refero Design MD

- Source: https://styles.refero.design/style/b2dab9ac-9e35-43f5-a8bb-dd9d6702acf0
- Original site: https://relume.io
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
AI-powered architectural blueprint

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#f1f0ee` | neutral | Page background or card surface |
| Surface White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Text | `#161616` | neutral | Primary text or dark surface |
| Dark Neutral Text | `#222222` | neutral | Primary text or dark surface |
| Medium Gray Text | `#686868` | neutral | Border, muted text, or supporting surface |
| Light Border | `#e4e2df` | neutral | Page background or card surface |
| Primary Purple | `#6248ff` | brand | Action accent / signal color |
| Muted Purple | `#e0daff` | accent | Action accent / signal color |
| Light Purple Accent | `#b8adf5` | accent | Action accent / signal color |
| System Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas: #f1f0ee;
  --ref-surface-white: #ffffff;
  --ref-charcoal-text: #161616;
  --ref-dark-neutral-text: #222222;
  --ref-medium-gray-text: #686868;
  --ref-light-border: #e4e2df;
  --ref-primary-purple: #6248ff;
  --ref-muted-purple: #e0daff;
}
```

## Typography direction
- **Relative**: 400, 500, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 24px, 32px, 40px, 48px, 56px, 224px, 1.00, 1.20, 1.40, 1.43, 1.50; substitute `Inter`.
- **Relative Faux**: 400, 96px, 1.10; substitute `Inter`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `cards: 16px, pills: 320px, buttons: 8px, default: 8px`

## Surface cues
- **Canvas** `#f1f0ee`: Base page background, providing a warm, light foundation.
- **Surface White** `#ffffff`: Primary surface for cards, buttons, modals, and input fields, appearing slightly elevated from the canvas.

## Component cues
- **AI Generate Input Bar**: Reference component style.
- **Feature Cards — Plan / Structure / Conceptualise**: Reference component style.
- **Prompt to Sitemap — Feature Block**: Reference component style.
- **Primary Filled Button**: Signaling primary actions and calls to action.
- **Secondary Outlined Button**: Neutral, supportive actions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
