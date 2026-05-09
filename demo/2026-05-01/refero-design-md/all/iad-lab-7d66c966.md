# Iad-lab - Refero Design MD

- Source: https://styles.refero.design/style/7d66c966-6cee-4c82-b2e4-2bf1ca7b2ccd
- Original site: https://iad-lab.ch
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Academic Dark Canvas – a stark, authoritative presentation with bold typographic statements on a deep charcoal ground.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Storm Charcoal | `#222222` | neutral | Primary text or dark surface |
| Cloud White | `#f8f8f8` | neutral | Page background or card surface |
| Slate Ink | `#2a2b2d` | neutral | Primary text or dark surface |
| Subtle Ash | `#757577` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-storm-charcoal: #222222;
  --ref-cloud-white: #f8f8f8;
  --ref-slate-ink: #2a2b2d;
  --ref-subtle-ash: #757577;
}
```

## Typography direction
- **Neue Haas Unica**: 400, 700, 16px, 18px, 24px, 27px, 36px, 1.10, 1.25, 1.30, 1.35; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `20px`
- Element Gap: `24px`
- Radius: `default: 20px, headings: 15px`

## Surface cues
- **Storm Charcoal Canvas** `#222222`: Primary page and content background.
- **Subtle Ash Interface** `#757577`: Secondary surface, used for interactive elements like navigation highlights.
- **Cloud White Surface** `#f8f8f8`: Elevated content containers, list backgrounds, and areas of high-contrast information display.

## Component cues
- **Ghost Navigation Item**: Navigation
- **Section Heading**: Title
- **Text Block**: Content
- **Hero Title**: Headline
- **Pill Navigation Dot**: Navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
