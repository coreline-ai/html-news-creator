# Reflect Notes - Refero Design MD

- Source: https://styles.refero.design/style/e7f92774-3c08-402b-917d-020ba1f3d489
- Original site: https://reflect.app
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Orbit in a Dark Universe. It feels like navigating a personal cosmos of interconnected thoughts, illuminated by subtle internal light.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Violet | `#030014` | neutral | Action accent / signal color |
| Subtle Violet | `#060317` | neutral | Action accent / signal color |
| Twilight Graphite | `#10093a` | neutral | Primary text or dark surface |
| Whisper White | `#ffffff` | neutral | Page background or card surface |
| Shadowed Slate | `#f4f0ff` | neutral | Page background or card surface |
| Muted Ash | `#a8a6b7` | neutral | Border, muted text, or supporting surface |
| Passive Gray | `#918ea0` | neutral | Border, muted text, or supporting surface |
| Inactive Steel | `#54525f` | neutral | Border, muted text, or supporting surface |
| Reflect Violet | `#5046e4` | brand | Action accent / signal color |
| Interactive Violet | `#9382ff` | brand | Action accent / signal color |

```css
:root {
  --ref-deep-violet: #030014;
  --ref-subtle-violet: #060317;
  --ref-twilight-graphite: #10093a;
  --ref-whisper-white: #ffffff;
  --ref-shadowed-slate: #f4f0ff;
  --ref-muted-ash: #a8a6b7;
  --ref-passive-gray: #918ea0;
  --ref-inactive-steel: #54525f;
}
```

## Typography direction
- **AeonikPro**: 500, 24px, 32px, 48px, 56px, 72px, 1.11, 1.14, 1.17, 1.25, 1.33; substitute `Montserrat`.
- **Inter V**: 400, 500, 12px, 13px, 14px, 15px, 16px, 18px, 1.20, 1.33, 1.43, 1.50, 1.54, 1.56, 1.60, 1.85; substitute `Inter`.

## Spacing / shape
- Section Gap: `72-120px`
- Radius: `cards: 16px, buttons: 6px, default: 5px, accentTags: 32px`

## Component cues
- **CTA Badge + Hero Buttons**: Reference component style.
- **Feature Grid Cards**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **Primary Call-to-Action Button**: Main user action.
- **Secondary Ghost Button**: Minor actions, navigation, or less prominent calls to action.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
