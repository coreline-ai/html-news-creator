# Aurora - Refero Design MD

- Source: https://styles.refero.design/style/fe7b8533-f56b-46bd-8713-f18886a1e986
- Original site: https://aurora.tech
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Industrial precision on frosted glass

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#001733` | brand | Action accent / signal color |
| Aurora Blue | `#006aed` | brand | Action accent / signal color |
| Distant Gray | `#f3f4f8` | neutral | Page background or card surface |
| Ash Mist | `#e6e9f0` | neutral | Page background or card surface |
| Slate Text | `#68748d` | neutral | Border, muted text, or supporting surface |
| Steel Text | `#464e5d` | neutral | Border, muted text, or supporting surface |
| Subtle Gray | `#d1d6e0` | neutral | Border, muted text, or supporting surface |
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Vivid Aqua | `#18dcdc` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #001733;
  --ref-aurora-blue: #006aed;
  --ref-distant-gray: #f3f4f8;
  --ref-ash-mist: #e6e9f0;
  --ref-slate-text: #68748d;
  --ref-steel-text: #464e5d;
  --ref-subtle-gray: #d1d6e0;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 12px, 14px, 16px, 20px, 24px, 36px, 44px, 52px, 64px, 90px, 0.90, 0.95, 0.96, 0.97, 1.00, 1.10, 1.20, 1.30, 1.40, 1.50; substitute `system-ui`.
- **Arial**: 400, 13px, 1.2.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `4px`
- Page Max Width: `1200px`
- Radius: `cards: 8px, links: 8px, badges: 4px, buttons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background and primary content containers.
- **Distant Gray** `#f3f4f8`: Secondary content areas and subtly differentiated card backgrounds, providing a soft background contrast.
- **Ash Mist** `#e6e9f0`: Dividers, borders, and footer backgrounds.

## Component cues
- **Primary Call to Action Button**: Filled button indicating primary actions.
- **Ghost Navigation Button**: Navigation links or secondary actions presented without a fill.
- **Pill Accent Button**: Decorative or small navigational buttons, often for page navigation within a component.
- **Content Card (Default)**: Containers for information without visual emphasis.
- **Content Card (Subtle Background)**: Containers for grouped information, providing a soft background separation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
