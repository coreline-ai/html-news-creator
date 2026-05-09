# Empower - Refero Design MD

- Source: https://styles.refero.design/style/8d3dc65e-4443-4bb3-b1a9-b0fc98381db9
- Original site: https://empower.me
- Theme: `mixed`
- Industry: `fintech`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
midnight command center, bright button

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Night Sky | `#100f0f` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Cloud Whisper | `#fffdf6` | neutral | Page background or card surface |
| Deep Space | `#171616` | neutral | Primary text or dark surface |
| Charcoal Card | `#262525` | neutral | Primary text or dark surface |
| Metal Gray | `#64635c` | neutral | Border, muted text, or supporting surface |
| Button Yellow | `#e4e24e` | brand | Action accent / signal color |
| Muted Yellow | `#faf9b6` | accent | Action accent / signal color |

```css
:root {
  --ref-night-sky: #100f0f;
  --ref-canvas-white: #ffffff;
  --ref-cloud-whisper: #fffdf6;
  --ref-deep-space: #171616;
  --ref-charcoal-card: #262525;
  --ref-metal-gray: #64635c;
  --ref-button-yellow: #e4e24e;
  --ref-muted-yellow: #faf9b6;
}
```

## Typography direction
- **GTAmericaExtended**: 400, 11px, 13px, 16px, 18px, 20px, 21px, 26px, 1.20, 1.27, 1.33, 1.38, 1.48, 1.50; substitute `Inter`.
- **GTAmericaExpanded**: 400, 500, 11px, 12px, 13px, 16px, 1.50, 1.54, 1.82; substitute `Inter`.
- **Gravity**: 400, 900, 16px, 24px, 40px, 48px, 96px, 205px, 1.00, 1.50; substitute `Poppins`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `cards: 24px, buttons: 16777216px, modules: 16px`

## Surface cues
- **Night Sky** `#100f0f`: Primary dark background for the highest level of UI, particularly navigation and footer.
- **Deep Space** `#171616`: Dominant background for hero sections and expansive dark content blocks, creating depth while maintaining darkness.
- **Canvas White** `#ffffff`: Background for light feature sections, providing a stark contrast to dark areas and improving readability for dense content.
- **Cloud Whisper** `#fffdf6`: Subtle light surface within light sections, used for cards or content blocks to create a slight separation without strong borders.
- **Muted Yellow** `#faf9b6`: Accent surface for specific cards or callouts, offering a soft visual highlight.

## Component cues
- **Primary Action Button**: Main call to action across the site.
- **Ghost Navigation Button**: Secondary action or navigation in dark sections.
- **Ghost Secondary Button**: Clickable elements requiring less emphasis, often in light sections.
- **Dark Photo Card**: Displaying imagery with associated monetary values against a dark background.
- **Light Content Card**: General content display in light sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
