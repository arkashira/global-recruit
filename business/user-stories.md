# user-stories.md

> Product: **global-recruit** — unified ops platform for international student recruitment agencies (leads → applications → documents → commissions → comms).
> Personas: **Counselor** (front-line recruiter), **Agency Admin** (owner/ops manager), **Compliance Officer**, **Student/Applicant**, **University Partner**.

---

## Epic 1 — Lead Capture & Pipeline Management

### US-1.1 — Multi-source lead intake
**As a** Counselor, **I want** leads from web forms, WhatsApp, education fairs, and CSV imports to land in one inbox, **so that** no inquiry slips through the cracks across channels.
- **AC:**
  - Web form, WhatsApp Business API, and CSV upload all create a lead record with source tagged.
  - Duplicate detection on email + phone merges or flags within 2s of ingest.
  - Unassigned leads surface in a "New" queue with SLA timer (default 24h).
  - Each lead stores destination-country and intended intake-term fields.
- **Complexity:** L

### US-1.2 — Pipeline stage tracking
**As an** Agency Admin, **I want** a Kanban view of leads across stages (Inquiry → Counseling → Application → Offer → Enrolled), **so that** I can see conversion bottlenecks at a glance.
- **AC:**
  - Drag-and-drop moves a lead between stages and writes an audit entry.
  - Stage conversion rate and avg time-in-stage shown per column.
  - Filter by counselor, destination country, and intake term.
  - Stale leads (no activity > 14 days) are visually flagged.
- **Complexity:** M

### US-1.3 — Counselor assignment & workload
**As an** Agency Admin, **I want** to auto-assign incoming leads by destination expertise and current load, **so that** work is balanced and students reach the right specialist.
- **AC:**
  - Round-robin and rule-based (country/language) assignment modes selectable.
  - A counselor's open-lead count is visible before manual reassignment.
  - Reassignment notifies both old and new owner.
- **Complexity:** M

---

## Epic 2 — Applications & Document Management

### US-2.1 — Application checklist per program
**As a** Counselor, **I want** a per-program application checklist (transcripts, passport, SOP, IELTS, financials), **so that** I know exactly what's outstanding for each student.
- **AC:**
  - Checklist auto-populates from the selected university/program template.
  - Each item shows status: Missing / Received / Verified / Rejected.
  - Overall application "% complete" computed and shown on the lead card.
  - Counselor can add ad-hoc custom items.
- **Complexity:** M

### US-2.2 — Secure document upload & versioning
**As a** Student, **I want** to upload my documents through a secure portal link, **so that** I don't have to email sensitive files back and forth.
- **AC:**
  - Tokenized upload link works without the student creating a full account.
  - Files encrypted at rest; PII access logged per view/download.
  - Re-uploading a document keeps prior versions with timestamps.
  - Accepted types/size enforced (PDF, JPG, PNG; ≤ 20 MB) with clear errors.
- **Complexity:** L

### US-2.3 — Document verification & compliance audit
**As a** Compliance Officer, **I want** an audit trail of who verified or rejected each document and why, **so that** we can defend against fraud and meet partner/regulatory requirements.
- **AC:**
  - Verify/reject actions require a reason and capture user + timestamp.
  - Immutable audit log exportable to CSV/PDF for a date range.
  - Rejected documents trigger an automatic student notification (per US-4.1).
  - Bulk verification disabled — each action is individual and attributable.
- **Complexity:** M

---

## Epic 3 — Commission & Partner Finance

### US-3.1 — Commission rules per university
**As an** Agency Admin, **I want** to configure commission terms (flat fee, % of tuition, tiered) per university and program, **so that** expected earnings are tracked automatically on enrollment.
- **AC:**
  - Support flat, percentage, and tiered/bonus structures with effective dates.
  - On a lead reaching "Enrolled", an expected-commission record is auto-created.
  - Multi-currency amounts stored with the partner's billing currency.
  - Rule changes do not retroactively alter already-locked commission records.
- **Complexity:** L

### US-3.2 — Commission reconciliation & payout tracking
**As an** Agency Admin, **I want** to reconcile invoiced vs. received commissions, **so that** I can chase universities for unpaid or short-paid amounts.
- **AC:**
  - Each commission record tracks: Expected / Invoiced / Received / Written-off.
  - Aging report lists commissions unpaid > 60/90/120 days.
  - Partial payments supported with running balance.
  - Discrepancy (received ≠ invoiced) is flagged for review.
- **Complexity:** M

### US-3.3 — Sub-agent / counselor commission split
**As an** Agency Admin, **I want** to split a commission between the agency and a referring sub-agent or counselor, **so that** downstream payouts are calculated automatically.
- **AC:**
  - Split rules definable by % or fixed amount per enrolled student.
  - Sub-agent payout statement generated per period.
  - Splits recompute if the parent commission amount changes before lock.
- **Complexity:** M

---

## Epic 4 — Student Communications & Engagement

### US-4.1 — Templated multi-channel messaging
**As a** Counselor, **I want** to send templated email/WhatsApp messages with student-specific merge fields, **so that** I communicate consistently without retyping.
- **AC:**
  - Templates support merge fields (name, program, missing docs, deadline).
  - Send via email and WhatsApp from the lead record; outbound logged to timeline.
  - Per-student opt-out/consent flag respected before any send.
  - Failed sends surface a retryable error, not a silent drop.
- **Complexity:** M

### US-4.2 — Automated deadline & follow-up reminders
**As a** Student, **I want** automatic reminders for missing documents and upcoming deadlines, **so that** I don't miss my application or visa window.
- **AC:**
  - Reminders trigger off checklist gaps and program deadline dates.
  - Cadence configurable (e.g., 7/3/1 days before deadline).
  - Reminders stop automatically once the item is Received/Verified.
  - All automated messages logged on the student timeline.
- **Complexity:** M

### US-4.3 — Unified conversation timeline
**As a** Counselor, **I want** every email, WhatsApp, note, and status change on one chronological timeline, **so that** I have full context when a student calls.
- **AC:**
  - Inbound and outbound messages from all channels appear in one thread.
  - Internal notes are visually distinct and never sent to the student.
  - Timeline searchable by keyword and filterable by type.
- **Complexity:** L

---

### Summary
| Epic | Stories | Complexity mix |
|------|---------|----------------|
| Lead Capture & Pipeline | 3 | L, M, M |
| Applications & Documents | 3 | M, L, M |
| Commission & Finance | 3 | L, M, M |
| Communications & Engagement | 3 | M, M, L |

**Build-first recommendation:** Epics 1 → 2 deliver the core "single source of truth" wedge; Epic 3 (commission tracking) is the strongest differentiator vs. generic CRMs and should be prioritized over polishing comms automation in Epic 4.