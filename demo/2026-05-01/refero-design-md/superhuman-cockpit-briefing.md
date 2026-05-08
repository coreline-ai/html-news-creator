# Superhuman - Refero Design MD

- Source: https://styles.refero.design/style/418b374a-be64-44f0-b17e-1d45308c7e62
- Original site: https://superhuman.com
- Theme: `mixed`
- Recommended fit: **Editorial report / reading mode**

## North star
Cinematic cockpit behind warm parchment - a productivity instrument panel where atmospheric photography meets structured cream-toned UI surfaces.

## Why this fits html-news-creator
Useful for long-form AI report pages where hierarchy, trust, and reading comfort matter more than decoration.

## Apply to
- Article-style report body
- Executive brief / PDF direction
- Research and policy sections

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment Canvas | `#f2f0eb` | neutral | Primary page background below the hero; the warm, slightly toasted off-white that distinguishes this from sterile white. |
| Ink | `#292827` | neutral | Primary text, borders, nav labels - near-black with a warm brown undertone instead of pure black |
| Bone | `#ffffff` | neutral | Card surfaces, hero text, button text on dark backgrounds |
| Fog | `#e3e3e2` | neutral | Subtle UI dividers, light button borders, tab backgrounds |
| Driftwood | `#dcd7d3` | neutral | Secondary dividers and section rule lines |
| Graphite | `#666666` | neutral | Secondary body text - feature descriptions and supporting copy beneath headings |
| Aubergine | `#421d24` | brand | Announcement banner background, footer background - deep muted red that brackets the page top and bottom |
| Aubergine Deep | `#4e242c` | brand | SVG icon fills and border accents within dark brand surfaces |

```css
:root {
  --ref-parchment-canvas: #f2f0eb;
  --ref-ink: #292827;
  --ref-bone: #ffffff;
  --ref-fog: #e3e3e2;
  --ref-driftwood: #dcd7d3;
  --ref-graphite: #666666;
  --ref-aubergine: #421d24;
}
```

## Typography direction
- Primary: **Super Sans VF**; substitute `Inter Variable or Neue Haas Grotesk`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: `64px`
- Card padding: `16px`
- Element gap: `8px`
- Radius: `{'cards': '16px', 'links': '12px', 'pills': '999px', 'buttons': '8px', 'cardsLarge': '24px', 'announcementBanner': '16px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
