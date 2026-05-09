# Threads - Refero Design MD

- Source: https://styles.refero.design/style/182f8743-fe22-45d3-98bc-9fd29d058602
- Original site: https://threads.net
- Theme: `light`
- Industry: `media`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Polaroid on white linen: clean, framed content on an understated, tactile canvas.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Text Black | `#000000` | neutral | Primary text or dark surface |
| Border Light | `#d5d5d5` | neutral | Border, muted text, or supporting surface |
| Muted Gray | `#969696` | neutral | Border, muted text, or supporting surface |
| Subtle Detail Gray | `#424242` | neutral | Border, muted text, or supporting surface |
| Active Violet | `#385898` | brand | Action accent / signal color |
| Link Blue | `#0095f6` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #fafafa;
  --ref-text-black: #000000;
  --ref-border-light: #d5d5d5;
  --ref-muted-gray: #969696;
  --ref-subtle-detail-gray: #424242;
  --ref-active-violet: #385898;
  --ref-link-blue: #0095f6;
}
```

## Typography direction
- **system-ui**: 400, 600, 700, 12px, 13px, 15px, 1.33, 1.40; substitute `Inter, Arial, Helvetica Neue`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `16px`
- Element Gap: `12px`
- Radius: `cards: 8px, images: 8px, avatars: 1000px, buttons: 1000px, feedPosts: 18px`

## Surface cues
- **Canvas White** `#fafafa`: Primary page background, base for all content.
- **Elevated Surface** `#efefef`: Subtly elevated content blocks or containers when a slight distinction from the canvas is needed.
- **Divider Gray** `#bcc0c4`: Used for hard dividers or structural elements that need more presence than a hairline border, but less than a full container.

## Component cues
- **Primary Filled Button**: Represents the most critical action on the page, like 'Log In'.
- **Ghost Icon Button**: Used for secondary, un-emphasized actions in navigation or content.
- **Ghost Icon Button - Rounded**: Used for specific icon actions like the 'Create' button in the sidebar.
- **Feed Post Card**: Container for individual content posts in the feed.
- **Active Link Text**: Text style for interactive links and primary brand emphasis.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
