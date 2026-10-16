---
type: Roadmap
title: Phase 3 — Production Ownership
description: Months 8–9. Observability, SLOs, incident response, and reliability for systems you own.
tags: [career, senior, study, schedule, sre, observability]
generated: { by: human:jvmazagao, at: 2026-10-15T00:00:00-03:00 }
status: draft
---

# Phase 3 — Production Ownership (Months 8–9)

← [[02 - Phase 2 - System Design]] · Next → [[04 - Phase 4 - Code Quality and Review]]

**Goal:** your work doesn't end at merge. You know how your service behaves in production, catch problems before users do, and lead incidents calmly.

**Deliverable:** SLOs + dashboard + actionable alerts for a service you own, and one postmortem you led.

## Assignments

Graded deliverables for this phase. Each engineer has a matching submission note in their `Cohort/<name>/Submissions/` folder. See [[Mentor Hub]].

| ID | Assignment | Due week | Format | Review |
|---|---|---|---|---|
| A3.1 | [[A3.1 - Observability Audit]] | 29 | 🏭 at-work | mentor |
| A3.2 | [[A3.2 - SLOs and Burn-Rate Alerts]] | 31 | 🏭 at-work | peer+mentor |
| A3.3 | [[A3.3 - Dashboard and Runbooks]] | 32 | 🏭 at-work | peer+mentor |
| A3.4 | [[A3.4 - Game Day]] | 33 | 🎤 live | live |
| A3.5 | [[A3.5 - Blameless Postmortem]] | 34 | 📝 written | peer+mentor |
| A3.6 | [[A3.6 - Load Test]] | 36 | 🏭 at-work | mentor |

## Resources

| Type | Resource | Use |
|---|---|---|
| 📖 ⭐ | [Google SRE book](https://sre.google/sre-book/table-of-contents/): ch. 4 (SLOs), 6 (Monitoring), 12–15 (Troubleshooting, Incidents, Postmortems) | Foundations |
| 📖 ⭐ | [The SRE Workbook](https://sre.google/workbook/table-of-contents/): ch. 2 (Implementing SLOs), 5 (Alerting on SLOs) | Practice |
| 📖 | *Observability Engineering*, Majors/Fong-Jones/Miranda | Traces, high-cardinality |
| 📖 | [OpenTelemetry docs](https://opentelemetry.io/docs/) | Instrumentation |
| 📖 | [Brendan Gregg — USE method](https://www.brendangregg.com/usemethod.html), RED method | Diagnosis frameworks |
| 📖 | [Learning from Incidents](https://www.learningfromincidents.io/) | Blameless culture |
| 📖 🔸 | *Release It!* 2e, Michael Nygard | Stability patterns |

## Month 8 — Observability

### Week 29 — Signals
- [ ] Logs vs metrics vs traces: when each is the right tool
- [ ] RED (Rate, Errors, Duration) for services; USE (Utilization, Saturation, Errors) for resources
- 🧪 Audit one service you own: what can you *not* answer today?

### Week 30 — Instrumentation
- [ ] Structured logging, correlation/trace IDs, span attributes, cardinality cost
- 🧪 Add missing traces/metrics to close gaps from week 17

### Week 31 — SLOs and alerting
- [ ] SLI vs SLO vs SLA; error budgets; burn-rate alerts
- [ ] Alert on symptoms, not causes. Every page must be actionable.
- 🧪 Define 2–3 SLOs for your service; replace noisy alerts with burn-rate alerts

### Week 32 — Dashboards and runbooks
- 🧪 Build a "is it healthy?" dashboard a new on-call can read in 30 seconds
- 🧪 Write a runbook for the top 3 alerts

## Month 9 — Incidents and reliability

### Week 33 — Incident response
- [ ] Roles: incident commander, comms, ops; severity levels
- [ ] Mitigate first, root-cause later (rollback, feature flag, scale up)
- 🧪 Shadow or lead an incident; if none, run a game day / tabletop exercise

### Week 34 — Postmortems
- [ ] Blameless format: timeline, impact, contributing factors, what went well, action items
- [ ] Contributing factors, not a single "root cause"
- 🧪 Write or lead a postmortem; track action items to completion

### Week 35 — Safe delivery
- [ ] Feature flags, canary / progressive rollouts, automated rollback, DORA metrics
- [ ] Deploying migrations and config changes safely
- 🧪 Improve one step of your team's deploy pipeline

### Week 36 — Cost and capacity
- [ ] Understand the cloud bill of your service; cost per request/tenant
- [ ] Capacity planning, autoscaling, load testing (k6, Locust)
- 🧪 Load test your service; find the first bottleneck

## Self-check

- [ ] I'd know my service is broken before a customer tells us
- [ ] Every alert on my service has a runbook and is actionable
- [ ] I've led or co-led an incident and written the postmortem
- [ ] I know roughly what my service costs and where it will break under load

📝 Atomic notes: `RED and USE`, `SLO and Error Budget`, `Burn Rate Alerts`, `Blameless Postmortem`, `Progressive Delivery`
