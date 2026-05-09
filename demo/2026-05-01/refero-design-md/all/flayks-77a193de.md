# Flayks - Refero Design MD

- Source: https://styles.refero.design/style/77a193de-2472-4637-802f-d930ec61c180
- Original site: https://flayks.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Overlapping typographic playground

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Forest | `#00381c` | brand | Action accent / signal color |
| Coral Punch | `#ff8370` | brand | Action accent / signal color |
| Lavender Haze | `#d1adff` | accent | Action accent / signal color |
| Vanilla Beam | `#ffe0ce` | accent | Action accent / signal color |
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Grey | `#272221` | neutral | Primary text or dark surface |
| Slate Surface | `#2c2f34` | neutral | Primary text or dark surface |
| Soft Spruce | `#546f57` | neutral | Border, muted text, or supporting surface |
| Ink Blue | `#002a3b` | accent | Action accent / signal color |
| Indigo Abyss | `#2d0458` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-forest: #00381c;
  --ref-coral-punch: #ff8370;
  --ref-lavender-haze: #d1adff;
  --ref-vanilla-beam: #ffe0ce;
  --ref-void-black: #000000;
  --ref-charcoal-grey: #272221;
  --ref-slate-surface: #2c2f34;
  --ref-soft-spruce: #546f57;
}
```

## Typography direction
- **Nohemi**: 400, 600, 14px, 18px, 0.85, 1.10, 1.20, 1.35; substitute `Montserrat`.
- **Mango Grotesque**: 500, 700, 32px, 40px, 48px, 88px, 94px, 97px, 144px, 256px, 518px, 0.80, 0.85, 1.00, 1.20; substitute `Anton`.
- **Arial**: 400, 13px, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `29px`
- Card Padding: `16px`
- Element Gap: `4px`
- Page Max Width: `1800px`
- Radius: `cards: 6px, buttons: 900px, general: 6px, largeElements: 10px`

## Surface cues
- **Void Black Canvas** `#000000`: Base page background, providing the deepest dark contrast.
- **Charcoal Grey Surface** `#272221`: Secondary page and section backgrounds, offering a slightly lighter dark tone.
- **Slate Surface Card** `#2c2f34`: Primary card and content block backgrounds, for grouping information above the base.

## Component cues
- **Ghost Text Button**: Interactive element for navigation and actions within content.
- **Outlined Accent Button**: Secondary action or navigational links where visual hierarchy needs to be present but not dominant.
- **Standard Card**: Group related content, such as project entries or information blocks.
- **Elevated Card**: Highlight key content or projects with a subtle sense of depth.
- **Dark Accent Card**: Visually distinct content blocks, often used for project showcases with specific visual themes.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
