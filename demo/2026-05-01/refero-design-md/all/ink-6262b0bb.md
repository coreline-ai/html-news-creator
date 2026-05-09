# INK - Refero Design MD

- Source: https://styles.refero.design/style/6262b0bb-ea6f-481b-b706-65df29507b6c
- Original site: https://weareink.co.uk
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble. Precision, clarity, spaciousness, and carefully chosen details unfold across a pristine, light-drenched surface.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#2e2a2b` | neutral | Primary text or dark surface |
| Frost Canvas | `#ffffff` | neutral | Page background or card surface |
| Warm Paper | `#e6dcd4` | neutral | Page background or card surface |
| Cool Stone | `#afa697` | neutral | Border, muted text, or supporting surface |
| Joby Aviation Sky | `#b6d0e2` | accent | Action accent / signal color |

```css
:root {
  --ref-ink-black: #2e2a2b;
  --ref-frost-canvas: #ffffff;
  --ref-warm-paper: #e6dcd4;
  --ref-cool-stone: #afa697;
  --ref-joby-aviation-sky: #b6d0e2;
}
```

## Typography direction
- **Good Sans**: 400, 18px, 22px, 27px, 60px, 1.00, 1.09, 1.14, 1.25, 1.31, 1.60, 1.75; substitute `Inter`.

## Spacing / shape
- Section Gap: `160px`
- Card Padding: `64px`
- Element Gap: `32px`
- Radius: `cards: 0px, inputs: 0px, buttons: 0px, navPills: 100px`

## Component cues
- **Ghost Button Group**: Reference component style.
- **Project Card — Portfolio Item**: Reference component style.
- **Email Subscription Input**: Reference component style.
- **Ghost Button**: Interactive elements, navigation, and 'Back to top' calls to action.
- **Navigation Pill Indicator**: Active state or selected item indicator within navigation menus.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
