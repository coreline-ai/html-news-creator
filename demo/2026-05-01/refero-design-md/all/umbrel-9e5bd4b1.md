# Umbrel - Refero Design MD

- Source: https://styles.refero.design/style/9e5bd4b1-0ba8-4592-a5ec-a935bd4ea9c6
- Original site: https://umbrel.com
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Space Luxury Console. The UI is a console in a dark, high-tech environment, with glowing accents and soft, tactile controls.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Obsidian Surface | `#292929` | neutral | Primary text or dark surface |
| Onyx Shadow | `#180f03` | neutral | Primary text or dark surface |
| Moonlight Glimmer | `#ffffff` | neutral | Page background or card surface |
| Warm Gray | `#61635d` | neutral | Border, muted text, or supporting surface |
| Cool Steel | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Pale Mist | `#e0e0e0` | neutral | Page background or card surface |
| System Gray | `#797985` | neutral | Border, muted text, or supporting surface |
| #0a0a0a | `#0a0a0a` | neutral | Primary text or dark surface |
| Violet Impulse | `#5351f3` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-obsidian-surface: #292929;
  --ref-onyx-shadow: #180f03;
  --ref-moonlight-glimmer: #ffffff;
  --ref-warm-gray: #61635d;
  --ref-cool-steel: #cccccc;
  --ref-pale-mist: #e0e0e0;
  --ref-system-gray: #797985;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 12px, 13px, 14px, 16px, 18px, 20px, 23px, 24px, 27px, 32px, 36px, 48px, 1.10, 1.20, 1.24, 1.30, 1.40; substitute `system-ui, sans-serif`.
- **Inter Display**: 600, 43px, 1.20; substitute `system-ui, sans-serif`.
- **Inter Tight**: 500, 12px, 1.20; substitute `system-ui, sans-serif`.

## Spacing / shape
- Card Padding: `12px`
- Radius: `cards: 24px, pills: 99px, images: 12px, inputs: 20px, buttons: 32px, default: 16px`

## Component cues
- **Product Cards — Umbrel Home & umbrelOS**: Reference component style.
- **Umbrel Pro Hero Banner**: Reference component style.
- **Feature Teaser Cards — App Showcase**: Reference component style.
- **Primary Filled Button**: Main call-to-action button, highlighted against dark backgrounds.
- **Ghost Button**: Secondary action or navigation element, subtle interaction.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
