# Sequence - Refero Design MD

- Source: https://styles.refero.design/style/5b188bcc-95f6-45b4-b0af-1c78e2ef05f2
- Original site: https://light.so/home
- Theme: `light`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Blockchain blueprint on bright canvas.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#f1f5f9` | neutral | Page background or card surface |
| Outline Gray | `#e5e7eb` | neutral | Page background or card surface |
| Text Primary | `#000000` | neutral | Primary text or dark surface |
| Text Secondary Dark | `#020618` | neutral | Primary text or dark surface |
| Text Detail | `#90a1b9` | neutral | Border, muted text, or supporting surface |
| Midnight Ink | `#0f172b` | neutral | Primary text or dark surface |
| Border Dark | `#1d293d` | neutral | Primary text or dark surface |
| Deep Space Gradient | `#6c00f6` | brand | Action accent / signal color |
| Dark Overlay Gradient | `#501e48` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ghost-gray: #f1f5f9;
  --ref-outline-gray: #e5e7eb;
  --ref-text-primary: #000000;
  --ref-text-secondary-dark: #020618;
  --ref-text-detail: #90a1b9;
  --ref-midnight-ink: #0f172b;
  --ref-border-dark: #1d293d;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 14px, 15px, 16px, 18px, 20px, 32px, 52px, 1.10, 1.20, 1.25, 1.30, 1.40, 1.50, 1.71, 2.00; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `tags: 1.67772e+07px, cards: 20px, input: 0px, other: 24px, buttons: 8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for most content.
- **Ghost Gray** `#f1f5f9`: Subtly darker background for distinct sections or elements that require slight differentiation from the main canvas.
- **Midnight Ink** `#0f172b`: Deep rich background for high-contrast sections, brand blocks, or areas requiring a sense of depth and focus.

## Component cues
- **Primary Action Button**: Main call-to-action button, often with a gradient fill.
- **Ghost Button (Dark)**: Secondary action or navigation with subtle interactive cue.
- **Ghost Button (Light Text)**: Secondary action or navigation on dark backgrounds.
- **Pill Ghost Button**: Tertiary action or navigational button with pill shape for less emphasis.
- **Content Card**: Container for features, solutions, or informational blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
