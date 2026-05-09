# 10X HUB - Refero Design MD

- Source: https://styles.refero.design/style/4acc13a0-c553-40d7-b78d-a9b6a4e94486
- Original site: https://10xdesigners.co
- Theme: `mixed`
- Industry: `agency`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast dynamic ledger. Stark black and white pages punctuated by sharp red markers.

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Scarlet Flash | `#ff1841` | brand | Action accent / signal color |
| Crimson Link | `#7b0016` | brand | Action accent / signal color |
| Input Gray | `#e8e6e6` | neutral | Page background or card surface |
| Accent Gray | `#949494` | neutral | Border, muted text, or supporting surface |
| Icon Gray | `#757575` | neutral | Border, muted text, or supporting surface |
| Indicator Blue | `#5e97ff` | accent | Action accent / signal color |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-pure-white: #ffffff;
  --ref-scarlet-flash: #ff1841;
  --ref-crimson-link: #7b0016;
  --ref-input-gray: #e8e6e6;
  --ref-accent-gray: #949494;
  --ref-icon-gray: #757575;
  --ref-indicator-blue: #5e97ff;
}
```

## Typography direction
- **Arial**: 400, 10px, 13px, 1.20; substitute `Arial`.
- **helvetica-w01-roman**: 400, 13px, 14px, 15px, 18px, 31px, 45px, 1.00, 1.20, 1.40, 1.60; substitute `Helvetica Neue`.
- **wfont_9aea05_daebdda91ced4d119f7837b7bae26e19**: 400, 24px, 298px, 1.00; substitute `Roboto Mono`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `misc: 12px, inputs: 0px, buttons: 999px`

## Component cues
- **Submit Resource CTA Button**: Reference component style.
- **Submit Resource Form**: Reference component style.
- **Toggle Switch & Header Controls**: Reference component style.
- **Primary Call to Action Button**: Interactive element
- **Ghost Header Button**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
