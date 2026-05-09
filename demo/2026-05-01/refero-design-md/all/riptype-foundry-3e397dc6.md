# Riptype Foundry - Refero Design MD

- Source: https://styles.refero.design/style/3e397dc6-0e68-435f-9dee-1966a9d245d3
- Original site: https://www.riptype.xyz
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Slate Terminal

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#121212` | neutral | Primary text or dark surface |
| Obsidian | `#292929` | neutral | Primary text or dark surface |
| Frost | `#ffffff` | neutral | Page background or card surface |
| Pale Ash | `#d0d0d0` | neutral | Border, muted text, or supporting surface |
| Steel Grey | `#a0a0a0` | neutral | Border, muted text, or supporting surface |
| Charger Green | `#d9ff00` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #121212;
  --ref-obsidian: #292929;
  --ref-frost: #ffffff;
  --ref-pale-ash: #d0d0d0;
  --ref-steel-grey: #a0a0a0;
  --ref-charger-green: #d9ff00;
}
```

## Typography direction
- **Office**: 400, 700, 12px, 16px, 43px, 0.95, 1.00, 1.19, 1.20, 1.58; substitute `Arial`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `12px`
- Element Gap: `6px`
- Page Max Width: `285px`
- Radius: `buttons: 4px, pillButtons: 144px`

## Surface cues
- **Canvas** `#121212`: The foundational background for the entire page and most primary content blocks.
- **Surface** `#292929`: A slightly lighter dark background used for secondary interactive elements like buttons, providing a subtle visual lift.
- **Glass Overlay** `#18181866`: Transparent, blurred overlay for potential modals or ephemeral UI elements, hinting at depth without heavy shadows.

## Component cues
- **Pill Accent Button**: Primary action button, often for CTAs or key navigation.
- **Standard Button**: Secondary action button for general interactivity.
- **Menu Item Card**: Interactive list items, used in navigational menus.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
