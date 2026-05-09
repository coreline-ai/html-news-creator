# Cohere - Refero Design MD

- Source: https://styles.refero.design/style/f1bff240-fa05-41db-9ae1-b165ea6ea2cb
- Original site: https://cohere.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep charcoal on white, with purple-violet washes. Like a digital slate occasionally illuminated by the aurora borealis.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#ffffff` | neutral | Page background or card surface |
| Night Sky | `#17171c` | neutral | Primary text or dark surface |
| Charcoal Slate | `#212121` | neutral | Primary text or dark surface |
| Ash Mist | `#e5e7eb` | neutral | Page background or card surface |
| Graphite | `#75758a` | neutral | Border, muted text, or supporting surface |
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Warm Violet Gradient | `#ff7759` | brand | Action accent / signal color |
| Cosmic Violet | `#9b60aa` | brand | Action accent / signal color |
| Soft Indigo Wash | `#f0dff3` | brand | Action accent / signal color |
| Azure Glow | `#00a1df` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #ffffff;
  --ref-night-sky: #17171c;
  --ref-charcoal-slate: #212121;
  --ref-ash-mist: #e5e7eb;
  --ref-graphite: #75758a;
  --ref-deep-space: #000000;
  --ref-warm-violet-gradient: #ff7759;
  --ref-cosmic-violet: #9b60aa;
}
```

## Typography direction
- **Unica77 Cohere Web**: 400, 700, 12px, 14px, 16px, 18px, 24px, 32px, 48px, 1.20, 1.30, 1.40, 1.50; substitute `Inter`.
- **CohereText**: 400, 60px, 72px, 1.00; substitute `Outfit`.
- **CohereMono**: 400, 14px, 1.40; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `16px`
- Radius: `buttons: 9999px, default: 22px, navigation: 4px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Trusted By Logo Bar**: Reference component style.
- **Feature Pillars — Security, Deployment, Customization**: Reference component style.
- **Primary Ghost Button**: Call to action, secondary actions.
- **Primary Filled Button**: Main call to action.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
