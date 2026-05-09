# Podia - Refero Design MD

- Source: https://styles.refero.design/style/342f1c3b-a123-49b6-a980-3491bc7793db
- Original site: https://www.podia.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful market stall atop soft-glowing white

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#06040e` | neutral | Primary text or dark surface |
| Deep Ocean | `#10242f` | neutral | Primary text or dark surface |
| Crystal Canvas | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#e1edf2` | neutral | Page background or card surface |
| Warm Sand | `#f5f5f5` | neutral | Page background or card surface |
| Sky Blue | `#a5c8d8` | accent | Action accent / signal color |
| Lavender Mist | `#cbb0eb` | accent | Action accent / signal color |
| Sunset Orange | `#e39a4d` | accent | Action accent / signal color |
| Rich Plum | `#1f1738` | brand | Action accent / signal color |
| Earthy Umber | `#452623` | brand | Action accent / signal color |

```css
:root {
  --ref-ink-black: #06040e;
  --ref-deep-ocean: #10242f;
  --ref-crystal-canvas: #ffffff;
  --ref-cloud-gray: #e1edf2;
  --ref-warm-sand: #f5f5f5;
  --ref-sky-blue: #a5c8d8;
  --ref-lavender-mist: #cbb0eb;
  --ref-sunset-orange: #e39a4d;
}
```

## Typography direction
- **StabilGrotesk**: 400, 500, 700, 11px, 12px, 16px, 18px, 20px, 22px, 24px, 36px, 40px, 60px, 1.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `misc: 24px, cards: 56px, links: 8px, buttons: 16px`

## Surface cues
- **Base Canvas** `#f5f5f5`: Primary page background.
- **Card Surface** `#ffffff`: Prominent surface for cards, banners, and primary content blocks.
- **Tertiary Surface** `#e1edf2`: Subtle background shifts, elevated section backgrounds.

## Component cues
- **Primary Filled Button**: Primary Call to Action
- **Secondary Filled Button**: Secondary Call to Action
- **Outlined Button**: Tertiary action or alternative navigation emphasis
- **Hero Feature Card - Sky Blue**: Primary feature showcase with distinct visual identity
- **Hero Feature Card - Sunset Orange**: Primary feature showcase with distinct visual identity

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
