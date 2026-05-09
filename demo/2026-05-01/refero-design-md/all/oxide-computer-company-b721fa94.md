# Oxide Computer Company - Refero Design MD

- Source: https://styles.refero.design/style/b721fa94-72e6-49ad-a9bc-bab3d075f19c
- Original site: https://oxide.computer
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Command Center.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#0b0e12` | neutral | Primary text or dark surface |
| Graphite | `#1f2124` | neutral | Primary text or dark surface |
| Slate | `#303235` | neutral | Primary text or dark surface |
| Dim Gray | `#434547` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#5d5e61` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#818284` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#a3a4a5` | neutral | Border, muted text, or supporting surface |
| Platinum | `#bababb` | neutral | Border, muted text, or supporting surface |
| Snow | `#dedede` | neutral | Page background or card surface |
| Terminal Green | `#00d892` | accent | Action accent / signal color |

```css
:root {
  --ref-carbon: #0b0e12;
  --ref-graphite: #1f2124;
  --ref-slate: #303235;
  --ref-dim-gray: #434547;
  --ref-steel-gray: #5d5e61;
  --ref-ash-gray: #818284;
  --ref-light-gray: #a3a4a5;
  --ref-platinum: #bababb;
}
```

## Typography direction
- **SuisseIntl**: 400, 11px, 12px, 14px, 16px, 18px, 20px, 25px, 36px, 50px, 65px, 1.00, 1.10, 1.17, 1.28, 1.29, 1.30, 1.33, 1.35, 1.38; substitute `Inter`.
- **GT America Mono**: 400, 10px, 11px, 12px, 13px, 20px, 1.00, 1.20, 1.25, 1.30, 1.33, 1.40, 1.45, 1.60; substitute `Fira Code`.

## Spacing / shape
- Section Gap: `56px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `none: 0px, cards: 1px, links: 1px, badges: 1px, inputs: 1px, buttons: 1px`

## Surface cues
- **Carbon** `#0b0e12`: Primary page background, base layer.
- **Graphite** `#1f2124`: Card and secondary section backgrounds, subtly raised from the base.
- **Deep Teal** `#002923`: Background for active components like filled buttons and badges, indicating interaction.

## Component cues
- **Primary Filled Button**: High-priority action button
- **Ghost Button**: Secondary action button for less emphasis
- **Navigation Link**: Main navigation and textual links
- **Badge (Active)**: Indicates status or small informational tags for active states
- **Badge (Inactive)**: Indicates status or small informational tags for inactive states

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
