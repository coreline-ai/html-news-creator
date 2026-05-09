# Spring/Summer - Refero Design MD

- Source: https://styles.refero.design/style/d56508d7-c307-47f7-ad30-052e5a69f01f
- Original site: https://springsummer.dk
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vintage academic journal — muted tones on rough-cut paper.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Greige Canvas | `#e5ebda` | neutral | Page background or card surface |
| Deep Plum | `#44394c` | brand | Action accent / signal color |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Ash Border | `#c0c3b6` | neutral | Border, muted text, or supporting surface |
| Input Pale Gray | `#b0b2a9` | neutral | Border, muted text, or supporting surface |
| True Black | `#000000` | neutral | Primary text or dark surface |
| Accent Yellow | `#ffff00` | accent | Action accent / signal color |

```css
:root {
  --ref-greige-canvas: #e5ebda;
  --ref-deep-plum: #44394c;
  --ref-pure-white: #ffffff;
  --ref-ash-border: #c0c3b6;
  --ref-input-pale-gray: #b0b2a9;
  --ref-true-black: #000000;
  --ref-accent-yellow: #ffff00;
}
```

## Typography direction
- **Montreal**: 400, 12px, 13px, 14px, 18px, 43px, 1.10, 1.20, 1.30, 1.40, 1.50; substitute `Inter`.
- **Grotesk**: 400, 40px, 170px, 386px, 0.75, 0.76; substitute `IBM Plex Sans Bold`.

## Spacing / shape
- Section Gap: `30px`
- Element Gap: `10px`
- Radius: `links: 4px, inputs: 4px`

## Component cues
- **Contact CTA Banner**: Reference component style.
- **Project Card Grid**: Reference component style.
- **Agency Description Block**: Reference component style.
- **Navigation Link**: Primary navigation within header/footer.
- **Unstyled Button**: Functional clickable elements (e.g., 'What we do').

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
