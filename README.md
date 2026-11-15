# AI Reference Library

**Intended live site:** [https://aitoolchart.net](https://aitoolchart.net)

A free, ad-free field guide to AI tools — chatbots, image generation, photo editing and enhancing, video generation, voice, music, coding assistants, transcription, AI search, agents, business and everyday AI apps, and 3D generation. Built as a plain static site (HTML, CSS, and JavaScript). Cloudflare Pages should use **no build command**; the HTML is already generated. Suggested Pages project name: `aitoolchart`.

The site URL is set once as `CANON` in `_build/generate.py` and is used for canonical tags, the sitemap, and Open Graph images. The apex `https://aitoolchart.net` is canonical; `www` should redirect to the apex.

There are no ads and no affiliate links. Official-site links go to the vendor.

Many ratings are relative judgments with cited sources. Check the vendor before you buy or standardize on a tool.

## Local preview

From this folder: `python3 -m http.server` then open `http://localhost:8000`.

To regenerate pages after editing the JSON in `_build/`:

```
python3 _build/generate.py
```

## Data

Comparison-chart rows are driven by a `DATA` array on each section page, generated from `_build/<section>.json`. After changing facts, also update `CHANGELOG.md` and add a short note on `updates.html`.

Visitor stats (optional, after deploy): Cloudflare Web Analytics, from the Pages project Metrics page.

## Sources

The November 2026 research notes and source list live in `CHANGELOG.md`.
