# FRANKY'S - Refero Design MD

- Source: https://styles.refero.design/style/7c84da5d-b7a0-436f-bfaa-68d0a14f8e86
- Original site: https://frankys-hats.com
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Retro Pixelated Arcade

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Screen | `#000000` | neutral | Primary text or dark surface |
| Paper Canvas | `#f3e5df` | neutral | Page background or card surface |
| Off-White Border | `#e5e7eb` | neutral | Page background or card surface |
| Subtle Charcoal | `#333333` | neutral | Primary text or dark surface |
| Ghostly Gray | `#737373` | neutral | Border, muted text, or supporting surface |
| Marigold Gold | `#faa21f` | brand | Action accent / signal color |
| Action Green | `#128e44` | accent | Action accent / signal color |
| Midnight Gradient Blue | `#2b4893` | accent | Action accent / signal color |
| Sunset Gradient Orange | `#cf4308` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-screen: #000000;
  --ref-paper-canvas: #f3e5df;
  --ref-off-white-border: #e5e7eb;
  --ref-subtle-charcoal: #333333;
  --ref-ghostly-gray: #737373;
  --ref-marigold-gold: #faa21f;
  --ref-action-green: #128e44;
  --ref-midnight-gradient-blue: #2b4893;
}
```

## Typography direction
- **Arcade**: 400, 700, 10px, 14px, 16px, 18px, 1.25, 1.43, 1.50, 1.56; substitute `Press Start 2P, IBM Plex Mono`.

## Spacing / shape
- Section Gap: `44px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `pill: 9999px, cards: 12px, buttons: 6px`

## Surface cues
- **Screen Background** `#000000`: The primary background for the entire application, simulating a dark digital screen.
- **Base Surface** `#333333`: Used for slightly elevated panels or dividers, providing a subtle layer above the main background.
- **Paper Canvas Card** `#f3e5df`: The main background for content cards and prominent UI elements, creating a visually distinct, aged-paper effect.

## Component cues
- **Ghost Button Thin Border**: Secondary action control
- **Ghost Button Subtle Border**: Tertiary action control
- **Ghost Button Rounded Subtle Border**: Tertiary action control with soft corners
- **Pill Button Left Rounded**: Segmented control left segment
- **Primary Action Button**: Main call to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
