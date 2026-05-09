# Toggl Track - Refero Design MD

- Source: https://styles.refero.design/style/813be405-c2b9-41be-9864-7b53d66483dc
- Original site: https://toggl.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Orchid Bloom Productivity Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Plum | `#412a4c` | brand | Action accent / signal color |
| Regal Violet | `#2c1338` | brand | Action accent / signal color |
| Orchid Bloom | `#e57cd8` | accent | Action accent / signal color |
| Misty Mauve | `#564260` | neutral | Border, muted text, or supporting surface |
| Slate Echo | `#6b5a74` | neutral | Border, muted text, or supporting surface |
| Pebble Gray | `#817187` | neutral | Border, muted text, or supporting surface |
| Sunbeam Yellow | `#ffde91` | accent | Action accent / signal color |
| White Canvas | `#fefbfa` | neutral | Page background or card surface |
| Frost Haze | `#fcf1f8` | neutral | Page background or card surface |
| Lilac Mist | `#fdeae2` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-plum: #412a4c;
  --ref-regal-violet: #2c1338;
  --ref-orchid-bloom: #e57cd8;
  --ref-misty-mauve: #564260;
  --ref-slate-echo: #6b5a74;
  --ref-pebble-gray: #817187;
  --ref-sunbeam-yellow: #ffde91;
  --ref-white-canvas: #fefbfa;
}
```

## Typography direction
- **GT Haptik Medium**: 400, 700, 16px, 18px, 19px, 20px, 22px, 32px, 43px, 60px, 69px, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.50, 1.60.
- **GT Haptik Medium Rotalic**: 400, 43px, 60px, 69px, 1.10, 1.20, 1.25.
- **Inter**: 400, 500, 700, 800, 12px, 13px, 14px, 15px, 16px, 18px, 22px, 24px, 32px, 43px, 1.15, 1.25, 1.30, 1.35, 1.40, 1.50, 1.55, 1.60, 1.70; substitute `system-ui`.

## Spacing / shape
- Section Gap: `75px`
- Card Padding: `30px`
- Element Gap: `10px`
- Radius: `cards: 14px, buttons: 26px, default: 10px, roundButtons: 200px`

## Surface cues
- **White Canvas** `#fefbfa`: Dominant page background, providing a clean base.
- **Frost Haze** `#fcf1f8`: Secondary background for cards and slightly elevated content blocks, creating subtle segmentation.
- **Lilac Mist** `#fdeae2`: Tertiary background for more distinct content areas or components within Frost Haze surfaces.
- **Lavender Whisper** `#fae5f7`: Higher elevation surface for specific cards or modals, providing a stronger visual lift without shadows.

## Component cues
- **Primary Action Button**: Calls to action, emphasizing core user journeys.
- **Ghost Action Button**: Secondary actions that should not compete with the primary call to action.
- **Navigation Link Button**: Navigation items within the primary header, appearing as a ghost button.
- **Inline Text Link**: Navigational links embedded within body text or footer, designed to be understated.
- **Default Card**: Containers for features, info blocks, and grouped content.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
