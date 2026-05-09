# Lama Lama - Refero Design MD

- Source: https://styles.refero.design/style/8e26bf8a-44b8-4fe1-9b4b-188dd5827c0f
- Original site: https://lamalama.nl
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight theater with luminous text

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Charcoal | `#111314` | neutral | Primary text or dark surface |
| Polar Mist | `#d7f3f5` | brand | Action accent / signal color |
| Void Black | `#020203` | neutral | Primary text or dark surface |

```css
:root {
  --ref-deep-charcoal: #111314;
  --ref-polar-mist: #d7f3f5;
  --ref-void-black: #020203;
}
```

## Typography direction
- **SuisseIntl**: 300, 400, 500, 700, 10px, 12px, 14px, 16px, 30px, 40px, 50px, 134px, 0.86, 1.00, 1.06, 1.17, 1.22, 1.25, 1.38, 1.50, 1.56; substitute `Inter`.

## Spacing / shape
- Section Gap: `60-80px`
- Card Padding: `40px`
- Element Gap: `8-10px`
- Radius: `cards: 15px, buttons: 8px, interactiveElements: 15px`

## Surface cues
- **Void Black** `#020203`: Base page background and secondary surface level for cards or content blocks.
- **Deep Charcoal** `#111314`: Primary content surface background, used for significant sections and card backgrounds against the base.

## Component cues
- **Ghost Action Button**: Primary interactive control for calls to action or navigation.
- **Feature Card**: Container for project highlights or content blocks.
- **Navigation Link**: Interactive text link within headers and footers.
- **Hero Headline**: Prominent headline for introductory sections.
- **Play Showreel Button**: Specific action button for media playback.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
