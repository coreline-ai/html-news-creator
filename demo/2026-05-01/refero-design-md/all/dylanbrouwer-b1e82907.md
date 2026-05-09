# Dylanbrouwer - Refero Design MD

- Source: https://styles.refero.design/style/b1e82907-d1cf-46cd-8ae7-3561c5b15fd0
- Original site: https://www.dylanbrouwer.design
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Brutalism meets engineered minimalism.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Slate | `#3c3a3e` | neutral | Primary text or dark surface |
| Ghost Gray | `#a2a2a2` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Platinum Mist | `#c9c7cc` | neutral | Border, muted text, or supporting surface |
| Silver Dust | `#f1f1f1` | neutral | Page background or card surface |
| Cool Stone | `#7b7a7c` | neutral | Border, muted text, or supporting surface |
| Deep Space | `#161616` | neutral | Primary text or dark surface |
| Sunrise Orange | `#ff4c24` | accent | Action accent / signal color |
| Action Orange | `#ff6436` | accent | Action accent / signal color |
| Grey Scale Gradient | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-ink-slate: #3c3a3e;
  --ref-ghost-gray: #a2a2a2;
  --ref-canvas-white: #ffffff;
  --ref-platinum-mist: #c9c7cc;
  --ref-silver-dust: #f1f1f1;
  --ref-cool-stone: #7b7a7c;
  --ref-deep-space: #161616;
  --ref-sunrise-orange: #ff4c24;
}
```

## Typography direction
- **Die Grotesk B**: 500, 12px, 17px, 18px, 21px, 36px, 54px, 60px, 1.00, 1.10, 1.25, 1.30; substitute `Arial, Helvetica, sans-serif`.
- **IBM Plex Mono**: 500, 600, 12px, 14px, 1.00, 1.20, 1.30; substitute `Consolas, Monaco, monospace`.
- **ABC Gravity Variable**: 400, 500, 12px, 24px, 96px, 274px, 288px, 0.74, 1.00, 1.30; substitute `Arial, Helvetica, sans-serif`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `12px`
- Element Gap: `6px`
- Radius: `all: 14.4px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, creating a bright, spacious default context.
- **Silver Dust** `#f1f1f1`: Secondary background for alternating content sections, providing a subtle visual break.
- **Card White Subtle** `#ffffff`: Semi-transparent card surfaces using 'rgba(255, 255, 255, 0.5)', creating a frosted, layered effect.
- **Deep Space** `#161616`: Used for sections or elements requiring maximum visual weight and contrast, often as a dark background for strong headlines.

## Component cues
- **Ghost Button**: Text-based navigation or secondary actions
- **Card (Transparent)**: Informational grouping, background for labels
- **Card (White Subtle)**: Content container with slight prominence
- **Badge (Transparent)**: Categorization or decorative text labels
- **Badge (Vivid Accent)**: Small, high-visibility status indicators

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
