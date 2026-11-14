# Changelog

All notable changes to the AI Reference Library, with sources.

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
