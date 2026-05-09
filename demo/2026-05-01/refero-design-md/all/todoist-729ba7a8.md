# Todoist - Refero Design MD

- Source: https://styles.refero.design/style/729ba7a8-35d5-44f3-abc0-1078ff6a3467
- Original site: https://todoist.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm, minimal productivity suite. Like a neatly organized desk bathed in natural light.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Paper White | `#fefdfc` | neutral | Page background or card surface |
| Soft Gray | `#d7d6d4` | neutral | Border, muted text, or supporting surface |
| Light Peach | `#fff6f0` | neutral | Page background or card surface |
| Subtle Ash | `#6f6c69` | neutral | Border, muted text, or supporting surface |
| True Black | `#000000` | neutral | Primary text or dark surface |
| Dusty Sage | `#94928f` | neutral | Border, muted text, or supporting surface |
| Action Red | `#e34432` | brand | Action accent / signal color |
| Link Orange | `#cf3520` | brand | Action accent / signal color |
| Accent Blue | `#0f66ae` | accent | Action accent / signal color |
| Success Green | `#4c7a45` | semantic | Action accent / signal color |

```css
:root {
  --ref-paper-white: #fefdfc;
  --ref-soft-gray: #d7d6d4;
  --ref-light-peach: #fff6f0;
  --ref-subtle-ash: #6f6c69;
  --ref-true-black: #000000;
  --ref-dusty-sage: #94928f;
  --ref-action-red: #e34432;
  --ref-link-orange: #cf3520;
}
```

## Typography direction
- **Graphik**: 400, 600, 700, 16px, 22px, 38px, 44px, 55px, 1.00, 1.15, 1.28; substitute `system-ui`.
- **Inter**: 400, 475, 500, 600, 625, 700, 12px, 14px, 15px, 16px, 17px, 18px, 19px, 21px, 1.00, 1.35, 1.40, 1.50, 1.60, 1.75; substitute `system-ui`.
- **Arial**: 400, 13px, 1.20; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `0px`
- Element Gap: `4px`
- Radius: `cards: 10px, badges: 6px, images: 15px, buttons: 15px, default: 8px`

## Component cues
- **Primary CTA Button Group**: Reference component style.
- **Announcement Banner**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **Primary Action Button**: Main call to action
- **Text Only Button**: Secondary action in nav/toolbar

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
