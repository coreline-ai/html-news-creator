# Brisbane Web Developer - Refero Design MD

- Source: https://styles.refero.design/style/23d83a89-8f22-405a-aa33-74fd0ebde9d8
- Original site: https://carlbeaverson.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Art Gallery Minimalism: Project thumbnails, like curated art pieces, float on a light, matte background, each framed by a subtle, soft shadow box.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f4f3f1` | neutral | Page background or card surface |
| Graphite Text | `#333333` | neutral | Primary text or dark surface |
| Ash Details | `#aaaaaa` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Dust Border | `#dddddd` | neutral | Page background or card surface |
| Inactive Slate | `#666666` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #f4f3f1;
  --ref-graphite-text: #333333;
  --ref-ash-details: #aaaaaa;
  --ref-stone-gray: #4d4d4d;
  --ref-dust-border: #dddddd;
  --ref-inactive-slate: #666666;
}
```

## Typography direction
- **sans-serif**: 400, 14px, 15px, 20px, 1.20, 1.40, 1.50; substitute `system-ui, 'Helvetica Neue', 'Segoe UI', Arial, sans-serif`.
- **Suisse Works Trial**: 400, 13px, 1.50; substitute `serif`.

## Spacing / shape
- Section Gap: `122px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 5px, inputs: 5px, buttons: 5px`

## Component cues
- **Project Thumbnail Card**: Reference component style.
- **Hero Bio Text Block**: Reference component style.
- **Newsletter Segmented Form**: Reference component style.
- **Primary Button**: Call-to-action buttons for submissions.
- **Secondary Button**: General interactive buttons.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
