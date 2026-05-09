# Felt - Refero Design MD

- Source: https://styles.refero.design/style/127a4efb-685c-42c3-83eb-72bb410a8429
- Original site: https://www.felt.com
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep forest data canvas

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Canvas | `#3d521e` | neutral | Border, muted text, or supporting surface |
| Nightfall Surface | `#314218` | neutral | Primary text or dark surface |
| Text Primary | `#eeeeee` | neutral | Page background or card surface |
| Text Secondary | `#ffffff` | neutral | Page background or card surface |
| Text Tertiary | `#333333` | neutral | Primary text or dark surface |
| Warm Ember | `#dc8c46` | brand | Action accent / signal color |
| Muted Sage | `#64754b` | neutral | Border, muted text, or supporting surface |
| Felt Deepest Green | `#212f0c` | neutral | Action accent / signal color |
| Felt Darkest Base | `#18210c` | neutral | Primary text or dark surface |

```css
:root {
  --ref-forest-canvas: #3d521e;
  --ref-nightfall-surface: #314218;
  --ref-text-primary: #eeeeee;
  --ref-text-secondary: #ffffff;
  --ref-text-tertiary: #333333;
  --ref-warm-ember: #dc8c46;
  --ref-muted-sage: #64754b;
  --ref-felt-deepest-green: #212f0c;
}
```

## Typography direction
- **Gt Alpina Standard**: 300, 400, 28px, 36px, 43px, 46px, 50px, 86px, 0.80, 0.96, 1.00, 1.11, 1.33; substitute `Georgia`.
- **Atlasgrotesk Cy Web**: 300, 400, 500, 700, 12px, 14px, 16px, 18px, 19px, 20px, 1.00, 1.11, 1.20, 1.25, 1.30, 1.33, 1.43, 1.50, 1.56; substitute `Inter`.
- **Arial**: 400, 14px, 16px, 1.25, 1.33, 1.43; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `12px`
- Element Gap: `12px`
- Radius: `buttons: 20px, default: 6px`

## Surface cues
- **Felt Darkest Base** `#18210c`: Lowest base layer, for deep background or the most recessed elements.
- **Felt Deepest Green** `#212f0c`: First level of elevated surface, typically for UI containers and card backgrounds within the main content area.
- **Nightfall Surface** `#314218`: Secondary elevated surface, providing a slight visual lift from base backgrounds for data panels or content blocks.
- **Forest Canvas** `#3d521`: Primary page background and large content section canvas, establishing the overall dark green tone.

## Component cues
- **Primary Action Button**: Main call-to-action button, drawing attention with the brand's accent color.
- **Secondary Action Button**: Subtle button with a transparent background, used for secondary actions or navigation.
- **Ghost Navigation Button**: Navigation items in the header, acting as ghost buttons.
- **Outline Link Button (Warm Ember)**: Outlined button or link, using the brand accent color for border and text.
- **Badge Neutral**: Inline labels or small informational markers.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
