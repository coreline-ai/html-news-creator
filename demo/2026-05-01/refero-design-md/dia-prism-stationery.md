# Dia Browser - Refero Design MD

- Source: https://styles.refero.design/style/b458ca1a-70f0-4f85-b745-f879a4d08457
- Original site: https://diabrowser.com
- Theme: `light`
- Recommended fit: **Visual board / presentation**

## North star
Prism on white stationery - light refracts color from a nearly monochrome surface.

## Why this fits html-news-creator
Useful for image-led demos, boardroom decks, and visual browsing of report sections.

## Apply to
- Visual Board / Focus Cards variants
- Boardroom deck slides
- Image evidence layouts

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#000000` | neutral | Primary text, headings, nav links, borders, icon fills - the sole chromatic anchor in an otherwise gray system |
| Snow | `#ffffff` | neutral | Card backgrounds (at 90% opacity), base fills, overlay surfaces |
| Canvas | `#f8f8f8` | neutral | Page background (--background token), the overall canvas beneath frosted cards |
| Fog | `#efefef` | neutral | Header background, subtle section dividers |
| Pebble | `#d9d9d9` | neutral | Filled button backgrounds ("Download Dia") - neutral gray buttons avoid competing with content; a deliberate anti-CTA t. |
| Graphite | `#636363` | neutral | Body text, secondary copy, subheadings beneath display type |
| Slate | `#959595` | neutral | Tertiary text, nav labels, metadata captions |
| Steel | `#aeaeae` | neutral | Disabled states, carousel indicator dots, icon strokes |

```css
:root {
  --ref-ink-black: #000000;
  --ref-snow: #ffffff;
  --ref-canvas: #f8f8f8;
  --ref-fog: #efefef;
  --ref-pebble: #d9d9d9;
  --ref-graphite: #636363;
  --ref-slate: #959595;
}
```

## Typography direction
- Primary: **ABC Oracle**; substitute `GT Super Display (weight 300) or DM Sans (lighter weights) for structure; for c.`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: `80-120px`
- Card padding: `32px`
- Element gap: `15-20px`
- Radius: `{'cards': '30px', 'images': '10px', 'buttons': '30px', 'navItems': '16px', 'containers': '40px', 'pillButtons': '9999px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
