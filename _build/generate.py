#!/usr/bin/env python3
import json, html as H, re as _re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "_build"
# Intended canonical site URL. Easy to change in one place (canonicals, sitemap, OG).
# Apex is canonical; www should redirect to the apex (set later in Cloudflare).
# Suggested Cloudflare Pages project name: aitoolchart
CANON = "https://aitoolchart.net"
CHECKED, CHECKED_ISO = "Nov 15, 2026", "2026-11-15"
UPDATED, UPDATED_ISO = "Nov 15, 2026", "2026-11-15"
ASSET_V = "20261115a"

def row_id(name):
    return "p-" + _re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

NAV = [
    ("index.html", "Home"),
    ("chatbots.html", "Chatbots"),
    ("image.html", "Image"),
    ("photo.html", "Photo"),
    ("video.html", "Video"),
    ("voice.html", "Voice"),
    ("music.html", "Music"),
    ("coding.html", "Coding"),
    ("transcription.html", "Transcripts"),
    ("search.html", "Search"),
    ("agents.html", "Agents"),
    ("apps.html", "Apps"),
    ("gen3d.html", "3D"),
    ("updates.html", "Updates"),
]
HERO_SVG = (BUILD / "hero.svg").read_text()
COMMON_HOW = """
<li><strong>Popularity</strong> is a 1–5 judgment (halves allowed) of how commonly a product shows up in recent traffic reports, app ranks, or usage leaderboards — relative to the other products on this page, not a computed formula.</li>
<li><strong>Captions</strong> name the source and a “checked Nov 2026” date. If there was no usable source, the caption says “Editorial estimate.”</li>
<li><strong>Best for</strong> is an editorial label of a typical use, not a test score.</li>
<li><strong>Cost</strong> is a five-step scale (Free / $ / $$ / $$$ / $$$$). See “How cost is rated” for the band definitions on this page. Captions cite a source or say the rating is an estimate.</li>
"""

def e(s):
    return H.escape(s, quote=True)

FONTS = "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap"
OG_ALT = "AI Reference Library: a dark grid and connected nodes"

def head(title, description, path):
    url = CANON + path
    typ = "website" if path == "/" else "article"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{e(url)}">
<meta property="og:type" content="{typ}">
<meta property="og:site_name" content="AI Reference Library">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{e(url)}">
<meta property="og:image" content="{CANON}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(OG_ALT)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{CANON}/og-image.png">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="theme.css?v={ASSET_V}">
</head>
"""

def nav(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'<li><a href="{href}"{cur}>{e(label)}</a></li>')
    return f"""<a class="skip" href="#main">Skip to content</a>
<nav class="topnav" aria-label="Primary">
  <div class="inner">
    <a class="brand" href="index.html">
      <svg width="28" height="28" viewBox="0 0 28 28" aria-hidden="true">
        <rect x="1" y="1" width="26" height="26" rx="4" fill="none" stroke="#c4a6ff" stroke-width="1"/>
        <circle cx="8" cy="18" r="2" fill="#c4a6ff"/>
        <circle cx="14" cy="10" r="2" fill="#c4a6ff"/>
        <circle cx="20" cy="15" r="2" fill="#c4a6ff"/>
        <path d="M8 18 L14 10 L20 15" fill="none" stroke="#c4a6ff" stroke-width="1.2"/>
      </svg>
      AI Reference Library
    </a>
    <ul class="nav-links">{''.join(items)}</ul>
  </div>
</nav>
"""

def footer(home=False):
    updated = ""
    if home:
        updated = f'<p class="kofi updated">Last updated <time datetime="{UPDATED_ISO}">{UPDATED}</time> · <a href="updates.html">See what changed →</a></p>\n'
    return f"""<footer class="site-footer">
{updated}<p class="kofi">Free and ad-free. If this site helped you, <a href="https://ko-fi.com/marcustravis" target="_blank" rel="noopener">buy me a coffee →</a></p>
</footer>
<script>
(function () {{
  function syncNavH() {{
    var nav = document.querySelector(".topnav");
    if (!nav) return;
    document.documentElement.style.setProperty("--nav-h", Math.ceil(nav.getBoundingClientRect().height) + "px");
  }}
  syncNavH();
  window.addEventListener("resize", syncNavH);
  if (window.ResizeObserver && document.querySelector(".topnav")) {{
    new ResizeObserver(syncNavH).observe(document.querySelector(".topnav"));
  }}
}})();
</script>
"""

def hero(eyebrow, title, lede, checked=True):
    check = ""
    if checked:
        check = f'<p class="checked">Data last checked: <time datetime="{CHECKED_ISO}">{CHECKED}</time> · <a href="updates.html">What changed</a></p>'
    return f"""<header class="hero">
  <div class="hero-art">{HERO_SVG}</div>
  <div class="hero-copy">
    <span class="eyebrow">{e(eyebrow)}</span>
    <h1>{e(title)}</h1>
    <p class="lede">{lede}</p>
    {check}
  </div>
