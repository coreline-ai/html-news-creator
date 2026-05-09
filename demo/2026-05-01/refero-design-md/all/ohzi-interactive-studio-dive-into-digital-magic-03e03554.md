# OHZI Interactive Studio / Dive into digital magic. - Refero Design MD

- Source: https://styles.refero.design/style/03e03554-d7aa-40da-9764-79320ecfa1d0
- Original site: https://ohzi.io
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep-space digital canvas

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#111111` | neutral | Primary text or dark surface |
| Supernova White | `#ffffff` | neutral | Page background or card surface |
| Digital Shadow | `#000000` | neutral | Primary text or dark surface |
| Star Dust | `#f5f5f7` | neutral | Page background or card surface |
| Nebula Gray | `#cfcfcf` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-void: #111111;
  --ref-supernova-white: #ffffff;
  --ref-digital-shadow: #000000;
  --ref-star-dust: #f5f5f7;
  --ref-nebula-gray: #cfcfcf;
}
```

## Typography direction
- **Unbounded**: 100, 400, 500, 600, 700, 14px, 16px, 17px, 18px, 19px, 23px, 24px, 30px, 32px, 38px, 1.20; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `15px`
- Element Gap: `20px`
- Radius: `cards: 0px, inputs: 0px, buttons: 0px`

## Component cues
- **Ghost Navigation Link**: Primary navigation item in header
- **Hero Action Button**: Primary call to action in hero section
- **Body Text Link**: Informational link within body copy or footer
- **Hamburger Menu Icon**: Mobile navigation toggle

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
