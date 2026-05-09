# Framer - Refero Design MD

- Source: https://styles.refero.design/style/d417b42f-824d-45ba-a02e-cbef3b8ea0d8
- Original site: https://framer.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Inky command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Charcoal Canvas | `#080808` | neutral | Primary text or dark surface |
| Vapor White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Slate Dust | `#666666` | neutral | Border, muted text, or supporting surface |
| Deep Space | `#171717` | neutral | Primary text or dark surface |
| Electric Blue | `#0099ff` | brand | Action accent / signal color |
| Sky Indigo | `#0055ff` | accent | Action accent / signal color |
| Cyan Fade | `#05ff9f` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-charcoal-canvas: #080808;
  --ref-vapor-white: #ffffff;
  --ref-ash-gray: #999999;
  --ref-silver-mist: #cccccc;
  --ref-slate-dust: #666666;
  --ref-deep-space: #171717;
  --ref-electric-blue: #0099ff;
}
```

## Typography direction
- **GT Walsheim Framer Medium**: 500, 110px, 0.85; substitute `Montserrat`.
- **GT Walsheim Medium**: 500, 32px, 62px, 85px, 0.95, 1.00, 1.13; substitute `Montserrat`.
- **Mona Sans**: 500, 12px, 13px, 17px, 18px, 62px, 1.00, 1.20, 1.30, 1.70, 2.28; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `10px`
- Element Gap: `4px`
- Radius: `cards: 8px, images: 8px, inputs: 8px, modals: 12px, buttons: 100px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Testimonial Card**: Reference component style.
- **Trusted By — Logo Bar**: Reference component style.
- **Primary Hero Button**: Call to action
- **Secondary Ghost Button**: Secondary call to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
