# Branded graphic

## Purpose

Make an on-brand image (a quote card, a tip, an announcement, or a carousel of slides) using the business's colours, fonts and logo, either in Canva or as a simple web page the owner screenshots.

## Use when

The owner asks for a visual: "make a graphic for this post", "turn these tips into a carousel", "quote card with this line", "an image announcing my new workshop", or another workflow needs an image.

## Load first

- `business/brand.md` (colours, fonts, logo, visual style, do and don't)
- `business/tools.md` (is Canva connected?)
- `business/profile.md` (business name and social handle for the footer)
- `business/voice.md` (if you're writing the words)
- The platform file in `.claude/skills/marketing/platforms/` (for the size)
- `departments/marketing/context.md`

## Steps

1. **Pin the brief.** You need: single image or carousel, the words on it, and the platform. If the words aren't given, write them: short heading (under about eight words), and an optional short body (under about 30 words) only if the heading needs backing up. If "Visual do and don't" in `brand.md` sets limits (for example "one line of text only" or "no more than two colours"), those win over these defaults and over the template's. For a carousel, plan the slides first: a hook slide, one point per slide, and a last slide with the next step. Default size is 1080 × 1350 portrait, which suits Instagram, LinkedIn and Facebook feeds. Use the platform file if it needs something else.
2. **Check the brand is filled in.** If `brand.md` is missing colours or fonts, say so in one line and ask for them, or offer a clean neutral look for now and note it in the file as `TODO`.
3. **If Canva is connected** (`tools.md` shows Canva as connected):
   - Use the business's Brand Kit in Canva if it has one, otherwise the colours and fonts from `brand.md`.
   - Create a design at the right size, with one page per slide for a carousel, and put in the words and logo.
   - Give the owner the link to the design and tell them it's ready to check and download in Canva.
4. **If Canva isn't connected**, build it from the template:
   - Copy `.claude/skills/marketing/assets/graphic-template.html` to `outputs/marketing/YYYY-MM-DD-<name>.html`. Never edit the template itself.
   - Fill the CSS variables at the top of the copy from `brand.md`: `--primary`, `--secondary`, `--accent`, `--background`, `--text`, `--font-heading`, `--font-body`. If a brand font is a Google Font, fill in the font link in the `<head>`; if not, use the closest common font and tell the owner.
   - Put in the heading, the body (or delete the body line if there isn't one) and the footer (business name or handle). Leave the footer colour as the template sets it (the text colour, slightly faded); don't change it to the secondary colour, which can disappear on light backgrounds. For the logo, point the image at the file in `business/brand-assets/` using `../../business/brand-assets/<file>`; if there is no logo file, delete the logo line (a missing file also hides itself).
   - For a carousel, copy the slide block once per slide, as the commented example in the file shows. Number the slides.
   - Tidy the copy: delete the instruction comment at the top of the file, and delete the commented slide example if you didn't use it.
   - For other sizes, change `--canvas-width` and `--canvas-height` (square: 1080 × 1080; story or reel cover: 1080 × 1920).
5. **Tell the owner how to get the image.** In plain steps: double-click the file to open it in their browser, make the browser window as big as possible, then take a screenshot of each slide.
   - Mac: press Cmd + Shift + 4, then drag a box around the slide.
   - Windows: press Windows key + Shift + S, then drag a box around the slide.

   The screenshot saves to their desktop (Mac) or clipboard (Windows) and is ready to upload. Most modern screens (such as a Mac's Retina screen) give a sharp enough image for social media. If they need it for print, or at an exact size, suggest Canva instead.

## Check before handing over

- Colours and fonts match `brand.md` exactly, and nothing breaks a "Do" or "Don't" in it (number of colours, amount of text, and so on).
- The text is easy to read on a phone: strong contrast against the background, not too many words, nothing tiny.
- Spelling is correct, and the business name and handle are right.
- No invented results, statistics or testimonials on the graphic.
- For a carousel: the first slide makes people swipe, each slide has one point, and the last slide has the next step.
- For the template route: read the saved file back and check no placeholder text, sample colours, instruction comment or unused commented slide are left.

## Save to

Canva route: the design stays in the owner's Canva account; save a note with the link and the words used to `outputs/marketing/YYYY-MM-DD-<name>.md`. Template route: `outputs/marketing/YYYY-MM-DD-<name>.html`. Tell the owner where it is in the chat.

## Needs a yes

Posting or publishing the graphic anywhere, and sharing the Canva design with anyone outside the business. Show the image or link, the caption, the platform and the account first. If the owner has allowed a platform without asking in `business/rules.md`, post and confirm.
