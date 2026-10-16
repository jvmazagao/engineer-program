---
type: Roadmap
title: Mid → Senior Software Engineer
description: A 15-month learning path (including CS fundamentals for non-CS backgrounds) that moves a mid-level engineer from delivering assigned tasks to owning problems, systems, and outcomes.
tags: [career, senior, study, roadmap, mentoring, algorithms]
generated: { by: human:jvmazagao, at: 2026-10-15T00:00:00-03:00 }
status: draft
---

# Mid → Senior Software Engineer

Phases: [[00 - Phase 0 - CS Fundamentals]] · [[01 - Phase 1 - Technical Depth]] · [[02 - Phase 2 - System Design]] · [[03 - Phase 3 - Production Ownership]] · [[04 - Phase 4 - Code Quality and Review]] · [[05 - Phase 5 - Influence and Communication]] · [[06 - Phase 6 - Scope and Promotion]]

Self-assessment: [[Senior Engineer Competency Matrix]]

**Running it as a mentor?** Start at [[Mentor Hub]]: 36 graded assignments ([[Assignments.base]]), per-engineer dashboards, a submission/review workflow, and live sessions. Engineers start at their own `Cohort/<name>/<name> — Dashboard`.

## What actually changes

Seniority is mostly about **scope and ambiguity**. Raw coding skill matters less than people expect.

| Dimension | Mid-level | Senior |
|---|---|---|
| **Input** | Well-defined tickets | Vague problems ("checkout is slow", "we keep losing events") |
| **Output** | Working code | Solved problem + design, rollout, monitoring, docs |
| **Scope** | A feature / a few files | A system, a service, or a cross-team project |
| **Time horizon** | This sprint | This quarter and the next 1–2 years of maintenance |
| **Risk** | Asks when blocked | Spots risks before others, de-risks early |
| **People** | Receives reviews and mentoring | Gives reviews, mentors, unblocks others |
| **Trade-offs** | Picks *a* solution | Names 2–3 options, picks one, writes down why |
| **Production** | Fixes bugs assigned | Owns on-call, leads incidents, prevents recurrence |
| **Communication** | Status updates | Writes RFCs, aligns stakeholders, says "no" with reasons |

**Test:** a senior engineer is someone the team can hand an ambiguous, important problem to and stop worrying about it.

## The pillars

0. **CS fundamentals (the foundation).** Complexity, data structures, algorithms, how a computer works. Mandatory for engineers without a CS degree; everything else builds on it.
1. **Technical depth.** Know one stack down to the runtime, plus the fundamentals underneath (concurrency, networking, databases).
2. **System design.** Design for scale, failure, and change, and justify the trade-offs.
3. **Production ownership.** Observability, incidents, reliability, cost.
4. **Code quality and review.** Readable, testable, evolvable code; reviews that teach.
5. **Influence and communication.** Write design docs, align people, mentor, give and take feedback.
6. **Scope and impact.** Pick the problems that matter, deliver them end to end, and make the impact visible.

## Schedule overview (15 months, ~6–8 h/week)

| Months | Phase | Deliverable |
|---|---|---|
| 1–3 | [[00 - Phase 0 - CS Fundamentals]] | `dsa-from-scratch` repo + ~80 problems solved with pattern notes |
| 4–5 | [[01 - Phase 1 - Technical Depth]] | Deep-dive write-up on your stack's runtime + a profiling/perf fix shipped |
| 6–7 | [[02 - Phase 2 - System Design]] | 1 RFC for a real system + 6 practice designs |
| 8–9 | [[03 - Phase 3 - Production Ownership]] | Dashboards/alerts/SLOs for a service you own + 1 led postmortem |
| 10–11 | [[04 - Phase 4 - Code Quality and Review]] | A refactor that removes real pain + 30 high-quality reviews |
| 12–13 | [[05 - Phase 5 - Influence and Communication]] | 1 mentee, 1 tech talk, 1 cross-team alignment |
| 14–15 | [[06 - Phase 6 - Scope and Promotion]] | A senior-scope project shipped + promo packet / brag doc |

