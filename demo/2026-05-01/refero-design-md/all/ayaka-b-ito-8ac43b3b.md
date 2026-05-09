# Ayaka B. Ito - Refero Design MD

- Source: https://styles.refero.design/style/8ac43b3b-7139-4777-bc77-217614e01e89
- Original site: https://ayakaito.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shifting Editorial Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Soft Umber | `#a65d4d` | brand | Action accent / signal color |
| Pale Rose Quartz | `#ddbad0` | neutral | Border, muted text, or supporting surface |
| Charcoal Ink | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Dusty Sage | `#576041` | accent | Action accent / signal color |
| Forest Moss | `#495116` | accent | Action accent / signal color |
| Misty Blue | `#9cb8d3` | accent | Action accent / signal color |
| Deep Teal | `#167070` | accent | Action accent / signal color |
| Cerulean Mist | `#9ec5d6` | accent | Action accent / signal color |
| Stone Grey | `#c7afac` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-soft-umber: #a65d4d;
  --ref-pale-rose-quartz: #ddbad0;
  --ref-charcoal-ink: #000000;
  --ref-paper-white: #ffffff;
  --ref-dusty-sage: #576041;
  --ref-forest-moss: #495116;
  --ref-misty-blue: #9cb8d3;
  --ref-deep-teal: #167070;
}
```

## Typography direction
- **Hanae Regular**: 400, 500, 10px, 11px, 13px, 16px, 18px, 20px, 23px, 25px, 32px, 38px, 40px, 62px, 68px, 1.00, 1.03, 1.05, 1.10, 1.16, 1.30, 1.31, 1.44, 1.82, 2.00, 2.12, 2.27, 2.45, 2.73; substitute `Lora`.
- **Open Sans**: 400, 700, 18px, 50px, 1.67; substitute `Inter`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `26px`
- Element Gap: `10px`
- Radius: `inputs: 140px, buttons: 120px, navItems: 180px`

## Surface cues
- **Paper White** `#ffffff`: Primary page background and default canvas for content.
- **Light Linen** `#eeecec`: Subtle background for card-like elements or differentiated content blocks, providing minimal contrast to the main canvas.
- **Soft Umber** `#a65d4d`: Hero sections and highly prominent content blocks, offering a warm, distinct visual anchor.

## Component cues
- **Ghost Button**: Primary interaction button
- **Outlined Input Field**: Text input areas
- **Navigation Item**: Primary navigation links
- **Editorial Header**: Section titles and prominent text blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
