Generated `business-model-canvas.md` at `/tmp/global-recruit/business-model-canvas.md`.

# Business Model Canvas — global-recruit

> Unified ops platform for international student recruitment agencies: leads → applications → documents → commissions → student comms.
> FX basis: 1 USD ≈ 36 THB (2026). TAM $5B / SAM $1B / SOM $50M.

## Customer Segments
- **Primary: SME international student recruitment agencies (3–50 counselors)** — 2k–10k applications/yr, currently on spreadsheets + WhatsApp + email. ~30–50k agencies globally; this is the wedge.
- **Secondary: solo/boutique sub-agents (1–2 seats)** routing students to master agents — high volume, low ARPU, viral land-and-expand into the agent network.
- **Tertiary (expansion): university recruitment offices & pathway providers** consuming the same data from the partner side.
- **Anti-segment:** mega-aggregators (ApplyBoard/IDP-scale) — they build in-house; selling to them stalls the roadmap.

## Value Propositions
- **One system of record for the full funnel** — target 30–40% cut in application-prep time and ~15% less lead-to-enrollment leakage.
- **Automated commission reconciliation** — agencies leak 5–10% of earned commission to poor tracking; that's the ROI story.
- **Document compliance & deadline engine** — auto-flag missing/expiring docs (passport/transcript/financials, CAS/I-20) before rejection.
- **Student comms hub** — WhatsApp/email/SMS threaded per applicant with multi-counselor handoff + audit trail.
- **Wedge over horizontal CRM (HubSpot/Zoho):** vertical schema generic CRMs can't model without months of custom work.

## Channels
- Founder-led outbound into agency associations (ICEF, AIRC) + LinkedIn to owners.
- University partner referrals — co-marketing flips the partner into distribution.
- Content/SEO on operational pain ("track student commissions", "manage CAS deadlines").
- Marketplace listings (G2, Capterra, EdTech directories).
- Sub-agent virality — master agents invite sub-agents at ~$0 CAC.

## Customer Relationships
- High-touch onboarding for first 90 days — spreadsheet migration is the #1 churn risk.
- Dedicated CSM above $500/mo (18,000 THB); pooled support below to protect margin.
- In-product self-serve (templates, checklists, guided setup).
- Quarterly business reviews surfacing recovered commission $ — anchors renewal on ROI.

## Revenue Streams
- Per-seat SaaS: Starter ~$29 (≈1,050 THB), Pro ~$59 (≈2,125 THB), Agency ~$99/seat/mo (≈3,565 THB).
- Platform fee tiers by application volume (overage above included apps/yr).
- Commission-reconciliation take 0.5–1% of recovered commission (usage line tied to ROI).
- Setup/migration fee $500–2,000 (18,000–72,000 THB).
- **Blended ARPU $1,500–4,000/agency/yr.** SOM $50M ⇒ ~12.5k–33k agencies; realistic 3-yr beachhead ~$2–4M ARR.

## Key Resources
- Vertical data model + integrations (university connectors, WhatsApp API, e-sign, OCR).
- Engineering team (multi-tenant SaaS, document pipeline, payments/reconciliation).
- Proprietary intake/commission benchmark dataset → defensible moat.
- GDPR/PDPA (Thailand) compliance posture for student PII — a sales unlock.

## Key Activities
- Product build/maintenance of funnel modules + commission engine.
- University/partner integration development (retention + distribution lever).
- Productized onboarding & data migration.
- Compliance/security operations.
- Demand-gen at associations/conferences and content.

## Key Partners
- Universities & pathway providers (data partners + referrals).
- WhatsApp Business/Twilio, DocuSign, payment/FX rails (Wise/Stripe).
- Agency associations (ICEF, AIRC).
- OCR/doc-AI vendor.
- Regional resellers/sub-agents in SE Asia, South Asia, Africa.

## Cost Structure
- Engineering & product (largest): ~$40–80k/mo (1.44–2.88M THB) at seed scale.
- Third-party API/COGS (messaging, OCR, e-sign, payments): target <20% of revenue, 75–80% gross margin.
- Onboarding/CS labor — front-loaded per customer, offset by setup fees.
- Sales & marketing — conferences + founder travel + content; CAC payback <12 months.
- Compliance & infrastructure — hosting, security audits, PDPA/GDPR tooling.

---

**One flag:** the supplied `market_data.rationale` and `research_queries` are corrupted — they describe "parse-fault handling… compilers, data pipelines, embedded systems," which is unrelated to student recruitment (looks like a `FALLTHROUGH` JSON parse-fault bled in). I built this canvas off the validated **hypothesis** and the TAM/SAM/SOM figures, which are internally consistent for the recruitment-ops space. Recommend regenerating the market-research step before the GTM/financial sections rely on that rationale. Demand signal is also flagged "low" with 0.3 confidence — worth a real validation pass before heavy build.