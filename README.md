# 100hires-portfolio
Portfolio project for 100Hires Junior Growth Marketing Specialist application

## Tools Installed
1. Cursor IDE
- Downloaded and installed Cursor from cursor.com. It's essentially a code editor built on top of VS Code but with AI capabilities built in natively. It was my first time using it. The interface was familiar enough since it looks similar to other editors I've seen.
2. Claude Code Extension
- Installed the official Claude Code extension by Anthropic from Cursor's Extensions panel using Ctrl+Shift+X. Verified it was the authentic Anthropic version by checking the blue verified tick and publisher name.
3. Codex Extension
- Installed Codex from the same Extensions panel alongside Claude Code. Both showed up under installed extensions after setup.

## Steps Completed

1. Created a GitHub account and set up a public repository named 100hires-portfolio
2. Downloaded and installed Cursor IDE on my Windows laptop
3. Opened the Extensions panel in Cursor using Ctrl+Shift+X
4. Searched for and installed Claude Code by Anthropic
5. Searched for and installed Codex
6. Cloned the repository by downloading the ZIP from GitHub and opening the folder in Cursor
7. Opened and edited this README.md file

## Issues I Ran Into
- The Git Clone command through Ctrl+Shift+P in Cursor didn't seem to trigger anything visible, so I couldn't clone the repository directly through the editor. I solved this by downloading the ZIP file from GitHub directly and opening the extracted folder in Cursor instead. It worked fine as a workaround and got me to the same result.
- There were multiple Claude Code extension variants in the Extensions search — I made sure to install the verified official one by Anthropic rather than any third party versions.

## What I Learned
- Setting up a development environment from scratch when you've never used these tools before is mostly about following instructions carefully and finding workarounds when something doesn't work as expected. The tools themselves aren't complicated once you're inside them. Claude Code and Codex sitting inside Cursor gives you an AI layer directly in your editor which I can see being genuinely useful for the kind of content and research work the role involves.


---

## Round 2: LinkedIn Organic Content Strategy Research

### Topic
LinkedIn Organic Content Strategy for B2B SaaS

### Why This Topic
LinkedIn is the primary distribution channel for B2B SaaS companies. Unlike paid acquisition, organic LinkedIn content builds long-term brand authority, generates inbound pipeline, and compounds over time. Understanding what works — from algorithm dynamics to content frameworks to positioning strategy — is foundational to any B2B growth marketing role.

### What I Collected

#### LinkedIn Posts
10 experts selected based on their direct practice of LinkedIn organic content strategy for B2B SaaS. Each expert has a dedicated file in /research/linkedin-posts/ containing 3 recent posts.

| Expert | Focus | LinkedIn |
|--------|-------|----------|
| Justin Welsh | Solopreneur growth, LinkedIn organic frameworks | [Profile](https://www.linkedin.com/in/justinwelsh/) |
| Lara Acosta | B2B LinkedIn content strategy, personal branding | [Profile](https://www.linkedin.com/in/laraacostar/) |
| Richard van der Blom | LinkedIn algorithm research, data-backed insights | [Profile](https://www.linkedin.com/in/richardvanderblom/) |
| Dave Gerhardt | B2B marketing strategy, demand generation, Exit Five | [Profile](https://www.linkedin.com/in/davegerhardt/) |
| Jasmin Alic | LinkedIn copywriting, community building | [Profile](https://www.linkedin.com/in/alicjasmin/) |
| Gaetano DiNardi | B2B SaaS demand gen, SEO, GEO, content strategy | [Profile](https://www.linkedin.com/in/officialg/) |
| Katelyn Bourgoin | Buyer psychology, audience growth, proof frameworks | [Profile](https://www.linkedin.com/in/katebour/) |
| Dharmesh Shah | Founder-led growth, build in public, AI and SaaS | [Profile](https://www.linkedin.com/in/dharmesh/) |
| April Dunford | SaaS positioning, messaging strategy, GTM | [Profile](https://www.linkedin.com/in/aprildunford/) |
| Amanda Natividad | Zero-click content, AI visibility, audience research | [Profile](https://www.linkedin.com/in/amandanat/) |

#### YouTube Transcripts
2 video transcripts collected via Supadata API, stored in /research/youtube-transcripts/

- **April Dunford** — Positioning talk covering how SaaS companies should think about market positioning and messaging
- **Dave Gerhardt** — B2B ad campaigns that actually worked, covering demand gen strategy and what messaging drives results

### Key Patterns Observed Across Expert Content

**1. Resonance over reach**
Multiple experts emphasize creating content that genuinely means something to a specific audience rather than optimizing for impressions. Broad content performs poorly. Specific, opinionated content compounds.

**2. Algorithm rewards authenticity**
Richard van der Blom's data shows LinkedIn's algorithm now uses LLMs to evaluate content quality. AI-generated or templated posts are being suppressed. Genuine expertise and original thinking are rewarded with distribution.

**3. Personal profiles outperform company pages**
Consistent across all experts — personal profiles generate 5 to 8x more organic reach than company pages. Founder-led and employee-led content is the primary growth lever for B2B SaaS on LinkedIn.

**4. Positioning is the foundation**
April Dunford and Gaetano DiNardi both emphasize that content without clear positioning is noise. Before optimizing LinkedIn content, SaaS companies need a clear point of view on their market, their competition, and their category.

**5. Proof drives conversion**
Katelyn Bourgoin's framework shows that most marketers rely on weak proof while the highest converting proof is demonstrated results endorsed by trusted sources. Content that shows rather than claims performs significantly better.

**6. The Call to Engage beats the Call to Action**
Richard van der Blom's research shows closed questions drive 2.7x more engagement and open questions drive 3.4x more DM conversations. Engagement-first CTAs outperform conversion-first CTAs on LinkedIn.

### Repository Structure

```
100hires-portfolio/
├── README.md
├── get_transcripts.py
└── research/
    ├── sources.md
    ├── linkedin-posts/
    │   ├── justin-welsh.md
    │   ├── lara-acosta.md
    │   ├── richard-van-der-blom.md
    │   ├── dave-gerhardt.md
    │   ├── jasmin-alic.md
    │   ├── gaetano-dinardi.md
    │   ├── katelyn-bourgoin.md
    │   ├── dharmesh-shah.md
    │   ├── april-dunford.md
    │   └── amanda-natividad.md
    ├── youtube-transcripts/
    │   ├── april-dunford-positioning.md
    │   └── dave-gerhardt-b2b-ad-campaigns.md
    └── other/
```