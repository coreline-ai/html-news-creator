# Superwhisper - Refero Design MD

- Source: https://styles.refero.design/style/b8a8976c-52d9-4ebb-95ea-4c40f4a9acab
- Original site: https://superwhisper.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Celestial Command Center: A dark, gradient-infused UI where sharp, functional elements glow with purpose against an expansive, cosmic void.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Eclipse | `#000000` | neutral | Primary text or dark surface |
| Starless Night | `#030719` | neutral | Primary text or dark surface |
| Twilight Ink | `#1c1d1f` | neutral | Primary text or dark surface |
| Ghostly Gray | `#e5e7eb` | neutral | Page background or card surface |
| Deep Ocean | `#001b33` | neutral | Primary text or dark surface |
| Frost | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#333333` | neutral | Primary text or dark surface |
| Iron Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Slate Gray | `#70757c` | neutral | Border, muted text, or supporting surface |
| Pewter | `#999999` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-eclipse: #000000;
  --ref-starless-night: #030719;
  --ref-twilight-ink: #1c1d1f;
  --ref-ghostly-gray: #e5e7eb;
  --ref-deep-ocean: #001b33;
  --ref-frost: #ffffff;
  --ref-ash-gray: #333333;
  --ref-iron-gray: #666666;
}
```

## Typography direction
- **Inter**: 300, 400, 500, 600, 700, 8px, 9px, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 24px, 30px, 31px, 48px, 60px, 1.00, 1.06, 1.07, 1.20, 1.25, 1.33, 1.40, 1.43, 1.45, 1.50, 1.56, 1.60, 1.63, 1.71; substitute `system-ui`.
- **ui-monospace**: 300, 400, 11px, 1.00, 1.30, 1.50; substitute `monospace`.
- **-apple-system**: 500, 9px, 10px, 1.60, 1.78; substitute `system-ui`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `card: 24px, pill: 9999px, image: 24px, button: 4px, default: 9px`

## Surface cues
- **Midnight Eclipse** `#000000`: Page background (base)
- **Starless Night** `#030719`: Subtle low-elevation background for cards/sections
- **Sky Blue Transparency** `#001b33`: Specialized card backgrounds, providing a cool dark tint
- **Frost** `#FFFFFF`: High-contrast card backgrounds, breaking the dark theme for emphasis

## Component cues
- **Primary Ghost Button**: Call to action
- **Pill Download Button (Light)**: Download action
- **Pill Download Button (Dark)**: Download action
- **Navigation Link**: Navigation element
- **Feature Card (Gradient BG)**: Content display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
