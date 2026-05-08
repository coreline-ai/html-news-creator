# Visitors - Refero Design MD

- Source: https://styles.refero.design/style/e7876363-181a-44a9-9e5c-2255cf98aea5
- Original site: https://visitors.now
- Theme: `light`
- Recommended fit: **Clean SaaS webapp**

## North star
Analytical canvas vibrant spectrum

## Why this fits html-news-creator
Useful for the admin webapp and future subscriber UI where clarity and restrained polish are required.

## Apply to
- New report option flows
- Settings and policy screens
- Subscriber dashboard cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page backgrounds, card surfaces, ghost button backgrounds |
| Slate Ink | `#181925` | neutral | Primary text, prominent headings, strong borders |
| Medium Gray | `#666666` | neutral | Body text, secondary headings, default icon color |
| Muted Gray | `#999999` | neutral | Muted text, helper text, inactive navigation items, dividers |
| Light Gray | `#e8e8e8` | neutral | Subtle borders, table dividers, ghost button borders |
| Whisper Purple | `#dad9fc` | brand | Subtle highlights, decorative borders, background accents |
| Radiant Violet | `#918df6` | brand | Primary action backgrounds, interactive indicators, brand highlight color for icons and accent borders |
| Electric Blue | `#2c78fc` | accent | Violet accent for outlined action borders, linked labels, and lightweight interactive emphasis; Decorative background g. |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-slate-ink: #181925;
  --ref-medium-gray: #666666;
  --ref-muted-gray: #999999;
  --ref-light-gray: #e8e8e8;
  --ref-whisper-purple: #dad9fc;
  --ref-radiant-violet: #918df6;
}
```

## Typography direction
- Primary: **OpenRunde**; substitute `system-ui, sans-serif`.
- Secondary/code: **monospace**; substitute `monospace`.

## Spacing / shape
- Section gap: `64px`
- Card padding: `16px`
- Element gap: `16px`
- Radius: `{'pill': '9999px', 'cards': '16px', 'large': '24px', 'buttons': '1.67772e+07px', 'default': '8px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
