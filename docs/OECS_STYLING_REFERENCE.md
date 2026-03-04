# OECS live site styling reference

Captured from oecs.mit.edu (PubPub) for porting to the static Hugo clone.

## Colors

| Token | Live value | Maps to |
|-------|------------|---------|
| Accent / primary | `#000000` | `--oecs-accent`, header/footer text |
| Header background | `#FFFFFF` | `--oecs-header-bg` |
| Footer background | `#FFFFFF` | `--oecs-footer-bg` |
| Header/footer/nav text | `#000000` | `--oecs-header-color` |
| Border (banner/divider) | `#474747` (0.5px solid) | `--oecs-color-border` |
| Body text | dark (inherited) | `--oecs-color-text` |
| Links (in content) | accent / black | `--oecs-color-link` |

## Typography

- **Font family:** Noto Sans, fallbacks: BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue, sans-serif.
- **Weights in use:** 300 (light), 400 (regular), 500 (medium); italic 300 for hero/quote.
- **Body (article):** 18px, line-height 30px (`.pub-body-component .editor.ProseMirror p`).
- **Layout text (general):** 16px, line-height 1.6.
- **H1:** line-height 1.25em, font-weight 500.
- **H2 (banner/hero):** 32px, line-height 1.5em, font-weight 300, padding 50px 0.
- **Hero/quote text:** 20px, font-weight 300, italic, line-height 1.5em.

## Layout

- **Content width:** Max width 720px (matches our `--oecs-max-width`). Live site also uses ~60–65% width for some text blocks.
- **Banner border:** 0.5px #474747 solid below header/banner.

## Responsive

- **Breakpoint:** 720px.
- Below 720px: hero text 16px, width 100%; H2 26px, width 85%; body text width 90%; article body 18px / 27px line-height.

## Notes

- OECS uses custom @font-face with PubPub-hosted Noto Sans (Regular, Light, LightItalic, Medium). Clone can use Google Fonts Noto Sans for equivalent weights.
- Header/footer/nav use white background and black text (accent inverted for chrome).