**Already have a CS degree?** Skip Phase 0 after passing its self-check and the plan becomes 12 months. **No CS background?** Don't skip it. Fundamentals gaps show up later in debugging, design, and reviews.

After Phase 0, keep **3 algorithm problems/week** (1 new, 2 re-solves) for the rest of the plan.

Phases overlap. **Phase 6 starts on day 1:** keep the brag doc from week 1 and look for a senior-scope project early, because promotion is evidence of work you already did at the next level.

## Weekly rhythm

- **Mon–Thu 1 h:** reading / course / practice.
- **Weekend 2–4 h:** hands-on (lab, design exercise, write-up).
- **At work (the real curriculum):** apply each phase to your current project. The study supports this; it does not replace it.
- **Friday 15 min:** update [[Brag Document]] and tick boxes.
- **Monthly:** 1:1 with manager/mentor using the [[Senior Engineer Competency Matrix]].

Legend: 📺 video · 📖 book/reading · 🧪 hands-on · 🔸 optional · ⭐ highest priority

## Core bookshelf

| Priority | Book | Why |
|---|---|---|
| ⭐ | *Grokking Algorithms* 2e, Aditya Bhargava | Gentle DS&A intro for non-CS backgrounds |
| ⭐ | *Designing Data-Intensive Applications*, Martin Kleppmann | The backend senior bible |
| ⭐ | *The Staff Engineer's Path*, Tanya Reilly | Ch. 1–4 describe senior behavior well |
| ⭐ | *A Philosophy of Software Design*, John Ousterhout | Complexity, deep modules |
| ⭐ | *Site Reliability Engineering* (Google, [free](https://sre.google/books/)) | Production ownership |
| | *System Design Interview* vol. 1–2, Alex Xu | Design vocabulary + practice |
| | *Refactoring* 2e, Martin Fowler | Safe change techniques |
| | *Working Effectively with Legacy Code*, Michael Feathers | Changing code you didn't write |
| | *The Pragmatic Programmer* 20th anniv. | Habits and craft |
| | *Staff Engineer*, Will Larson ([staffeng.com](https://staffeng.com/)) | Where this leads next |
| 🔸 | *Accelerate*, Forsgren et al. | Delivery metrics, DORA |
| 🔸 | *Thinking in Systems*, Donella Meadows | Systems thinking beyond software |
| 🔸 | *Crucial Conversations* | Hard conversations |

**Ongoing feeds:** [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/), [High Scalability](https://highscalability.com/), [ByteByteGo](https://blog.bytebytego.com/), company engineering blogs (Stripe, Uber, Discord, Cloudflare, Netflix), [danluu.com](https://danluu.com/).

## Anti-patterns to avoid

- **"Senior = writes more code faster."** No. Senior means more leverage per hour.
- **Hero mode.** Fixing everything yourself instead of making the system and the team better.
- **Resume-driven design.** Picking tech because it's interesting rather than because it fits.
- **Invisible work.** Great impact nobody knows about. Write it down.
- **Waiting for permission.** Seniors notice problems and propose solutions without being asked.
- **Only studying.** Promotion comes from demonstrated scope, not from finished courses.

## Exit criteria

You're operating at senior level when, for the last 3–6 months, you can point to evidence for most of:

- [ ] Can state the complexity of your code and pick the right data structure without thinking twice
- [ ] Led design and delivery of a multi-week project from ambiguous problem to production
- [ ] Wrote an RFC/design doc that others reviewed and that changed a decision
- [ ] Owned a service in production: dashboards, alerts, on-call, at least one postmortem
- [ ] Your code reviews regularly catch design/correctness issues, not just style
- [ ] Mentored at least one engineer with observable growth
- [ ] Made a trade-off call and communicated it to non-engineers
- [ ] Proactively identified and fixed a problem nobody assigned to you
- [ ] Manager and peers would describe you as "senior" without prompting
