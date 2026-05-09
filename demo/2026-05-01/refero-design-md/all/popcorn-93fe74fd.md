# Popcorn - Refero Design MD

- Source: https://styles.refero.design/style/93fe74fd-bac8-4d13-9d5b-3b5e242f74e6
- Original site: https://popcorn.space
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochrome canvas, silent authority

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#393737` | neutral | Primary text or dark surface |
| Canvas White | `#f7f7f7` | neutral | Page background or card surface |
| Snow Drift | `#ffffff` | neutral | Page background or card surface |
| Slate Mist | `#888787` | neutral | Border, muted text, or supporting surface |
| Pale Cloud | `#e9eff6` | neutral | Page background or card surface |
| Gradient Aura | `#e7f3ee` | accent | Action accent / signal color |
| Skylight Fade | `#dae8f5` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #393737;
  --ref-canvas-white: #f7f7f7;
  --ref-snow-drift: #ffffff;
  --ref-slate-mist: #888787;
  --ref-pale-cloud: #e9eff6;
  --ref-gradient-aura: #e7f3ee;
  --ref-skylight-fade: #dae8f5;
}
```

## Typography direction
- **Messina Sans**: 400, 600, 700, 11px, 13px, 14px, 16px, 18px, 19px, 64px, 88px, 1.00, 1.20, 1.40, 1.50; substitute `Inter`.
- **Untitled Serif**: 400, 20px, 22px, 24px, 30px, 40px, 58px, 84px, 1.00, 1.20; substitute `Freight Text Pro`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `18px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `cards: 12px, badges: 100px, buttons: 100px, largeElements: 64px`

## Surface cues
- **Page Canvas** `#f7f7f7`: The primary background of the application, providing a clean, light base.
- **Card Surface** `#ffffff`: Used for content blocks and cards that need to stand out slightly from the canvas.
- **Alternative Card Surface** `#e9eff6`: A subtle alternative card background for variation or grouping related content without strong visual breaks.
- **Dark Foreground** `#393737`: Used for background of sections meant for high contrast or a distinct visual break.

## Component cues
- **Primary Ghost Button**: Action button for primary calls to action, maintaining lightness and integrating into the design.
- **Elevated Feature Card**: Highlights key features or testimonials, using soft elevation to draw attention.
- **Base Feature Card**: Standard card for displaying information without strong visual hierarchy.
- **Badge Pill**: Categorization or status indicator.
- **Hero Pill Badge**: Prominent status indicator within hero sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
