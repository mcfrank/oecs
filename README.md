# Open Encyclopedia of Cognitive Science (OECS) — Static Site

Static, Markdown-based mirror of the [Open Encyclopedia of Cognitive Science](https://oecs.mit.edu), built with [Hugo](https://gohugo.io/) and deployable to GitHub Pages.

---

## Table of contents

- [Setup](#setup)
- [Updating content](#updating-content)
- [Building locally](#building-locally)
- [Deploying to GitHub Pages](#deploying-to-github-pages)
- [Project layout](#project-layout)

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/<user-or-org>/oecs-static.git
cd oecs-static
```

### 2. Python virtual environment and dependencies

Scripts in `scripts/` require Python 3 and a few packages. Use a virtual environment so dependencies don’t conflict with other projects.

**Create and activate a venv:**

- **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- **Windows (Command Prompt):**
  ```cmd
  python -m venv .venv
  .venv\Scripts\activate.bat
  ```
- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run scripts from the repo root** (so `scripts/` and `articles/` paths resolve correctly). Always **activate the venv first** in each new terminal (e.g. `source .venv/bin/activate` on macOS/Linux). If you see `ModuleNotFoundError: No module named 'requests'`, you're not in the venv—create it with `python3 -m venv .venv`, activate it, then `pip install -r requirements.txt`.

### 3. (Optional) PubPub credentials for re-fetching articles

If you will re-run the article fetcher (see [Updating content](#updating-content)):

1. Copy `.secrets.example` to `.secrets` (create the example file if needed, with placeholder keys).
2. Add `OECS_PASSWORD=<your-pubpub-password>` (and any other vars your scripts expect).
3. Ensure `config.json` exists with PubPub `base_url`, `email`, `collection_id`, `community_id`, etc., as used by `scripts/fetch_articles.py`.

Do not commit `.secrets` or real credentials.

---

## Updating content

Content is generated from (1) the live OECS site and (2) the article JSON in `articles/`. Run these from the **repo root** with your **virtual environment activated**.

### Step 1: Re-fetch site pages and thematic data (recommended after OECS changes)

Scrapes the live site (HTTPS), updates thematic collections, and writes the semantic-network iframe URL used on the home page:

```bash
python scripts/fetch_site_pages.py
```

This will:

- Fetch home, articles list, thematic collections index, and each theme page from https://oecs.mit.edu.
- Fetch editors, about, and FAQ pages.
- Write thematic collection data (e.g. `metadata/thematic_collections.json` or into `data/`).
- Write the iframe URL to `data/iframe_semantic_network.json` for the home page. If the iframe isn’t found, you can edit this file manually (e.g. `{"url": "https://..."}`).
- **Convert editors, about, and FAQ HTML to Markdown** and write `content/editors/_index.md`, `content/about/_index.md`, and `content/faq/_index.md` (requires `markdownify`, which is in `requirements.txt`).

Add `--output-html` to also save raw HTML under `scripts/output/site_pages/` for debugging.

### Step 2: (Optional) Re-fetch article JSON from PubPub

Only needed when you want to pull new or updated articles from the OECS PubPub backend. Requires `.secrets` and `config.json`:

```bash
python scripts/fetch_articles.py
```

Optionally limit how many to fetch:

```bash
python scripts/fetch_articles.py --limit 10
```

### Step 3: (Optional) Regenerate metadata CSVs from article JSON

After fetching or changing article JSON:

```bash
python scripts/extract_current_links.py
```

This updates `metadata/current_articles.csv` and crosslink CSVs from the JSON in `articles/`.

### Step 4: Regenerate article Markdown and optional data

Converts all article JSON in `articles/` to Hugo Markdown under `content/articles/` and optionally updates `data/articles.json`:

```bash
python scripts/json_to_markdown.py
```

Internal links to OECS articles are rewritten to `/articles/{slug}` for the static site.

After these steps, you can [build locally](#building-locally) or push to trigger a [GitHub Pages build](#deploying-to-github-pages).

---

## Building locally

### Install Hugo

You need [Hugo (Extended)](https://gohugo.io/installation/) installed (e.g. from the site, your package manager, or GitHub Actions only for deployment).

Check:

```bash
hugo version
```

### Preview the site

From the repo root:

```bash
hugo server
```

Open the URL shown (typically http://localhost:1313). The site will use the baseURL from config; for local preview you may need `hugo server --baseURL "/"` or a baseURL set in `hugo.toml` for development.

### Production build

To build the static site into `public/`:

```bash
hugo build --gc --minify
```

Output is in `public/`. Do not commit `public/` if you deploy via GitHub Actions (the workflow builds it on the server).

---

## Deploying to GitHub Pages

### One-time setup

1. Push the repo to GitHub (e.g. `github.com/<user-or-org>/oecs-static`).
2. In the repo: **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions** (not “Deploy from a branch”).
4. Ensure the workflow file exists: `.github/workflows/hugo.yaml` (or the name used in the plan). It should:
   - Trigger on push to `main` (and optionally `workflow_dispatch`).
   - Install Hugo Extended, run `hugo build --gc --minify` with the correct baseURL for GitHub Pages.
   - Use `actions/upload-pages-artifact@v3` and `actions/deploy-pages@v4`.

### Base URL

The workflow must set the Hugo baseURL to your Pages URL, for example:

- User/org site: `https://<username>.github.io/`
- Project site: `https://<username>.github.io/oecs-static/`

Set this in the workflow when calling `hugo build`, e.g.:

`--baseURL "${{ steps.pages.outputs.base_url }}/"`

(or the equivalent for your repo name so the project site is `https://<user>.github.io/oecs-static/`).

### Deploying updates

- **Automatic:** Push changes to the default branch (e.g. `main`). The GitHub Action will build and deploy.
- **Manual:** In the repo go to **Actions**, select the Hugo workflow, and run **Run workflow**.

After a successful run, the site will be available at the URL shown in the workflow (e.g. `https://<user-or-org>.github.io/oecs-static/`).

---

## Project layout

| Path | Purpose |
|------|--------|
| `scripts/` | Helper scripts: fetch site pages, fetch articles, extract links, JSON→Markdown. Run from repo root with venv active. |
| `articles/` | Source article JSON from PubPub; input for `json_to_markdown.py`. |
| `metadata/` | CSVs and generated thematic collection data; input for scripts and (via copy) Hugo `data/`. |
| `content/` | Hugo content (Markdown): articles, thematic collections, editors, about, faq, home). Largely generated; can be hand-edited. |
| `layouts/` | Hugo templates (base, list, single, shortcodes). |
| `assets/` | CSS (and optional JS) for styling. |
| `static/` | Static files (favicon, etc.) copied as-is. |
| `data/` | Hugo data files (e.g. thematic collections, `iframe_semantic_network.json`, optional articles list). |
| `public/` | Built site (generated by `hugo build`; usually not committed when using GitHub Actions). |
| `requirements.txt` | Python dependencies for scripts; use with a virtual environment. |

---

## Editing the semantic-network iframe URL

The home page embeds an iframe for the OECS semantic network. Its URL is read from **`data/iframe_semantic_network.json`**, e.g.:

```json
{ "url": "https://example.com/semantic-network" }
```

- It is normally written by `scripts/fetch_site_pages.py` when it scrapes the OECS home page.
- To set or override it manually, edit `data/iframe_semantic_network.json`.
- Optionally, the theme or config can support a `params.semantic_network_iframe_url` override in `hugo.toml` so you don’t have to edit the JSON.
