# Brex - Refero Design MD

- Source: https://styles.refero.design/style/b58d92f6-68a8-4358-8fc9-6ea58e6d483b
- Original site: https://brex.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precision engineered toolkit — crisp, organized, and focused on clarity.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000710` | neutral | Primary text or dark surface |
| Action Orange | `#ff5900` | brand | Action accent / signal color |
| Primary Text | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Soft Gray | `#f3f3f7` | neutral | Page background or card surface |
| Muted Slate | `#b9bbc6` | neutral | Border, muted text, or supporting surface |
| Cool Stone | `#60646c` | neutral | Border, muted text, or supporting surface |
| Ash Gray | `#6f737b` | neutral | Border, muted text, or supporting surface |
| Silver Pine | `#8b8d98` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #000710;
  --ref-action-orange: #ff5900;
  --ref-primary-text: #000000;
  --ref-paper-white: #ffffff;
  --ref-soft-gray: #f3f3f7;
  --ref-muted-slate: #b9bbc6;
  --ref-cool-stone: #60646c;
  --ref-ash-gray: #6f737b;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 10px, 12px, 13px, 14px, 16px, 20px, 24px, 36px, 48px, 72px, 1.00, 1.20, 1.21, 1.33, 1.43, 1.50, 1.57; substitute `system-ui`.
- **Flecha**: 500, 36px, 1.11; substitute `serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24-32px`
- Element Gap: `8-16px`
- Radius: `cards: 12px, input: 0px, buttons: 6px, default: 6px, navItem: 10px`

## Component cues
- **Email Signup CTA Bar**: Reference component style.
- **Feature Product Cards Row**: Reference component style.
- **Cookie Consent Banner**: Reference component style.
- **Primary Action Button**: Calls to action
- **Navigation Link Button**: Header navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
