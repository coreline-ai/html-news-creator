# ChatGPT - Refero Design MD

- Source: https://styles.refero.design/style/52a007ed-ad1b-46a6-bd44-b76f91df6d0c
- Original site: https://chatgpt.com
- Theme: `light`
- Recommended fit: **Visual board / presentation**

## North star
Frosted glass workstation. An environment of quiet focus, where soft grays frame crisp textual interaction.

## Why this fits html-news-creator
Useful for image-led demos, boardroom decks, and visual browsing of report sections.

## Apply to
- Visual Board / Focus Cards variants
- Boardroom deck slides
- Image evidence layouts

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#0d0d0d` | neutral | Primary text, critical headings, icons - its near-black depth offers strong contrast against the light surfaces. |
| Snow | `#ffffff` | neutral | Page backgrounds, card surfaces, interactive button fills - the purest backdrop for content. |
| Fog | `#f9f9f9` | neutral | Secondary background for navigation panels, subtly differentiating sidebars from main content areas. |
| Pewter | `#5d5d5d` | neutral | Secondary text, placeholder text - a muted gray that recedes subtly, hinting at information without demanding attention. |
| Stone | `#8f8f8f` | neutral | Placeholder text, inactive icons, subtle borders - an even lighter presence than Pewter, indicating non-primary element. |
| Arctic Mist | `#ececec` | neutral | Ghost button background for hover states, providing a faint highlight against white. |
| Link Blue | `#007aff` | accent | Interactive elements, links, indicating clickable actions within conversational text. |

```css
:root {
  --ref-carbon: #0d0d0d;
  --ref-snow: #ffffff;
  --ref-fog: #f9f9f9;
  --ref-pewter: #5d5d5d;
  --ref-stone: #8f8f8f;
  --ref-arctic-mist: #ececec;
  --ref-link-blue: #007aff;
}
```

## Typography direction
- Primary: **ui-sans-serif**; substitute `system-ui, sans-serif`.
- Secondary/code: **OpenAI Sans**; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section gap: `64px`
- Card padding: `20px`
- Element gap: `4px`
- Radius: `{'input': '28px', 'buttons': '10px', 'default': '10px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
