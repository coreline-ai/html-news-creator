# Obscura - Refero Design MD

- Source: https://styles.refero.design/style/c445eb73-e403-4a00-8b90-f454c9181fd6
- Original site: https://obscura.net
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Pixelated secure cloud

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Storm Gray | `#232629` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Steel Gray | `#5c6066` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#989ea4` | neutral | Border, muted text, or supporting surface |
| Sky Blue | `#e3f1fe` | neutral | Action accent / signal color |
| Pixel Orange | `#ff5e24` | brand | Action accent / signal color |
| Deep Orange | `#6c3200` | brand | Action accent / signal color |
| Coal Black | `#000000` | neutral | Primary text or dark surface |
| Highlight Blue | `#2473eb` | accent | Action accent / signal color |
| Success Green | `#2fa73b` | accent | Action accent / signal color |

```css
:root {
  --ref-storm-gray: #232629;
  --ref-canvas-white: #ffffff;
  --ref-steel-gray: #5c6066;
  --ref-silver-mist: #989ea4;
  --ref-sky-blue: #e3f1fe;
  --ref-pixel-orange: #ff5e24;
  --ref-deep-orange: #6c3200;
  --ref-coal-black: #000000;
}
```

## Typography direction
- **Manrope Variable**: 400, 500, 600, 700, 800, 12px, 14px, 16px, 18px, 1.33, 1.43, 1.50, 1.56, 1.75; substitute `system-ui, sans-serif`.
- **Jersey 10**: 400, 500, 36px, 48px, 60px, 72px, 96px, 0.70, 0.80, 0.85, 1.00, 1.11; substitute `system-ui, monospace`.

## Spacing / shape
- Section Gap: `36px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `tags: 6px, cards: 12px, forms: 6px, images: 24px, buttons: 6px`

## Surface cues
- **Page Canvas** `#e3f1fe`: Dominant page background, providing a soft, light blue base.
- **Content Surface** `#ffffff`: Primary background for cards, modals, and content blocks.
- **Elevated Surface** `#ffffff`: Higher-prominence cards and containers with more pronounced shadows.
- **Decorative Tint** `#00000033`: Subtly tinted transparent backgrounds for specific UI elements.

## Component cues
- **Primary Action Button**: Main call-to-action button for initiating key user flows.
- **Ghost Navigation Button**: Navigation links or secondary actions within a header or sidebar.
- **Basic Card (Padded)**: Default container for content sections, forms, or data displays.
- **Elevated Feature Card**: Prominent content blocks, often for feature highlights or testimonials.
- **Soft Background Card**: Decorative or informational blocks with a transparent, tinted background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
