# Base Design - Refero Design MD

- Source: https://styles.refero.design/style/6be758be-344f-4301-8ff9-60706356ea00
- Original site: https://www.basedesign.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Minimalist canvas, bold typography.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#ababab` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-ash-gray: #ababab;
}
```

## Typography direction
- **BaseGrotesk**: 300, 400, 500, 700, 12px, 16px, 18px, 25px, 30px, 32px, 50px, 60px, 65px, 1.15, 1.17, 1.20, 1.30, 1.33, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `7px`
- Radius: `buttons: 54px`

## Surface cues
- **Canvas Background** `#ffffff`: Primary page background and default surface for all content.

## Component cues
- **Pill Ghost Button**: Secondary action button
- **Contrast Fill Button**: Primary action button, often for content blocks
- **Text Link Button**: Minimal interactive element, typically for navigation or inline actions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
