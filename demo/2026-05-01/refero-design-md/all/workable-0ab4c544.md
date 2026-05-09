# Workable - Refero Design MD

- Source: https://styles.refero.design/style/0ab4c544-6147-4998-8365-3a0f6191e54f
- Original site: https://www.workable.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Clean canvas, purposeful accents

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Porcelain | `#fff5ee` | neutral | Page background or card surface |
| White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#0f161e` | neutral | Primary text or dark surface |
| Harbor Mist | `#333942` | neutral | Primary text or dark surface |
| Forest Canopy | `#012620` | brand | Action accent / signal color |
| Deep Teal | `#004038` | brand | Action accent / signal color |
| Fresh Teal | `#00f5dc` | accent | Action accent / signal color |
| Muted Sage | `#00544c` | brand | Action accent / signal color |
| Soft Peach | `#fde8ce` | accent | Action accent / signal color |
| Muted Mandarin | `#ffdcbf` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-porcelain: #fff5ee;
  --ref-white: #ffffff;
  --ref-midnight-ink: #0f161e;
  --ref-harbor-mist: #333942;
  --ref-forest-canopy: #012620;
  --ref-deep-teal: #004038;
  --ref-fresh-teal: #00f5dc;
  --ref-muted-sage: #00544c;
}
```

## Typography direction
- **Proxima Nova**: 400, 700, 16px, 18px, 20px, 24px, 32px, 56px, 72px, 1.00, 1.13, 1.14, 1.17, 1.20, 1.22, 1.25, 1.38, 1.50, 1.56, 1.75; substitute `Open Sans`.
- **Source Serif Pro**: 400, 24px, 1.50; substitute `Merriweather`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `32px`
- Element Gap: `8px`
- Radius: `cards: 16px, badges: 25px, buttons: 16px, navigation: 8px`

## Surface cues
- **Canvas Porcelain** `#fff5ee`: Base page background
- **White** `#ffffff`: Primary card and elevated component background
- **Soft Peach** `#fde8ce`: Accentuated card backgrounds for differentiation
- **Muted Mandarin** `#ffdcbf`: Secondary accent card background
- **Sky Haze** `#bee9f4`: Tertiary accent card background

## Component cues
- **Primary Ghost Button**: Call to action with minimal visual weight
- **Secondary Ghost Button**: Outlined action with rounded corners
- **Default Card**: Content container for features or information blocks
- **Highlight Card - Soft Peach**: Emphasized content container with a warm background tint
- **Highlight Card - Fresh Teal**: Emphasized content container with a vivid background tint

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
