# Bumble - Refero Design MD

- Source: https://styles.refero.design/style/f32595cf-478e-4ccd-8722-0daffa693d76
- Original site: https://bumble.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
sunny confident playground

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Bumble Yellow | `#ffdb5b` | brand | Action accent / signal color |
| Amber Glow | `#fff386` | brand | Action accent / signal color |
| Charcoal Ink | `#202020` | neutral | Primary text or dark surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Deep Gray | `#3b3b3b` | neutral | Primary text or dark surface |
| Cloud Gray | `#f3f3f3` | neutral | Page background or card surface |
| Muted Stone | `#343333` | neutral | Primary text or dark surface |
| Subtle Slate | `#575656` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-bumble-yellow: #ffdb5b;
  --ref-amber-glow: #fff386;
  --ref-charcoal-ink: #202020;
  --ref-arctic-white: #ffffff;
  --ref-deep-gray: #3b3b3b;
  --ref-cloud-gray: #f3f3f3;
  --ref-muted-stone: #343333;
  --ref-subtle-slate: #575656;
}
```

## Typography direction
- **BumbleSans**: 400, 500, 600, 700, 15px, 16px, 17px, 18px, 20px, 24px, 32px, 34px, 40px, 49px, 68px, 1.00, 1.10, 1.12, 1.18, 1.20, 1.25, 1.29, 1.33, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `40px`
- Element Gap: `24px`
- Page Max Width: `224px`
- Radius: `cards: 16px, badges: 1000px, buttons: 16px, navigation: 16px`

## Surface cues
- **Page Canvas** `#ffdb5b`: The foundational background color, used for large sections and the overall page, defining the brand's vibrant presence.
- **Section Background** `#ffffff`: Clean, open backgrounds for content blocks and distinct sections within the page.
- **Subtle Card Surface** `#f3f3f3`: A very light gray surface for cards, offering a slight visual differentiation from the white page background.
- **Accent Card Surface** `#fff386`: A lighter yellow background for cards, providing a brighter accent within sections.

## Component cues
- **Primary Filled Button**: Call to action.
- **Ghost Navigation Button**: Secondary navigation or interactive text.
- **Subtle Background Button**: Interactive elements with a softer visual presence.
- **Yellow Feature Card**: Highlights key features or content areas.
- **White Information Card**: Displays content on a neutral background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
