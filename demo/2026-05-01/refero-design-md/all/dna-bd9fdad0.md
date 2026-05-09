# DNA - Refero Design MD

- Source: https://styles.refero.design/style/bd9fdad0-ebe6-4546-a5c0-ed132ed0a471
- Original site: https://dnacapital.com
- Theme: `dark`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight data stream, whispered authority

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#070708` | neutral | Primary text or dark surface |
| Arctic Mist | `#ffffff` | neutral | Page background or card surface |
| Ghost Gray | `#8f8f93` | neutral | Border, muted text, or supporting surface |
| Deep Space Blue | `#1954ec` | brand | Action accent / signal color |
| Fading Nebula Gradient | `#423676` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #070708;
  --ref-arctic-mist: #ffffff;
  --ref-ghost-gray: #8f8f93;
  --ref-deep-space-blue: #1954ec;
  --ref-fading-nebula-gradient: #423676;
}
```

## Typography direction
- **Darius**: 300, 45px, 52px, 54px, 72px, 1.13, 1.34; substitute `Playfair Display`.
- **Graphik**: 200, 300, 400, 500, 9px, 10px, 13px, 14px, 15px, 18px, 59px, 0.90, 1.00, 1.20, 1.40, 1.50, 1.55, 1.80; substitute `Inter`.
- **Arial**: 400, 500, 13px, 1.20; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `59px`
- Card Padding: `23px`
- Element Gap: `23px`
- Radius: `links: 4px`

## Surface cues
- **Midnight Ink Canvas** `#070708`: Primary page background, foundation for all content.
- **Arctic Mist Card Surface** `#ffffff`: Used sparingly for content cards or highlighted information blocks where a light surface is contextually necessary, providing stark contrast against…

## Component cues
- **Ghost Button**: Minimal interactive button for secondary actions or navigation.
- **Icon Button (Menu)**: Navigation toggle or action with a minimalist icon.
- **Text Link with Underline**: Inline navigation or reference links.
- **Scroll Indicator Button**: Visual cue for page progression.
- **Small Badge**: Informational marker or tag.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
