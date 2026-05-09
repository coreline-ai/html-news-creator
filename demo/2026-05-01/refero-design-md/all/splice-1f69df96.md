# Splice - Refero Design MD

- Source: https://styles.refero.design/style/1f69df96-675d-4ee0-aa85-e085d9d39981
- Original site: https://splice.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Studio, Cobalt Glow. A dark, immersive interface with bursts of vivid, digital-native color.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#121214` | neutral | Primary text or dark surface |
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Ghost Gray | `#09090a` | neutral | Primary text or dark surface |
| Cloudburst | `#232426` | neutral | Primary text or dark surface |
| Arctic Mist | `#ffffff` | neutral | Page background or card surface |
| Storm Cloud | `#a6a8ad` | neutral | Border, muted text, or supporting surface |
| Pewter | `#c8c9cc` | neutral | Border, muted text, or supporting surface |
| Slate Border | `#63656d` | neutral | Border, muted text, or supporting surface |
| Cobalt Blue | `#1253ff` | brand | Action accent / signal color |
| Active Link Blue | `#528fff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #121214;
  --ref-deep-space: #000000;
  --ref-ghost-gray: #09090a;
  --ref-cloudburst: #232426;
  --ref-arctic-mist: #ffffff;
  --ref-storm-cloud: #a6a8ad;
  --ref-pewter: #c8c9cc;
  --ref-slate-border: #63656d;
}
```

## Typography direction
- **InterVariable**: 400, 500, 600, 700, 12px, 13px, 14px, 16px, 18px, 20px, 26px, 1.20, 1.25, 1.43, 1.50; substitute `Inter`.
- **SoehneBreit**: 400, 14px, 28px, 36px, 48px, 54px, 1.25, 1.43; substitute `Arial Black`.
- **Soehne**: 400, 20px, 1.25; substitute `Arial`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `nav: 1440px, buttons: 60px, default: 8px`

## Component cues
- **Announcement Banner**: Reference component style.
- **Primary CTA Button Group**: Reference component style.
- **Pricing Plan Card**: Reference component style.
- **Primary Call to Action Button**: Core user interaction
- **Secondary Ghost Button**: Secondary action or subtle navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