</header>
"""

def chips(data):
    seen, tags = set(), []
    for d in data:
        for t in d["tags"]:
            if t not in seen:
                seen.add(t); tags.append(t)
    out = ['<button class="chip" data-f="all" aria-pressed="true">All</button>']
    for t in tags:
        out.append(f'<button class="chip" data-f="{e(t)}" aria-pressed="false">{e(t)}</button>')
    return "\n".join(out)

def wrap(inner):
    return f'<div class="page-bg"></div>\n{inner}'

COST_HOW = """        <li>Cost is rated on the typical individual paid plan most people buy, per month, when we could find a published price this session. If the vendor marks a plan as popular or most popular, that is the plan we use. Otherwise we use the ordinary individual paid plan (not the cheapest limited tier, and not an ultra or teams tier). The caption names the plan. Annual “per month” equivalents are noted when the vendor publishes them. Higher ultra tiers do not set the band.</li>
        <li><strong>Free</strong> — no individual paid plan is required for the core product.</li>
        <li><strong>$</strong> — under $15 / month.</li>
        <li><strong>$$</strong> — $15–29 / month.</li>
        <li><strong>$$$</strong> — $30–99 / month.</li>
        <li><strong>$$$$</strong> — $100+ / month, or quote-only with no public individual plan found this session.</li>
        <li>If the product is mainly a usage-based API, or no public individual price turned up, the caption says so and the band is an editorial estimate — never an invented dollar amount. Always confirm current pricing with the vendor.</li>"""

VISUAL_HOW = "The first column is meant to look like the product’s app or site icon. Official vendor or App Store app icons are used when we could find one this session. If not, the tile is a generated initials icon in the same rounded-square style."

def write_catalog(sec):
    data = json.loads((BUILD / sec["json"]).read_text())
    base_keys = ("name","maker","knownFor","tags","price","pop","popCaption","cost","costCaption","learn","pro","con","url","icon","iconOfficial")
    extra_cols = sec.get("extraCols") or []
    extra_keys = [c["key"] for c in extra_cols]
    payload = [dict(id=row_id(d["name"]), **{k: d[k] for k in list(base_keys) + extra_keys if k in d}) for d in data]
    first_col = sec.get("firstCol", "Tool")
    table_class = "chart chart-wide" if extra_cols else "chart"
    extra_ths = "".join(f'\n          <th>{e(c["label"])}</th>' for c in extra_cols)
    extras_js = json.dumps(extra_keys)
    html = head(sec["title"] + " · AI Reference Library", sec["description"], "/" + sec["slug"])
    html += "<body>\n" + wrap(nav(sec["file"]))
    html += '<div class="wrap chart-wrap" id="main">\n'
    html += hero("Independent AI tools guide", sec["title"], sec["lede"])
    html += f"""  <div id="catalog">
  <div class="toolbar">
    <div class="chips" role="group" aria-label="Filter">{chips(data)}</div>
    <label class="search">Search
      <input type="search" id="search" placeholder="Name, maker, or tag" autocomplete="off">
    </label>
    <label class="sort">Sort
      <select id="sort">
        <option value="pop">Popularity</option>
        <option value="name">Name</option>
        <option value="cost-asc">Cost: cheapest first</option>
        <option value="cost-desc">Cost: priciest first</option>
      </select>
    </label>
  </div>
  <p class="count" id="count"></p>
  <div class="table-box">
    <table class="{table_class}">
      <thead>
        <tr>
          <th><button type="button" class="th-btn" data-k="name">{e(first_col)}</button></th>
          <th>Known for</th>{extra_ths}
          <th><button type="button" class="th-btn" data-k="pop">Popularity</button></th>
          <th><button type="button" class="th-btn" data-k="cost">Cost</button></th>
          <th class="learn-th">Best for<span class="th-note">editorial rating</span></th>
          <th>Pros &amp; cons</th>
          <th>Official site</th>
        </tr>
      </thead>
      <tbody id="rows"></tbody>
    </table>
  </div>
  </div>
  <div class="notes">
    <section>
      <h2>How the ratings work</h2>
      <ul>{COMMON_HOW}<li>{e(sec["relative"])}</li></ul>
    </section>
    <section>
      <h2>How cost is rated</h2>
      <ul>
{COST_HOW}
      </ul>
    </section>
    <section>
      <h2>Sources and limits</h2>
      <p>{e(sec["limits"])}</p>
    </section>
    <section>
      <h2>Independence</h2>
      <p>This site is ad-free and has no affiliate links. Official-site buttons go straight to the vendor. Stars are not paid placement.</p>
    </section>
    <section>
      <h2>About the icons</h2>
      <p>{e(VISUAL_HOW)}</p>
    </section>
  </div>
