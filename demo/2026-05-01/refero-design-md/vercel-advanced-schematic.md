# Vercel - Refero Design MD

- Source: https://styles.refero.design/style/f24daf3a-d43f-4dec-85a9-8ac1d5148a03
- Original site: https://vercel.com
- Theme: `light`
- Recommended fit: **Admin operations / developer tooling**

## North star
Advanced schematic on white canvas - every element precisely placed, every line deliberate.

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud Canvas | `#fafafa` | neutral | Page backgrounds, elevated surfaces like cards, modal backgrounds - the foundational white that ensures contrast. |
| Storm Gray Wash | `#f0fbff` | neutral | Subtle background for UI elements, hover states, or secondary container fill, providing a soft lift from the main canva. |
| Text Primary | `#171717` | neutral | Primary text, prominent headings, solid button fills for main actions - the dominant dark shade on light backgrounds. |
| Text Secondary | `#4d4d4d` | neutral | Secondary text, descriptive paragraphs, helper text, and subtle icon fills; a softer contrast than Text Primary. |
| Graphite Accent | `#000000` | neutral | Observed in nav fill, icon fill, other stroke. Extracted usage does not support a distinct primary control color. |
| Border Light | `#ebebeb` | neutral | Observed in other borderColor, nav borderColor, card borderColor. Extracted usage does not support a distinct primary c. |
| Border Neutral | `#666666` | neutral | Observed in nav borderColor, nav color, nav fill. Extracted usage does not support a distinct primary control color. |
| Text Muted | `#7d7d7d` | neutral | Less prominent text, captions, and disabled states; provides a low contrast for tertiary information. |

```css
:root {
  --ref-cloud-canvas: #fafafa;
  --ref-storm-gray-wash: #f0fbff;
  --ref-text-primary: #171717;
  --ref-text-secondary: #4d4d4d;
  --ref-graphite-accent: #000000;
  --ref-border-light: #ebebeb;
  --ref-border-neutral: #666666;
}
```

## Typography direction
- Primary: **Geist**; substitute `Inter`.
- Secondary/code: **Geist Mono**; substitute `SFMono-Regular`.

## Spacing / shape
- Section gap: `48px`
- Card padding: `12px`
- Element gap: `12px`
- Radius: `{'large': '12px', 'pills': '100px', 'buttons': '9999px', 'default': '6px', 'minimal': '6px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
