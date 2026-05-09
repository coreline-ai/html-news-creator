# Dot Inc. - Refero Design MD

- Source: https://styles.refero.design/style/4bcd0728-0d28-4835-ba9f-d61554f797b1
- Original site: https://pad.dotincorp.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp monochrome utility with orange spark

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#e5e7eb` | neutral | Page background or card surface |
| Dark Graphite | `#1f1f1f` | neutral | Primary text or dark surface |
| Stone Gray | `#b7bfc1` | neutral | Border, muted text, or supporting surface |
| Cloud Gray | `#f5f5f5` | neutral | Page background or card surface |
| Charcoal Text | `#333333` | neutral | Primary text or dark surface |
| Mid Gray | `#707070` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#dddddd` | neutral | Page background or card surface |
| Sunburst Orange | `#ff5a2f` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-ash-gray: #e5e7eb;
  --ref-dark-graphite: #1f1f1f;
  --ref-stone-gray: #b7bfc1;
  --ref-cloud-gray: #f5f5f5;
  --ref-charcoal-text: #333333;
  --ref-mid-gray: #707070;
}
```

## Typography direction
- **Plus Jakarta Sans**: 300, 400, 500, 600, 700, 800, 12px, 14px, 15px, 16px, 18px, 20px, 22px, 24px, 30px, 32px, 40px, 46px, 50px, 60px, 80px, 1.34, 1.40, 1.45, 1.50, 1.60, 1.64, 1.78, 1.80; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `40px`
- Element Gap: `24px`
- Radius: `cards: 20px, forms: 30px, badges: 20px, images: 20px, buttons: 8px`

## Component cues
- **Primary Filled Button**: Primary call-to-action button, highly visible.
- **Outlined Call to Action Button**: Secondary action button, providing a clear but less dominant call to action.
- **Ghost Button**: Tertiary action button or navigation item.
- **Standard Card**: Container for content sections, features, or product details.
- **Alternating Background Card**: Container for content sections in an alternating background layout.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
