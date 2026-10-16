---
type: Roadmap
title: Phase 4 — Code Quality and Review
description: Months 10–11. Managing complexity, testing strategy, safe refactoring, and code reviews that teach.
tags: [career, senior, study, schedule, code-quality]
generated: { by: human:jvmazagao, at: 2026-10-15T00:00:00-03:00 }
status: draft
---

# Phase 4 — Code Quality and Review (Months 10–11)

← [[03 - Phase 3 - Production Ownership]] · Next → [[05 - Phase 5 - Influence and Communication]]

**Goal:** write code that is easy to change for the next person, and use reviews to raise the bar of the whole team.

**Deliverable:** one refactor that removes real, measurable pain + a log of 30 substantive code reviews.

## Assignments

Graded deliverables for this phase. Each engineer has a matching submission note in their `Cohort/<name>/Submissions/` folder. See [[Mentor Hub]].

| ID | Assignment | Due week | Format | Review |
|---|---|---|---|---|
| A4.1 | [[A4.1 - Feared Module Analysis]] | 39 | 🏭 at-work | mentor |
| A4.2 | [[A4.2 - Ship the Refactor]] | 40 | 🏭 at-work | peer+mentor |
| A4.3 | [[A4.3 - Planted-Bug Review]] | 42 | 🎤 live | live |
| A4.4 | [[A4.4 - Review Log 30]] | 44 | 📝 written | mentor |

## Resources

| Type | Resource | Use |
|---|---|---|
| 📖 ⭐ | *A Philosophy of Software Design*, Ousterhout | Complexity, deep modules, information hiding |
| 📖 ⭐ | *Refactoring* 2e, Fowler | Catalog of safe transformations |
| 📖 | *Working Effectively with Legacy Code*, Feathers | Seams, characterization tests |
| 📖 | [Google Engineering Practices — Code Review](https://google.github.io/eng-practices/review/) ⭐ | How to review |
| 📖 | [Testing pyramid / Test Desiderata — Kent Beck](https://testdesiderata.com/) | What makes a good test |
| 📖 | *Tidy First?*, Kent Beck | Small structural changes |
| 📖 🔸 | *Domain-Driven Design Distilled*, Vaughn Vernon | Boundaries, ubiquitous language |

## Month 10 — Designing code

### Week 37 — Complexity
- [ ] Ousterhout ch. 1–6: change amplification, cognitive load, unknown unknowns; deep vs shallow modules
- 🧪 Find the module your team fears touching. Write down *why* it's hard.

### Week 38 — Abstractions and boundaries
- [ ] Information hiding, pulling complexity down, errors defined out of existence
- [ ] Coupling vs cohesion; dependency direction; when *not* to abstract (rule of three)
- 🧪 Sketch a better boundary for the feared module

### Week 39 — Testing strategy
- [ ] Unit vs integration vs contract vs e2e; what to mock and what not to
- [ ] Characterization tests before changing legacy code; flaky tests as bugs
- 🧪 Add characterization tests around the feared module

### Week 40 — Refactor safely
- [ ] Fowler: small steps, always green; strangler fig; branch by abstraction
- 🧪 Ship the refactor in small, reviewable PRs. Measure the result (bug rate, lead time, LOC touched per change).

## Month 11 — Reviewing code

### Week 41 — How to review
- [ ] Google eng-practices: what to look for (design → correctness → complexity → tests → naming → style)
- [ ] Label severity: `blocking` / `suggestion` / `nit` / `question`
- 🧪 Start your review log: PR, issue found, category

### Week 42 — Reviews that teach
- [ ] Explain *why*, link to a source, offer an alternative, praise good decisions
- [ ] Review the design before the diff; ask for a smaller PR when needed
- 🧪 10 reviews focusing on correctness and edge cases (errors, concurrency, retries, nulls)

### Week 43 — Raising the team bar
- [ ] Turn repeated review comments into lint rules, templates, or docs
- 🧪 Automate one recurring review comment (linter rule, CI check, PR template)

### Week 44 — Receiving review
- [ ] Write PR descriptions that make review easy: context, what/why, how to test, risks
- 🧪 20 more reviews; reread your log: are you catching design issues or only style?

## Self-check

- [ ] My PRs are small, well-described, and rarely need big rework
- [ ] My reviews regularly catch bugs/design issues, not just style
- [ ] I can refactor legacy code without breaking production
- [ ] I can explain when an abstraction is worth it and when it isn't

📝 Atomic notes: `Deep Modules`, `Characterization Tests`, `Strangler Fig`, `Code Review Checklist`, `Test Pyramid`
