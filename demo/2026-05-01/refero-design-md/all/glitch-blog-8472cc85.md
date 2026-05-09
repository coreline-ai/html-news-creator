# Glitch Blog - Refero Design MD

- Source: https://styles.refero.design/style/8472cc85-e4fa-4011-b742-1b9fc7966d76
- Original site: https://glitch.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful code journal

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Outline Gray | `#e4e4e4` | neutral | Page background or card surface |
| Input Border | `#b4b4b4` | neutral | Border, muted text, or supporting surface |
| Glitch Pink | `#ff00bc` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-outline-gray: #e4e4e4;
  --ref-input-border: #b4b4b4;
  --ref-glitch-pink: #ff00bc;
}
```

## Typography direction
- **Inter Variable**: 400, 600, 700, 14px, 16px, 18px, 20px, 40px, 1.20, 1.38; substitute `Inter, Arial, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `8px`
- Page Max Width: `1024px`
- Radius: `none: 0px, inputs: 0px`

## Component cues
- **Primary Navigation Link**: Main navigation items
- **Blog Post Card**: Container for individual blog post previews on listing pages
- **Article Title**: Headline for blog posts and prominent content sections
- **Date Metadata**: Timestamp for blog posts
- **Search Input Field**: Interactive text input for searching content

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
