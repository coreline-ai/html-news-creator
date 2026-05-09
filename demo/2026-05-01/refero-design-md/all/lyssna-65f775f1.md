# Lyssna - Refero Design MD

- Source: https://styles.refero.design/style/65f775f1-6dcc-4c49-80d2-b5a017b76f59
- Original site: https://www.lyssna.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Serene teal workspace

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Pine | `#061d29` | neutral | Primary text or dark surface |
| Arctic Mist | `#e5e7eb` | neutral | Page background or card surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Zenith Teal | `#006e75` | brand | Action accent / signal color |
| Pale Mint | `#b9ffe8` | brand | Action accent / signal color |
| Pale Amber | `#fffded` | neutral | Page background or card surface |
| Soft Stone | `#425d6d` | neutral | Border, muted text, or supporting surface |
| Rose Sunset | `#ffb0a4` | accent | Action accent / signal color |
| Warm Berry | `#4d0037` | accent | Action accent / signal color |
| Soft Magenta | `#ffc3e6` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-pine: #061d29;
  --ref-arctic-mist: #e5e7eb;
  --ref-canvas-white: #ffffff;
  --ref-zenith-teal: #006e75;
  --ref-pale-mint: #b9ffe8;
  --ref-pale-amber: #fffded;
  --ref-soft-stone: #425d6d;
  --ref-rose-sunset: #ffb0a4;
}
```

## Typography direction
- **mint**: 400, 500, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 22px, 26px, 1.22, 1.25, 1.50; substitute `Inter`.
- **grenette**: 400, 22px, 46px, 60px, 1.05, 1.15, 1.20; substitute `Outfit`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `cards: 24px, buttons: 8px, elements: 12px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background.
- **Pale Amber** `#fffded`: Secondary card surfaces, subtle accent sections.
- **Pale Mint** `#b9ffe8`: Accented card backgrounds, active state indicators.

## Component cues
- **Primary Filled Button**: Call-to-action button for initiating key actions.
- **Ghost Outline Button**: Secondary action button, blends into content.
- **Navigation Link Button**: Navigation items in the header or active states.
- **Default Card**: Content containers on white backgrounds.
- **Accent Card - Pale Amber**: Decorative or highlighted content containers.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
