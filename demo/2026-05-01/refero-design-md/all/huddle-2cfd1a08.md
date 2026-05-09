# Huddle - Refero Design MD

- Source: https://styles.refero.design/style/2cfd1a08-e5b1-4bd8-9270-29aa08f80aa0
- Original site: https://www.huddle.works
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Matte pastel blocks on midnight

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Canvas | `#000000` | neutral | Primary text or dark surface |
| Ash Cloud | `#ffffff` | neutral | Page background or card surface |
| Slate Text | `#333333` | neutral | Primary text or dark surface |
| Cream Paper | `#e5e6e1` | neutral | Page background or card surface |
| Warm Violet | `#bbb2ce` | brand | Action accent / signal color |
| Golden Ochre | `#e4b976` | brand | Action accent / signal color |
| Deep Plum | `#453b60` | brand | Action accent / signal color |
| Rose Blush | `#cb9da2` | brand | Action accent / signal color |
| Earth Clay | `#65451d` | brand | Action accent / signal color |
| Charcoal Teal | `#3a4444` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-canvas: #000000;
  --ref-ash-cloud: #ffffff;
  --ref-slate-text: #333333;
  --ref-cream-paper: #e5e6e1;
  --ref-warm-violet: #bbb2ce;
  --ref-golden-ochre: #e4b976;
  --ref-deep-plum: #453b60;
  --ref-rose-blush: #cb9da2;
}
```

## Typography direction
- **Nng**: 300, 400, 500, 700, 12px, 13px, 14px, 15px, 16px, 18px, 21px, 22px, 29px, 40px, 44px, 69px, 1.10, 1.20, 1.22, 1.25, 1.30, 1.32, 1.35, 1.42, 1.45, 1.50, 1.58; substitute `Inter`.
- **Roboto**: 400, 14px, 16px, 1.25, 1.43; substitute `Roboto`.
- **Apercu pro mono**: 400, 14px, 1.42, 1.43; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `12px`
- Page Max Width: `1200px`
- Radius: `tags: 8px, cards: 40px, lists: 24px, badges: 4px, buttons: 1000px`

## Surface cues
- **Midnight Canvas** `#000000`: Primary page background, base layer
- **Deep Plum Card** `#453b60`: Interactive elements, input cards, subtle accent areas
- **Warm Violet Card** `#bbb2ce`: Prominent project cards, key content blocks
- **Golden Ochre Card** `#e4b976`: Highlight project cards, distinct content segments
- **Cream Paper Card** `#e5e6e1`: Foreground elements, feedback cards, highly elevated sections (less used)

## Component cues
- **Pill Button - Dark Filled**: Primary action button
- **Pill Button - Earth Clay Filled**: Emphasis action button
- **Pill Button - Charcoal Teal Filled**: Secondary action button
- **Project Card - Warm Violet**: Content container for ongoing or active projects
- **Project Card - Golden Ochre**: Content container for shipped projects

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
