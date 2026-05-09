# Schema - Refero Design MD

- Source: https://styles.refero.design/style/2b07d62c-d706-4c9d-a3fb-9c163da09f03
- Original site: https://schema.figma.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Abstract art playground

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Pale Mist | `#e2e2e2` | neutral | Page background or card surface |
| Charcoal Text | `#0f0f0f` | neutral | Primary text or dark surface |
| Jade Accent | `#24cb71` | accent | Action accent / signal color |
| Aqua Wash | `#c7f8fb` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-pale-mist: #e2e2e2;
  --ref-charcoal-text: #0f0f0f;
  --ref-jade-accent: #24cb71;
  --ref-aqua-wash: #c7f8fb;
}
```

## Typography direction
- **Figma VF-normal-700-75**: 400, 24px, 1.2.
- **Figma Sans Text**: 400, 600, 13px, 16px, 18px, 24px, 72px, 1.00, 1.20, 1.22, 1.40; substitute `Inter`.
- **Figma Sans Display**: 400, 700, 16px, 24px, 32px, 56px, 72px, 86px, 0.90, 1.00, 1.10, 1.20, 1.30, 1.40; substitute `Inter Display`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `16px`
- Element Gap: `24px`
- Radius: `links: 20px, buttons: 20px`

## Component cues
- **Ghost Button**: Primary interactive element for event registration or key actions.
- **Navigation Link**: Top-level navigation items.
- **Section Divider Accent**: Visual separator for content blocks, creating graphic interest.
- **Speaker Card**: Display individual speaker profiles.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
