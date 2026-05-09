# Free Podcast Hosting - Refero Design MD

- Source: https://styles.refero.design/style/b409c050-ab0f-4cf0-a388-95fd7072cd6a
- Original site: https://www.buzzsprout.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Pine forest studio

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Shadow | `#214538` | brand | Action accent / signal color |
| Sunlit Yellow | `#faefc3` | brand | Action accent / signal color |
| Validation Green | `#208619` | accent | Action accent / signal color |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#e4e5e6` | neutral | Page background or card surface |
| Deep Graphite | `#151e1b` | neutral | Primary text or dark surface |
| Pale Sage | `#e5ede9` | neutral | Page background or card surface |
| Cloud Mist | `#f4f4f4` | neutral | Page background or card surface |
| Whisper Gray | `#4d4d4f` | neutral | Border, muted text, or supporting surface |
| Golden Gradient | `#fae78b` | accent | Action accent / signal color |

```css
:root {
  --ref-forest-shadow: #214538;
  --ref-sunlit-yellow: #faefc3;
  --ref-validation-green: #208619;
  --ref-canvas-white: #ffffff;
  --ref-ash-gray: #e4e5e6;
  --ref-deep-graphite: #151e1b;
  --ref-pale-sage: #e5ede9;
  --ref-cloud-mist: #f4f4f4;
}
```

## Typography direction
- **Graphik**: 400, 500, 600, 700, 10px, 12px, 14px, 15px, 16px, 18px, 20px, 24px, 25px, 30px, 35px, 48px, 50px, 60px, 1.00, 1.10, 1.20, 1.33, 1.40, 1.43, 1.50, 1.60, 1.80, 2.50; substitute `Inter`.
- **Girott**: 600, 168px, 1.00, 1.50; substitute `Oswald`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `24px`
- Element Gap: `10px`
- Radius: `tags: 9999px, cards: 12px, inputs: 8px, buttons: 6px`

## Surface cues
- **Canvas White** `#ffffff`: Default page background. Provides a clean, bright foundation.
- **Pale Sage** `#e5ede9`: Secondary background for cards and distinct sections, offering a subtle tonal shift without being distracting.
- **Sunlit Yellow** `#faefc3`: Highlight background for specific cards or content blocks, adding a touch of warmth and visual interest.

## Component cues
- **Primary Filled Button**: Main call to action
- **Secondary Filled Button**: Prominent action, slightly smaller than primary
- **Ghost Button (Minimal)**: Subtle actions or navigation items
- **Ghost Button (Tag)**: Categorization or filter tags
- **Product Feature Card**: Displaying product features with iconography

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
