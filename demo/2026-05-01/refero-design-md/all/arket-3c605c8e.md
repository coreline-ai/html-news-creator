# ARKET - Refero Design MD

- Source: https://styles.refero.design/style/3c605c8e-daf2-4d46-94d7-2cb705a93b7b
- Original site: https://arket.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial Minimal Canvas — Think high-contrast type on stark white pages, framed by precise, almost invisible borders, allowing rich product photography to dominate.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#e0e0e0` | neutral | Page background or card surface |
| Soft Graphite | `#666666` | neutral | Border, muted text, or supporting surface |
| Hint of Gray | `#eaeae8` | neutral | Page background or card surface |
| Body Text Gray | `#767676` | neutral | Border, muted text, or supporting surface |
| Command Blue | `#3860be` | accent | Action accent / signal color |
| Success Green | `#38793f` | semantic | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-ash-gray: #e0e0e0;
  --ref-soft-graphite: #666666;
  --ref-hint-of-gray: #eaeae8;
  --ref-body-text-gray: #767676;
  --ref-command-blue: #3860be;
  --ref-success-green: #38793f;
}
```

## Typography direction
- **arketSansMono**: 400, 10px, 12px, 16px, 22px, 28px, 1.21, 1.27, 1.38, 1.50, 1.88; substitute `IBM Plex Mono`.
- **Arket Sans**: 400, 10px, 13px, 16px, 18px, 24px, 1.23, 1.50; substitute `Inter`.
- **arketSCSansMono**: 400, 10px, 12px, 16px, 1.00, 1.38, 1.50; substitute `IBM Plex Mono (short caps variant)`.

## Spacing / shape
- Section Gap: `80-128px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `inputs: 4px, buttons: 2px, general: 0px`

## Component cues
- **Membership Callout Modal**: Reference component style.
- **Announcement Banner**: Reference component style.
- **Editorial Article Cards**: Reference component style.
- **Primary Ghost Button**: Navigation links, inline actions
- **Subtle Outlined Button**: Secondary actions, filtering

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
