# cthdrl - Refero Design MD

- Source: https://styles.refero.design/style/565bfc50-3a19-4224-9a4c-125edaeb7bef
- Original site: https://cthdrl.co
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black canvas, stark typography

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Ghost Sand | `#e7ded1` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-ghost-sand: #e7ded1;
}
```

## Typography direction
- **NB Akademie**: 400, 32px, 35px, 121px, 0.85, 1.00, 1.20; substitute `Montserrat`.
- **NB Akademie Mono**: 400, 11px, 32px, 1.00, 1.20; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `26px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `buttons: 0px`

## Component cues
- **Ghost Navigation Link**: Top navigation and inline links
- **Ghost Primary Button**: Call to action buttons

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
