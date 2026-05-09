# Design - Refero Design MD

- Source: https://styles.refero.design/style/bbfbe753-a417-43ec-9af7-ef6c08a5140d
- Original site: https://design.cash.app
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dark mode precision, neon punctuation

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Border | `#e5e7eb` | neutral | Page background or card surface |
| Subtle Gray | `#858585` | neutral | Border, muted text, or supporting surface |
| Hinting Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-ghost-border: #e5e7eb;
  --ref-subtle-gray: #858585;
  --ref-hinting-gray: #b3b3b3;
}
```

## Typography direction
- **CashSans**: 400, 500, 700, 10px, 12px, 16px, 86px, 117px, 122px, 1.00, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `0px`
- Element Gap: `12px`
- Radius: `cards: 0px, images: 15px, buttons: 0px`

## Component cues
- **Ghost Navigation Button**: Navigation items and secondary actions without visual hierarchy
- **Plain Card**: Container for content; appears as a content block within the page structure
- **Image with Rounded Corners**: Visual content container with minimal styling aside from radius

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
