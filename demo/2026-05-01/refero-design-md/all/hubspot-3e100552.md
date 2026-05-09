# HubSpot - Refero Design MD

- Source: https://styles.refero.design/style/3e100552-a8ad-4179-b89a-6aa5113b92e1
- Original site: https://www.hubspot.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm,橙色效率

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#1f1f1f` | neutral | Primary text or dark surface |
| Canvas White | `#fcfcfa` | neutral | Page background or card surface |
| Frosted Gray | `#f8f5ee` | neutral | Page background or card surface |
| Midnight | `#000000` | neutral | Primary text or dark surface |
| Lead Gray | `#60605f` | neutral | Border, muted text, or supporting surface |
| Pale Ash | `#cacac8` | neutral | Border, muted text, or supporting surface |
| Marketing Orange | `#ff4800` | brand | Action accent / signal color |
| Accent Violet | `#0000c5` | accent | Action accent / signal color |
| Sunset Gradient | `#ff4900` | accent | Action accent / signal color |

```css
:root {
  --ref-ink-black: #1f1f1f;
  --ref-canvas-white: #fcfcfa;
  --ref-frosted-gray: #f8f5ee;
  --ref-midnight: #000000;
  --ref-lead-gray: #60605f;
  --ref-pale-ash: #cacac8;
  --ref-marketing-orange: #ff4800;
  --ref-accent-violet: #0000c5;
}
```

## Typography direction
- **HubSpot Sans**: 300, 400, 500, 12px, 14px, 16px, 18px, 22px, 24px, 40px, 1.10, 1.15, 1.42, 1.45, 1.56, 1.57, 1.60, 1.67, 1.75, 1.78, 2.40; substitute `Inter`.
- **HubSpot Serif Page Header Human**: 500, 80px, 1.19; substitute `Merriweather`.
- **HubSpot Serif**: 500, 40px, 48px, 1.10, 1.15; substitute `Merriweather`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `32px`
- Element Gap: `16px`
- Radius: `cards: 16px, badges: 4px, buttons: 8px`

## Surface cues
- **Canvas White** `#fcfcfa`: Base page background for most content areas, creating a bright and airy feel.
- **Default Card** `#ffffff`: Primary surface for grouping related content within cards, slightly lighter than Canvas White for subtle elevation.
- **Ink Black Footer** `#1f1f1f`: Deep, grounding background for the footer section, providing a strong visual anchor at the bottom of the page.

## Component cues
- **Primary Action Button**: Call-to-action button for initiating primary user flows.
- **Ghost Button (Text Link)**: Secondary action or navigational link mimicking button behavior.
- **Default Card**: Container for grouped content, features, or product listings.
- **Badge Pill**: Small informational tag, often for categorization or status.
- **Tag Badge**: Smaller, more compact informational tag.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
