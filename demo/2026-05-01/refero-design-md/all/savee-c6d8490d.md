# Savee - Refero Design MD

- Source: https://styles.refero.design/style/c6d8490d-e3f2-45c8-aebf-fe5f11daf116
- Original site: https://savee.it
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Inked Canvas, Violet Spark. A high-contrast space where inspiration pops against deep monochrome.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#050505` | neutral | Primary text or dark surface |
| Ghost White | `#fdfdfd` | neutral | Page background or card surface |
| Parchment | `#e5e5e5` | neutral | Page background or card surface |
| Slate Mist | `#d4d4d4` | neutral | Border, muted text, or supporting surface |
| Graphite | `#151515` | neutral | Primary text or dark surface |
| Deep Ash | `#2f2f2f` | neutral | Primary text or dark surface |
| Stone Gray | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Cadet Grey | `#737373` | neutral | Border, muted text, or supporting surface |
| Cool Violet | `#1500ff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #050505;
  --ref-ghost-white: #fdfdfd;
  --ref-parchment: #e5e5e5;
  --ref-slate-mist: #d4d4d4;
  --ref-graphite: #151515;
  --ref-deep-ash: #2f2f2f;
  --ref-stone-gray: #a3a3a3;
  --ref-cadet-grey: #737373;
}
```

## Typography direction
- **Savee Font**: 400, 500, 13px, 14px, 16px, 18px, 1.38, 1.29, 1.25, 1.23; substitute `Inter`.
- **Savee Font**: 400, 500, 21px, 24px, 30px, 36px, 60px, 96px, 1.13, 1.11, 1.00, 0.96; substitute `Inter`.

## Spacing / shape
- Section Gap: `64px`
- Element Gap: `8px`
- Radius: `avatars: 9999px, buttons: 9999px, general: 14px`

## Component cues
- **Primary & Secondary Button Group**: Reference component style.
- **Social Proof — Trusted Brands Bar**: Reference component style.
- **Feature Highlight Cards**: Reference component style.
- **Primary Action Button**: Main call to action
- **Secondary Ghost Button**: Secondary call to action or navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
