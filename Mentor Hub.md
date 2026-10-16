---
type: Dashboard
title: Mentor Hub
description: Mentor's control panel for the Mid → Senior cohort; review queue, overdue work, upcoming live sessions, and progress per engineer.
tags: [career, senior, cohort, mentoring]
generated: { by: human:jvmazagao, at: 2026-10-15T00:00:00-03:00 }
status: draft
---

# Mentor Hub

Program: [[Mid to Senior Engineer Roadmap]] · Catalog: [[Assignments.base]] · Tracker: [[Cohort.base]]

## 📥 Review queue (oldest first)

![[Cohort.base#Review queue]]

## ⚠️ Overdue

![[Cohort.base#Overdue]]

## 📅 Due in the next 14 days

![[Cohort.base#Due in next 14 days]]

## 🎤 Upcoming live sessions

Book these 1–2 weeks ahead. Some need prep: seeded PR for A4.3, failure scenario for A3.4, panel for A6.4.

![[Cohort.base#Upcoming live sessions]]

## 📈 Progress by engineer

![[Cohort.base#By engineer]]

---

## Running the program

### Enroll an engineer

```bash
cd _scripts
python3 new_engineer.py "Ana Souza" 2026-11-02 --peer "Bruno Lima"
```

This creates `Cohort/Ana Souza/` with:
- **Dashboard.** Their personal tracker (embeds their own assignments). Share this link with them.
- **1-1 Log.** For your 1:1 notes (use [[1-1 Template]]).
- **Submissions/.** One note per assignment (36), each with a computed `due` date and `state: not-started`.

Re-running the script never overwrites; it only adds submissions for new cards. Use it after adding assignments.

Pair engineers as peer buddies, A ↔ B, so `peer+mentor` items always have a reviewer.

### Submission workflow

| State | Who sets it | Meaning |
|---|---|---|
| `not-started` | script | Default |
| `in-progress` | engineer | Working on it |
| `submitted` | engineer | Ready for review; also set `submitted:` date |
| `changes-requested` | mentor | Feedback in the note; engineer fixes and re-submits |
| `approved` | mentor | Done; set `score:` (average of rubric rows) and `reviewed:` date |

### Review SLA

- **Written/code:** review within 3 working days of `submitted`. Use the card's *Mentor review prompts*.
- **Peer+mentor:** peer reviews first (48 h), then mentor.
- **Live:** score in the session, fill in the submission note the same day.
- **Rule:** at least one 👍 and at most three 🔧 per review. Prioritize; don't drown them.

### Cadence

| When | What |
|---|---|
| Weekly (15 min) | Clear the review queue; check *Overdue* |
| Biweekly (30 min) | 1:1 per engineer, logged in their 1-1 Log |
| Monthly | Engineer re-scores the [[Senior Engineer Competency Matrix]]; you score independently and compare |
| End of each phase | Live gate (A0.9, A1.5, A2.2, A3.4, A4.3, A5.2, A6.4); don't advance below avg 3 without a plan |
| Monthly (cohort) | 1 h group session: 2 engineers demo an approved deliverable, then open Q&A |

### Gates

| Phase | Gate assignment | Pass bar |
|---|---|---|
| 0 | [[A0.9 - Phase 0 Exam]] | avg ≥ 3 |
| 1 | [[A1.5 - Deep-Dive Talk]] | avg ≥ 3 |
| 2 | [[A2.2 - Mock Design Interview]] | avg ≥ 3 |
| 3 | [[A3.4 - Game Day]] | avg ≥ 3 |
| 4 | [[A4.3 - Planted-Bug Review]] | ≥ 5 of 8 issues + comment quality ≥ 3 |
| 5 | [[A5.2 - Brown-Bag Talk]] | avg ≥ 3 |
| 6 | [[A6.4 - Senior Readiness Panel]] | "ready" or "ready with gaps" + gap plan |
