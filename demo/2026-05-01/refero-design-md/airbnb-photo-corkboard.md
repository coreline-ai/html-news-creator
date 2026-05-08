# Airbnb - Refero Design MD

- Source: https://styles.refero.design/style/c2325884-4391-4688-85cd-e143f5107517
- Original site: https://www.airbnb.com
- Theme: `light`
- Recommended fit: **Visual board / presentation**

## North star
Vacation photos pinned to a white corkboard - bright photography contained in rounded frames against a near-white surface, with a single coral pin holding everything together.

## Why this fits html-news-creator
Useful for image-led demos, boardroom decks, and visual browsing of report sections.

## Apply to
- Visual Board / Focus Cards variants
- Boardroom deck slides
- Image evidence layouts

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Rausch Coral | `#ff385c` | brand | Brand logo fill, active nav underline, search button icon background, carousel dot active state - the single chromatic. |
| Rausch Deep | `#e00b41` | brand | Hover state darkening of Rausch Coral on interactive brand elements |
| Carbon | `#222222` | neutral | Primary text, headings, borders, icon strokes - the dominant neutral forming almost all typographic content |
| Slate | `#6a6a6a` | neutral | Secondary text (metadata, subtext, secondary labels), secondary icon fill |
| Silver | `#c1c1c1` | neutral | Disabled button text and icon strokes, inactive carousel navigation arrows |
| Stone | `#b0b0b0` | neutral | Skeleton/loading placeholder backgrounds |
| Pebble | `#dddddd` | neutral | Card image placeholder backgrounds, tertiary borders, disabled borders |
| Mist | `#ebebeb` | neutral | Subtle dividers and secondary section borders |

```css
:root {
  --ref-rausch-coral: #ff385c;
  --ref-rausch-deep: #e00b41;
  --ref-carbon: #222222;
  --ref-slate: #6a6a6a;
  --ref-silver: #c1c1c1;
  --ref-stone: #b0b0b0;
  --ref-pebble: #dddddd;
}
```

## Typography direction
- Primary: **Airbnb Cereal VF**; substitute `Inter Variable`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: `48px`
- Card padding: `12px`
- Element gap: `8px`
- Radius: `{'cards': '20px', 'pills': '32px', 'badges': '4px', 'inputs': '14px', 'buttons': '8px', 'searchBar': '20px', 'iconButtons': '50%'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
