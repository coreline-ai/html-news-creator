# Sequel - Refero Design MD

- Source: https://styles.refero.design/style/1bd3b2ba-9ad9-44ed-9130-03f9d94de821
- Original site: https://sequel.co
- Theme: `dark`
- Recommended fit: **Dark premium dashboard**

## North star
Black canvas, sharp typography

## Why this fits html-news-creator
Useful as a high-contrast alternative for operator and executive views.

## Apply to
- Dark dashboard shells
- Premium subscriber surfaces
- Status-heavy UI states

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Page backgrounds, primary dark surfaces, text on light elements. |
| Cloud Whisper | `#ffffff` | neutral | Primary text, critical UI elements, borders for ghost buttons - creating stark contrast against dark backgrounds. |
| Slate Dust | `#f5f5f0` | neutral | Primary background for solid buttons, providing a subtle off-white alternative to pure white for interactive elements. |
| Steel Gray | `#202020` | neutral | Secondary background for containers, slightly differentiated from the deepest black. |
| Mist Gray | `#c0c0c0` | neutral | Subtle text, less prominent borders, and icons. |
| Charcoal Tone | `#333333` | neutral | Badge backgrounds when slightly darker contrast is needed, secondary borders. |
| Ash Accent | `#999999` | neutral | Tertiary text, descriptive labels, less emphasized information. |
| Light Ash | `#cccccc` | neutral | Fine print, less important body copy. Similar to Ash Accent but slightly lighter. |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-cloud-whisper: #ffffff;
  --ref-slate-dust: #f5f5f0;
  --ref-steel-gray: #202020;
  --ref-mist-gray: #c0c0c0;
  --ref-charcoal-tone: #333333;
  --ref-ash-accent: #999999;
}
```

## Typography direction
- Primary: **VisueltPro**; substitute `system-ui, sans-serif`.
- Secondary/code: **Bradford**; substitute `serif`.

## Spacing / shape
- Section gap: `47-76px`
- Card padding: `0px`
- Element gap: `3-28px`
- Radius: `{'cards': '10px', 'badges': '9999px', 'buttons': '9999px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
