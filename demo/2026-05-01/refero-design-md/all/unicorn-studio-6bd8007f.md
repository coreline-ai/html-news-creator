# Unicorn Studio - Refero Design MD

- Source: https://styles.refero.design/style/6bd8007f-01bc-46cc-8599-b396a39c1474
- Original site: https://www.unicorn.studio
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#08080a` | neutral | Primary text or dark surface |
| Twilight Slate | `#0d0d12` | neutral | Primary text or dark surface |
| Soft Black | `#17171c` | neutral | Primary text or dark surface |
| Ash Gray | `#25252d` | neutral | Primary text or dark surface |
| Steel Gray | `#31313a` | neutral | Primary text or dark surface |
| Ghostly Gray | `#aeaac0` | neutral | Border, muted text, or supporting surface |
| Muted Silver | `#dad7de` | neutral | Border, muted text, or supporting surface |
| Subtle Charcoal | `#8b8e9c` | neutral | Border, muted text, or supporting surface |
| Faded Stone | `#62626f` | neutral | Border, muted text, or supporting surface |
| Cosmic Violet | `#8e6ce4` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #08080a;
  --ref-twilight-slate: #0d0d12;
  --ref-soft-black: #17171c;
  --ref-ash-gray: #25252d;
  --ref-steel-gray: #31313a;
  --ref-ghostly-gray: #aeaac0;
  --ref-muted-silver: #dad7de;
  --ref-subtle-charcoal: #8b8e9c;
}
```

## Typography direction
- **Overused Grotesk**: 400, 500, 26px, 32px, 48px, 64px, 215px, 0.99, 1.00; substitute `Inter`.
- **Sprat**: 500, 46px, 61px, 1.00; substitute `Anton`.
- **-apple-system**: 400, 500, 600, 13px, 14px, 16px, 18px, 1.20, 1.40; substitute `Inter`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `30px`
- Element Gap: `20px`
- Page Max Width: `1440px`
- Radius: `tags: 3px, cards: 10px, buttons: 3px`

## Surface cues
- **Midnight Ink** `#08080a`: Base page background and primary card surface.
- **Twilight Slate** `#0d0d12`: Slightly elevated background for secondary content blocks or modals.
- **Soft Black** `#17171c`: Further elevated background, often used for nested UI components or hover states.
- **Ash Gray** `#25252d`: Interactive element backgrounds like buttons, providing a distinct clickable area.

## Component cues
- **Filled Action Button**: Primary Call to Action
- **Outlined Button (Primary)**: Secondary action or link with brand emphasis
- **Navigation Link**: Top navigation and inline links
- **Content Card**: Container for features, testimonials, or product modules
- **Info Tag**: Small, informative labels, often used for status or categories

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
