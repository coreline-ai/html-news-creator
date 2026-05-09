# Moving Parts - Refero Design MD

- Source: https://styles.refero.design/style/fb459c9d-c089-4d0b-b5b0-d147b1c4ebd7
- Original site: https://movingparts.io
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast geometric clarity

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghostly Gray | `#121212` | neutral | Primary text or dark surface |
| Fog Grid | `#bcc1c7` | neutral | Border, muted text, or supporting surface |
| Warm Mist | `#efefef` | neutral | Page background or card surface |
| Cloud Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Pale Ash | `#999999` | neutral | Border, muted text, or supporting surface |
| Deep Royal Blue | `#0000ff` | brand | Action accent / signal color |
| Emerald Green | `#00d37c` | accent | Action accent / signal color |
| Conic Spectrum | `#57c0f1` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-ghostly-gray: #121212;
  --ref-fog-grid: #bcc1c7;
  --ref-warm-mist: #efefef;
  --ref-cloud-gray: #b3b3b3;
  --ref-pale-ash: #999999;
  --ref-deep-royal-blue: #0000ff;
}
```

## Typography direction
- **Whyte Semi-Mono**: 400, 500, 600, 12px, 17px, 18px, 21px, 25px, 27px, 30px, 34px, 35px, 1.06, 1.15, 1.18, 1.20, 1.36, 1.89, 2.38; substitute `Space Mono`.
- **Unica77**: 400, 500, 600, 700, 18px, 21px, 22px, 23px, 26px, 27px, 28px, 30px, 31px, 32px, 35px, 38px, 40px, 47px, 51px, 53px, 58px, 62px, 67px, 70px, 100px, 110px, 0.92, 0.93, 0.94, 0.95, 0.96, 1.00, 1.05, 1.12, 1.19, 1.20, 1.21, 1.22, 1.27, 1.32, 1.37, 1.47, 1.61, 1.71, 1.81; substitute `Roboto`.
- **PP Neue Montreal**: 400, 500, 27px, 32px, 60px, 81px, 98px, 0.82, 0.84, 0.85, 0.87, 1.20, 1.21; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `30px`
- Element Gap: `13px`
- Radius: `cards: 90.3833px, icons: 18px, images: 14px, buttons: 0px, largeCards: 106.333px, smallElements: 2.5px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background and default card surface.
- **Warm Mist** `#efefef`: Soft background distinction for sections or subtle component elevation.
- **Ghostly Gray** `#121212`: Accent background for dark sections or strong visual breaks.

## Component cues
- **Primary Action Button**: Main call-to-action
- **Ghost Button (Primary)**: Secondary action or navigation
- **Pill Button (Neutral)**: Status tags or filters
- **Rounded Corner Card**: Content container
- **Large Rounded Card (Bottom-Flat)**: Hero or feature container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
