# Superpower - Refero Design MD

- Source: https://styles.refero.design/style/5d34568d-4bdc-445d-a527-c6f5249fa8fb
- Original site: https://superpower.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Clinical precision, vibrant pulse. A highly legible monochrome foundation with a single, sharp burst of color highlighting interaction.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Charcoal Black | `#18181b` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Warm Gray | `#71717a` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#e4e4e7` | neutral | Page background or card surface |
| Whisper Gray | `#f4f4f5` | neutral | Page background or card surface |
| Vermillion Accent | `#fc5f2b` | brand | Action accent / signal color |
| Sunset Gradient | `#fc5f2b` | brand | Action accent / signal color |
| Soft Vermillion | `#feaf95` | brand | Action accent / signal color |
| Canary Yellow | `#ffdd61` | accent | Action accent / signal color |
| Sky Blue | `#42a5f5` | accent | Action accent / signal color |

```css
:root {
  --ref-charcoal-black: #18181b;
  --ref-pure-white: #ffffff;
  --ref-warm-gray: #71717a;
  --ref-light-gray: #e4e4e7;
  --ref-whisper-gray: #f4f4f5;
  --ref-vermillion-accent: #fc5f2b;
  --ref-sunset-gradient: #fc5f2b;
  --ref-soft-vermillion: #feaf95;
}
```

## Typography direction
- **Nb international pro webfont**: 400, 700, 11px, 13px, 15px, 17px, 19px, 22px, 26px, 30px, 37px, 45px, 56px, 60px, 66px, 1.00, 1.06, 1.10, 1.13, 1.20, 1.25, 1.40, 1.50; substitute `Inter`.
- **Nb International mono pro**: 400, 11px, 13px, 1.40, 1.50; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `64-96px`
- Element Gap: `4px`
- Radius: `misc: 29.9832px, cards: 16px, inputs: 11.2437px, buttons: 9999px`

## Component cues
- **Pricing Card — Superpower Membership**: Reference component style.
- **Button Group — Primary, Secondary, Ghost**: Reference component style.
- **Stat / Feature Blocks — Health Intelligence**: Reference component style.
- **Primary Call to Action Button**: Button
- **Secondary Outline Button**: Button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
