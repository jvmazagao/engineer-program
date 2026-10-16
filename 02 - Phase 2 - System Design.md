---
type: Roadmap
title: Phase 2 — System Design
description: Months 6–7. Design distributed systems for scale, failure, and change, and write it down as an RFC.
tags: [career, senior, study, schedule, system-design]
generated: { by: human:jvmazagao, at: 2026-10-15T00:00:00-03:00 }
status: draft
---

# Phase 2 — System Design (Months 6–7)

← [[01 - Phase 1 - Technical Depth]] · Next → [[03 - Phase 3 - Production Ownership]]

**Goal:** take a fuzzy requirement and produce a design that handles scale, failure, and future change, with the trade-offs written down.

**Deliverable:** one real RFC/design doc at work + six practice designs in your vault.

## Assignments

Graded deliverables for this phase. Each engineer has a matching submission note in their `Cohort/<name>/Submissions/` folder. See [[Mentor Hub]].

| ID | Assignment | Due week | Format | Review |
|---|---|---|---|---|
| A2.1 | [[A2.1 - Design Kata Series]] | 26 | 📝 written | peer+mentor |
| A2.2 | [[A2.2 - Mock Design Interview]] | 26 | 🎤 live | live |
| A2.3 | [[A2.3 - Real RFC]] | 27 | 🏭 at-work | peer+mentor |
| A2.4 | [[A2.4 - RFC Reviewer]] | 28 | 📝 written | mentor |

## Resources

| Type | Resource | Use |
|---|---|---|
| 📖 ⭐ | *DDIA* ch. 5–9, 11 (replication, partitioning, transactions, distributed trouble, consistency, streams) | Core theory |
| 📖 ⭐ | *System Design Interview* vol. 1 (Alex Xu) | Vocabulary + templates |
| 📖 | [System Design Primer](https://github.com/donnemartin/system-design-primer) | Reference |
| 📖 | [Google SRE book — Handling Overload, Addressing Cascading Failures](https://sre.google/sre-book/table-of-contents/) | Failure modes |
| 📖 | Real RFCs: [Rust RFCs](https://github.com/rust-lang/rfcs), company eng blogs | Format examples |
| 📖 🔸 | *A Philosophy of Software Design* ch. 1–9 | Module design |
| 📺 🔸 | [MIT 6.824 Distributed Systems](https://pdos.csail.mit.edu/6.824/) | Rigor |

## Month 6 — Building blocks

### Week 21 — Scaling basics
- [ ] Vertical vs horizontal scaling, stateless services, load balancing
- [ ] Caching: cache-aside, write-through, TTL, invalidation, stampede
- 🧪 Practice design #1: URL shortener

### Week 22 — Data distribution
- [ ] DDIA ch. 5–6: replication (leader/follower, multi-leader, leaderless), partitioning/sharding
- [ ] CAP, PACELC, consistency models (strong, eventual, read-your-writes)
- 🧪 Practice design #2: news feed / timeline

### Week 23 — Async and messaging
- [ ] Queues vs logs (SQS/RabbitMQ vs Kafka), at-least-once, ordering, DLQs
- [ ] Idempotency keys, outbox pattern, sagas, workflow engines (e.g. Temporal, Airflow)
- 🧪 Practice design #3: payment / order processing with retries

### Week 24 — Failure and resilience
- [ ] Timeouts, retries with backoff + jitter, circuit breakers, bulkheads, rate limiting
- [ ] Backpressure, load shedding, cascading failures
- 🧪 Practice design #4: rate limiter

## Month 7 — Design as a practice

### Week 25 — API and data modeling
- [ ] REST vs gRPC vs events; versioning; pagination; backward compatibility
- [ ] Schema evolution, migrations without downtime (expand → migrate → contract)
- 🧪 Practice design #5: notification system

### Week 26 — Trade-off thinking
- [ ] For each practice design, write "Options considered" with 2–3 alternatives and why they lost
- [ ] Learn to estimate: QPS, storage, bandwidth (back-of-the-envelope)
- 🧪 Practice design #6: a system from your own company's domain

### Week 27 — Write a real RFC
- [ ] Pick a real upcoming change at work
- [ ] Template: Context · Problem · Goals/Non-goals · Proposal · Alternatives · Risks · Rollout · Observability · Open questions
- [ ] Get early feedback from 1 senior/staff engineer *before* the big review

### Week 28 — Review and iterate
- [ ] Run the RFC review, incorporate feedback, record the decision (ADR)
- [ ] Review 2 RFCs written by others

## Self-check

- [ ] I can design a system in 45 min and defend every box on the diagram
- [ ] I always write non-goals and alternatives
- [ ] I can estimate load and storage on the back of an envelope
- [ ] I know how my design fails and what the user sees when it does

📝 Atomic notes: `Caching Strategies`, `Consistency Models`, `Outbox Pattern`, `Retries and Backoff`, `Zero-Downtime Migrations`, `RFC Template`
