# RainbowKit - Refero Design MD

- Source: https://styles.refero.design/style/7421c174-a1b1-4695-a9e7-a82dc6f5ea3b
- Original site: https://www.rainbowkit.com
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Nebula Canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Eclipse Black | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Slate Deep | `#1b1c1e` | neutral | Primary text or dark surface |
| Charcoal Grey | `#25292e` | neutral | Primary text or dark surface |
| Vivid Blue | `#0e76fd` | brand | Action accent / signal color |
| Deep Violet | `#38228f` | brand | Action accent / signal color |
| Sky Blue | `#3898ff` | brand | Action accent / signal color |
| Azure Glow | `#5f5afa` | accent | Action accent / signal color |
| Flamingo Pink | `#ff5ca0` | accent | Action accent / signal color |
| Volcanic Red | `#fa423c` | accent | Action accent / signal color |

```css
:root {
  --ref-eclipse-black: #000000;
  --ref-cloud-white: #ffffff;
  --ref-slate-deep: #1b1c1e;
  --ref-charcoal-grey: #25292e;
  --ref-vivid-blue: #0e76fd;
  --ref-deep-violet: #38228f;
  --ref-sky-blue: #3898ff;
  --ref-azure-glow: #5f5afa;
}
```

## Typography direction
- **SFRounded**: 400, 500, 600, 700, 800, 11px, 14px, 16px, 18px, 20px, 24px, 40px, 52px, 1.00, 1.05, 1.17, 1.20, 1.25, 1.29, 1.31, 1.33.
- **Arial**: 400, 13px, 16px, 1.20.
- **system-ui**: 400, 20px, 1.05.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `18px`
- Element Gap: `12px`
- Radius: `cards: 24px, icons: 12px, buttons: 9999px, default: 6px`

## Surface cues
- **Page Canvas** `#000000`: Dominant background for the entire application, creating a deep, immersive dark mode experience.
- **Base Surface** `#1b1c1`: Used for sections or panels that rest directly on the page canvas, providing a slight elevation without heavy shadows.
- **Elevated Surface** `#25292`: Further elevated elements like cards or modals, offering a distinct visual separation from the base surface.
- **Light Modal Surface** `#ffffff`: A deliberate contrast for pop-ups or specific modals, creating a focused, light-themed interaction layer within the dark environment.

## Component cues
- **Ghost Button**: Ghost interactive element for secondary actions.
- **Primary Action Button**: Main call-to-action button, conveying primary interaction.
- **Icon Button (Circular)**: Small, circular button for actions related to icons or status.
- **Modal Card (Light)**: Elevated container primarily for interactive dialogs or pop-ups.
- **Code Snippet Container**: Container for showcasing code or command-line instructions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
