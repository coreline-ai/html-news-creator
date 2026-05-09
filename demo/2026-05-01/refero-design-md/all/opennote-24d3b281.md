# Opennote - Refero Design MD

- Source: https://styles.refero.design/style/24d3b281-04a6-4cc7-8a74-634b08472291
- Original site: https://www.opennote.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
ink on parchment

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment | `#fffdf8` | neutral | Page background or card surface |
| Ink Black | `#0a0a0a` | neutral | Primary text or dark surface |
| Slate Gray | `#474747` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#8c8c8c` | neutral | Border, muted text, or supporting surface |
| Whisper Border | `#e5e5e5` | neutral | Page background or card surface |
| Ghost Border | `#d1d1d1` | neutral | Border, muted text, or supporting surface |
| Burnt Umber | `#512906` | brand | Action accent / signal color |
| Blue Violet | `#242d64` | accent | Action accent / signal color |
| Forest Green | `#0c3b1a` | accent | Action accent / signal color |
| Crimson Blush | `#5e0831` | accent | Action accent / signal color |

```css
:root {
  --ref-parchment: #fffdf8;
  --ref-ink-black: #0a0a0a;
  --ref-slate-gray: #474747;
  --ref-ash-gray: #8c8c8c;
  --ref-whisper-border: #e5e5e5;
  --ref-ghost-border: #d1d1d1;
  --ref-burnt-umber: #512906;
  --ref-blue-violet: #242d64;
}
```

## Typography direction
- **IowanOld**: 400, 500, 16px, 20px, 32px, 42px, 48px, 1.08, 1.10, 1.12, 1.20, 1.50; substitute `Iowan Old Style`.
- **SuisseIntl**: 400, 14px, 16px, 1.00, 1.43, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `40-80px`
- Card Padding: `16px`
- Element Gap: `12px`
- Page Max Width: `1200px`
- Radius: `cards: 10px, buttons: 10px, general: 10px`

## Surface cues
- **Parchment Base** `#fffdf8`: Primary page background, expansive canvas for content.
- **Subtle Card** `#f9f9f9`: Slightly elevated card surfaces, subtly distinguished from the base.
- **Accent Block** `#fef5de`: Backgrounds for highlighted content sections or decorative areas, introducing a warm tint.

## Component cues
- **Primary Filled Button**: Main call to action, drawing immediate attention.
- **Secondary Outlined Button**: Alternative actions, less emphasized than the primary.
- **Ghost Navigation Link**: Main navigation items, in-text links.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
