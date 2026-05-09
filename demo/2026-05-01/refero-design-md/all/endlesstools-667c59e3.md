# Endlesstools - Refero Design MD

- Source: https://styles.refero.design/style/667c59e3-aaba-46e8-a2b3-255254328b6e
- Original site: https://endlesstools.io
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Darkmode vibrant console

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#080808` | neutral | Primary text or dark surface |
| Stormy Night | `#1e1e1e` | neutral | Primary text or dark surface |
| Deep Shadow | `#373737` | neutral | Primary text or dark surface |
| Ash Gray | `#959595` | neutral | Border, muted text, or supporting surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Border | `#505050` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#1d9bf0` | accent | Action accent / signal color |
| Vibrant Gradient | `#b8ff45` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #080808;
  --ref-stormy-night: #1e1e1e;
  --ref-deep-shadow: #373737;
  --ref-ash-gray: #959595;
  --ref-cloud-white: #ffffff;
  --ref-charcoal-border: #505050;
  --ref-electric-blue: #1d9bf0;
  --ref-vibrant-gradient: #b8ff45;
}
```

## Typography direction
- **Inter**: 400, 500, 8px, 12px, 14px, 16px, 18px, 24px, 42px, 0.83, 1.08, 1.10, 1.11, 1.17, 1.25, 1.29, 1.50, 2.08, 2.19, 2.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `15px`
- Element Gap: `5px`
- Radius: `small: 7px, default: 10px`

## Component cues
- **Primary Filled Button**: Main call-to-action button, conveying primary interaction.
- **Secondary Filled Button**: Secondary action button, providing a less prominent, yet active, option.
- **Ghost Button**: Minimal interaction button, often used for navigation links or less critical actions.
- **Input Field**: Text input areas for forms.
- **Content Card**: Container for distinct content blocks, especially for visual assets or listings.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
