# Linus Rogge - Refero Design MD

- Source: https://styles.refero.design/style/81a66e75-23af-4525-8a4e-f4a54c2700e7
- Original site: https://linusrogge.com
- Theme: `mixed`
- Industry: `agency`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Photographic Contact Sheet — a high-contrast, monochrome canvas where every element is framed with intentional space.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Deep Shadow | `#0a0a0a` | neutral | Primary text or dark surface |
| Faint Gray | `#e5e5e5` | neutral | Page background or card surface |
| Light Gray | `#d4d4d4` | neutral | Border, muted text, or supporting surface |
| Mid Gray | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Dark Gray | `#737373` | neutral | Border, muted text, or supporting surface |
| Charcoal | `#525252` | neutral | Border, muted text, or supporting surface |
| Deep Charcoal | `#404040` | neutral | Border, muted text, or supporting surface |
| Near Black | `#262626` | neutral | Primary text or dark surface |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-pure-white: #ffffff;
  --ref-deep-shadow: #0a0a0a;
  --ref-faint-gray: #e5e5e5;
  --ref-light-gray: #d4d4d4;
  --ref-mid-gray: #a3a3a3;
  --ref-dark-gray: #737373;
  --ref-charcoal: #525252;
}
```

## Typography direction
- **ABC Oracle**: 400, 500, 14px, 1.00, 1.25, 1.43; substitute `Inter`.

## Spacing / shape
- Card Padding: `12px`
- Element Gap: `6px`
- Radius: `buttons: 1.67772e+07px`

## Component cues
- **Writing Post List**: Reference component style.
- **About Bio with CTA Button**: Reference component style.
- **Project Card — Regpit**: Reference component style.
- **Primary Black Button**: Call-to-action and navigation.
- **Project Link Card**: Showcasing individual projects.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
