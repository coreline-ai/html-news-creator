# AgentQL - Refero Design MD

- Source: https://styles.refero.design/style/d5307f56-76de-4d13-9741-f969c42e9aa5
- Original site: https://www.agentql.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep space console: layered dark surfaces, focused luminosity.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Gaze | `#0e111b` | neutral | Primary text or dark surface |
| Astral Deep | `#0d172b` | neutral | Primary text or dark surface |
| Nebula Black | `#050606` | neutral | Primary text or dark surface |
| Crystal White | `#ffffff` | neutral | Page background or card surface |
| Lunar Dust | `#abaebb` | neutral | Border, muted text, or supporting surface |
| Ash Outline | `#777a88` | neutral | Border, muted text, or supporting surface |
| Comet Grey | `#c7c9d1` | neutral | Border, muted text, or supporting surface |
| Twilight Indigo | `#12244f` | brand | Action accent / signal color |
| Cosmic Violet | `#1b346e` | brand | Action accent / signal color |
| Starlight Violet | `#85a6e9` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-gaze: #0e111b;
  --ref-astral-deep: #0d172b;
  --ref-nebula-black: #050606;
  --ref-crystal-white: #ffffff;
  --ref-lunar-dust: #abaebb;
  --ref-ash-outline: #777a88;
  --ref-comet-grey: #c7c9d1;
  --ref-twilight-indigo: #12244f;
}
```

## Typography direction
- **Figtree**: 500, 600, 32px, 36px, 44px, 48px, 64px, 1.00, 1.13; substitute `Montserrat`.
- **Inter**: 300, 400, 500, 600, 9px, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 28px, 40px, 1.00, 1.13, 1.25, 1.38, 1.50; substitute `Inter`.
- **IBM Plex Mono**: 400, 13px, 1.00, 1.25, 1.50; substitute `JetBrains Mono`.

## Spacing / shape
- Section Gap: `104px`
- Card Padding: `16px`
- Element Gap: `4px`
- Page Max Width: `1408px`
- Radius: `cards: 12px, badges: 9999px, inputs: 8px, modals: 12px, buttons: 9999px`

## Surface cues
- **Page Canvas** `#0b0c0`: The deepest, foundational background of the entire page.
- **Base Surface** `#0e111b`: Primary background for main content areas and standard cards.
- **Elevated Surface** `#0d172b`: Used for sections with slightly more prominence or interactive components.
- **Accent Card Surface** `#12244f`: Distinct card background, often for highlighted features or integrations.

## Component cues
- **Primary Ghost Button**: Main action button for driving user engagement, appearing as an outlined element against dark backgrounds.
- **Filled Secondary Button**: Secondary calls to action or interactive toggles.
- **Integration Grid Card**: Displaying individual integration partners, with varied background colors to add visual interest to groupings.
- **Elevated Content Card**: Standard container for content blocks, features, or pricing tiers, providing an elevated surface.
- **Product Hunt Badge**: Prominent display of achievements or endorsements.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
