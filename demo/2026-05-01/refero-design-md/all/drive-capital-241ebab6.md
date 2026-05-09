# Drive Capital - Refero Design MD

- Source: https://styles.refero.design/style/241ebab6-1f3a-4637-8754-4f6b164ea090
- Original site: https://www.thesummerdrive.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type-driven retro blueprint

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment | `#fff8f1` | neutral | Page background or card surface |
| Steel Blue | `#e2e8f0` | neutral | Action accent / signal color |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Drive Blue | `#006eff` | brand | Action accent / signal color |

```css
:root {
  --ref-parchment: #fff8f1;
  --ref-steel-blue: #e2e8f0;
  --ref-midnight-ink: #000000;
  --ref-drive-blue: #006eff;
}
```

## Typography direction
- **Founders Grotesk**: 300, 400, 16px, 18px, 21px, 28px, 38px, 0.95, 1.00, 1.20, 1.25, 1.50; substitute `Inter`.
- **Editorial New**: 100, 300, 62px, 77px, 120px, 0.95, 1.00; substitute `Lora`.

## Spacing / shape
- Section Gap: `29px`
- Card Padding: `14px`
- Element Gap: `20px`
- Radius: `buttons: 60.0048px`

## Component cues
- **Outline Button - Tickets**: Primary interactive element for calls to action.
- **Section Divider**: Visual separation between content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
