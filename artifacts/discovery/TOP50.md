# Top 50 plugins, skills and connectors (computed from ranked.json)

Score = 20 x (0.30 leverage + 0.25 verifiability + 0.20 fit + 0.15 readiness + 0.10 safety). Readiness is computed from install status; the other four are the mean of three judges on a 1-5 scale. Arithmetic is code; the judgments are model judgments against the stated rubric.

| Rank | Score | Type | Status | Name | What it is (catalog) | Why it ranks (architect judge) |
|---|---|---|---|---|---|---|
| 1 | 94.7 | connector | installed | Alpha Vantage MCP Server | Stock market data: stocks, options, fundamentals, earnings, SEC filings, indices, news, exchange rates, commodities, and trading signals. | About 150 read-only tools incl. EARNINGS, INCOME_STATEMENT, TIME_SERIES_DAILY: code-retrieved numbers for the markets playbook. |
| 2 | 94.0 | connector | installed | Supabase | Manage databases, authentication, and storage. | execute_sql and get_advisors return ground-truth data on the live stack; apply_migration and deploy_edge_function can change production. |
| 3 | 93.3 | connector | installed | Semrush | SEO, keyword research, competitor analysis, traffic and market analytics, backlink analysis, domain analysis, and PPC. | keyword_research, site_audit, position_tracking return ground-truth SEO data for local haul-and-leaf SEO; research reads only. |
| 4 | 92.3 | connector | installed | Airtable | Bring your structured data to Claude. | List and search records are deterministic lookups on the core data store; delete records and automations widen the blast radius. |
| 5 | 91.3 | skill | installed | forge-web-stack | Build web apps, dashboards, capture forms and AI features on the VitaForge/PANTHEON stack: Netlify functions calling the Claude API, passcode-gated dashboards over Airtable; accuracy mandate (code computes every number). | Netlify functions over Airtable with accuracy mandate: code computes every number. Exactly the user's stack. |
| 6 | 87.7 | connector | installed | Vercel | Analyze, debug, and manage projects and deployments. | Runtime logs and deployment state are ground truth for the serverless stack; but it includes purchase tools (act). |
| 7 | 87.7 | connector | installed | Netlify | Create, deploy, manage, and secure websites on Netlify. | Netlify is core stack; deploy and project readers give state checks, but deploy updaters can push to live sites. |
| 8 | 86.0 | connector | installed | Stripe | Payment processing and financial infrastructure tools. | get_balance_summary and stripe_analytics give real revenue numbers, but stripe_api_write can move money. |
| 9 | 84.0 | skill | session | claude-api | Reference for the Claude API and Anthropic SDK: model ids, pricing, parameters, streaming, tool use, MCP, agents, caching, token counting. | Reference for model ids, pricing, caching, token counting: lookup, not recall, for the Anthropic API in stack. |
| 10 | 83.0 | connector | installed | Google Drive | Search, read, and upload files. | read_file_content is retrieval from the user's own Drive; share_file and trash_file give outward and destructive reach. |
| 11 | 82.0 | connector | installed | Gmail | Draft replies, summarize threads, and search your inbox. | search_threads and get_thread retrieve real mail daily; send_message, reply, forward are act tools with outward reach. |
| 12 | 81.7 | skill | installed | xlsx | Open, edit, create and clean spreadsheets (xlsx, csv, tsv) with formulas and formatting. | Spreadsheet formulas compute numbers in files; local, no outward action. |
| 13 | 81.3 | connector | installed | Make | Run Make scenarios and manage your Make account. | Make is in stack and has blueprint validation, but scenarios run and activate can fire arbitrary downstream actions. |
| 14 | 80.7 | connector | needs-auth | FireCrawl | Search, scrape, crawl and map the web; paper-index search; page monitors. | firecrawl_search and scrape return citable page content; keyless search and scrape worked this session despite needs_reconnect. |
| 15 | 80.0 | connector | available | OpenSEO | SEO made simple: rank tracking, site audits, SERP competitors. | get_audit_issues and find_serp_competitors return checkable SEO data for local and launched sites. |
| 16 | 80.0 | connector | installed | Notion | Search, update, and power workflows across tools from your Notion workspace. | Query data sources and fetch retrieve workspace records; create-pages and update-page write only inside the user's Notion. |
| 17 | 79.7 | connector | available | Bigdata.com | AI grounding layer for finance: market data, SEC filings, earnings calls, sentiment, news, private documents, all cited. | SEC filings, earnings calls and tearsheets all cited via fetch_document: retrieval for the markets playbook. |
| 18 | 79.3 | connector | session | GitHub | Repos, issues, pull requests, branches, code search, Actions logs, secret scanning, review threads; merge is act-scope. | search_code, get_file_contents and run_secret_scanning return checkable data; merge_pull_request is act-scope, so blast radius is real. |
| 19 | 79.0 | connector | installed | Google Calendar | Manage your schedule and coordinate meetings. | list_events and suggest_time are retrieval for scheduling; delete_event and update_event are act-scope writes. |
| 20 | 79.0 | skill | installed | venture-launch-playbook | End-to-end workflow for launching a revenue-ready web business at $0 infrastructure cost, with a quality ladder and competitor recon so each launch beats the last. | Enabled user skill for $0-infra web launches with competitor recon matches the venture launcher; output is a workflow, not a check. |
| 21 | 77.7 | connector | installed | apify | Marketplace of Actors for scraping and data extraction. | get-dataset-items returns structured scraped data for local SEO and research; call-actor runs third-party marketplace Actors. |
| 22 | 77.3 | plugin | available | Samautomation Workflows (n8n) | Build or repair importable n8n workflow JSON, check its structure, test valid, duplicate and invalid events in isolation. | Read-only checker plus fixture tested on n8n 2.23.4 turns workflow JSON into a check; no network, no activation. |
| 23 | 77.3 | connector | available | Local Falcon | AI visibility and local search intelligence platform. | runLocalFalconScan returns local rank grid data for the haul service; campaigns create and run spend inside the account. |
| 24 | 77.0 | skill | installed | firecrawl (skill) | Web search (catalog description is two words). | Web search retrieval is core for research, but the FireCrawl connector entries need reconnect. |
| 25 | 77.0 | skill | installed | google-workspace | Create or change Google Docs, Sheets and Slides in Drive, with helper scripts for document positions, cell ranges and slide layout. | Helper scripts for cell ranges and document positions write Docs and Sheets inside the user's own Drive. |
| 26 | 75.0 | skill | installed | pdf | Read, merge, split, rotate, watermark, create, fill, encrypt, OCR PDFs. | Read and OCR PDFs to extract filing and lease text as data; local file operations only. |
| 27 | 75.0 | connector | installed | Zapier | Automate workflows across thousands of apps via conversation. | Execute write actions across 9,000+ apps is huge reach and huge blast radius; output is action receipts, not checks. |
| 28 | 74.7 | connector | available | Context7 | Up-to-date documentation for LLMs and AI code editors. | resolve-library-id and query-docs retrieve current docs, replacing model memory on Supabase, Netlify, and Stripe APIs. |
| 29 | 74.3 | skill | installed | skill-creator | Create, modify and evaluate skills; run evals, benchmark with variance analysis, optimize descriptions for triggering. | Runs evals and benchmarks with variance analysis, turning skill triggering into a measured check. |
| 30 | 73.3 | plugin | available | playwright (Microsoft MCP plugin) | Browser automation and end-to-end testing MCP server by Microsoft: interact with pages, take screenshots, fill forms, click elements, run automated browser tests. | Runs automated browser tests and screenshots, an exit-code check for static front ends; can fill forms and click. |
| 31 | 72.7 | connector | available | Cotality | Property and location intelligence. | find property by address and home price index return property data for the real estate venture, read-only. |
| 32 | 72.7 | connector | available | Parallel Search | Free, token-efficient web search. | Authless web_search and web_fetch are read-only retrieval with sources; not installed yet. |
| 33 | 71.7 | connector | available | TomTom Maps | Maps, routing, geocoding and traffic data. | geocode and poi-search turn haul service-area and routing lookups into tool output. |
| 34 | 71.7 | skill | installed | form-filler | Drive the user's Chrome to fill forms and official filings (LLC formation, state registrations, EIN) and pause only for passwords, card numbers, SSN and signatures. | Drives Chrome to file LLC, state registrations, EIN: direct fit, but submits official filings outward. |
| 35 | 69.7 | connector | available | AccuWeather | Hyper-local forecasts and alerts. | Authless hourly forecasts and historical data; schedules leaf-cleanup jobs on retrieved data, not guesses. |
| 36 | 68.0 | connector | needs-auth | Brevo | Analyze campaigns, know your audience and create drafts. | Brevo is in stack and analyzes campaigns, but installState needs_reconnect, so it cannot fire today; creates drafts only. |
| 37 | 68.0 | skill | session | dataviz | Chart, dashboard and data-visualization method: form heuristic, color formula with a runnable validator, mark specs, interaction rules. | Color formula ships a runnable validator; the rest is chart method guidance. |
| 38 | 67.7 | skill | session | security-review (skill) | Complete a security review of the pending changes on the current branch. | Reviews pending branch changes for the serverless functions; model review, read-only session skill. |
| 39 | 67.3 | skill | session | code-review (skill) | Review the current diff, PR number or branch for correctness bugs at a chosen effort level; --comment posts inline, --fix applies findings. | Reviews diff for correctness bugs at chosen effort; --comment posts inline and --fix applies findings. |
| 40 | 67.0 | connector | available | Paxton Legal Research | Research U.S. law with citations you can open and verify. | get_citator_info and get_source_text give openable citations for LLC, landlord and real estate questions; readiness 2. |
| 41 | 67.0 | connector | installed | Windsor.ai | Connect Meta Ads, Google Ads, TikTok Ads, LinkedIn Ads and 320 more sources. | get_data reads 320+ ad sources; execute_action writes to ad budgets and Google Business Profile. |
| 42 | 66.3 | connector | needs-auth | Intuit QuickBooks | Business finances made simple. | Profit and loss and cash flow tools are ledger data for LLCs, but not_connected and transaction import writes. |
| 43 | 65.3 | plugin | available | IQland Real Estate | U.S. real-estate development data: parcel and zoning lookup, construction cost, build feasibility, comparable sales, appraisals, property analytics. | Parcel, zoning and comps lookups for real estate via MCP iqland; community publisher, remote reach. |
| 44 | 65.3 | skill | session | workflow-authoring | Reference for writing Workflow scripts: parallel agents, pipelines, resume, quality patterns such as adversarial verify and loop-until-dry. | Reference for adversarial verify and loop-until-dry patterns; read-only reference, not itself a check. |
| 45 | 65.0 | plugin | available | Customer Research Kit | Traceable customer research from pasted text: quote ledger with ids, theme-by-source count table, fixed evidence-strength rule, contradictions, self-check that every quote appears verbatim, pseudonymised participants. | Self-check that every quote appears verbatim plus quote ledger ids makes reviews traceable; no connectors, contained. |
| 46 | 65.0 | skill | installed | mcp-builder | Guide for building high-quality MCP servers in Python (FastMCP) or TypeScript. | Guide for FastMCP or TypeScript servers lets the founder wrap Airtable or Brevo endpoints as tools; guidance only. |
| 47 | 64.7 | connector | available | Exa | Web search and code docs search. | web_search_exa and get_code_context_exa are read-only retrieval; not installed and overlaps existing search. |
| 48 | 64.7 | skill | session | fewer-permission-prompts | Scan transcripts for common read-only Bash and MCP calls and add a prioritized allowlist to project settings. | Scans transcripts for real call frequency, but writes an allowlist into project settings, loosening permission gates. |
| 49 | 64.3 | skill | session | update-config | Configure the Claude Code harness through settings.json: hooks, permissions, environment variables. | Configures hooks and permissions in settings.json, the mechanism that makes exit-code checks block; edits privileged config. |
| 50 | 64.3 | skill | session | artifact-capabilities | Runtime capabilities for published Artifact pages: live data, shared state, a database, asking Claude, file storage. | Live data, shared state and a database for published pages suit single-file HTML front ends; writes shared state. |

## Just outside the top 50

- 51. Browserbase (64.0, installed)
- 52. Axe Accessibility (Deque) (63.0, available)
- 53. equity-research (Anthropic FSI) (63.0, available)
- 54. morning (63.0, installed)
- 55. small-business (Anthropic Knowledge Work) (61.7, available)
- 56. marketing (Anthropic Knowledge Work) (60.7, available)
- 57. session-start-hook (60.3, session)
- 58. web-artifacts-builder (59.3, installed)
- 59. docx (59.0, installed)
- 60. Malwarebytes (58.7, available)
