# Hashnode - Refero Design MD

- Source: https://styles.refero.design/style/6a8bf4c2-8cf2-463a-bcb9-36c15ea177c2
- Original site: https://hashnode.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble. Light, precise, and structured, guiding builders through their thoughts.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#f9fafb` | neutral | Page background or card surface |
| Storm Gray | `#f4f5f7` | neutral | Page background or card surface |
| Stone Dust | `#e6e8eb` | neutral | Page background or card surface |
| Charcoal Black | `#16191c` | neutral | Primary text or dark surface |
| Carbon Slate | `#1c2024` | neutral | Primary text or dark surface |
| Ash Mist | `#7b8187` | neutral | Border, muted text, or supporting surface |
| Border Silver | `#d1d4d9` | neutral | Border, muted text, or supporting surface |
| Electric Indigo | `#1d52de` | brand | Action accent / signal color |
| Success Green | `#009966` | semantic | Action accent / signal color |
| Vivid Green | `#00bc7d` | semantic | Action accent / signal color |

```css
:root {
  --ref-cloud-white: #f9fafb;
  --ref-storm-gray: #f4f5f7;
  --ref-stone-dust: #e6e8eb;
  --ref-charcoal-black: #16191c;
  --ref-carbon-slate: #1c2024;
  --ref-ash-mist: #7b8187;
  --ref-border-silver: #d1d4d9;
  --ref-electric-indigo: #1d52de;
}
```

## Typography direction
- **suisseIntl**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 30px, 1.00, 1.33, 1.38, 1.43, 1.50, 1.56, 1.63; substitute `Inter`.
- **Font Awesome 7 Jelly**: 400, 900, 14px, 16px, 18px, 20px, 1.00; substitute `Font Awesome 6 Free`.
- **Font Awesome 7 Pro**: 400, 900, 12px, 14px, 18px, 1.00; substitute `Font Awesome 6 Pro`.

## Spacing / shape
- Section Gap: `48px`
- Page Max Width: `1176px`
- Radius: `tags: 1.67772e+07px, cards: 10px-14px, buttons: 10px, default: 10px`

## Component cues
- **Article Card — New & Popular**: Reference component style.
- **What's New Notification Card**: Reference component style.
- **Live Stats Bar + CTA Button Group**: Reference component style.
- **Primary Button**: Main call to action
- **Ghost Button**: Secondary action or link-like button

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
