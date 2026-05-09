# Phantom Studios - Refero Design MD

- Source: https://styles.refero.design/style/1f0cc2ef-9de0-4cbb-909f-ca120ef6d0ae
- Original site: https://www.phantom.land
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black canvas, vivid pixel shimmer

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Slate Border | `#333333` | neutral | Primary text or dark surface |
| Muted Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Neon Green | `#1eff66` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-ghost-white: #ffffff;
  --ref-slate-border: #333333;
  --ref-muted-gray: #666666;
  --ref-neon-green: #1eff66;
}
```

## Typography direction
- **Helvetica Now**: 400, 500, 700, 16px, 18px, 22px, 24px, 56px, 0.93, 1.20; substitute `Arial, sans-serif`.
- **ballinger-mono**: 400, 11px, 1.10; substitute `Menlo, Monaco, monospace`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `body: 14px`

## Component cues
- **Outline Text Link**: Interactive text link
- **Monospace Data Label**: Small descriptive label
- **Primary Section Heading**: Main content division title
- **Subtle Content Divider**: Visual separator for content areas

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
