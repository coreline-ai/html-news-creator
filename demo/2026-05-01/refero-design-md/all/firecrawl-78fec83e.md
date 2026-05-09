# Firecrawl - Refero Design MD

- Source: https://styles.refero.design/style/78fec83e-4b27-44ab-9f64-31e9dee53e46
- Original site: https://www.firecrawl.dev
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard blueprints, with a single neon 'active' indicator.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Fire Orange | `#ff4d00` | brand | Action accent / signal color |
| Code Blue | `#006fff` | accent | Action accent / signal color |
| Cloud Canvas | `#e5e7eb` | neutral | Page background or card surface |
| Ink Black | `#262626` | neutral | Primary text or dark surface |
| Paper White | `#f9f9f9` | neutral | Page background or card surface |
| Slate Gray | `#727272` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#616161` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#949494` | neutral | Border, muted text, or supporting surface |
| Frost Gray | `#c7c7c7` | neutral | Border, muted text, or supporting surface |
| Pale Sienna | `#fcddcc` | neutral | Page background or card surface |

```css
:root {
  --ref-fire-orange: #ff4d00;
  --ref-code-blue: #006fff;
  --ref-cloud-canvas: #e5e7eb;
  --ref-ink-black: #262626;
  --ref-paper-white: #f9f9f9;
  --ref-slate-gray: #727272;
  --ref-stone-gray: #616161;
  --ref-silver-mist: #949494;
}
```

## Typography direction
- **suisse**: 400, 450, 500, 10px, 12px, 13px, 14px, 15px, 16px, 20px, 24px, 40px, 52px, 60px, 1.00, 1.07, 1.08, 1.10, 1.20, 1.33, 1.40, 1.43, 1.50, 1.54, 1.60, 1.67; substitute `Inter`.
- **GeistMono**: 400, 500, 12px, 13px, 14px, 1.33, 1.54, 1.57; substitute `SF Mono`.

## Spacing / shape
- Section Gap: `164px`
- Card Padding: `16px`
- Element Gap: `12px`
- Page Max Width: `1200px`
- Radius: `tags: 999px, cards: 16px, inputs: 8px, buttons: 999px, menuItems: 8px`

## Surface cues
- **Canvas** `#e5e7eb`: The primary background for the entire page, providing a consistent, light base.
- **Card Base** `#f9f9f9`: Used for standard card backgrounds and slightly elevated sections, creating gentle separation from the canvas.
- **Elevated Card** `#ffffff`: Applied to more prominent interactive cards or panels, enhanced with shadows for distinct layering.

## Component cues
- **Primary Action Button**: Calls to action, signup, and key interactive elements.
- **Ghost Button**: Secondary actions that need less emphasis, often next to a primary button.
- **Navigation Link Button**: Navigation items in headers and footers.
- **Feature Card**: Showcasing product features or benefits.
- **Hero Input Field**: Main input for search/URL, prominent on hero section.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
