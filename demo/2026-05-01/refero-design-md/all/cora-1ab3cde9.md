# Cora - Refero Design MD

- Source: https://styles.refero.design/style/1ab3cde9-0833-4e38-8ada-fc23156f730e
- Original site: https://cora.computer
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sky canvas, cloud cards

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Canvas | `#117bc8` | brand | Action accent / signal color |
| Midnight Accent | `#09426c` | brand | Action accent / signal color |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#dadada` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Text Gray | `#2b2b2b` | neutral | Primary text or dark surface |
| Muted Silver | `#a1a1a1` | neutral | Border, muted text, or supporting surface |
| Blue Border | `#60a8dd` | accent | Action accent / signal color |
| Carbon Shadow | `#0d5c96` | accent | Action accent / signal color |
| Error Red | `#cf372d` | accent | Action accent / signal color |

```css
:root {
  --ref-sky-canvas: #117bc8;
  --ref-midnight-accent: #09426c;
  --ref-cloud-white: #ffffff;
  --ref-ash-gray: #dadada;
  --ref-ink-black: #000000;
  --ref-text-gray: #2b2b2b;
  --ref-muted-silver: #a1a1a1;
  --ref-blue-border: #60a8dd;
}
```

## Typography direction
- **switzer**: 400, 500, 600, 700, 12px, 14px, 15px, 16px, 17px, 18px, 20px, 22px, 1.00, 1.02, 1.20, 1.24; substitute `system-ui, sans-serif`.
- **signifier**: 300, 400, 24px, 34px, 36px, 45px, 55px, 1.02, 1.18, 1.20; substitute `serif`.
- **Times**: 400, 16px, 1.20; substitute `serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `cards: 12px, forms: 8px, avatars: 9999px, buttons: 9999px`

## Component cues
- **Pill Button - Primary**: Main call to action button.
- **Pill Button - Ghost**: Secondary action button, typically on dark backgrounds.
- **Pill Button - White**: Secondary action button, typically on light backgrounds.
- **Default Card**: Standard content container.
- **Cloud Card - Testimonial**: Elevated card for testimonials or featured content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
