# partner-targets.md — global-recruit Partner Integration Roadmap

> Scope note: supplied market data references "parse-fault handling" and a low/no-competitor niche — that payload is corrupted and unrelated to international student recruitment. This roadmap is built from the product hypothesis (lead → application → document → commission → comms lifecycle for student recruitment agencies), not the broken market blob.

## Prioritization logic
Rank = **(revenue-share potential × user-job criticality) ÷ integration effort**. Anything with an affiliate or rev-share kicker is floated to the top because it offsets our own infra/COGS and creates a margin line independent of subscription ARPU.

## Tier 1 — Revenue-share / affiliate first (build in MVP)

### 1. Flywire (Education payments + agent commissions) — **rev-share ⭐**
- **User job:** Collect tuition/deposit payments from students across 140+ currencies; track and reconcile agency commissions paid by partner universities.
- **Why it's #1:** Flywire's core business *is* paying education agents. Integrating their API lets us own the commission-reconciliation workflow that agencies bleed hours on today, and Flywire runs partner/referral economics on payment volume.
- **Free tier:** No flat fee to integrate; revenue is FX margin + ~$0–30 transfer fee borne by payer. No sandbox cap that matters at our volume.
- **Effort:** **M** (REST API + webhook reconciliation, KYC onboarding ~2–4 wks).
- **Rev model:** Referral/volume share on processed tuition. **High** — this is the single biggest margin lever.

### 2. Wise Platform (Multi-currency commission payouts) — **rev-share ⭐**
- **User job:** Pay sub-agents and counselors their commission split across borders cheaply; hold balances in 40+ currencies.
- **Why:** Agencies lose 3–6% to bank FX on outbound commission splits. Wise Platform offers embedded payouts with explicit **revenue-share / interchange-share** for platforms.
- **Free tier:** Sandbox free; live = mid-market FX + small fixed fee.
- **Effort:** **M** (Platform API, business verification gating).
- **Rev model:** Share of FX spread on payout volume. **High.**

### 3. Calendly (Counselor ↔ student scheduling) — **affiliate ⭐**
- **User job:** Book counseling/visa-prep calls without email tag; sync to counselor calendars.
- **Why:** Fastest path to a "looks complete" booking experience; embeddable widget.
- **Free tier:** 1 event type/user free; Standard ~$10/seat/mo for round-robin (what agencies need).
- **Effort:** **S** (embed + webhook on event.created).
- **Rev model:** Calendly affiliate program (recurring %). **Medium.**

## Tier 2 — Core workflow enablers (MVP or fast-follow)

### 4. Twilio (WhatsApp Business API + SMS) 
- **User job:** Student communications — the #1 channel for SEA/South-Asia/Africa recruitment is WhatsApp, not email. Application status nudges, document requests, deadline reminders.
- **Why:** Owns the "communications in one place" pillar of the hypothesis. WhatsApp template messaging + SMS fallback in one vendor.
- **Free tier:** $15 trial credit; WhatsApp conversation pricing ~$0.005–0.08 per 24h window by country.
- **Effort:** **M** (Conversations API + WhatsApp template approval ~1–2 wks lead time).
- **Rev model:** Markup on message volume (we resell at a margin). **Medium.**

### 5. Documenso / DocuSign (offer-letter & agreement e-signature)
- **User job:** Get student/parent signatures on representation agreements, offer acceptances, financial declarations.
- **Why:** Removes the print-sign-scan loop. **Recommend Documenso (open-source, self-hostable)** for MVP to avoid per-envelope COGS; offer DocuSign as enterprise toggle.
- **Free tier:** Documenso self-host = $0 infra-only; DocuSign API sandbox free, prod ~$0.50–2/envelope.
- **Effort:** **S** (Documenso) / **M** (DocuSign full API + branding).
- **Rev model:** None direct (cost center) → favor self-host. **Low.**

### 6. Onfido or Persona (passport / document verification)
- **User job:** Verify passport, prior transcripts, and financial-proof documents are authentic before submission to universities — fraud here kills agency-university relationships.
- **Why:** Differentiator vs. generic CRMs; universities increasingly demand verified docs.
- **Free tier:** Persona has a usable free dev tier (~limited verifications/mo); Onfido sandbox free, prod ~$1–3/check.
- **Effort:** **M** (SDK + async result webhook + manual-review fallback UI).
- **Rev model:** Resell verification at markup. **Medium.**

## Tier 3 — Stickiness / back-office (post-PMF)

### 7. QuickBooks Online / Xero (commission accounting sync) — **affiliate**
- **User job:** Push earned/paid commission ledger into the agency's accounting system; no double entry.
- **Why:** Once an agency's books flow through us, churn drops hard. Both have **affiliate/partner programs** paying recurring referral %.
- **Free tier:** Dev sandbox free; QBO/Xero subs ~$15–40/mo paid by the agency.
- **Effort:** **L** (OAuth, chart-of-accounts mapping, idempotent invoice sync — accounting edge cases are deep).
- **Rev model:** Affiliate referral + retention lift. **Medium-High (strategic).**

### 8. DeepL API (multi-language student comms & doc translation)
- **User job:** Translate student messages and university docs (counselors serve students across 10+ language groups).
- **Why:** Cheap polish feature; higher quality than Google for formal docs.
- **Free tier:** **500,000 chars/mo free**, then ~$5.49/mo + usage.
- **Effort:** **S** (single endpoint).
- **Rev model:** None direct. **Low** (UX value-add only).

## Sequenced roadmap

| Phase | Partners | Rationale |
|-------|----------|-----------|
| **MVP (wks 0–8)** | Flywire, Twilio/WhatsApp, Documenso, Calendly | Money in, comms, signatures, scheduling — the four jobs an agency does daily. Two carry rev-share. |
| **Fast-follow (wks 8–16)** | Wise Platform, Onfido/Persona | Outbound commission payouts + doc fraud defense — both monetizable. |
| **Post-PMF (wks 16+)** | QuickBooks/Xero, DeepL | Back-office lock-in + localization polish. |

## Margin thesis
Three of the eight (Flywire, Wise, QuickBooks/Xero) plus Twilio/Onfido markups give global-recruit a **transactional revenue line on top of seat-based SaaS**. Target: ≥25% of gross margin from partner rev-share/markup by month 12, so ARPU is not the only growth lever. **Do not integrate any payment partner that forbids platform rev-share** — that constraint should gate vendor selection during the Flywire/Wise contract phase.