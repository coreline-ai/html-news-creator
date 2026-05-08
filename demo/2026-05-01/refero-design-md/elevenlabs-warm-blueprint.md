# ElevenLabs - Refero Design MD

- Source: https://styles.refero.design/style/031056ff-7af1-46db-8daa-115f731c5d26
- Original site: https://elevenlabs.io
- Theme: `light`
- Recommended fit: **Editorial report / reading mode**

## North star
Architect's blueprint on warm vellum - Waldenburg weight-300 headlines at 48px with -0.02em tracking anchored against an eggshell ground, pure black pill buttons as the only punctuation.

## Why this fits html-news-creator
Useful for long-form AI report pages where hierarchy, trust, and reading comfort matter more than decoration.

## Apply to
- Article-style report body
- Executive brief / PDF direction
- Research and policy sections

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Eggshell | `#fdfcfc` | neutral | Page background and primary surface - the near-white warmth distinguishes this from pure #ffffff, landing type with ext. |
| Powder | `#f5f3f1` | neutral | Secondary surface, hover states, subtle section backgrounds |
| Chalk | `#e5e5e5` | neutral | All borders, dividers, card outlines, button outlines - the single border color used universally |
| Fog | `#b1b0b0` | neutral | Disabled states, placeholder elements, logo grid grayscale treatment |
| Gravel | `#777169` | neutral | Secondary body text, nav items, subheadings, captions - warm stone undertone separates it from a cold gray |
| Slate | `#a59f97` | neutral | Tertiary text, icon strokes, deemphasized labels |
| Cinder | `#57534` | neutral | Mid-tone text, secondary headings on light surfaces |
| Obsidian | `#000000` | neutral | Primary text, filled CTA buttons (background), logo mark - the absolute black against eggshell creates 20.5:1 contrast |

```css
:root {
  --ref-eggshell: #fdfcfc;
  --ref-powder: #f5f3f1;
  --ref-chalk: #e5e5e5;
  --ref-fog: #b1b0b0;
  --ref-gravel: #777169;
  --ref-slate: #a59f97;
  --ref-cinder: #57534;
}
```

## Typography direction
- Primary: **Waldenburg**; substitute `Cormorant Garamond 300, or Libre Baskerville 300`.
- Secondary/code: **WaldenburgFH**; substitute `Inter 700 with letter-spacing 0.7px`.

## Spacing / shape
- Section gap: `80-120px`
- Card padding: `16-24px`
- Element gap: `8-12px`
- Radius: `{'tags': '9999px', 'cards': '16px', 'badges': '12px', 'inputs': '4px', 'modals': '24px', 'panels': '20px', 'buttons': '9999px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
