# tech-spec.md — global-recruit v1

> Scope note: the attached "market data" block describes parse-fault tooling, not recruitment — it's a mismatched RAG payload (note the embedded `parse-fault: Extra data: line 10 column 1` and `demand_signal: low`, `confidence: 0.3`). This spec is built against the **product hypothesis** (international student recruitment agency platform), not that block. Flagging upstream: BD/validation should re-run market research before dev spends a sprint here.

---

## Stack

| Layer | Choice | Why |
|---|---|---|
| Language | **TypeScript** (strict) end-to-end | One language across API + web; large hiring pool; agency CRUD is not perf-bound |
| Backend framework | **NestJS** (Node 20 LTS) | Opinionated modules map cleanly to domains (leads/applications/commissions); built-in DI, guards, validation pipes |
| API style | **REST + OpenAPI 3.1** (tRPC rejected — agencies will want integrations/Zapier later) | Contract-first, auto-generated client SDK |
| ORM | **Prisma 5** | Type-safe, migration tooling, good Postgres fit |
| Web frontend | **Next.js 14 (App Router) + React 18 + TanStack Query + shadcn/ui** | SSR for SEO-light dashboard, fast forms |
| Database | **PostgreSQL 16** | Relational core (leads→applications→commissions are heavily relational); JSONB for flexible per-university application fields |
| File/object store | **S3-compatible** (Cloudflare R2) | Student documents (passport, transcripts, financial proof) |
| Queue/async | **BullMQ on Redis** | Email/WhatsApp sends, document OCR, commission reconciliation jobs |
| Auth | **Lucia / Auth.js** w/ Postgres session table | No per-MAU vendor cost at seed stage; org-scoped multi-tenancy |

Runtime: Node 20 LTS, containerized (Docker, distroless base).

---

## Hosting (free-tier-first)

| Component | Platform | Free tier reality |
|---|---|---|
| API + workers | **Railway** (or Fly.io) | $5 starter credit; scales to 1 small instance ~$5–10/mo |
| Web (Next.js) | **Vercel Hobby** | Free for 1 project, non-commercial limit — move to Pro ($20/mo) at first paying customer |
| Postgres | **Neon** free tier | 0.5 GB, autosuspend; upgrade to Launch ($19/mo) at ~3 agencies |
| Redis | **Upstash** free tier | 10k cmd/day — fine for v1 job volume |
| Object storage | **Cloudflare R2** | 10 GB free, **zero egress** — critical for document-heavy app |
| Email | **Resend** free | 3k emails/mo, 100/day |
| WhatsApp/SMS | **Meta WhatsApp Cloud API** | 1k free conversations/mo (student comms differentiator vs generic CRM) |

**Cost ceiling at 0 customers: $0/mo.** First paying agency: ~$45–60/mo all-in.

---

## Data model

Multi-tenant: every table carries `org_id` (the recruitment agency). Row-Level Security enforced in Postgres.

**`organizations`** — `id`, `name`, `country`, `default_currency`, `subscription_tier`, `created_at`

**`users`** — `id`, `org_id`, `email`, `role` (`owner|counselor|finance|viewer`), `password_hash`, `last_login_at`

**`students`** (the lead) — `id`, `org_id`, `full_name`, `email`, `phone`, `nationality`, `target_country`, `intake_term`, `stage` (`new|qualifying|applying|offer|enrolled|lost`), `assigned_counselor_id`, `source`, `created_at`

**`institutions`** — `id`, `name`, `country`, `commission_rate_default`, `currency` (shared reference data, optionally org-scoped overrides)

**`applications`** — `id`, `org_id`, `student_id`, `institution_id`, `program_name`, `intake_term`, `status` (`draft|submitted|offer|rejected|deposit_paid|enrolled`), `tuition_amount`, `submitted_at`, `decision_at`, `custom_fields` (JSONB — per-institution form data)

**`documents`** — `id`, `org_id`, `student_id`, `application_id?`, `type` (`passport|transcript|ielts|financial|sop|offer_letter`), `r2_key`, `status` (`pending|verified|rejected|expired`), `expires_at`, `uploaded_by`

**`commissions`** — `id`, `org_id`, `application_id`, `institution_id`, `expected_amount`, `currency`, `status` (`forecast|invoiced|received|disputed`), `expected_date`, `received_amount`, `received_at`

**`communications`** — `id`, `org_id`, `student_id`, `channel` (`email|whatsapp|note`), `direction`, `body`, `template_id?`, `sent_by`, `external_id`, `created_at`

**`audit_log`** — `id`, `org_id`, `actor_id`, `entity`, `entity_id`, `action`, `diff` (JSONB), `created_at`

