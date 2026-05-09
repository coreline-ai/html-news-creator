# LottieFiles - Refero Design MD

- Source: https://styles.refero.design/style/a80507cb-afda-46dd-a2b9-ba91f3a78e78
- Original site: https://lottiefiles.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Playful Precision amidst Animation; a digital canvas vibrant with motion, grounded by clear, spacious layouts.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Ash White | `#fafafa` | neutral | Page background or card surface |
| Slate Gray | `#e4e4e7` | neutral | Page background or card surface |
| Dark Graphite | `#f4f4f5` | neutral | Page background or card surface |
| Carbon Black | `#09090b` | neutral | Primary text or dark surface |
| Charcoal Black | `#18181b` | neutral | Primary text or dark surface |
| Steel Gray | `#71717b` | neutral | Border, muted text, or supporting surface |
| Cadet Gray | `#9f9fa9` | neutral | Border, muted text, or supporting surface |
| Lottie Teal | `#019d91` | brand | Action accent / signal color |
| Vivid Aqua | `#00ddb3` | brand | Action accent / signal color |

```css
:root {
  --ref-cloud-white: #ffffff;
  --ref-ash-white: #fafafa;
  --ref-slate-gray: #e4e4e7;
  --ref-dark-graphite: #f4f4f5;
  --ref-carbon-black: #09090b;
  --ref-charcoal-black: #18181b;
  --ref-steel-gray: #71717b;
  --ref-cadet-gray: #9f9fa9;
}
```

## Typography direction
- **DM Sans**: 400, 500, 600, 14px, 16px, 18px, 20px, 24px, 32px, 48px, 64px, 96px, 1.04-1.56; substitute `DM Sans (Google Fonts)`.
- **Inter**: 400, 500, 600, 10px, 12px, 14px, 16px, 18px, 24px, 32px, 1.10-1.71; substitute `Inter (Google Fonts)`.

## Spacing / shape
- Section Gap: `40-80px`
- Card Padding: `24-32px`
- Element Gap: `8-24px`
- Page Max Width: `1200px`
- Radius: `cards: 16px, forms: 8px, buttons: 12px, thumbnails: 24px`

## Component cues
- **Feature Highlight Badges**: Reference component style.
- **Testimonial Card**: Reference component style.
- **CTA Button Group with Search**: Reference component style.
- **Primary Lottie Teal Button**: Primary call to action
- **Ghost Navigation Button (Active)**: Navigation links and secondary actions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
