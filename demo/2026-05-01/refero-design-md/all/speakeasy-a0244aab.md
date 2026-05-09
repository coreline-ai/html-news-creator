# Speakeasy - Refero Design MD

- Source: https://styles.refero.design/style/a0244aab-0dba-45fe-a595-416c1f0715be
- Original site: https://www.speakeasy.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochrome Blueprint, Rainbow Spectrum. A highly structured and functional interface with a vibrant, linear brand accent.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#dbdbdb` | neutral | Page background or card surface |
| Charcoal | `#242424` | neutral | Primary text or dark surface |
| Slate | `#545454` | neutral | Border, muted text, or supporting surface |
| Silver Thread | `#969696` | neutral | Border, muted text, or supporting surface |
| Ghost Gray | `#f1f1f1` | neutral | Page background or card surface |
| Deep Space | `#333333` | neutral | Primary text or dark surface |
| Rainbow Horizon | `#330f1f` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-ash-gray: #dbdbdb;
  --ref-charcoal: #242424;
  --ref-slate: #545454;
  --ref-silver-thread: #969696;
  --ref-ghost-gray: #f1f1f1;
  --ref-deep-space: #333333;
}
```

## Typography direction
- **ui-sans-serif**: 400, 500, 600, 700, 9px, 10px, 11px, 12px, 13px, 14px, 16px, 18px, 1.43, 1.50, 1.75; substitute `system-ui, sans-serif`.
- **diatype**: 300, 400, 500, 14px, 16px, 18px, 23px, 26px, 1.29, 1.38, 1.60, 1.75; substitute `Georgia, serif`.
- **tobias**: 100, 20px, 38px, 51px, 67px, 140px, 1.00, 1.20, 1.30, 1.38, 1.40; substitute `serif`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `24px`
- Element Gap: `6px`
- Radius: `cards: 8px, badges: 2px, buttons: 1.67772e+07px, default: 4px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base layer.
- **Ghost Gray** `#f1f1f1`: Secondary background for alternating sections or elevated UI elements.
- **Ash Gray (muted)** `#dbdbdb`: Background for subtle states or very light contextual elements, dividers.

## Component cues
- **Primary Filled Button**: Calls to action, form submissions, primary interactions.
- **Ghost Button**: Secondary actions, navigation links, less prominent calls to action.
- **Badge**: Categorization, status indicators, small labels.
- **Content Card**: To encapsulate related information, features, or testimonials.
- **Nav Item**: Top navigation links.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
