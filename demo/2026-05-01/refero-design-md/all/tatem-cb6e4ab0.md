# Tatem - Refero Design MD

- Source: https://styles.refero.design/style/cb6e4ab0-b8fe-45b0-bd22-6339b073e26d
- Original site: https://tatem.com
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal, cool and precise. This visual evokes a dark, command-line interface with subtle interactive glows.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Twilight Ink | `#000000` | neutral | Primary text or dark surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Pewter Mist | `#919191` | neutral | Border, muted text, or supporting surface |
| Silver Tone | `#b5b5b5` | neutral | Border, muted text, or supporting surface |
| Obsidian Grey | `#606060` | neutral | Border, muted text, or supporting surface |
| Charcoal Black | `#3b3b3b` | neutral | Primary text or dark surface |
| Mist Grey | `#c2c2c2` | neutral | Border, muted text, or supporting surface |
| Cerulean Accent | `#007eed` | accent | Action accent / signal color |
| Sky Gradient | `#5a7694` | brand | Action accent / signal color |

```css
:root {
  --ref-twilight-ink: #000000;
  --ref-polar-white: #ffffff;
  --ref-pewter-mist: #919191;
  --ref-silver-tone: #b5b5b5;
  --ref-obsidian-grey: #606060;
  --ref-charcoal-black: #3b3b3b;
  --ref-mist-grey: #c2c2c2;
  --ref-cerulean-accent: #007eed;
}
```

## Typography direction
- **Inter**: 400, 13px, 14px, 16px, 20px, 40px, 1.20, 1.43, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `28px`
- Element Gap: `8px`
- Radius: `large: 10px, default: 6px, hero_element: 16px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Section — Split Inbox**: Reference component style.
- **Keyboard Shortcuts Section**: Reference component style.
- **Primary Ghost Button**: Call to action, navigation items.
- **Navigation Link Button**: Secondary actions, internal navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
