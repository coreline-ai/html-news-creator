# The Pop Manifesto - Refero Design MD

- Source: https://styles.refero.design/style/80913fb2-60ee-4d6c-b2c8-17600351096a
- Original site: https://thepopmanifesto.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
digital zine, high contrast

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Neon Pink | `#ff29f1` | brand | Action accent / signal color |
| Electric Blue | `#287aea` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-neon-pink: #ff29f1;
  --ref-electric-blue: #287aea;
}
```

## Typography direction
- **Roobert**: 400, 12px, 15px, 22px, 33px, 0.70, 1.20; substitute `Inter`.
- **Roobert Bold**: 400, 15px, 1.20; substitute `Inter Bold`.

## Spacing / shape
- Card Padding: `25px`
- Element Gap: `20px`
- Radius: `none: 0px`

## Surface cues
- **Electric Blue Canvas** `#287aea`: Base page background or primary content block background.
- **Neon Pink Surface** `#ff29f1`: Elevated content block background, providing strong visual distinction from the canvas.

## Component cues
- **Section Headline**: Main content headings for distinct page sections.
- **Navigation Link**: Top-level navigation items.
- **Image Card**: Displays photographic content with prominent captions.
- **Interactive Link Block**: Clickable blocks usually containing descriptive text.
- **Sub-Navigation Link**: Secondary navigation or category links.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
