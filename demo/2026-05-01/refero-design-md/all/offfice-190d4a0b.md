# OFFFICE : - Refero Design MD

- Source: https://styles.refero.design/style/190d4a0b-0353-4fc8-be09-affa6e977146
- Original site: https://offficestud.io
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black Box Gallery; objects artfully framed within a deep, dark void, highlighted by stark text.

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#111111` | neutral | Primary text or dark surface |
| Exhibition White | `#fefefe` | neutral | Page background or card surface |

```css
:root {
  --ref-void-black: #111111;
  --ref-exhibition-white: #fefefe;
}
```

## Typography direction
- **ak**: 400, 700, 12px, 14px, 18px, 20px, 58px, 216px, 0.80, 0.90, 1.00, 1.10, 1.33, 1.40, 1.50, 1.56; substitute `Montserrat`.
- **gs**: 400, 12px, 72px, 0.90, 1.33; substitute `Roboto Mono`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `8px`
- Radius: `all: 0px`

## Component cues
- **Studio Tagline Block**: Reference component style.
- **Project Archive List**: Reference component style.
- **Project Detail Navigation Bar**: Reference component style.
- **Navigation Link**: Interactive text link
- **Hero Headline**: Dominant page title

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
