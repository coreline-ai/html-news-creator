# Patch - Refero Design MD

- Source: https://styles.refero.design/style/7af0134b-c299-42f8-9d95-7004e2d0e278
- Original site: https://thepatchsystem.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric blueprint, high-fidelity lines

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Blueprint | `#1f00ff` | brand | Action accent / signal color |
| Blaze Orange | `#ff622b` | accent | Action accent / signal color |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#ececec` | neutral | Page background or card surface |
| Faded Grid | `#d3d3d3` | neutral | Border, muted text, or supporting surface |
| Deep Graphite | `#212121` | neutral | Primary text or dark surface |
| Surface Light | `#f2f2f2` | neutral | Page background or card surface |
| Surface Lighter | `#f8f8f8` | neutral | Page background or card surface |

```css
:root {
  --ref-blueprint: #1f00ff;
  --ref-blaze-orange: #ff622b;
  --ref-canvas-white: #ffffff;
  --ref-ash-gray: #ececec;
  --ref-faded-grid: #d3d3d3;
  --ref-deep-graphite: #212121;
  --ref-surface-light: #f2f2f2;
  --ref-surface-lighter: #f8f8f8;
}
```

## Typography direction
- **Archivo**: 300, 400, 600, 10px, 11px, 13px, 14px, 17px, 19px, 23px, 24px, 29px, 38px, 333px, 1.00, 1.07, 1.11, 1.20, 1.22, 1.33, 1.40, 1.50, 1.58, 1.67, 2.00; substitute `Arial`.
- **PP Right**: 400, 800, 12px, 13px, 14px, 19px, 21px, 24px, 29px, 33px, 38px, 48px, 62px, 67px, 90px, 95px, 133px, 152px, 200px, 524px, 0.79, 0.85, 0.86, 0.90, 0.94, 1.00, 1.10, 1.13, 1.20, 1.57, 1.85, 2.00, 2.32; substitute `Impact`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `38px`
- Element Gap: `11px`
- Radius: `cards: 4.7619px, buttons: 4.7619px, mediumCards: 9.52381px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background and default card surface.
- **Surface Lighter** `#f8f8f8`: Slightly elevated card background.
- **Surface Light** `#f2f2f2`: Secondary elevated card background, notably used for cards with 9.52381px radius.
- **Ash Gray** `#ececec`: Background for subtle UI elements and interactive states, slightly darker than other surface neutrals.
- **Deep Graphite** `#212121`: Highest contrast card background, used for featured content blocks.

## Component cues
- **Primary Action Button**: Filled Call to Action
- **Inverse Primary Action Button**: Filled Call to Action for Blueprint backgrounds
- **Ghost Outline Button**: Secondary action or subtle interaction
- **Standard Card**: Content container
- **Blueprint Card**: Highlight or featured content card

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
