# Beau - Refero Design MD

- Source: https://styles.refero.design/style/c73ba3d8-42fe-4d53-bec1-b6643949c582
- Original site: https://beau.to
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome precision, vibrant core

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Subtle Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Electric Gradient | `#ff8308` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-subtle-gray: #999999;
  --ref-whisper-gray: #666666;
  --ref-silver-mist: #b3b3b3;
  --ref-electric-gradient: #ff8308;
}
```

## Typography direction
- **Geist**: 400, 500, 14px, 17px, 20px, 28px, 33px, 40px, 56px, 1.10, 1.15, 1.20, 1.30, 1.40; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `24px`
- Element Gap: `24px`
- Page Max Width: `1428px`
- Radius: `cards: 6px, buttons: 200px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background and default surface for most content sections.
- **Dark Card** `#000000`: Alternative background for specific content blocks that require higher visual contrast or a 'dark mode' feel within the light theme.
- **White Card with Shadow** `#ffffff`: Elevated card surfaces, differentiated by a subtle shadow to indicate hierarchy and interactivity.
- **Silver Mist** `#b3b3b3`: Used for compact badges and certain decorative elements, providing a muted background.

## Component cues
- **Primary Action Button**: Main call to action button.
- **Ghost Action Button**: Secondary action button, or for navigation.
- **White Card**: Content container for features or information.
- **Dark Card**: Container for content in dark mode sections.
- **Compact Tag Badge**: Informational tags or status indicators.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
