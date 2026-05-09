# KeepGrading - Refero Design MD

- Source: https://styles.refero.design/style/2f0a053b-0596-4212-a4f4-8a7b580acb90
- Original site: https://www.keepgrading.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery in an Empty Room

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#080808` | neutral | Primary text or dark surface |
| Canvas White | `#f8f8f8` | neutral | Page background or card surface |
| Onyx Shadow | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-void-black: #080808;
  --ref-canvas-white: #f8f8f8;
  --ref-onyx-shadow: #000000;
}
```

## Typography direction
- **Inter**: 400, 16px, 20px, 1.40, 1.50; substitute `system-ui`.
- **Cabinet Grotesk**: 400, 16px, 20px, 24px, 96px, 1.00, 1.33, 1.40, 1.50; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `15px`
- Radius: `cards: 160px, buttons: 9999px, navigation: 9999px`

## Component cues
- **Navigation Link**: Top-level navigation items and secondary links.
- **Primary Heading**: Main page titles and large section headings.
- **Ghost Button**: Secondary calls to action or navigation elements.
- **Media Card**: Containers for images and videos with associated text.
- **Menu Toggle Button**: Hamburger menu icon for mobile or hidden navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
