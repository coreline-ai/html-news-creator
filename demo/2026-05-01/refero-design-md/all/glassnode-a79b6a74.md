# Glassnode - Refero Design MD

- Source: https://styles.refero.design/style/a79b6a74-6b67-4c9f-9d69-bff80869b943
- Original site: https://glassnode.com
- Theme: `mixed`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Analytical Console on Dark Steel. The design feels like a sophisticated yet functional tool built for focused data analysis, emphasizing clarity with deliberate restraint.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#1a1a1a` | neutral | Primary text or dark surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Cloud Gray | `#f7f8fa` | neutral | Page background or card surface |
| Ash Concrete | `#edeff2` | neutral | Page background or card surface |
| Stone Whisper | `#dedfe1` | neutral | Page background or card surface |
| Slate Text | `#5a5a5a` | neutral | Border, muted text, or supporting surface |
| Granite Text | `#6f6f6f` | neutral | Border, muted text, or supporting surface |
| Mist Gray | `#a0a0a0` | neutral | Border, muted text, or supporting surface |
| Deep Marine | `#e2e7fc` | brand | Action accent / signal color |
| Violet Signal | `#8fa5f6` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-charcoal: #1a1a1a;
  --ref-arctic-white: #ffffff;
  --ref-cloud-gray: #f7f8fa;
  --ref-ash-concrete: #edeff2;
  --ref-stone-whisper: #dedfe1;
  --ref-slate-text: #5a5a5a;
  --ref-granite-text: #6f6f6f;
  --ref-mist-gray: #a0a0a0;
}
```

## Typography direction
- **Inter**: 400, 500, 700, 12px, 14px, 16px, 20px, 24px, 32px, 1.00, 1.20, 1.30, 1.40, 1.50; substitute `system-ui, sans-serif`.
- **Fraktion**: 700, 56px, 1.20; substitute `Inter, system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `inputs: 2px, buttons: 2px, general: 2px`

## Component cues
- **Announcement Banner + CTA Buttons**: Reference component style.
- **Feature List — Dark Section**: Reference component style.
- **Research Cards + Email Subscribe**: Reference component style.
- **Primary Navigation Link**: Interactive element
- **Hero CTA Button**: Call to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
