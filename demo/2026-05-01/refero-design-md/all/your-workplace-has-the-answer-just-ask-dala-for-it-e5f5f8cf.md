# Your workplace has the answer. Just ask Dala for it. - Refero Design MD

- Source: https://styles.refero.design/style/e5f5f8cf-e68d-4ed1-bbf5-6b67569af648
- Original site: https://dala.craftedbygc.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep space digital holo-deck

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Holo White | `#ffffff` | neutral | Page background or card surface |
| Stardust Gray | `#bdbdbd` | neutral | Border, muted text, or supporting surface |
| Ghost Gray | `#9a9a9a` | neutral | Border, muted text, or supporting surface |
| Cosmic Violet | `#8052ff` | brand | Action accent / signal color |
| Sunflare Yellow | `#ffb829` | accent | Action accent / signal color |
| Quantum Teal | `#15846e` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-holo-white: #ffffff;
  --ref-stardust-gray: #bdbdbd;
  --ref-ghost-gray: #9a9a9a;
  --ref-cosmic-violet: #8052ff;
  --ref-sunflare-yellow: #ffb829;
  --ref-quantum-teal: #15846e;
}
```

## Typography direction
- **Acronym**: 200, 400, 600, 700, 12px, 14px, 15px, 18px, 24px, 27px, 36px, 42px, 48px, 78px, 113px, 0.81, 0.90, 1.00, 1.10, 1.20, 1.25, 1.30, 1.50; substitute `Montserrat, Raleway`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `15px`
- Element Gap: `6px`
- Radius: `cards: 24px, buttons: 24px, navItems: 24px`

## Component cues
- **Primary Action Button**: Main call-to-action
- **Ghost Navigation Button**: Secondary navigation or text-based actions
- **Naked Link**: Inline text links
- **Main Header**: Site-wide sticky header

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
