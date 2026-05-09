# Honk - Refero Design MD

- Source: https://styles.refero.design/style/ca4708f7-7175-4da2-a47f-ce8f5e601f99
- Original site: https://honk.me
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
joyful, high-contrast messaging

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Canvas | `#008fff` | brand | Action accent / signal color |
| Sunshine Accent | `#ffe400` | accent | Action accent / signal color |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Text | `#111111` | neutral | Primary text or dark surface |
| Deep Space | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-sky-canvas: #008fff;
  --ref-sunshine-accent: #ffe400;
  --ref-paper-white: #ffffff;
  --ref-charcoal-text: #111111;
  --ref-deep-space: #000000;
}
```

## Typography direction
- **Honk Header**: 700, 52px, 1.23; substitute `Montserrat`.
- **Honk Sans**: 400, 500, 600, 13px, 14px, 16px, 17px, 19px, 0.70, 1.00, 1.20, 1.38, 1.47, 1.55; substitute `Inter`.

## Spacing / shape
- Section Gap: `48-64px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `links: 6px, other: 16px`

## Surface cues
- **Sky Canvas Background** `#008fff`: Primary page background layer, providing the brand's signature vibrant blue.
- **Paper White Elements** `#ffffff`: Used for content blocks, text bubbles, and interactive surfaces that sit atop the Sky Canvas to contain and present information clearly.

## Component cues
- **Ghost Link Button**: Minimal interactive element for secondary actions, often paired with an icon.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
