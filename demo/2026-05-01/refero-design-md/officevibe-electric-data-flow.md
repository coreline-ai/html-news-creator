# Officevibe - Refero Design MD

- Source: https://styles.refero.design/style/ced1c98f-d489-48f7-a01f-1fa59a07b706
- Original site: https://officevibe.com
- Theme: `light`
- Recommended fit: **Data dashboard / source ledger**

## North star
Electric Data Flow; a structured, approachable canvas where sharp insights meet soft edges.

## Why this fits html-news-creator
Useful for evidence-heavy screens: source tables, confidence labels, cluster metrics, and verification states.

## Apply to
- Source evidence tables
- Cluster scoring dashboards
- Admin metrics and QA panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Boardroom Navy | `#0c1754` | brand | Primary text, prominent headings, badge text, footer background - establishes a serious, trustworthy brand presence. |
| Brand Electric | `#2545ff` | brand | Primary call-to-action buttons, active navigation indicators, key interactive links - provides a vibrant, unmistakable. |
| Lilac Accent | `#d9d4ff` | accent | Subtle background accents, decorative elements - a muted counterpoint to Brand Electric, adding depth without visual no. |
| Feedback Yellow | `#ffc13a` | accent | Accents, potentially informational highlights or status indicators - a warm, vivid pop of color. |
| Soft Off-White | `#f9f8f6` | neutral | Page backgrounds, card surfaces, form inputs - the dominant background neutral, providing a soft, canvas-like base. |
| Pure White | `#ffffff` | neutral | Focal backgrounds, cards, button text on Brand Electric - used for highlighted foreground elements. |
| Pitch Black | `#171417` | neutral | Dominant text color for body, links, some headings - provides high contrast against light backgrounds. |
| Medium Gray | `#222222` | neutral | Secondary text, navigation items, ghost button text - a softer dark alternative for less prominent text. |

```css
:root {
  --ref-boardroom-navy: #0c1754;
  --ref-brand-electric: #2545ff;
  --ref-lilac-accent: #d9d4ff;
  --ref-feedback-yellow: #ffc13a;
  --ref-soft-off-white: #f9f8f6;
  --ref-pure-white: #ffffff;
  --ref-pitch-black: #171417;
}
```

## Typography direction
- Primary: **Inter**; substitute `system-ui, sans-serif`.
- Secondary/code: **Abcfavoritvariable**; substitute `Arial, sans-serif`.

## Spacing / shape
- Section gap: `64px`
- Card padding: ``
- Element gap: `8px`
- Radius: `{'cards': '16px', 'badges': '16px', 'inputs': '0px', 'buttons': '100px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
