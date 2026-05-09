# Ferrari - Refero Design MD

- Source: https://styles.refero.design/style/80164adf-a898-4f7c-bce7-12f3f62e1649
- Original site: https://ferrari.com
- Theme: `mixed`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precision engineered machinery. Like the interior of a sleek, high-performance engine, where every component is black or silver, and only critical indicators glow red.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian Black | `#000000` | neutral | Primary text or dark surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Shadow Graphite | `#181818` | neutral | Primary text or dark surface |
| Steel Gray | `#303030` | neutral | Primary text or dark surface |
| Ash Mist | `#8f8f8f` | neutral | Border, muted text, or supporting surface |
| Rosso Corsa | `#ff0000` | brand | Action accent / signal color |

```css
:root {
  --ref-obsidian-black: #000000;
  --ref-polar-white: #ffffff;
  --ref-shadow-graphite: #181818;
  --ref-steel-gray: #303030;
  --ref-ash-mist: #8f8f8f;
  --ref-rosso-corsa: #ff0000;
}
```

## Typography direction
- **custom**: 11px, 12px, 13px, 1.27, 1.50, 1.78, 2.00; substitute `Arial, Helvetica, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `all: 0px`

## Component cues
- **Hero Slide Indicator & CTA**: Reference component style.
- **News Feature Card**: Reference component style.
- **Navigation Link Group & Carousel Pagination**: Reference component style.
- **Ghost Navigation Link**: Primary navigation item
- **Hero Action Arrow Button**: Call to action in hero section

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
