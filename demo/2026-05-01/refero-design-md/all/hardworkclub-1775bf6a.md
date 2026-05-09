# Hardworkclub - Refero Design MD

- Source: https://styles.refero.design/style/1775bf6a-afdd-48b1-8435-b92ec585c674
- Original site: https://www.hardworkclub.com
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Stage Black: content bathed in light, surrounded by deep, velvety darkness.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Violet Bloom | `#1200e3` | accent | Action accent / signal color |
| Slate Whisper | `#313130` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-ghost-white: #ffffff;
  --ref-violet-bloom: #1200e3;
  --ref-slate-whisper: #313130;
}
```

## Typography direction
- **Founders Grotesk**: 300, 500, 700, 16px, 18px, 22px, 31px, 0.78, 1.00, 1.10, 1.20, 1.21, 1.50, 1.67; substitute `Inter`.
- **Maligna**: 300, 500, 31px, 61px, 1.10, 1.20; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `pill: 1440px, buttons: 1440px, default: 8px`

## Surface cues
- **Canvas** `#000000`: The foundational background for all pages and sections.
- **Interactive Surface** `#1200e3`: Subtle background for specific interactive elements when they require a distinct, non-textual highlight.
- **Accent Surface** `#ffffff`: Used sparingly for inverted sections or to highlight full-bleed content, creating strong visual breaks.

## Component cues
- **Ghost Button**: Call to action button for secondary actions or navigation.
- **Pill Link**: Interactive elements that appear as text but have a distinct pill-shaped hover state or background.
- **Work Card**: Container for showcasing featured work items.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