</div>
{footer()}
<script src="app.js?v={ASSET_V}"></script>
<script src="scroll-hint.js?v={ASSET_V}"></script>
<script>
const DATA = {json.dumps(payload, ensure_ascii=False)};
initCatalog(DATA, {{ noun: {json.dumps(sec["noun"])}, defaultSort: "pop", extraCols: {extras_js} }});
</script>
</body>
</html>
"""
    (ROOT / sec["file"]).write_text(html)
    sourced = sum(1 for d in data if d["sourced"])
    editorial = len(data) - sourced
    cost_s = sum(1 for d in data if d.get("costSourced"))
    official = sum(1 for d in data if d.get("iconOfficial"))
    print(f"wrote {sec['file']}: {len(data)} products, pop sourced={sourced}, editorial={editorial}, cost sourced={cost_s}, official visuals={official}")
    return len(data), sourced, editorial, cost_s, official

SECTION_LABELS = {
    "chatbots": "LLMs & chatbots",
    "image": "Image generation",
    "photo": "Photo editing & enhancing",
    "video": "Video generation",
    "voice": "Voice, TTS & cloning",
    "music": "Music generation",
    "coding": "Coding assistants",
    "transcription": "Transcription & STT",
    "search": "AI search",
    "agents": "Agents & automation",
    "apps": "Business & everyday AI apps",
    "gen3d": "3D generation",
}

def search_index(sections):
    idx = []
    for sec in sections:
        for d in json.loads((BUILD / sec["json"]).read_text()):
            idx.append({
                "name": d["name"], "maker": d["maker"], "tags": d["tags"], "icon": d.get("icon"),
                "section": SECTION_LABELS[sec["slug"]],
                "href": f'{sec["file"]}#{row_id(d["name"])}',
            })
    return idx

def write_home(counts, sections):
    index = search_index(sections)
    index_js = json.dumps(index, ensure_ascii=False).replace("</", "<\\/")
    cards = [
        ("chatbots.html", f"{counts['chatbots'][0]} chatbots", "LLMs &amp; chatbots", "ChatGPT, Claude, Gemini, Grok, Copilot, DeepSeek, and other assistants people actually open."),
        ("image.html", f"{counts['image'][0]} image tools", "Image generation", "Midjourney, ChatGPT Images, Ideogram, Flux, Firefly, Leonardo, and related image models."),
        ("photo.html", f"{counts['photo'][0]} photo tools", "Photo editing &amp; enhancing", "Reface, Remini, Lensa, Picsart, FaceApp, Photoroom, and other photo editors and enhancers."),
        ("video.html", f"{counts['video'][0]} video tools", "Video generation", "Runway, Pika, Kling, Luma, Sora, Veo, Hailuo, and other text-to-video tools."),
        ("voice.html", f"{counts['voice'][0]} voice tools", "Voice, TTS &amp; cloning", "ElevenLabs, OpenAI TTS, PlayAI, Cartesia, Hume, Descript, and related voice tools."),
        ("music.html", f"{counts['music'][0]} music tools", "Music generation", "Suno, Udio, Stable Audio, Google Lyria, AIVA, and other song and score tools."),
        ("coding.html", f"{counts['coding'][0]} coding assistants", "Coding assistants", "Cursor, GitHub Copilot, Claude Code, Windsurf, Codex, and other coding tools."),
        ("transcription.html", f"{counts['transcription'][0]} transcription tools", "Transcription &amp; STT", "Whisper, Deepgram, AssemblyAI, Otter, Fireflies, Fathom, and meeting notetakers."),
        ("search.html", f"{counts['search'][0]} search tools", "AI search", "Perplexity, ChatGPT Search, Google AI Mode, Copilot, Grok, You.com, and related answer engines."),
        ("agents.html", f"{counts['agents'][0]} agent tools", "Agents &amp; automation", "ChatGPT agents, Claude computer use, Zapier, Make, n8n, Lindy, Manus, and related tools."),
        ("apps.html", f"{counts['apps'][0]} apps", "Business &amp; everyday AI apps", "GoHighLevel, HubSpot, Grammarly, Notion AI, Canva Magic Studio, Jasper, and other business and everyday AI apps."),
        ("gen3d.html", f"{counts['gen3d'][0]} 3D tools", "3D generation", "Meshy, Tripo, Rodin, CSM, Spline, Hunyuan3D, and other image-to-3D tools."),
    ]
    grid = "".join(
        f'<a class="card" href="{href}"><span class="cnt">{cnt}</span><span class="nm">{name}</span><span class="ds">{ds}</span><span class="go">Open guide →</span></a>'
        for href, cnt, name, ds in cards
    )
    html = head(
        "AI Reference Library",
        "Free, ad-free guide to AI tools: chatbots, image generation, photo editing, video, voice, music, coding assistants, transcription, AI search, agents, business and everyday apps, and 3D, with cited ratings.",
        "/",
    )
    html += "<body>\n" + wrap(nav("index.html"))
    html += '<div class="wrap chart-wrap" id="main">\n'
    html += hero("Independent AI tools guide", "AI Reference Library",
                 "A free, ad-free field guide to the AI tools people actually use to chat, draw, retouch, film, speak, compose, code, transcribe, search, automate, run a business, write, and model in 3D. Popularity is cited, not invented.")
    html += f"""  <section class="site-search" role="search" aria-labelledby="site-search-h">
    <h2 id="site-search-h">Search every product</h2>
    <label for="site-search">Chatbots, image tools, photo editors, coding assistants, business apps, and the rest — by name, maker, or tag</label>
    <input type="search" id="site-search" placeholder="Try ChatGPT, Midjourney, Cursor, ElevenLabs…" autocomplete="off" spellcheck="false" aria-describedby="site-status" aria-controls="site-results">
    <p class="sr-status" id="site-status" aria-live="polite">Searches all {len(index)} products across every section.</p>
    <ul class="sr-list" id="site-results" hidden></ul>
  </section>
  <section class="grp">
    <h2>Start here</h2>
    <div class="grid">{grid}</div>
  </section>
  <div class="notes">
    <section>
      <h2>How to use this site</h2>
      <p>Search above to jump straight to any product’s row, or open a section. Each section opens as a compact, scrollable comparison chart — one row per product — that you can filter, search, and sort. Stars are a 1–5 popularity judgment with a source caption. Cost uses a Free / $ / $$ / $$$ / $$$$ scale with a source caption, rated on the typical individual paid plan most people buy. “Best for” labels are editorial. Official-site links are not affiliate links.</p>
    </section>
    <section>
      <h2>Where the numbers come from</h2>
      <p>Web-traffic figures are third-party estimates of website visits, not app sessions or unique people. Chatbot shares among seven assistants (October 2026) come from Similarweb: ChatGPT 55.7%, Gemini 24.2%, Claude 11.5%, DeepSeek 3.4%, Grok 2.2%, Copilot 1.1%, Perplexity 0.8%. Most other visit counts are Similarweb estimates for October 2026, as published by SeekTool. A few use Semrush estimates for September 2026 from Tako’s a16z Top 100 table, GitHub star counts, or OpenRouter token rankings. Cost figures come from official vendor pricing pages, checked in November 2026, and are rated on the typical individual paid plan most people buy. If a product has no usable source, the caption says “Editorial estimate.”</p>
    </section>
    <section>
      <h2>What this is not</h2>
      <p>This is not a vendor ranking you should buy from blindly. It is a starting map for people learning the AI tools landscape. Model versions change quickly; confirm current pricing and terms with the vendor.</p>
    </section>
  </div>
