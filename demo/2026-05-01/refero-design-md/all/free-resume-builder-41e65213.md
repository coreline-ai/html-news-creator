# Free Resume Builder - Refero Design MD

- Source: https://styles.refero.design/style/41e65213-1c4a-41c4-b715-50427fa8926e
- Original site: https://resume.io
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Calm productivity, like a well-organized office. Light-filled and orderly, with key tools highlighted in a crisp blue.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Slate Text | `#1e2532` | neutral | Primary text or dark surface |
| Midtone Gray | `#656e83` | neutral | Border, muted text, or supporting surface |
| Soft Gray | `#828ba2` | neutral | Border, muted text, or supporting surface |
| Hover Gray | `#9fa6bb` | neutral | Border, muted text, or supporting surface |
| Light Steel | `#d9deeb` | neutral | Page background or card surface |
| Faded Blueprint | `#f1f2ff` | neutral | Action accent / signal color |
| Whisper White | `#f7f9fc` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Action Blue | `#1a91f0` | brand | Action accent / signal color |
| Recruiter Blue | `#1a1c6a` | brand | Action accent / signal color |

```css
:root {
  --ref-slate-text: #1e2532;
  --ref-midtone-gray: #656e83;
  --ref-soft-gray: #828ba2;
  --ref-hover-gray: #9fa6bb;
  --ref-light-steel: #d9deeb;
  --ref-faded-blueprint: #f1f2ff;
  --ref-whisper-white: #f7f9fc;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **TT Commons**: 400, 500, 600, 14px, 15px, 16px, 18px, 19px, 22px, 24px, 28px, 31px, 40px, 52px, 67px, 0.96, 1.00, 1.07, 1.14, 1.16, 1.17, 1.20, 1.22, 1.25, 1.26, 1.27, 1.43; substitute `Inter`.

## Spacing / shape
- Section Gap: `48-80px`
- Card Padding: `24px`
- Element Gap: `4px`
- Radius: `tags: 24px, cards: 4px, images: 4px, buttons: 4px, pillButtons: 36px`

## Component cues
- **Hero CTA Button Group**: Reference component style.
- **Feature Tool Cards**: Reference component style.
- **Stats & Feature Highlights**: Reference component style.
- **Secondary Outline Button**: Alternative action button
- **Rounded Service Card**: Feature or service description

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
