# Engineer Program: Mid → Senior

A structured, mentor-led program that takes a mid-level software engineer to senior level in 12–15 months.

## Why this exists

Most engineers stall at mid-level for the same reason: nobody tells them what "senior" actually means, and the advice they get ("take more ownership", "think bigger") can't be practiced. Courses and books help, but promotion comes from **demonstrated behavior at work**, not from finished courses.

This repo turns "become senior" into concrete, gradable work:

- A clear definition of the target. Seniority is mostly about **scope and ambiguity**: someone the team can hand a vague, important problem to and stop worrying about it.
- A sequenced path that covers the gaps that actually block people: fundamentals, depth, design, production, review, communication, scope.
- Assignments with rubrics, so progress is evidence, not a feeling.
- A lightweight operating model for a mentor running a cohort of engineers.

It is written for two readers: **engineers** who want a path to senior, and **mentors / tech leads** who want to run that path for a team.

## How it works

The program has seven phases. Each phase ends in a **live gate**: a session scored against a rubric. An engineer doesn't advance below an average of 3 out of 4 without a plan.

| Months | Phase | You come out with |
|---|---|---|
| 1–3 | 0 · CS Fundamentals | A `dsa-from-scratch` repo + ~80 problems solved with pattern notes |
| 4–5 | 1 · Technical Depth | A deep-dive on your stack's runtime + a profiled perf fix shipped |
| 6–7 | 2 · System Design | A real RFC at work + 6 practice designs |
| 8–9 | 3 · Production Ownership | Dashboards, SLOs, and alerts for a service you own + a led postmortem |
| 10–11 | 4 · Code Quality and Review | A refactor that removes real pain + 30 high-quality reviews |
| 12–13 | 5 · Influence and Communication | A mentee, a tech talk, a cross-team decision driven to closure |
| 14–15 | 6 · Scope and Promotion | A senior-scope project shipped + a promotion packet |

Engineers with a CS degree can test out of Phase 0, which brings the program to 12 months. Expected load is about 6–8 hours a week of study, with most of the learning applied to their real job.

Across the phases there are **36 assignments**:

| Format | Count | What it looks like |
|---|---|---|
| 🧪 Code | 8 | Build it from scratch, test it, benchmark it |
| ✍️ Written | 9 | Explainers, design docs, analyses |
| 🏢 At work | 11 | Applied to real systems: profiling, SLOs, RFCs, refactors |
| 🎤 Live | 8 | Mock interviews, game days, talks, readiness panel |

Every assignment card has the same shape: why it matters, a brief, tasks, acceptance criteria, a 1–4 rubric, prompts for the mentor's review, and a stretch goal. Reviews are done by the mentor, by a peer then the mentor, or live.

## What's in the repo

| Path | Purpose |
|---|---|
| [`Mid to Senior Engineer Roadmap.md`](Mid%20to%20Senior%20Engineer%20Roadmap.md) | **Start here.** What changes from mid to senior, the pillars, schedule, bookshelf, exit criteria |
| [`Senior Engineer Competency Matrix.md`](Senior%20Engineer%20Competency%20Matrix.md) | Self-assessment rubric, re-scored monthly by the engineer and the mentor |
| `00 … 06 - Phase N - *.md` | Phase guides: goal, deliverable, reading list, month-by-month plan, self-check |
| [`Assignments/`](Assignments) | The 36 assignment cards (`A<phase>.<n>`) |
| [`Mentor Hub.md`](Mentor%20Hub.md) | How to run the program: enrollment, submission states, review SLA, cadence, gates |
| [`Brag Document.md`](Brag%20Document.md) | Weekly impact log that becomes the promotion packet |
| [`Templates/`](Templates) | Assignment card, submission, and 1:1 templates |
| [`_scripts/new_engineer.py`](_scripts/new_engineer.py) | Enrolls an engineer and generates dated submission notes |
| `Assignments.base`, `Cohort.base` | Obsidian Bases views: catalog, review queue, overdue work, progress per engineer |

## Using it

**As an engineer, solo:** read the roadmap, score yourself on the competency matrix, and work through the phases. The assignment rubrics show what good looks like even without a reviewer.

**As a mentor, running a cohort:**

1. Open this folder as an [Obsidian](https://obsidian.md) vault (the trackers use Obsidian Bases; every note is plain Markdown and readable anywhere).
2. Enroll each engineer with a Monday start date, and pair them as peer reviewers:
   ```bash
   cd _scripts
   python3 new_engineer.py "Ana Souza" 2026-11-02 --peer "Bruno Lima"
   ```
   This creates `Cohort/Ana Souza/` with a personal dashboard, a 1:1 log, and one submission note per assignment with its due date.
3. Run the loop in [`Mentor Hub.md`](Mentor%20Hub.md): clear the review queue weekly, hold 1:1s every two weeks, re-score the matrix monthly, and run the live gate at the end of each phase.

`Cohort/` is git-ignored on purpose: it holds names, 1:1 notes, and scores. Keep it private.

## Adapting it

The content is stack- and company-agnostic. Before running it with a team, map Phase 6 to your company's career ladder, swap the "at work" assignments to fit your systems, and adjust the pacing to the time your engineers actually have.
