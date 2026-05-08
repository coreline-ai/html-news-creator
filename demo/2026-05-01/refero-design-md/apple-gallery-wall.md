# Apple - Refero Design MD

- Source: https://styles.refero.design/style/c9cabb96-32fa-4896-837a-f2497ce1c856
- Original site: https://www.apple.com/macbook-neo
- Theme: `light`
- Recommended fit: **Visual board / presentation**

## North star
Gallery wall at natural light - enormous type casts shadows on a white surface, color enters only as product.

## Why this fits html-news-creator
Useful for image-led demos, boardroom decks, and visual browsing of report sections.

## Apply to
- Visual Board / Focus Cards variants
- Boardroom deck slides
- Image evidence layouts

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#1d1d1f` | neutral | Primary text, headings, nav labels, icon fills - near-black with just enough warmth to avoid harshness on white |
| Graphite | `#707070` | neutral | Secondary body copy, captions, footnotes, muted nav items |
| Slate | `#474747` | neutral | Tertiary body text, supporting link text, secondary nav |
| Ash | `#333333` | neutral | Icon strokes, mid-weight body text, button labels in ghost state |
| Fog | `#f5f5f7` | neutral | Page canvas background, section divider bands, badge fills |
| Snow | `#ffffff` | neutral | Card surfaces, nav background, elevated container fills |
| Obsidian | `#000000` | neutral | Dark card variant, hero icon fills, maximum-contrast black card |
| Silver Mist | `#e8e8ed` | neutral | Frosted pill button background (country selector), input backgrounds |

```css
:root {
  --ref-ink: #1d1d1f;
  --ref-graphite: #707070;
  --ref-slate: #474747;
  --ref-ash: #333333;
  --ref-fog: #f5f5f7;
  --ref-snow: #ffffff;
  --ref-obsidian: #000000;
}
```

## Typography direction
- Primary: **SF Pro Display**; substitute `Inter, system-ui`.
- Secondary/code: **SF Pro Text**; substitute `Inter, system-ui`.

## Spacing / shape
- Section gap: `80-120px`
- Card padding: `28px`
- Element gap: `10px`
- Radius: `{'cards': '28px', 'buttons': '999px', 'navItems': '980px', 'pillButtons': '999px', 'featureLinks': '28px', 'smallButtons': '10px', 'roundedButtons': '36px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
