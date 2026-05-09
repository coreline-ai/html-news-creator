# Say Briefly - Refero Design MD

- Source: https://styles.refero.design/style/8b91f4c9-74e5-4925-90a3-3dd31fd5725e
- Original site: https://saybriefly.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Olive Canvas, Highlighted Briefs, Warm Accents

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fcfaf5` | neutral | Page background or card surface |
| Deep Olive | `#1a3300` | brand | Action accent / signal color |
| Highlight Yellow | `#ffe95c` | accent | Action accent / signal color |
| Charcoal Black | `#000000` | neutral | Primary text or dark surface |
| Soft Teal | `#a8e5e5` | accent | Action accent / signal color |
| Muted Sage | `#d5f5c2` | accent | Action accent / signal color |
| Warm Orange | `#cb5521` | accent | Action accent / signal color |
| Pale Pink | `#f6d0ff` | accent | Action accent / signal color |
| Light Gray | `#f1f1f1` | neutral | Page background or card surface |
| Border Gray | `#b6b6b6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #fcfaf5;
  --ref-deep-olive: #1a3300;
  --ref-highlight-yellow: #ffe95c;
  --ref-charcoal-black: #000000;
  --ref-soft-teal: #a8e5e5;
  --ref-muted-sage: #d5f5c2;
  --ref-warm-orange: #cb5521;
  --ref-pale-pink: #f6d0ff;
}
```

## Typography direction
- **Bricolage Grotesque**: 800, 55px, 66px, 90px, 1.00, 1.15, 1.20; substitute `system-ui`.
- **Inter**: 300, 400, 500, 600, 700, 11px, 12px, 14px, 16px, 17px, 18px, 20px, 24px, 28px, 30px, 32px, 36px, 38px, 40px, 64px, 0.93, 1.03, 1.10, 1.20, 1.25, 1.30, 1.38, 1.40, 1.50, 1.56, 1.63; substitute `Arial`.
- **Roboto Mono**: 400, 12px, 15px, 16px, 1.00, 1.33, 1.38; substitute `monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1320px`
- Radius: `cards: 6px, buttons: 6px, navItems: 16px, highlightedElements: 9999px`

## Surface cues
- **Canvas White** `#fcfaf5`: Primary page background, foundation for all content.
- **Soft Accent Surfaces** `#d5f5c2`: Subtle background for specific sections or button groups, providing a slight visual break.
- **Highlighted Cards** `#ffe95c`: Prominent content blocks that demand attention, or functional cards.
- **Decorative Thematic Cards** `#a8e5e5`: Distinct content containers using alternate brand accent colors for visual variety.

## Component cues
- **Navigation Link**: Text link within the top navigation.
- **Primary Call-to-Action Button**: Main interactive element, driving user conversion.
- **Secondary Outlined Button**: Less prominent interactive actions.
- **Highlight Card**: Prominent information display, often with a subtle background color.
- **Decorative Card - Warm Orange**: visually distinct sections or feature highlights.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
