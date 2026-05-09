# Buymeacoffee - Refero Design MD

- Source: https://styles.refero.design/style/1b2aaf14-43b0-4c23-bd25-1d49924fe85e
- Original site: https://buymeacoffee.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, buoyant community canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#e5e7eb` | neutral | Page background or card surface |
| Surface | `#ffffff` | neutral | Page background or card surface |
| Deep Graphite | `#222222` | neutral | Primary text or dark surface |
| Text Accent | `#717171` | neutral | Border, muted text, or supporting surface |
| Rich Black | `#000000` | neutral | Primary text or dark surface |
| Goldenrod | `#ffdd00` | brand | Action accent / signal color |
| Amber Glow | `#f7d046` | brand | Action accent / signal color |
| Sunset Coral | `#d8573f` | accent | Action accent / signal color |
| Blush Tone | `#f5d5cf` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas: #e5e7eb;
  --ref-surface: #ffffff;
  --ref-deep-graphite: #222222;
  --ref-text-accent: #717171;
  --ref-rich-black: #000000;
  --ref-goldenrod: #ffdd00;
  --ref-amber-glow: #f7d046;
  --ref-sunset-coral: #d8573f;
}
```

## Typography direction
- **ui-sans-serif**: 400, 16px, 1.5.
- **Circular**: 400, 10px, 12px, 14px, 16px, 18px, 22px, 24px, 40px, 1.20, 1.33, 1.50, 1.67; substitute `system-ui, sans-serif`.
- **Circular**: 500, 14px, 16px, 20px, 24px, 64px, 96px, 0.99, 1.00, 1.17, 1.20, 1.25, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `cards: 24px, links: 16px, images: 8px, inputs: 8px, buttons: 9999px`

## Surface cues
- **Canvas Base** `#e5e7eb`: The foundational background for the entire page, providing a slight off-white anchor.
- **Primary Surface** `#ffffff`: Used for content cards, modals, and interactive elements, allowing text and UI to stand out clearly.

## Component cues
- **Support Card**: Informational display for creators, featuring a soft shadow and rounded corners.
- **Pill-shaped Creator Card**: Compact display for creators, often used in lists or carousels, with a strong pill-like radius.
- **Marketing Feature Card**: Large, inviting card for presenting key features or sections, generous padding and soft radius.
- **Interactive Item Card**: Smaller card for interactive elements like input fields or message bubbles, with a subtle semantic background and no shadow.
- **Call-to-Action Button**: Primary action button, bright and inviting, commanding attention with its distinct color and rounded shape.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
