# reboot - Refero Design MD

- Source: https://styles.refero.design/style/ac14ea36-ea3e-4a25-bd16-11fb50d806fb
- Original site: https://reboot.studio
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Type Ink | `#000000` | neutral | Primary text or dark surface |
| Subtle Gray | `#232323` | neutral | Primary text or dark surface |
| Whisper Gray | `#a7a7a7` | neutral | Border, muted text, or supporting surface |
| Outline Ash | `#e5e7eb` | neutral | Page background or card surface |
| Frost | `#c8c8c8` | neutral | Border, muted text, or supporting surface |
| Oceanic Blue Gradient | `#00c8fb` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-type-ink: #000000;
  --ref-subtle-gray: #232323;
  --ref-whisper-gray: #a7a7a7;
  --ref-outline-ash: #e5e7eb;
  --ref-frost: #c8c8c8;
  --ref-oceanic-blue-gradient: #00c8fb;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 14px, 16px, 40px, 1.43, 1.50, 1.60, 1.80; substitute `Inter`.
- **Inter**: 400, 500, 600, 14px, 16px, 40px, 1.43, 1.50, 1.60, 1.80; substitute `Inter`.
- **Inter**: 400, 500, 600, 14px, 16px, 40px, 1.43, 1.50, 1.60, 1.80; substitute `Inter`.

## Spacing / shape
- Radius: `cards: 16px, buttons: 9999px`

## Component cues
- **Hiring Badge / Navigation Pill**: Reference component style.
- **Hero Text Block**: Reference component style.
- **CTA Block with See Work Button**: Reference component style.
- **Outline Pill Button**: Primary Call to Action for secondary actions
- **Ghost Header Button**: Navigation items and subtle actions in the header

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
