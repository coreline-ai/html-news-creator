# Charlie Phipps - Refero Design MD

- Source: https://styles.refero.design/style/7f6799d9-0733-4523-9a94-036b9ad3bf28
- Original site: https://phippscharlie.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center: precise lines on a deep, expansive canvas, guided by stark textual contrasts.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Canvas | `#101011` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Obsidian Text | `#000000` | neutral | Primary text or dark surface |
| Ash Panel | `#ededed` | neutral | Page background or card surface |
| Whisper Grey | `#bab7b2` | neutral | Border, muted text, or supporting surface |
| Charcoal Detail | `#888888` | neutral | Border, muted text, or supporting surface |
| Dark Granite Border | `#262627` | neutral | Primary text or dark surface |
| Deep Space Accent | `#080809` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-canvas: #101011;
  --ref-cloud-white: #ffffff;
  --ref-obsidian-text: #000000;
  --ref-ash-panel: #ededed;
  --ref-whisper-grey: #bab7b2;
  --ref-charcoal-detail: #888888;
  --ref-dark-granite-border: #262627;
  --ref-deep-space-accent: #080809;
}
```

## Typography direction
- **Helvetica Neue**: 400, 16px, 17px, 19px, 21px, 52px, 64px, 162px, 0.90, 1.00, 1.20; substitute `Arial, Helvetica`.
- **Times**: 400, 13px, 1.20; substitute `Times New Roman`.

## Spacing / shape
- Section Gap: `41px`
- Card Padding: `13px`
- Element Gap: `6px`
- Radius: `none: 0px`

## Component cues
- **Navigation Link**: Top and bottom navigation items.
- **Text Card**: Container for textual content or project summaries.
- **Interactive Text Box**: Visually distinct blocks of text that might respond to interaction.
- **Page Header Nav**: Persistent top-level navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
