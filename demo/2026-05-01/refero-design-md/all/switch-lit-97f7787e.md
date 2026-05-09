# Switch-Lit - Refero Design MD

- Source: https://styles.refero.design/style/97f7787e-bba0-4d37-8b74-4b0cb8d5a57c
- Original site: https://switch-lit.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type-driven collaborative canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Cloud Canvas | `#f9f9f7` | neutral | Page background or card surface |
| Stone Whisper | `#d2ddd2` | neutral | Page background or card surface |
| Mist Gray | `#edf0e9` | neutral | Page background or card surface |
| Lunar Dust | `#dee5dd` | neutral | Page background or card surface |
| Sky Tint | `#bed4fb` | accent | Action accent / signal color |
| Lime Glow | `#edfe5e` | accent | Action accent / signal color |
| Mint Burst | `#31e992` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-cloud-canvas: #f9f9f7;
  --ref-stone-whisper: #d2ddd2;
  --ref-mist-gray: #edf0e9;
  --ref-lunar-dust: #dee5dd;
  --ref-sky-tint: #bed4fb;
  --ref-lime-glow: #edfe5e;
  --ref-mint-burst: #31e992;
}
```

## Typography direction
- **ABCArizonaSans**: 400, 500, 700, 11px, 13px, 15px, 16px, 18px, 1.00, 1.15, 1.18, 1.25, 1.27; substitute `Inter`.
- **ABCArizonaSansVariable**: 400, 500, 11px, 15px, 18px, 1.00, 1.11, 1.18, 1.36, 1.40; substitute `Inter Variable`.
- **ABCArizonaFlare-Regular**: 300, 400, 24px, 27px, 28px, 57px, 0.93, 1.04, 1.07, 1.11; substitute `Lora`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `cards: 6px, forms: 6px, links: 3px, buttons: 24px, elements: 6px`

## Surface cues
- **Cloud Canvas** `#f9f9f7`: Primary page and card backgrounds, the base layer of the UI.
- **Mist Gray** `#edf0e9`: Background for secondary buttons and subtle accents, slightly differentiated from the main canvas.
- **Accent Wash** `#bed4fb`: Sectional background washes (e.g., Sky Tint, Lime Glow) to visually segment content or highlight areas.

## Component cues
- **Primary Filled Button**: Main calls to action
- **Secondary Filled Button**: Secondary actions or navigation
- **Ghost Outlined Button**: Tertiary actions or navigation
- **Basic Card**: Content grouping without visual elevation
- **Sectional Card (subtle background)**: Content grouping with slight visual separation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
