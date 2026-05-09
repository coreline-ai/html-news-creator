# Artboard - Refero Design MD

- Source: https://styles.refero.design/style/989d8d71-c161-4410-8157-ad6ade0bd4be
- Original site: https://artboard.studio
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm digital canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Forest Ink | `#0d1400` | brand | Action accent / signal color |
| Dune Beige | `#ffe4c3` | accent | Action accent / signal color |
| Sky Tint | `#cbedff` | accent | Action accent / signal color |
| Mint Leaf | `#caf3aa` | accent | Action accent / signal color |
| Sage Whisper | `#838976` | neutral | Border, muted text, or supporting surface |
| Artboard Green | `#aaff00` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-forest-ink: #0d1400;
  --ref-dune-beige: #ffe4c3;
  --ref-sky-tint: #cbedff;
  --ref-mint-leaf: #caf3aa;
  --ref-sage-whisper: #838976;
  --ref-artboard-green: #aaff00;
}
```

## Typography direction
- **system-ui**: 400, 700, 16px, 1.00, 1.50; substitute `system-ui, sans-serif`.
- **Vend Sans**: 400, 600, 700, 11px, 13px, 19px, 43px, 61px, 1.20, 1.50; substitute `ui-sans-serif, Noto Sans, system-ui`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `cards: 12px, badges: 8px, buttons: 8px, navItems: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default neutral surface
- **Accent Card Surface** `#ffe4c3`: Alternating background for showcasing product categories or features
- **Accent Card Surface** `#cbedff`: Alternating background for showcasing product categories or features
- **Accent Card Surface** `#caf3aa`: Alternating background for showcasing product categories or features

## Component cues
- **Primary Filled Button**: Main call-to-action button
- **Ghost Button**: Secondary action button, text-based
- **Standard Card**: Content container for mockups and features
- **Color-Tinte Card**: Promotional or featured content card
- **Ghost Badge**: Informational tag for categories or features

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
