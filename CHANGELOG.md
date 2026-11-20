# Changelog

All notable changes to the AI Reference Library, with sources.

## Nov 20, 2026 — Search and AI-crawler pass

A search and AI-search pass, all generated from `_build/generate.py` and `_build/seo.json`. Product data, ratings, and captions were not changed; data was last checked November 15, 2026.

- Unique “comparison chart · AI Reference Library” document titles for every section, and a new home title and description.
- A short plain-English intro under each section hero, a “Related charts” block, and a visible “Common questions” FAQ on the home page and every section. The FAQ text is taken verbatim from `_build/seo.json`.
- Structured data (JSON-LD): WebSite, Organization, and FAQPage on the home page; BreadcrumbList, ItemList of SoftwareApplication, and FAQPage on each section; WebPage and BreadcrumbList on Updates. No prices or offers are included.
- `twitter:image:alt` and an `llms.txt` alternate link in every page head.
- New generated files: `llms.txt` (plain-text site summary) and an IndexNow key file. `robots.txt` now explicitly allows major AI and search crawlers. `sitemap.xml` has `lastmod` dates.
- Product icons below the first four rows now load lazily (`loading="lazy"`, `decoding="async"`).

## Nov 15, 2026 — Business and everyday AI apps section

Added a twelfth comparison chart, [Business and everyday AI apps](https://aitoolchart.net/apps), for marketing and CRM, sales, customer support, writing, and productivity tools used by businesses and by regular people. The new page follows the same recipe as the other sections: product icon in the first column, sourced or labeled-editorial popularity and cost ratings, plain-word filter chips (Business, Personal, Marketing, CRM and sales, Support, Writing), search, sort, and a sticky horizontal scrollbar. A home-page card and nav item (“Apps”) were added. The generated HTML, sitemap, and 404 links were updated by `_build/generate.py`.

The 14 tools are Canva Magic Studio, Notion AI, Salesforce Agentforce, Zendesk AI, Grammarly, HubSpot (Breeze AI), QuillBot, ClickUp Brain, Gamma, GoHighLevel (HighLevel), Superhuman, Intercom Fin, Jasper, and Copy.ai. None were already on another page. Zapier stays on the Agents and automation page. Canva Magic Studio was not already on the Image generation or Photo editing pages.

Popularity is sourced for all 14 rows. No numbers were invented. Several visit figures are for a whole product platform, not only the AI feature; those captions say so. The Salesforce figure is for salesforce.com, which also covers many products besides Agentforce.

**Popularity sources (checked 15 November 2026)**

- Similarweb website-visit estimates for October 2026, as published on SeekTool: Canva 954.6M (canva.com); Notion 175.3M (notion.com); Salesforce 111.9M (salesforce.com, company site); Zendesk 61.0M (zendesk.com); Grammarly 58.9M (grammarly.com); HubSpot 44.1M (hubspot.com); QuillBot 36.6M (quillbot.com); ClickUp 33.9M (clickup.com); Gamma 20.8M (gamma.app); Superhuman 6.51M (superhuman.com); Intercom 4.47M (intercom.com); Jasper 373.0K (jasper.ai); Copy.ai 344.3K (copy.ai). Website visits under-count tools that live mainly inside a desktop or mobile app, and platform-wide counts over-count a single AI feature.
- Semrush website-visit estimate for October 2026, from Semrush’s public domain overview for gohighlevel.com (last updated 11 November 2026): GoHighLevel 14.2M. A SeekTool Similarweb figure was not found for that domain this session.
- Official vendor claims cited in captions: Grammarly, “trusted by over 40 million people and 50,000 organizations” (grammarly.com/plans).

**Official pricing (checked 15 November 2026)**

- Canva Pro US$144/year for one person (about $12/month billed yearly): canva.com/pricing. Business is US$250/year per person.
- Notion Business $20 per member/month, labeled Recommended, includes Notion Agent: notion.com/pricing. Plus is $10 per member/month and includes only a trial of Notion AI.
- Salesforce Agentforce User License $50 USD/user/month: salesforce.com/agentforce/pricing. Other Agentforce uses are Flex Credits or larger editions (Max Edition from $550/user/month was also listed).
- Zendesk Suite Professional $115/agent/month paid yearly, labeled most popular: zendesk.com/pricing. Suite Team is $55/agent/month paid yearly; Support Team is $19/agent/month paid yearly. Automated resolutions are usage-based.
- Grammarly Pro $12/member/month billed annually ($144/year), or $30/member/month billed monthly: grammarly.com/plans and Grammarly Support, “How much does Grammarly Pro cost?”
- HubSpot Starter Core Seat $20/month per seat, including Breeze Assistant: legal.hubspot.com/hubspot-product-and-services-catalog. Marketing Hub Starter was also shown as starting at $20/month per seat, with a limited-time new-customer price from $10: hubspot.com/products/marketing/get-started.
- QuillBot Premium $8.33/month billed annually as $99.95, or $19.95/month: official QuillBot blog, “How much is QuillBot Premium?”
- ClickUp Business $17/user/month billed yearly, which includes Brain² Premium Models: clickup.com/pricing. Core is $9/user/month billed yearly; Max is $100/user/month billed yearly.
- GoHighLevel Starter $97/month, or $970/year: gohighlevel.com/pricing. Unlimited is $297/month, or $2,970/year; Pro is $497/month, or $4,970/year. Usage charges apply for phone, SMS, email, and some AI features.
- Superhuman Mail Starter $25 per member/month, billed annually: superhuman.com/mail/pricing.
- Intercom Essential $19/seat/month billed annually, or $29/seat/month billed monthly, plus $0.99 per Fin outcome: intercom.com/pricing.
- Jasper Pro $59/month billed yearly, or $69/month billed monthly: jasper.ai/pricing. Business is custom pricing (contact sales).
- Copy.ai Chat $24/month billed annually as $288/year, or $29/month billed monthly, for a 5-seat plan: copy.ai/pricing. Growth starts at $1,000/month.

Gamma’s cost band is an editorial estimate. Gamma’s help center lists Free, Plus, Pro, Ultra, and Business plans, but no public dollar figure was captured from gamma.app/pricing this session. No dollar amounts were invented for that row.

**Icons**

- Official vendor icons, stored locally as 128×128 PNGs. QuillBot’s site returned 403 for direct favicon URLs, so its icon was retrieved via Google’s favicon service and stored locally. See `icons/README.md` for the per-file source list.

## Nov 14, 2026 — Photo editing and enhancing section

Added an eleventh comparison chart, [Photo editing and enhancing](https://aitoolchart.net/photo), for face swap, photo enhance and restore, AI avatars, retouching, and background removal. The new page follows the same recipe as the other sections: product icon in the first column, sourced or labeled-editorial popularity and cost ratings, plain-word filter chips, search, sort, and a sticky horizontal scrollbar. A home-page card and nav item (“Photo”) were added. The generated HTML, sitemap, and 404 links were updated by `_build/generate.py`.

The 11 tools are Picsart, Photoroom, FaceApp, Facetune, Reface, Remini, Fotor, Lensa, Topaz Photo, Let’s Enhance, and Magnific. None were already on the Image generation page. Picsart and Fotor can also generate images; that overlap is noted on their rows. Adobe Firefly and Photoshop stay on the Image generation page. Topaz Photo is the current Topaz Labs product that replaces the older Topaz Photo AI app. Magnific is now the Freepik creative platform at magnific.com and is still known for the Magnific upscaler.

Popularity is sourced for 10 of 11 rows. Magnific is an editorial estimate: SeekTool’s October 2026 figure of 39.87K visits is for the old magnific.ai domain, and magnific.com’s mixed stock-and-AI traffic was not used as a clean product figure. No numbers were invented.

**Popularity sources (checked 14 November 2026)**

- Similarweb website-visit estimates for October 2026, as published on SeekTool: Photoroom 18.2M (photoroom.com); Picsart 16.5M (picsart.com); Fotor 5.8M (fotor.com); Topaz Labs 2.7M (topazlabs.com, company site that also covers other Topaz apps); Let’s Enhance 649.3K (letsenhance.io); Facetune 436.3K (facetuneapp.com); Remini 388.8K (app.remini.ai); Reface 260.4K (reface.ai); Lensa 27.0K (lensa.app). Website visits under-count mobile-first apps.
- US App Store rating counts, checked 14 November 2026: FaceApp 1.8M ratings at 4.7 average (FaceApp: Perfect Face Editor); Picsart 1.2M ratings, #12 in Photo & Video; Lensa 418K ratings at 4.7 average; Remini 360K ratings at 4.6 average, #75 in Photo & Video; Photoroom 232K ratings.
- Official review totals cited by the vendor: Reface, 474,468 Apple App Store reviews at 4.8 (reface.ai/unboring); Facetune, 338K App Store reviews and 765K Google Play reviews (facetuneapp.com/pricing).
- Google Play structured data for Reface: Face Swap AI Generator (play.google.com/store/apps/details?id=video.reface.app): 1.8M ratings (ratingCount 1,804,633).
- Photoroom’s official App Store listing states it is trusted by over 300 million users. That is a vendor claim, noted as such in the caption.

**Official pricing (checked 14 November 2026)**

- Picsart Pro $15/month, or $10.50/month billed yearly, labeled most popular: picsart.com/pricing.
- Photoroom Pro $7.50/month billed yearly, labeled most popular: photoroom.com/pricing.
- Facetune Yearly $77.99/year (about $6.50/month), labeled most popular; monthly starts at $25/month: facetuneapp.com/pricing.
- Reface web Basic $7.58/month billed annually as $90.99 (a $113.99 figure was shown struck through); Premium $9.99/month billed annually as $119.99: reface.ai/unboring. Mobile app prices may differ.
- Topaz Photo Personal $39/month with no commitment, or $25/month on an annual commitment, or $199/year billed annually: topazlabs.com/topaz-photo. Rated on Personal $39/month.
- Let’s Enhance Pro $32/month, or $24/month billed annually, labeled most popular; Starter $12/month, or $9/month billed annually: letsenhance.io/pricing.
- Magnific Premium $20/month, or $14.50/month billed annually: magnific.com/pricing. Plus is labeled best value.

FaceApp, Remini, Lensa, and Fotor have editorial cost bands. FaceApp and Lensa publish no public price list (in-app only). Remini’s US App Store listing shows Remini Pro Weekly at $9.99, Remini Lite Weekly from $4.99, and a 1 Month plan at $9.99, but offers vary and there is no single public list. Fotor’s official pricing page did not expose a dollar figure as text in this session. No dollar amounts were invented for those rows.

**Icons**

- Official vendor or App Store / Google Play app icons, stored locally as 128×128 PNGs. See `icons/README.md` for the per-file source list.

## Nov 14, 2026 — More sourced popularity, shorter captions

A second research pass replaced editorial popularity estimates wherever a real, citable figure could be found. Popularity sourced rows went from 20 to 78 of 101. The remaining 23 stay labeled “Editorial estimate.” No numbers were invented.

Captions were shortened to one or two short lines (plan and price, source, checked date). Cost is now rated, on every page, on the typical individual paid plan most people buy: the plan the vendor marks as popular or most popular when they mark one; otherwise the ordinary individual paid plan, not the cheapest limited tier and not an ultra or teams tier.

**Caption and band fixes**

- ElevenLabs: wording corrected to Creator $22/month ($11 first month), labeled popular; Starter is $6/month after a $1 first month (elevenlabs.io/pricing).
- Midjourney: band moved from Basic $10 (`$`) to Standard $30 (`$$$`), the typical individual paid plan most people buy (midjourney.com/pricing).
- Suno: Pro $10/month or $8/month billed yearly, labeled most popular, is now a sourced price (suno.com/pricing). Previously the dollar figure had not been captured.
- Cursor and Grok: rechecked against official cursor.com/pricing and x.ai/pricing. They do share one X Subscription ladder and a usage pool (Free; Plus $8/month, Grok models only in Cursor; Premium $30/month, labeled most popular; Super $100; Ultra $200). Subscriptions are sold through X Subscription Corp. The earlier caption was kept and tightened, not reversed.

**New or added popularity sources (checked 14 November 2026)**

- Similarweb website-visit estimates for October 2026, as published on SeekTool category and tool pages (SeekTool states the figures come from Similarweb and that visits are not unique users). Examples: Character.AI 154.2M; Suno 78.1M; Meta AI 43.9M; ElevenLabs 42.4M; Qwen 35.1M; Cursor 23.3M; Tripo 25.2M; Meshy 19.5M; Manus 19.2M; SeaArt 15.7M; Kling 16.1M; Google Antigravity 16.1M; Rodin/hyper3d.ai 10.8M; HeyGen 9.7M; Midjourney 8.6M; Mistral.ai 8.0M (company site); Leonardo 7.6M; Runway 7.5M; Otter 7.36M; Speechify 5.46M; Make 5.16M; Zapier 5.07M; n8n.io 4.52M; Fireflies 4.41M; Vidu 4.0M; Descript 3.27M; Notta 2.59M; Windsurf 2.55M; Luma Labs 2.25M; Ideogram 1.9M; Cartesia 1.78M; Microsoft Designer 1.64M; Recraft 1.54M; Rev 1.52M; Udio 1.06M; Pika 1.06M; Exa 1.06M; You.com 948K; Deepgram 864K; Fathom 807K; Spline 588K; 3D AI Studio 616K; AssemblyAI 454K; Lindy 323K; Gemini Code Assist (codeassist.google) 231K; Soundraw 205K; Relevance AI 192K; Hume 188K; Resemble 185K; Grain 174K; Beatoven 156K; AIVA 113K; Tabnine 70K; Phind 9.6K.
- Semrush website-visit estimates for September 2026, from Tako’s “Digital Performance of a16z Top 100 Gen AI Consumer Apps” table (Tako cites Semrush via Tako): Hailuo (hailuoai.video) 5.9M.
- GitHub API star counts, checked 14 November 2026, including earlier figures and new ones: n8n-io/n8n 210,503; openai/whisper 112,711; cline/cline 71,633; Aider-AI/aider 50,118; continuedev/continue 36,481; black-forest-labs/flux 26,059; Tencent-Hunyuan/Hunyuan3D-2 15,412; Stability-AI/stable-audio-tools 3,911.
- OpenRouter public model rankings (openrouter.ai/rankings), mid-November 2026, still used as an API-side signal (for example GLM models near the top of token usage).
- The October 2026 Similarweb seven-assistant website-visit shares used at launch are unchanged: ChatGPT 55.7%, Gemini 24.2%, Claude 11.5%, DeepSeek 3.4%, Grok 2.2%, Microsoft Copilot 1.1%, Perplexity 0.8%.

A GitHub Copilot “50 million users” figure circulating in secondary write-ups was not used. Microsoft’s FY26 Q4 earnings discussion (July 29, 2026) that we could check reported GitHub Copilot revenue growth and more than 30 million paid Microsoft 365 Copilot seats, which is a different product.

Company-wide domains were not used as product traffic (for example adobe.com for Firefly, jetbrains.com for JetBrains AI). Feature-inside-a-larger-app rows such as Sora, Veo, ChatGPT Agent, and Google AI Mode stay editorial where there is no separate public usage table.

**Published**

- Public GitHub repository: https://github.com/MarcusTravis/ai-reference (branch `main`).
- Cloudflare Pages project `aitoolchart`, production branch `main`, no build command, output directory the repo root.
- Live canonical site: https://aitoolchart.net. www.aitoolchart.net redirects to the apex with a 301.
- Connected automatic deploys from GitHub `main` to the `aitoolchart` Pages project.

**Layout**

- `--nav-h` is set from the live `.topnav` height on load and resize, so deep links and `scroll-margin-top` clear the nav on desktop and on a wrapped mobile nav. Chart column headers still stick inside the horizontal scrollport, same as bimchart.net.

## Nov 14, 2026 — Initial local release

Built the first version of the site locally: homepage with search across every product, plus ten comparison charts (LLMs and chatbots, image generation, video generation, voice/TTS and cloning, music generation, coding assistants, transcription and STT including meeting notetakers, AI search, agents and automation, and 3D generation), an Updates page, sitemap, robots.txt, and a 404 page.

The intended canonical address is https://aitoolchart.net (apex). www should redirect to the apex when the site is published. Suggested Cloudflare Pages project name: `aitoolchart`. Nothing was pushed, deployed, or purchased in this pass.

Popularity scores are 1–5 judgments (halves allowed), relative to other products on the same page. Each caption cites a source and a checked date. Captions that say “Editorial estimate” had no usable quantitative source in this research pass. Figures were not invented.

Cost is rated on a typical individual paid plan per month: Free; $ under $15; $$ $15–29; $$$ $30–99; $$$$ $100+ or quote-only. Usage-based APIs are labeled as editorial estimates when there is no fair individual monthly seat. The caption names the plan and the official page.

### Sources used in November 2026

**Traffic and usage**

- Similarweb estimates of visits to seven generative AI assistant websites, October 2026: ChatGPT 55.7%, Gemini 24.2%, Claude 11.5%, DeepSeek 3.4%, Grok 2.2%, Microsoft Copilot 1.1%, Perplexity 0.8%. Reported by Similarweb and by contemporaneous write-ups of those monthly shares (including Similarweb’s own AI-search blog and a November 2026 summary of the October figures). These are website visits, not app sessions or people.
- OpenRouter public model rankings (openrouter.ai/rankings), mid-November 2026, for API-side token usage (for example DeepSeek V4.1 Flash variants in the lead, GLM 5.3 Flash near the top, Kimi K3.1 Pro in the top ten). Licensed by OpenRouter; this is routed API usage, not consumer-app traffic.
- GitHub API star counts, checked 14 November 2026: n8n-io/n8n 210,503; cline/cline 71,633; Aider-AI/aider 50,118; continuedev/continue 36,481; openai/whisper 112,711.

**Official pricing pages (checked November 2026)**

- ChatGPT Plus $20/month: OpenAI Help, “What is ChatGPT Plus?” (help.openai.com). Pro tiers $100 / $200 / $500/month: OpenAI Help, “About ChatGPT Pro tiers.” chatgpt.com/pricing lists Go, Plus, Pro, Business, and Enterprise (the Plus dollar figure was taken from Help because it was not present as text in the pricing-page HTML).
- Claude Pro $20/month or $17/month billed annually ($200 up front); Max $100/month; Ultra $200/month: claude.com/pricing.
- Google AI Plus $4.99/month, Google AI Pro $19.99/month, Google AI Ultra $99.99/month (5x) and $199.99/month (20x): one.google.com/about/google-ai-plans and gemini.google/subscriptions.
- X Subscription / Grok / Cursor: Plus $8/month, Premium $30/month (most popular), Super $100/month, Ultra $200/month: x.ai/pricing and cursor.com/pricing (same public ladder in this research pass).
- Microsoft 365 Premium $19.99/month (regular price; a first-month promotion was also shown); Microsoft 365 Pro $99.99/month: microsoft.com/en-us/copilot/pricing/individuals.
- Midjourney Basic $10/month ($8 yearly), Standard $30 ($24 yearly), Pro $60 ($48 yearly), Mega $120 ($96 yearly): midjourney.com/pricing (official page content; a direct fetch of the URL returned 403 in this environment).
- ElevenLabs Starter $6/month, Creator $22/month (popular), Pro $99/month, Scale $299, Business $990: elevenlabs.io/pricing.
- GitHub Copilot Pro $10/month, Pro+ $39/month, Max $100/month, Business $19/user/month, Enterprise $39/user/month: docs.github.com, “Plans for GitHub Copilot.”
- Windsurf Pro $20/month, Max $200/month: windsurf.com/pricing.
- Runway Standard $15/month or $12/month billed annually; Pro $35 or $28 billed annually; Max $95 or $76 billed annually: runwayml.com/pricing.
- Otter Pro $16.99/user/month, or $8.33/user/month billed annually: otter.ai/pricing.
- Zapier Professional starting from $19.99/month; Team from $69/month; Agents Pro $33.33/month billed annually ($400/year): zapier.com/pricing.
- n8n Cloud Starter 20€/month billed annually; Pro 50€/month billed annually; Business 667€/month billed annually: n8n.io/pricing.
- Mistral Pro $14.99/month (students $5.99); Team $24.99/user/month: mistral.ai/pricing.

Where a vendor pricing page could not be read, or only a usage-based API rate exists, the product caption says so and the cost band is an editorial estimate. No dollar amounts were invented for those rows.

**Icons**

- Official favicons, apple-touch icons, or app icons from vendor sites, stored locally as 128×128 PNGs. Some were retrieved through Google’s favicon service and then stored locally. See `icons/README.md` for the per-file source list. Cline uses a generated initials tile because the official page is a GitHub repository and GitHub’s site icon was not reused as the product mark.
