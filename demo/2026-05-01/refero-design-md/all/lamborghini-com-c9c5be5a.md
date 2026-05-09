# Lamborghini.com - Refero Design MD

- Source: https://styles.refero.design/style/c9c5be5a-aaa1-4338-9681-8378d2e24fbd
- Original site: https://lamborghini.com
- Theme: `mixed`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precision-engineered black steel with yellow accents. Every edge is sharp, every surface polished, reflecting light with purpose.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon Black | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Concrete Gray | `#f5f5f5` | neutral | Page background or card surface |
| Graphite | `#202020` | neutral | Primary text or dark surface |
| Dark Metal | `#181818` | neutral | Primary text or dark surface |
| Engine Yellow | `#917300` | brand | Action accent / signal color |
| Speed Yellow | `#ffc000` | brand | Action accent / signal color |

```css
:root {
  --ref-carbon-black: #000000;
  --ref-ghost-white: #ffffff;
  --ref-concrete-gray: #f5f5f5;
  --ref-graphite: #202020;
  --ref-dark-metal: #181818;
  --ref-engine-yellow: #917300;
  --ref-speed-yellow: #ffc000;
}
```

## Typography direction
- **LamboType**: 400, 10px, 12px, 16px, 18px, 27px, 32px, 40px, 54px, 80px, 120px, 0.92, 1.00, 1.13, 1.15, 1.19, 1.37, 1.38, 1.50, 1.56, 1.63, 1.83, 2.00; substitute `Montserrat`.
- **Open Sans**: 400, 16px, 1.50; substitute `Open Sans`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `0px`
- Element Gap: `24px`
- Radius: `all: 0px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Event Announcement Banner**: Reference component style.
- **News Article Card**: Reference component style.
- **Primary Action Button - Engine Yellow**: Call to action
- **Secondary Action Button - Speed Yellow**: Call to action (more urgent)

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
