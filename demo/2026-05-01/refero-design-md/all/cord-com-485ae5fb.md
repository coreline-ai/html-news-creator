# cord.com - Refero Design MD

- Source: https://styles.refero.design/style/485ae5fb-8f25-4aa3-a4e4-1deb1590d7d6
- Original site: https://cord.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sky blueprint on frosted glass

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#0b3658` | brand | Action accent / signal color |
| Cloud Gray | `#dde7ee` | neutral | Page background or card surface |
| Oceanic Blue | `#4e9ad9` | accent | Action accent / signal color |
| Subtle Mist | `#e6f1fa` | neutral | Page background or card surface |
| Slate Text | `#486984` | neutral | Border, muted text, or supporting surface |
| Muted Stone | `#688dac` | neutral | Border, muted text, or supporting surface |
| Soft Ash | `#97b5ce` | neutral | Border, muted text, or supporting surface |
| Subtle Gray | `#c8d8e4` | neutral | Border, muted text, or supporting surface |
| Success Teal | `#42b3b1` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #0b3658;
  --ref-cloud-gray: #dde7ee;
  --ref-oceanic-blue: #4e9ad9;
  --ref-subtle-mist: #e6f1fa;
  --ref-slate-text: #486984;
  --ref-muted-stone: #688dac;
  --ref-soft-ash: #97b5ce;
}
```

## Typography direction
- **Figtree**: 400, 600, 700, 800, 10px, 14px, 16px, 18px, 20px, 22px, 24px, 32px, 48px, 100px, 1.00, 1.10, 1.20, 1.25, 1.30, 1.40, 1.43, 1.50, 2.00, 2.81; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `28px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `cards: 24px, badges: 5px, fields: 8px, avatars: 50%, buttons: 8px`

## Surface cues
- **Canvas Background** `#ffffff`: Dominant background for the entire page, providing a clean, light base.
- **Elevated Card Surface** `#ffffff`: Background for primary content cards and interactive modules, distinguished by subtle shadow.
- **Subtle Fill** `#e6f1fa`: Lightest background for interactive elements on hover, or for secondary content blocks requiring a minimal lift.
- **Ghost Button Background** `#c8d8e4`: Used for ghost buttons or indicators for options with lowest visual prominence.

## Component cues
- **Primary Filled Button**: Main call-to-action.
- **Outlined Accent Button**: Secondary action or navigation link.
- **Ghost Circular Action Button**: Icon-only action within components or headers.
- **Text Link Button**: Inline or minimal action.
- **Elevated Card**: Content container for features, job listings, or product info.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