</div>
{footer(home=True)}
<script>window.SEARCH_INDEX = {index_js};</script>
<script src="home-search.js?v={ASSET_V}"></script>
</body>
</html>
"""
    (ROOT / "index.html").write_text(html)
    print("wrote index.html")

def write_updates():
    html = head("Updates · AI Reference Library", "What changed on the AI Reference Library, in plain English.", "/updates")
    html += "<body>\n" + wrap(nav("updates.html"))
    html += '<div class="wrap chart-wrap" id="main">\n'
    html += hero("Changelog", "Updates", "A short, plain-English record of what changed on this site.", checked=False)
    html += f"""  <article>
    <div class="log">
      <h3>New section: Business and everyday AI apps</h3>
      <p><time datetime="2026-11-15">Nov 15, 2026</time></p>
      <p>Added a twelfth comparison chart for apps that use AI for practical work — marketing and CRM, sales, customer support, writing, and productivity — for businesses and for regular people, including GoHighLevel, HubSpot (Breeze AI), Salesforce Agentforce, Intercom Fin, Zendesk AI, Jasper, Copy.ai, Grammarly, Notion AI, Canva Magic Studio, Gamma, Superhuman, QuillBot, and ClickUp Brain. It has the same columns, filter chips, search, sort, and sticky scrollbar as the other charts. Zapier stays on the Agents and automation page. Popularity is sourced for all 14 rows (SeekTool’s October 2026 Similarweb website-visit estimates, plus a Semrush October 2026 figure for gohighlevel.com). Cost follows the same rule as the other pages: the typical individual or entry paid plan most people buy, with business seat pricing noted. Gamma’s cost band is an editorial estimate because no public dollar figure was captured from its pricing page this session. See CHANGELOG.md for the source list.</p>
    </div>
    <div class="log">
      <h3>New section: Photo editing and enhancing</h3>
      <p><time datetime="2026-11-14">Nov 14, 2026</time></p>
      <p>Added an eleventh comparison chart for AI photo editing and enhancing — face swap, restore, retouching, AI avatars, and background removal — with Reface, Remini, Lensa, Picsart, FaceApp, Photoroom, Facetune, Fotor, Topaz Photo, Let’s Enhance, and Magnific. It has the same columns, filter chips, search, sort, and sticky scrollbar as the other charts. Popularity is sourced where a citable figure was found (SeekTool’s October 2026 Similarweb website-visit estimates, plus App Store and Google Play rating counts for mobile-first apps). Cost follows the same rule as the other pages: the typical individual paid plan most people buy. Picsart and Fotor can also generate images, but they are listed here rather than on the Image generation page. See CHANGELOG.md for the source list.</p>
    </div>
    <div class="log">
      <h3>Published at aitoolchart.net</h3>
      <p><time datetime="2026-11-14">Nov 14, 2026</time></p>
      <p>The site is live at <a href="https://aitoolchart.net">aitoolchart.net</a>. The public repository is <a href="https://github.com/MarcusTravis/ai-reference">github.com/MarcusTravis/ai-reference</a>. www.aitoolchart.net redirects to the apex.</p>
    </div>
    <div class="log">
      <h3>More sourced popularity, shorter captions</h3>
      <p><time datetime="2026-11-14">Nov 14, 2026</time></p>
      <p>A second research pass filled in quantitative popularity sources for many rows that had been editorial estimates, mostly Similarweb website-visit estimates for October 2026 via SeekTool, plus Semrush September 2026 figures from Tako’s a16z Top 100 table, GitHub star counts, and OpenRouter token rankings. Numbers were not invented; rows still without a usable source stay labeled “Editorial estimate.” Cost and popularity captions were shortened. Cost is now rated, on every page, on the typical individual paid plan most people buy (the vendor’s popular plan when they mark one). The ElevenLabs price wording was cleaned up, Midjourney is rated on Standard, and Suno Pro $10/month is now sourced from suno.com/pricing. Official cursor.com/pricing and x.ai/pricing still show one X Subscription ladder shared by Cursor and Grok. See CHANGELOG.md for the source list.</p>
    </div>
    <div class="log">
      <h3>Site launch</h3>
      <p><time datetime="2026-11-14">Nov 14, 2026</time></p>
      <p>The first version of the AI Reference Library: a homepage with search across every product, plus ten comparison charts — LLMs and chatbots, image generation, video generation, voice/TTS and cloning, music generation, coding assistants, transcription and speech-to-text (including meeting notetakers), AI search, agents and automation, and 3D generation. Each chart has filter chips, search, sort (including cheapest-first and priciest-first), a sticky header, and a sticky horizontal scrollbar. Popularity and cost captions were researched in November 2026. See CHANGELOG.md in the repository for the source list.</p>
    </div>
  </article>
