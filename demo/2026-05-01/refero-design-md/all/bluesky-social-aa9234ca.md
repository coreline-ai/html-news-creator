# Bluesky Social - Refero Design MD

- Source: https://styles.refero.design/style/aa9234ca-0cc8-470b-bd38-398712de3e95
- Original site: https://bsky.app
- Theme: `light`
- Industry: `media`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp white canvas, quiet blue accent. The layout feels like a well-organized corkboard of fleeting thoughts and visual snippets, neatly pinned and easily digestible.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ebony Text | `#000000` | neutral | Primary text or dark surface |
| Sky Blue | `#006aff` | brand | Action accent / signal color |
| Horizon Gray | `#dce2ea` | neutral | Page background or card surface |
| Cloud Cover | `#f9fafb` | neutral | Page background or card surface |
| Ghost Button Background | `#eff2f6` | neutral | Page background or card surface |
| Slate Text | `#405168` | neutral | Border, muted text, or supporting surface |
| Steel Icon | `#667b99` | neutral | Border, muted text, or supporting surface |
| Icon Gray | `#8798b0` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ebony-text: #000000;
  --ref-sky-blue: #006aff;
  --ref-horizon-gray: #dce2ea;
  --ref-cloud-cover: #f9fafb;
  --ref-ghost-button-background: #eff2f6;
  --ref-slate-text: #405168;
  --ref-steel-icon: #667b99;
}
```

## Typography direction
- **InterVariable**: 400, 500, 600, 700, 11px, 12px, 13px, 15px, 16px, 24px, 1.00, 1.13, 1.20, 1.25, 1.30, 1.33; substitute `Inter`.

## Spacing / shape
- Section Gap: `24px`
- Element Gap: `4px`
- Radius: `cards: 12px, inputs: 0px, avatars: 999px, buttons: 999px`

## Component cues
- **Post Card**: Reference component style.
- **Trending Sidebar Card**: Reference component style.
- **Auth Panel with Tab Bar**: Reference component style.
- **Primary Navigation Button**: Primary Call to Action
- **Secondary Navigation Button**: Secondary Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
