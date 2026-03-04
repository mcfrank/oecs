# Plan: Article format improvements (match OECS live site)

Compare: [Acquired Language Disorders on OECS](https://oecs.mit.edu/pub/gasxfap5/release/1?readingCollection=9dd2a47d) vs our static version. Goals:

1. **Restore metadata (author, section editor, editors-in-chief)**
2. **Restore "also, Aphasia" subtitle**
3. **Fix citations: single parens instead of double**
4. **Fix crosslink paths for GitHub Pages (baseURL)**
5. **Confirm reference / Further reading section is present**

---

## 1. Metadata (author, section editor, editors-in-chief)

**Source:** Article JSON `raw_pub.attributions`:
- `isAuthor: true` → author(s)
- `roles: ["Section Editor"]` → section editor
- `roles` containing "Editor-in-Chief" → editors-in-chief  
Names from `attribution.name` or `attribution.user.fullName`.

**Changes:**
- **json_to_markdown.py:** Add to front matter:
  - `subtitle` from `raw_pub.description` (e.g. `"also, Aphasia"`) when present
  - `section_editors`: list of names with role Section Editor
  - `editors_in_chief`: list of names with role Editor-in-Chief  
  Keep existing `authors` (isAuthor).
- **layouts/articles/single.html** (or override **layouts/_default/single.html** for articles): Below the title, output:
  - Subtitle line if `Params.subtitle` (e.g. “also, Aphasia”)
  - “by [Author names]”
  - “Section Editor(s): …” if `Params.section_editors`
  - “Editors-in-Chief: …” if `Params.editors_in_chief`
  - Published date (from `Params.date`) and DOI (from `Params.doi`) in a small metadata block.

**Files:** `scripts/json_to_markdown.py`, `layouts/_default/single.html` or `layouts/articles/single.html`.

---

## 2. “also, Aphasia” subtitle

**Source:** `raw_pub.description` (e.g. `"also, Aphasia"`). Not all articles have it.

**Changes:** Already covered in (1): add `subtitle` to front matter and render it in the article layout directly under the main title.

---

## 3. References: single parens instead of double

**Current behavior:** Converter outputs a citation node as `(customLabel)`, e.g. `(Broca, 1861)`. When the surrounding text already has parentheses, we get `((Broca, 1861))`.

**Change:** In **scripts/json_to_markdown.py**, in `render_inline()` for `type == "citation"`, output only the label, **no** extra parentheses:  
`buf.append(label)` instead of `buf.append(f"({label})")`.  
The prose in the doc already has “(” before and “)” after the citation node, so the result will be “(Broca, 1861)” with single parens.

**File:** `scripts/json_to_markdown.py` (one-line change).

---

## 4. Crosslink paths (invalid URLs under GitHub Pages)

**Problem:** We emit internal links as `/articles/3bgjh908`. With baseURL `https://user.github.io/oecs-static/`, the browser resolves that to `https://user.github.io/articles/3bgjh908` (missing `oecs-static`).

**Options:**
- **A (recommended): Hugo render hook**  
  Add **layouts/_default/_markup/render-link.html** and, for links whose destination is an internal article (path starts with `/articles/` or matches our article section), set `href` to `{{ .Page.Site.BaseURL }}articles/{{ slug }}/` (or use `relLangURL`/`absURL` with the article path). Then existing markdown can keep `/articles/slug` and the hook fixes the URL at build time.
- **B: Relative links in markdown**  
  In the converter, emit relative links like `../3bgjh908/` from article to article. Works but makes markdown less readable and is tied to URL structure.

**Recommended:** Implement (A). Create the render hook; detect internal article links (e.g. path prefix `/articles/` or check if the URL is a path under the articles section); output `href="{{ .Page.Site.BaseURL }}articles/TARGET_SLUG/"` (or equivalent) so the final link is correct for GitHub Pages.

**File:** `layouts/_default/_markup/render-link.html` (new).

---

## 5. Reference / “Further reading” section

**Current state:** For at least one article (e.g. gasxfap5), the “Further reading” section is already present in the generated markdown (heading + bullet list). So the ProseMirror → Markdown conversion is emitting that block.

**Actions:**
- Spot-check a few more articles to ensure “Further reading” (or similar reference sections) are not dropped.
- If any are missing, verify in the JSON that the section exists in `raw_text.content` (e.g. `heading` + `bullet_list`/`ordered_list`) and that **json_to_markdown.py** handles all block types in that subtree (no early return or skip that would drop list items or paragraphs inside lists).

No code change needed if spot-checks confirm sections are present; otherwise fix the converter for the affected block structure.

---

## Implementation order

1. **Citations:** Change citation to output `label` only in `json_to_markdown.py`.
2. **Crosslinks:** Add `layouts/_default/_markup/render-link.html` and fix internal article links using BaseURL.
3. **Metadata + subtitle:** Extend front matter in `json_to_markdown.py` (subtitle, section_editors, editors_in_chief); update article single layout to show subtitle, authors, section editor(s), editors-in-chief, date, DOI.
4. **Re-run:** `python scripts/json_to_markdown.py` to regenerate all article markdown with new front matter and citation format.
5. **Verify:** Spot-check “Further reading” and crosslinks on a few articles (including gasxfap5) locally and on a GitHub Pages preview.
