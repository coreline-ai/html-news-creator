# Heavyweight - Refero Design MD

- Source: https://styles.refero.design/style/d991c31d-2ffa-4a94-ab37-7f7d8f7d6a0c
- Original site: https://heavyweight-type.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type foundry catalog on stark white

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Heavy Ink | `#222222` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Surface Frost | `#f3f5fa` | neutral | Page background or card surface |
| Border Graphite | `#2d2d2d` | neutral | Primary text or dark surface |
| Muted Ash | `#888888` | neutral | Border, muted text, or supporting surface |
| Accent Green | `#39d17f` | accent | Action accent / signal color |

```css
:root {
  --ref-heavy-ink: #222222;
  --ref-canvas-white: #ffffff;
  --ref-surface-frost: #f3f5fa;
  --ref-border-graphite: #2d2d2d;
  --ref-muted-ash: #888888;
  --ref-accent-green: #39d17f;
}
```

## Typography direction
- **Nuckle website**: 400, 500, 14px, 16px, 1.00, 1.14, 1.25; substitute `Inter`.

## Spacing / shape
- Section Gap: `166px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `all: 11px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background, primary canvas for content
- **Surface Frost** `#f3f5fa`: Secondary background for card-like elements or interactive components, e.g., default buttons
- **Heavy Ink Surface** `#222222`: Darkest surface, used for high-contrast elements like selected button backgrounds or header sections to create visual impact

## Component cues
- **Default Button**: Standard interactive element for general actions.
- **Primary Dark Button**: Emphasized action, often a confirmation or acceptance.
- **Outlined Light Button**: Alternative action, often used in conjunction with a primary dark button.
- **Font Showcase Card (Minimal)**: Displays font examples with minimal visual chrome.
- **Font Showcase Card (Image Placeholder)**: Card with an explicit aspect ratio for image/video content (e.g., animated font previews).

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
