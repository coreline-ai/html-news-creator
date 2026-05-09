# ProtoPie - Refero Design MD

- Source: https://styles.refero.design/style/031302e5-3269-4735-ab56-d4c7d02edc01
- Original site: https://protopie.io
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Tech console, soft glow.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#181818` | neutral | Primary text or dark surface |
| Stone Gray | `#555555` | neutral | Border, muted text, or supporting surface |
| Pale Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Crystal Frost | `#e9e9e9` | neutral | Page background or card surface |
| Iris Bloom | `#8169ff` | brand | Action accent / signal color |
| Violet Signal | `#6d4ff0` | brand | Action accent / signal color |
| Lavender Haze | `#c9bfff` | accent | Action accent / signal color |
| Aqua Tint | `#3eb2b2` | accent | Action accent / signal color |
| Violet Fade | `#ab9eff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #181818;
  --ref-stone-gray: #555555;
  --ref-pale-gray: #999999;
  --ref-ghost-white: #ffffff;
  --ref-crystal-frost: #e9e9e9;
  --ref-iris-bloom: #8169ff;
  --ref-violet-signal: #6d4ff0;
  --ref-lavender-haze: #c9bfff;
}
```

## Typography direction
- **Gilroy**: 400, 700, 16px, 18px, 20px, 22px, 28px, 48px, 62px, 1.29, 1.30, 1.33, 1.43, 1.45, 1.50, 1.56, 1.60; substitute `Montserrat`.
- **Inter**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 24px, 1.30, 1.40, 1.43, 1.50, 1.56, 1.67; substitute `Inter`.
- **Palmer Lake Print**: 400, 32px, 0.80; substitute `Rubik`.

## Spacing / shape
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 16px, links: 12px, other: 8px, pills: 9999px, buttons: 4px`

## Component cues
- **Primary Filled Button**: Main call-to-action.
- **Secondary Soft Button**: Alternative call-to-action or secondary action.
- **Ghost Text Button**: Navigation or less prominent actions.
- **Pill Button**: Tags, categories, or filtering elements.
- **Header Navigation Link**: Main navigation items.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
