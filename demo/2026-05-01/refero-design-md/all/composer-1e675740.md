# Composer - Refero Design MD

- Source: https://styles.refero.design/style/1e675740-7935-4a49-b4c8-e5aa9fda06dd
- Original site: https://www.composer.trade
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Algorithmic Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f7f7f7` | neutral | Page background or card surface |
| Ash Gray | `#e5e7eb` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#101516` | neutral | Primary text or dark surface |
| Steel Gray | `#bec6cc` | neutral | Border, muted text, or supporting surface |
| Composer Blue | `#1871da` | brand | Action accent / signal color |
| Emerald Green | `#31805a` | accent | Action accent / signal color |
| Bubblegum Pink | `#ffb4ed` | accent | Action accent / signal color |
| Vivid Green | `#1ec072` | accent | Action accent / signal color |
| Hot Pink | `#f6609f` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #f7f7f7;
  --ref-ash-gray: #e5e7eb;
  --ref-midnight-ink: #000000;
  --ref-graphite: #101516;
  --ref-steel-gray: #bec6cc;
  --ref-composer-blue: #1871da;
  --ref-emerald-green: #31805a;
  --ref-bubblegum-pink: #ffb4ed;
}
```

## Typography direction
- **Neue Haas Grotesk Display**: 400, 500, 600, 700, 14px, 16px, 20px, 24px, 32px, 36px, 56px, 64px, 244px, 1.00, 1.07, 1.11, 1.20, 1.25, 1.30, 1.33, 1.40, 1.43, 1.50; substitute `system-ui, sans-serif`.
- **Inter**: 400, 500, 600, 700, 9px, 10px, 12px, 14px, 16px, 1.25, 1.33, 1.43, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `4px`
- Page Max Width: `1200px`
- Radius: `none: 0px, small: 2px, button: 9999px, default: 6px, circular: 100px, cardAccentCorner: 12px`

## Surface cues
- **Canvas White** `#f7f7f7`: Primary page background, expansive and neutral base.
- **Light Card Surface** `#ffffff`: Elevated cards and contained content blocks, slightly brighter than the canvas.
- **Dark Card Surface** `#262d2f`: Cards or containers within dark-themed sections, providing strong contrast.
- **Accent Card Surface** `#31805a`: Cards or blocks with a saturated brand accent background.

## Component cues
- **Primary Action Button**: Main call to action for key conversions.
- **Ghost Nav Link**: Navigation items and secondary inline actions.
- **Contained White Card**: Standard content containers with subtle elevation.
- **Dark Overlay Card**: Content within dark sections or for visual contrast.
- **Header 'Sign Up' Button**: Distinguished action button in the header.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
