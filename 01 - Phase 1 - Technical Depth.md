---
type: Roadmap
title: Phase 1 — Technical Depth
description: Months 4–5. Go below the framework into runtime, concurrency, networking, and databases.
tags: [career, senior, study, schedule, fundamentals]
generated: { by: human:jvmazagao, at: 2026-10-15T00:00:00-03:00 }
status: draft
---

# Phase 1 — Technical Depth (Months 4–5)

← [[00 - Phase 0 - CS Fundamentals]] · Next → [[02 - Phase 2 - System Design]]

**Goal:** stop treating your stack as magic. When something is slow, leaks, deadlocks, or behaves strangely, you can explain why from first principles.

**Deliverable:** a written deep-dive ("How X actually works in our stack") + one performance or reliability fix shipped, backed by profiling data.

## Assignments

Graded deliverables for this phase. Each engineer has a matching submission note in their `Cohort/<name>/Submissions/` folder. See [[Mentor Hub]].

| ID | Assignment | Due week | Format | Review |
|---|---|---|---|---|
| A1.1 | [[A1.1 - Runtime Explainer]] | 13 | 📝 written | mentor |
| A1.2 | [[A1.2 - Race Condition Lab]] | 14 | 🧪 code | mentor |
| A1.3 | [[A1.3 - Profile and Fix]] | 16 | 🏭 at-work | mentor |
| A1.4 | [[A1.4 - Query Plan Lab]] | 18 | 🏭 at-work | peer+mentor |
| A1.5 | [[A1.5 - Deep-Dive Talk]] | 20 | 🎤 live | live |

## Resources

| Type | Resource | Use |
|---|---|---|
| 📖 ⭐ | *DDIA* ch. 1–3 (data models, storage, indexes) | Database internals |
| 📖 ⭐ | Official docs for your language runtime (e.g. Python asyncio + GIL, Go scheduler, JVM GC, Node event loop) | Runtime model |
| 📖 | [Use The Index, Luke](https://use-the-index-luke.com/) | SQL indexing |
| 📖 | *High Performance Browser Networking* ([free](https://hpbn.co/)) ch. 1–4, 9–12 | TCP, TLS, HTTP |
| 📺 | [CMU 15-445 Database Systems](https://15445.courses.cs.cmu.edu/) 🔸 | Deeper DB rigor |
| 🧪 | Profilers: `py-spy`, `pprof`, async-profiler, Chrome DevTools | Hands-on |
| 📖 | [Latency numbers every programmer should know](https://gist.github.com/jboner/2841832) | Intuition |

## Month 4 — Runtime and concurrency

### Week 13 — Your runtime
- [ ] Draw the execution model of your main language: threads, event loop, scheduler, GC
- [ ] Explain: what blocks? what's CPU-bound vs I/O-bound? how does your framework handle a request?
- 🧪 Write a tiny program that demonstrates a blocking call starving an event loop / thread pool

### Week 14 — Concurrency primitives
- [ ] Locks, semaphores, channels/queues, atomics, futures/promises
- [ ] Race conditions, deadlocks, livelocks; check-then-act bugs
- 🧪 Reproduce a race condition, then fix it two ways (lock vs. redesign)

### Week 15 — Memory and performance
- [ ] Stack vs heap, allocation, GC pauses, memory leaks in managed languages
- [ ] Big-O vs. constant factors vs. I/O; cache locality
- 🧪 Profile a real endpoint/job at work. Find the top 3 costs.

### Week 16 — Ship a perf fix
- [ ] Pick one finding from week 3, fix it, measure before/after
- 📝 Write it up: hypothesis → measurement → change → result

## Month 5 — Networking and data

### Week 17 — Networking
- [ ] TCP handshake, keep-alive, connection pools, TLS, DNS
- [ ] HTTP/1.1 vs HTTP/2 vs gRPC; timeouts (connect vs read vs total)
- 🧪 `curl -v`, `tcpdump`/Wireshark one request end to end

### Week 18 — Databases I
- [ ] DDIA ch. 3: B-trees vs LSM-trees; how indexes work
- [ ] `EXPLAIN`/`EXPLAIN ANALYZE`; composite indexes; covering indexes
- 🧪 Find the slowest query in a system you own and explain its plan

### Week 19 — Databases II
- [ ] Transactions, isolation levels (read committed, repeatable read, serializable), anomalies
- [ ] N+1 queries, connection pool exhaustion, lock contention
- 🧪 Demonstrate a lost update under read committed, then fix it

### Week 20 — Deep-dive write-up
- [ ] Publish "How X actually works" internally (runtime, a DB, a queue, a framework)
- [ ] Present it in 15 min to your team

## Self-check

- [ ] I can explain why a request in our service is slow without guessing
- [ ] I know which isolation level our DB uses and what anomalies that allows
- [ ] I can explain what happens between `fetch(url)` and the response bytes
- [ ] I've used a profiler on production-like workloads

📝 Atomic notes: `Event Loop`, `Race Condition`, `Isolation Levels`, `B-Tree vs LSM`, `Connection Pooling`, `Timeouts`
