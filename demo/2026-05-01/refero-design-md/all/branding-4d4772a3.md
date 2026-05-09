# Branding - Refero Design MD

- Source: https://styles.refero.design/style/4d4772a3-e1da-415f-a6d7-658dcefdcecd
- Original site: https://www.svz.io
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight atelier of digital craftsmanship

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Deep Space | `#080808` | neutral | Primary text or dark surface |
| Nightfall Gray | `#171617` | neutral | Primary text or dark surface |
| Charcoal Surface | `#262525` | neutral | Primary text or dark surface |
| Slate Highlight | `#393939` | neutral | Primary text or dark surface |
| Cloud White | `#fcfcfc` | neutral | Page background or card surface |
| Glacial White | `#f3efef` | neutral | Page background or card surface |
| Ash Accent | `#d4d2d2` | neutral | Border, muted text, or supporting surface |
| Dim Gray | `#b5b2b2` | neutral | Border, muted text, or supporting surface |
| Steel Border | `#525252` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-deep-space: #080808;
  --ref-nightfall-gray: #171617;
  --ref-charcoal-surface: #262525;
  --ref-slate-highlight: #393939;
  --ref-cloud-white: #fcfcfc;
  --ref-glacial-white: #f3efef;
  --ref-ash-accent: #d4d2d2;
}
```

## Typography direction
- **Kmr Waldenburg**: 300, 400, 700, 10px, 12px, 14px, 24px, 32px, 42px, 64px, 80px, 160px, 0.90, 1.00, 1.05, 1.10, 1.20, 1.50; substitute `Montserrat`.
- **system-ui**: 300, 400, 12px, 14px, 1.20, 1.50; substitute `Inter`.
- **Editorialnew**: 300, 14px, 20px, 32px, 1.00, 1.10, 1.50; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `24px`
- Page Max Width: `1440px`
- Radius: `cards: 8px, buttons: 8px, default: 3px, interactive: 3px, texturedCard: 14.4px`

## Surface cues
- **Absolute Zero** `#000000`: Dominant page background, deepest stage for content.
- **Deep Space** `#080808`: Default interactive backgrounds, subtle base for cards and content sections.
- **Nightfall Gray** `#171617`: Footer background, slightly elevated content blocks.
- **Charcoal Surface** `#262525`: Elevated card backgrounds requiring distinct separation.

## Component cues
- **Primary Action Button**: Filled button for critical calls to action.
- **Secondary Ghost Button**: Outlined button for secondary actions, blending into dark contexts.
- **Textured Card**: Card with subtle background texture and inset shadow.
- **Feature Content Card**: Solid background card for feature blocks.
- **Navigation Link**: Interactive text link within navigation menus.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
