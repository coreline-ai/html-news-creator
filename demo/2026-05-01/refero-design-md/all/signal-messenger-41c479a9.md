# Signal Messenger - Refero Design MD

- Source: https://styles.refero.design/style/41c479a9-7b41-445b-9ea7-c7a6331828f0
- Original site: https://signal.org
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
open sky, clear communication

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud Cover | `#ffffff` | neutral | Page background or card surface |
| Sky Dust | `#f6f6f6` | neutral | Page background or card surface |
| Stone Whisper | `#e9e9e9` | neutral | Page background or card surface |
| Signal Blue | `#9dbbf8` | brand | Action accent / signal color |
| Ocean Deep | `#2c6bed` | accent | Action accent / signal color |
| Night Sky | `#1b1b1b` | neutral | Primary text or dark surface |
| Deep Space | `#404654` | neutral | Border, muted text, or supporting surface |
| Slate Shadow | `#3c3744` | neutral | Primary text or dark surface |
| Link Blue | `#2942ff` | accent | Action accent / signal color |
| Subtle Mist | `#a5cad5` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-cloud-cover: #ffffff;
  --ref-sky-dust: #f6f6f6;
  --ref-stone-whisper: #e9e9e9;
  --ref-signal-blue: #9dbbf8;
  --ref-ocean-deep: #2c6bed;
  --ref-night-sky: #1b1b1b;
  --ref-deep-space: #404654;
  --ref-slate-shadow: #3c3744;
}
```

## Typography direction
- **Inter**: 400, 600, 800, 16px, 20px, 28px, 40px, 60px, 1.07, 1.10, 1.14, 1.38, 1.40, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `30px`
- Element Gap: `12px`
- Page Max Width: `1344px`
- Radius: `cards: 16px, images: 16px, buttons: 8px`

## Component cues
- **Get Signal CTA Button Group**: Reference component style.
- **Share Without Insecurity Feature Block**: Reference component style.
- **Donate to Signal Card**: Reference component style.
- **Primary Call-to-Action Button**: Primary interactive element for key actions
- **Navigation Link Button**: Secondary action in header navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
