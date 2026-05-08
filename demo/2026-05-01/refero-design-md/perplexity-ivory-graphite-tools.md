# Perplexity AI - Refero Design MD

- Source: https://styles.refero.design/style/81afaa5c-73ac-4ef4-9a99-296da325ea6c
- Original site: https://perplexity.ai
- Theme: `light`
- Recommended fit: **Clean SaaS webapp**

## North star
Ivory Desk, Graphite Tools - a pristine, brightly lit workspace filled with essential gray instruments.

## Why this fits html-news-creator
Useful for the admin webapp and future subscriber UI where clarity and restrained polish are required.

## Apply to
- New report option flows
- Settings and policy screens
- Subscriber dashboard cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#000000` | neutral | Primary text, interactive icons, active states - commands immediate attention against the subtle backgrounds. |
| Paper White | `#FFFFFF` | neutral | Main page background, pristine canvas for content. The brightest neutral. |
| Parchment | `#FAF8F5` | neutral | Interactive element backgrounds like search bars and buttons in inactive states, providing a soft contrast to the main. |
| Graphite | `#27251` | neutral | Secondary text, subtle backgrounds for elevated elements, and borders for input fields - registers as dark but softer t. |
| Faded Stone | `#92918B` | neutral | Placeholder text, subtle contextual information, providing low-contrast visual guiding. |
| Dusk Gray | `#72706B` | neutral | Tertiary text, inactive icons, divider lines - defines softer visual cues and non-critical information. |

```css
:root {
  --ref-inkwell: #000000;
  --ref-paper-white: #FFFFFF;
  --ref-parchment: #FAF8F5;
  --ref-graphite: #27251;
  --ref-faded-stone: #92918B;
  --ref-dusk-gray: #72706B;
}
```

## Typography direction
- Primary: **pplxSans**; substitute `Inter`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: `32px`
- Card padding: `12px`
- Element gap: `8px`
- Radius: `{'cards': '16px', 'inputs': '8px', 'buttons': '9999px', 'navigation': '8px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
