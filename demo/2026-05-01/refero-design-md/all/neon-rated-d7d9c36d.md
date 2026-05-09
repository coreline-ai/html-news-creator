# NEON Rated - Refero Design MD

- Source: https://styles.refero.design/style/d7d9c36d-fec9-4218-9e17-3d129dfb2dee
- Original site: https://neonrated.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cinematic Contrast, Dark Drama

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Screen | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Off-White Screen | `#f3f3f3` | neutral | Page background or card surface |
| Ghost Gray | `#e5e7eb` | neutral | Page background or card surface |
| Subtle Gray | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Rebel Red | `#821e1e` | brand | Action accent / signal color |
| Luminous Blue | `#9dc1fb` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-screen: #000000;
  --ref-canvas-white: #ffffff;
  --ref-off-white-screen: #f3f3f3;
  --ref-ghost-gray: #e5e7eb;
  --ref-subtle-gray: #cccccc;
  --ref-rebel-red: #821e1e;
  --ref-luminous-blue: #9dc1fb;
}
```

## Typography direction
- **Flatspot**: 400, 500, 700, 9px, 10px, 12px, 14px, 16px, 1.00, 1.07, 1.17, 1.20, 1.40, 1.50; substitute `Montserrat`.
- **Girott**: 400, 700, 36px, 41px, 42px, 160px, 0.80, 0.90; substitute `Oswald`.

## Spacing / shape
- Section Gap: `140px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 8px, badges: 80px, buttons: 4px, default: 4px, circular: 100px`

## Surface cues
- **Midnight Screen** `#000000`: Primary page background, setting a dark, cinematic tone.
- **Canvas White** `#ffffff`: Alternative high-contrast page background for certain sections, or as primary foreground on dark backgrounds.
- **Off-White Screen** `#f3f3f3`: Card background on light canvases, providing a subtle differentiation.
- **Translucent Dark** `#ffffff14`: Card background for overlays or content on top of large visuals, giving a frosted appearance.

## Component cues
- **Ghost Bordered Button**: Default interactive element, often for secondary actions.
- **Transparent Accent Button**: Tertiary calls to action or embedded controls.
- **Dark Filled Accent Button**: Branded button for specific actions, contrasting against light backgrounds.
- **Content Card - Light**: Displaying film posters or brief informational blocks on light backgrounds.
- **Content Card - Dark Translucent**: Displaying content over visual media, such as hero images.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
