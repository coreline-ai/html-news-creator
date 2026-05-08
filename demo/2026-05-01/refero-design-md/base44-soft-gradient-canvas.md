# Base44 - Refero Design MD

- Source: https://styles.refero.design/style/e869e214-f672-4ac3-bfc2-bd25de7b003b
- Original site: https://base44.com
- Theme: `light`
- Recommended fit: **Visual board / presentation**

## North star
Softly Lit Gradient Canvas

## Why this fits html-news-creator
Useful for image-led demos, boardroom decks, and visual browsing of report sections.

## Apply to
- Visual Board / Focus Cards variants
- Boardroom deck slides
- Image evidence layouts

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Pearl | `#faf9f7` | neutral | Page backgrounds, subtle card surfaces |
| Snowdrift White | `#ffffff` | neutral | Observed in link borderColor, other backgroundColor, button borderColor. Extracted usage does not support a distinct pr. |
| Ink Black | `#000000` | neutral | Primary text, prominent headings, strong borders |
| Graphite Text | `#232529` | neutral | Secondary text, input placeholder text, subtle borders |
| Slate Gray | `#324158` | neutral | Dividers, subtle accent borders on cards |
| Stone Whisper | `#696f7b` | neutral | Muted body text, supportive captions, subtle input backgrounds |
| #e6e6e6 | `#e6e6e6` | neutral | Backgrounds for decorative elements and subtle section dividers |
| Ash Border | `#cfcfcf` | neutral | Default button borders, light input borders |

```css
:root {
  --ref-canvas-pearl: #faf9f7;
  --ref-snowdrift-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-graphite-text: #232529;
  --ref-slate-gray: #324158;
  --ref-stone-whisper: #696f7b;
  --ref-e6e6e6: #e6e6e6;
}
```

## Typography direction
- Primary: **Arial**; substitute `Arial`.
- Secondary/code: **wfont_343a2a_5b4cd32fc19d46e1b8c1b142abb27d39**; substitute `system-ui`.

## Spacing / shape
- Section gap: `45px`
- Card padding: `40px`
- Element gap: `10px`
- Radius: `{'cards': '7.42183px', 'small': '3px', 'buttons': '999px', 'default': '9.89577px', 'compact-buttons': '300px', 'decorative-large': '741.445px', 'prominent-elements': '13.8541px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
