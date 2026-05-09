# Copy - Refero Design MD

- Source: https://styles.refero.design/style/1ae4bcfe-c613-42fc-aab7-f9583381e7cc
- Original site: https://copy.ai
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Strategic blueprint on polished steel. Organized hierarchy and vibrant violet accents against a muted canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#171717` | neutral | Primary text or dark surface |
| Cloud Burst | `#f6fafb` | neutral | Page background or card surface |
| Slate Echo | `#e4edf1` | neutral | Page background or card surface |
| Ash Veil | `#e2e8eb` | neutral | Page background or card surface |
| Graphite Tone | `#5d5d5d` | neutral | Border, muted text, or supporting surface |
| Violet Impulse | `#693edf` | brand | Action accent / signal color |
| Deep Space Violet | `#3b0d96` | brand | Action accent / signal color |
| Dawn Violet | `#c1b9f4` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #171717;
  --ref-cloud-burst: #f6fafb;
  --ref-slate-echo: #e4edf1;
  --ref-ash-veil: #e2e8eb;
  --ref-graphite-tone: #5d5d5d;
  --ref-violet-impulse: #693edf;
  --ref-deep-space-violet: #3b0d96;
  --ref-dawn-violet: #c1b9f4;
}
```

## Typography direction
- **ABC Normal**: 500, 600, 24px, 26px, 28px, 32px, 48px, 56px, 88px, 1.00, 1.18, 1.31, 1.40, 1.42, 1.50; substitute `Montserrat`.
- **ABC Normal Regular**: 400, 26px, 1.31; substitute `Montserrat`.
- **Inter**: 400, 500, 600, 700, 12px, 14px, 16px, 22px, 24px, 1.17, 1.33, 1.43, 1.45, 1.50, 1.57, 1.69, 2.00; substitute `Inter Variable`.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `30px`
- Element Gap: `16px`
- Radius: `buttons: 4px, default: 4px`

## Component cues
- **GTM AI Playbook Feature Card**: Reference component style.
- **GTM AI Platform Architecture Block**: Reference component style.
- **Hero Email CTA with Process Steps**: Reference component style.
- **Login Button**: Secondary call to action
- **Input Field**: User data entry

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
