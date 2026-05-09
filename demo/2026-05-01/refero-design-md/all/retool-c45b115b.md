# Retool - Refero Design MD

- Source: https://styles.refero.design/style/c45b115b-dcb5-446d-8952-85aef740f8e4
- Original site: https://retool.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm obsidian workshop — a precision tool surface lit by ember glow, where everything is built.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian Canvas | `#151515` | neutral | Primary text or dark surface |
| Void Black | `#0e0e0e` | neutral | Primary text or dark surface |
| Ember Surface | `#242424` | neutral | Primary text or dark surface |
| Charcoal Rim | `#3f403d` | neutral | Primary text or dark surface |
| Copper Wire | `#8b867f` | neutral | Border, muted text, or supporting surface |
| Ash Text | `#94958e` | neutral | Border, muted text, or supporting surface |
| Fog Text | `#cbccc4` | neutral | Border, muted text, or supporting surface |
| Limestone | `#b6b8af` | neutral | Border, muted text, or supporting surface |
| Parchment | `#e9ebdf` | neutral | Page background or card surface |
| Forest Deep | `#185849` | brand | Action accent / signal color |

```css
:root {
  --ref-obsidian-canvas: #151515;
  --ref-void-black: #0e0e0e;
  --ref-ember-surface: #242424;
  --ref-charcoal-rim: #3f403d;
  --ref-copper-wire: #8b867f;
  --ref-ash-text: #94958e;
  --ref-fog-text: #cbccc4;
  --ref-limestone: #b6b8af;
}
```

## Typography direction
- **saansFont**: 300, 380, 570, 14px, 16px, 18px, 24px, 32px, 36px, 48px, 60px, 72px, 1.00 at 60-72px, 1.05 at 36-48px, 1.20 at 18-32px, 1.50 at 14-16px; substitute `Inter, DM Sans`.
- **pxGroteskFont**: 400, 12px, 14px, 1.00, 1.20; substitute `Space Grotesk, Geist`.
- **ui-sans-serif**: 400, 16px, 1.50; substitute `System UI stack`.

## Spacing / shape
- Section Gap: `80-120px`
- Card Padding: `24px`
- Element Gap: `8-16px`
- Page Max Width: `1200px`
- Radius: `cards-large: 12px, pills-large: 36px, tags-badges: 4px, buttons-pill: 9999px, cards-default: 8px, buttons-square: 0px`

## Surface cues
- **Void** `#0e0e0`: Deepest background — recessed panels, testimonial blocks, elements that should feel inset below canvas
- **Canvas** `#151515`: Dominant page background — the ground all content sits on
- **Raised** `#242424`: Card surfaces, panel backgrounds, interactive tiles — lifted above canvas by lightness alone
- **Teal Wash** `#185849`: Atmospheric section tint — used as a large-area background color wash to signal a distinct content zone

## Component cues
- **Announcement Bar + CTA Button Group**: Reference component style.
- **Stat / Social Proof Cards**: Reference component style.
- **Feature Section Card — AppGen**: Reference component style.
- **Pill Button — Filled**: Primary call-to-action (e.g. 'Book a demo', 'Get early access')
- **Ghost Button — Square**: Secondary actions, nav-level text links with visible border

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
