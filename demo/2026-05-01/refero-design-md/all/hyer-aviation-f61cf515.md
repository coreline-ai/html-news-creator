# Hyer Aviation - Refero Design MD

- Source: https://styles.refero.design/style/f61cf515-ccd5-4494-bdd1-be9fe4d7258c
- Original site: https://www.flyhyer.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochromatic luxury, sharp contrast

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian | `#000d10` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Slate Mist | `#8e8e95` | neutral | Border, muted text, or supporting surface |
| Desert Sienna | `#bc7155` | accent | Action accent / signal color |

```css
:root {
  --ref-obsidian: #000d10;
  --ref-canvas-white: #ffffff;
  --ref-slate-mist: #8e8e95;
  --ref-desert-sienna: #bc7155;
}
```

## Typography direction
- **HelveticaNowDisplay**: 400, 700, 17px, 18px, 20px, 23px, 30px, 37px, 52px, 60px, 63px, 131px, 187px, 0.80, 0.91, 1.00, 1.09, 1.10, 1.20, 1.61; substitute `system-ui`.
- **sans-serif**: 700, 17px, 1.00; substitute `Arial`.

## Spacing / shape
- Section Gap: `68px`
- Card Padding: `22px`
- Element Gap: `23px`
- Radius: `links: 1000px, other: 45px, buttons: 1000px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for content.
- **Obsidian Surface** `#000d10`: Elevated dark surfaces, footer, and backgrounds for prominent sections.

## Component cues
- **Primary Filled Button**: Main call-to-action button, promoting core actions.
- **Obsidian Filled Button**: Secondary call-to-action or general action buttons.
- **Obsidian Ghost Button**: Alternative action buttons, appearing less prominent than filled variants.
- **Navigation Link**: Primary navigation items in the header and footer.
- **Feature Card**: Displays key features or offerings with associated text.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
