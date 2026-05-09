# Limitless - Refero Design MD

- Source: https://styles.refero.design/style/626ae2de-c402-4805-b859-2c6adca41022
- Original site: https://limitless.ai
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble. The visual identity relies on precise lines, muted tones, and selective accents to convey controlled innovation.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Page Graphite | `#0f172a` | neutral | Primary text or dark surface |
| Body Slate | `#475569` | neutral | Border, muted text, or supporting surface |
| Subtle Gray | `#334155` | neutral | Primary text or dark surface |
| Link Ash | `#64748b` | neutral | Border, muted text, or supporting surface |
| Violet Signal | `#8a53e1` | brand | Action accent / signal color |
| Porcelain White | `#e5e7eb` | neutral | Page background or card surface |
| Snowdrift | `#f2f3f5` | neutral | Page background or card surface |
| Divider Silver | `#d1d5db` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-page-graphite: #0f172a;
  --ref-body-slate: #475569;
  --ref-subtle-gray: #334155;
  --ref-link-ash: #64748b;
  --ref-violet-signal: #8a53e1;
  --ref-porcelain-white: #e5e7eb;
  --ref-snowdrift: #f2f3f5;
  --ref-divider-silver: #d1d5db;
}
```

## Typography direction
- **Greycliff**: 300, 400, 500, 600, 700, 14px, 16px, 18px, 30px, 36px, 60px, 1.00, 1.11, 1.20, 1.43, 1.50, 1.56, 1.63; substitute `Inter`.

## Spacing / shape
- Section Gap: `48-64px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 16px, buttons: 9999px, default: 8px`

## Component cues
- **Announcement Hero Heading**: Reference component style.
- **CEO Message Content Card**: Reference component style.
- **Navigation Link Group + Sign In Button**: Reference component style.
- **Navigation Link**: Primary navigation items in the header.
- **Pill Ghost Button**: Subtle, interactive elements and secondary actions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
