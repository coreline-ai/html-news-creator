# Josephmark - Refero Design MD

- Source: https://styles.refero.design/style/58c0af12-8706-428f-8282-482d57d7b90e
- Original site: https://josephmark.studio
- Theme: `light`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochromatic gallery space

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Platinum Mist | `#e5e7eb` | neutral | Page background or card surface |
| Cloud Gray | `#f4f5ef` | neutral | Page background or card surface |
| Granite | `#666666` | neutral | Border, muted text, or supporting surface |
| Stone | `#a9a498` | neutral | Border, muted text, or supporting surface |
| Carbon | `#4e5449` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight: #000000;
  --ref-canvas-white: #ffffff;
  --ref-platinum-mist: #e5e7eb;
  --ref-cloud-gray: #f4f5ef;
  --ref-granite: #666666;
  --ref-stone: #a9a498;
  --ref-carbon: #4e5449;
}
```

## Typography direction
- **Scto Grotesk A**: 300, 400, 500, 12px, 14px, 16px, 19px, 20px, 28px, 36px, 70px, 1.10, 1.20, 1.25, 1.38, 1.40, 1.50; substitute `Inter`.

## Spacing / shape
- Section Gap: `64-96px`
- Card Padding: `20px`
- Element Gap: `16px`
- Radius: `buttons: 9999px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background and default card background.
- **Cloud Gray** `#f4f5ef`: Secondary background for alternating content sections, providing minimal visual separation.
- **Midnight** `#000000`: Dominant background for hero elements, full-width banners, and high-impact content blocks to create stark contrast.

## Component cues
- **Ghost Primary Button**: Interactive element for main calls to action, appearing as a transparent pill with a white border.
- **Outlined Card Button**: Secondary action or category filter within content sections, offering structure through a subtle border.
- **Text Input (Underlined)**: Form element for user data entry, with a minimal, focus-driven border.
- **Navigation Link**: Interactive text link for site navigation and inline content, maintaining high contrast on all backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
