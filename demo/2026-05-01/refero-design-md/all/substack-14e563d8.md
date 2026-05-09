# Substack - Refero Design MD

- Source: https://styles.refero.design/style/14e563d8-a35a-4867-b4bf-15d1620ddae7
- Original site: https://substack.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm editorial gateway. Like a clean, well-organized newsstand where one striking orange magazine cover catches your eye amidst a collection of white and gray.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Orange Ember | `#ff6719` | brand | Action accent / signal color |
| Midnight Graphite | `#363737` | neutral | Primary text or dark surface |
| Anchor Gray | `#777777` | neutral | Border, muted text, or supporting surface |
| UI White | `#ffffff` | neutral | Page background or card surface |
| Silver Mist | `#eeeeee` | neutral | Page background or card surface |
| Dark Overlay | `#232525` | neutral | Primary text or dark surface |
| Cool Stone | `#c8c8c8` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#b6b6b6` | neutral | Border, muted text, or supporting surface |
| Ghost Shadow | `#e6e6e6` | neutral | Page background or card surface |

```css
:root {
  --ref-orange-ember: #ff6719;
  --ref-midnight-graphite: #363737;
  --ref-anchor-gray: #777777;
  --ref-ui-white: #ffffff;
  --ref-silver-mist: #eeeeee;
  --ref-dark-overlay: #232525;
  --ref-cool-stone: #c8c8c8;
  --ref-light-steel: #b6b6b6;
}
```

## Typography direction
- **system-ui**: 400, 500, 600, 12px, 13px, 15px, 19px, 20px, 1.00, 1.20, 1.33, 1.40, 1.54; substitute `Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif`.
- **Cahuenga**: 500, 24px, 32px, 1.24, 1.25.
- **Spectral**: 400, 19px, 1.20; substitute `Georgia, Times New Roman, serif`.

## Spacing / shape
- Section Gap: `24-32px`
- Card Padding: `16-24px`
- Element Gap: `4-12px`
- Radius: `cards: 8px, inputs: 12px, buttons: 9999px, elements: 8px, 12px`

## Component cues
- **Log In or Sign Up Card**: Reference component style.
- **Up Next Recommendations Card**: Reference component style.
- **Feed Post Card with Engagement Actions**: Reference component style.
- **Pill Ghost Button**: Secondary action, subtle navigation items
- **Rounded Ghost Button**: Tertiary actions, filters, tags

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
