# Voicenotes - Refero Design MD

- Source: https://styles.refero.design/style/cafcbe97-58eb-4331-9a0a-c5e6969e8a04
- Original site: https://voicenotes.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Ledger on Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#faf9f5` | neutral | Page background or card surface |
| Slate Ink | `#0d0d0d` | neutral | Primary text or dark surface |
| Subtle Gray | `#e5e7eb` | neutral | Page background or card surface |
| Text Gray | `#717171` | neutral | Border, muted text, or supporting surface |
| Shadow Blue | `#eaf2f8` | neutral | Action accent / signal color |
| Deep Graphite | `#222222` | neutral | Primary text or dark surface |
| Success Green | `#34c759` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ghost-gray: #faf9f5;
  --ref-slate-ink: #0d0d0d;
  --ref-subtle-gray: #e5e7eb;
  --ref-text-gray: #717171;
  --ref-shadow-blue: #eaf2f8;
  --ref-deep-graphite: #222222;
  --ref-success-green: #34c759;
}
```

## Typography direction
- **ui-sans-serif**: 400, 16px, 1.5.
- **InstrumentSerif-Regular**: 400, 20px, 60px, 80px, 1.00, 1.17, 1.40; substitute `Source Serif Pro`.
- **Inter**: 400, 10px, 12px, 14px, 15px, 16px, 18px, 20px, 1.33, 1.38, 1.40, 1.43, 1.47, 1.50, 1.56, 1.71; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `20px`
- Element Gap: `16px`
- Radius: `cards: 16px, forms: 6px, avatars: 9999px, buttons: 9999px, smallCard: 12px`

## Component cues
- **Primary Action Button**: Navigational or primary action button
- **Subtle Bordered Card**: Container for content sections
- **Shadowed Flyout Card**: Elevated menu or tooltip container
- **Secondary Background Card**: Background for feature blocks or subtle distinctions

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