</div>
{footer()}
</body>
</html>
"""
    (ROOT / "updates.html").write_text(html)
    print("wrote updates.html")

def write_404():
    cards = [
        ("/", "All guides", "Home →"),
        ("/chatbots", "LLMs & chatbots", "Open →"),
        ("/image", "Image generation", "Open →"),
        ("/photo", "Photo editing", "Open →"),
        ("/video", "Video generation", "Open →"),
        ("/voice", "Voice &amp; TTS", "Open →"),
        ("/music", "Music generation", "Open →"),
        ("/coding", "Coding assistants", "Open →"),
        ("/transcription", "Transcription", "Open →"),
        ("/search", "AI search", "Open →"),
        ("/agents", "Agents", "Open →"),
        ("/apps", "Business apps", "Open →"),
        ("/gen3d", "3D generation", "Open →"),
    ]
    grid = "".join(
        f'<a class="card" href="{CANON}{href}"><span class="nm">{name}</span><span class="go">{go}</span></a>'
        for href, name, go in cards
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Page not found · AI Reference Library</title>
<meta name="robots" content="noindex">
<link rel="icon" href="{CANON}/favicon.ico" sizes="any">
<link rel="icon" href="{CANON}/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{CANON}/apple-touch-icon.png">
<link rel="stylesheet" href="{FONTS.replace('&', '&amp;')}">
<link rel="stylesheet" href="{CANON}/theme.css">
<script>
(function(){{var p=location.pathname;if(p.length>1&&p.charAt(p.length-1)==="/")location.replace(p.slice(0,-1)+location.search+location.hash);}})();
</script>
</head>
<body>
<div class="page-bg"></div>
<div class="wrap" id="main">
  <span class="eyebrow">Error 404</span>
  <h1>Page not found</h1>
  <p class="lede">That page is not here. It may have moved, or the link has a typo. Try one of these instead.</p>
  <div class="grid">
    {grid}
  </div>
</div>
{footer()}
</body>
</html>
"""
    (ROOT / "404.html").write_text(html)
    print("wrote 404.html")