Key indexes: `(org_id, stage)` on students, `(org_id, status)` on applications/commissions, `(student_id)` on documents/communications.

---

## API surface

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/v1/students` | Create a lead (also the public lead-capture webhook target) |
| `GET` | `/v1/students?stage=&counselor=&q=` | Paginated, filtered pipeline view |
| `PATCH` | `/v1/students/:id/stage` | Move lead through funnel (emits audit + automation events) |
| `POST` | `/v1/students/:id/applications` | Open an application to an institution |
| `PATCH` | `/v1/applications/:id/status` | Update application status; on `enrolled` auto-creates commission `forecast` |
| `POST` | `/v1/documents` | Request presigned R2 upload URL + register document metadata |
| `GET` | `/v1/commissions/summary?from=&to=` | Forecast vs received revenue dashboard (core $ value of product) |
| `PATCH` | `/v1/commissions/:id` | Mark invoiced/received, attach amount |
| `POST` | `/v1/communications/send` | Send email/WhatsApp to student via template |
| `GET` | `/v1/audit-log?entity=&entity_id=` | Compliance/audit trail |

All responses envelope `{ data, meta }`; cursor pagination; OpenAPI spec generated from NestJS decorators.

---

## Security model

- **AuthN:** Session cookies (httpOnly, SameSite=Lax, Secure) backed by Postgres session table; argon2id password hashing; optional TOTP 2FA for `owner`/`finance` roles.
- **AuthZ:** Two layers — (1) NestJS `RolesGuard` for endpoint-level RBAC; (2) **Postgres Row-Level Security** keyed on `org_id` from a session-set `app.current_org` GUC, so a query bug can't leak across tenants.
- **Documents:** R2 objects are private; access only via short-lived (≤5 min) presigned URLs scoped per request. PII docs (passports, financials) — server-side encryption at rest (R2 default) + never logged.
- **Secrets:** No secrets in repo. `.env` for local; **Railway/Vercel encrypted env vars** in prod; rotate DB/R2/WhatsApp tokens quarterly. Use a single `JWT/SESSION_SECRET`, `DATABASE_URL`, `R2_*`, `RESEND_API_KEY`, `WHATSAPP_TOKEN`.
- **IAM:** R2 token scoped to single bucket, read+write only. Neon role = least-privilege app user (no superuser). CI deploy uses a scoped Railway/Vercel deploy token, not personal creds.
- **Input:** Zod/class-validator on every DTO; rate-limit auth + lead-capture endpoints (10 req/min/IP via `@nestjs/throttler`).
- **Compliance posture:** student PII implies GDPR/PDPA exposure — data export + delete endpoints scoped to `org_id` from day 1; document retention `expires_at` enforced by a purge job.

---

## Observability

- **Logs:** Structured JSON via **Pino**, one line per request with `request_id`, `org_id`, `user_id`, latency, status. Ship to **Better Stack / Logtail free tier** (1 GB/mo). Never log document bodies or PII fields.
- **Metrics:** `/metrics` Prometheus endpoint (request count/latency histogram, queue depth, job success/fail, commission-reconciliation lag). Scraped by **Grafana Cloud free tier** (10k series).
- **Traces:** **OpenTelemetry** SDK auto-instrumenting HTTP + Prisma + BullMQ; export OTLP to Grafana Tempo free tier. Trace span on every async job (email send, OCR).
- **Errors:** **Sentry free tier** (5k events/mo) on both Next.js and Nest.
- **Health:** `/health` (liveness) + `/ready` (DB + Redis + R2 ping) for platform health checks.
- **Product analytics (early):** PostHog free tier — funnel events on stage transitions to feed the validation loop back to BRAIN.

---

## Build/CI

- **Monorepo:** pnpm workspaces (`apps/api`, `apps/web`, `packages/shared` for Zod schemas + generated OpenAPI client).
- **CI (GitHub Actions, free for public/small private):**
  1. `lint` — ESLint + Prettier check + `tsc --noEmit`
  2. `test` — Vitest unit + Prisma integration against ephemeral Postgres service container
  3. `build` — Docker build (api), `next build` (web)
  4. `migrate-check` — `prisma migrate diff` fails CI on un-migrated schema drift
- **CD:** push to `main` → Railway (api/worker) + Vercel (web) auto-deploy; Prisma migrations run as a Railway pre-deploy release command.
- **Quality gates:** PRs require green CI + 1 review; coverage floor 60% on `packages/shared` and commission logic (the money path).
- **Branching:** trunk-based, short-lived feature branches; semantic-release tags on `main`.