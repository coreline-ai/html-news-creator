# teenage engineering - Refero Design MD

- Source: https://styles.refero.design/style/aecf9dda-5cba-4dc7-9e73-59b65d895cdf
- Original site: https://teenage.engineering
- Theme: `light`
- Industry: `other`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
engineered precision against industrial gray

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#f6f8f7` | neutral | Page background or card surface |
| Graphite | `#0f0e12` | neutral | Primary text or dark surface |
| Ink | `#000000` | neutral | Primary text or dark surface |
| Steel | `#e5e5e5` | neutral | Page background or card surface |
| Smoke | `#b2b2b2` | neutral | Border, muted text, or supporting surface |
| Electric Blue | `#0071bb` | accent | Action accent / signal color |
| Verdant Accent | `#006837` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas: #f6f8f7;
  --ref-graphite: #0f0e12;
  --ref-ink: #000000;
  --ref-steel: #e5e5e5;
  --ref-smoke: #b2b2b2;
  --ref-electric-blue: #0071bb;
  --ref-verdant-accent: #006837;
}
```

## Typography direction
- **te-20**: 100, 300, 13px, 19px, 24px, 26px, 1.11, 1.15, 1.50; substitute `Inter`.
- **te-40**: 300, 40px, 1.11; substitute `Inter`.

## Spacing / shape
- Section Gap: `66px`
- Card Padding: `22px`
- Element Gap: `15px`
- Radius: `default: 0px`

## Surface cues
- **Canvas** `#f6f8f7`: Primary page background, light canvases for product display.
- **Graphite** `#0f0e12`: Secondary background for navigation, footers, or sections intended to recede or provide contrast for lighter elements.
- **Ink** `#000000`: High-contrast background for specific elements or headers within darker sections, providing maximum textual legibility against lighter content.

## Component cues
- **Primary Navigation Link**: Navigation element
- **Product Grid Item**: Product display
- **Footer Link**: Utility link
- **Promotional Banner (Top)**: Brand communication
- **Cookie Consent Banner**: Legal disclosure

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