def write_meta(stats):
    pages = ["/", "/chatbots", "/image", "/photo", "/video", "/voice", "/music", "/coding", "/transcription", "/search", "/agents", "/apps", "/gen3d", "/updates"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in pages:
        sm.append(f"  <url><loc>{CANON}{p}</loc></url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {CANON}/sitemap.xml\n")
    (ROOT / "_headers").write_text(
        f"# Apex {CANON.removeprefix('https://')} is the canonical address.\n"
        f"# www should redirect to the apex (set later in Cloudflare DNS / Pages).\n"
        f"# aitoolchart.pages.dev can stay up; it just points search engines at the .net copy.\n"
        f"/*\n  Link: <{CANON}/:splat>; rel=\"canonical\"\n"
        "  X-Content-Type-Options: nosniff\n"
        "  Referrer-Policy: strict-origin-when-cross-origin\n"
        "  X-Frame-Options: SAMEORIGIN\n"
    )
    (ROOT / "README.md").write_text(f"""# AI Reference Library

**Intended live site:** [{CANON}]({CANON})

A free, ad-free field guide to AI tools — chatbots, image generation, photo editing and enhancing, video generation, voice, music, coding assistants, transcription, AI search, agents, business and everyday AI apps, and 3D generation. Built as a plain static site (HTML, CSS, and JavaScript). Cloudflare Pages should use **no build command**; the HTML is already generated. Suggested Pages project name: `aitoolchart`.

The site URL is set once as `CANON` in `_build/generate.py` and is used for canonical tags, the sitemap, and Open Graph images. The apex `{CANON}` is canonical; `www` should redirect to the apex.

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
""")
    print("wrote sitemap, robots, _headers, README")

def main():
    sections = json.loads((BUILD / "sections.json").read_text())
    stats = {}
    for sec in sections:
        stats[sec["slug"]] = write_catalog(sec)
    write_home(stats, sections)
    write_updates()
    write_404()
    write_meta(stats)
    print("DONE", stats)

if __name__ == "__main__":
    main()
