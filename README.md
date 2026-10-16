# Senior Engineer Program

A mid → senior engineering mentoring program: 7 phases, 36 assignment cards with rubrics, templates, and a script to enroll engineers. Built as an [Obsidian](https://obsidian.md) vault (uses Bases for the trackers), but every note is plain Markdown.

## Layout

| Path | What |
|---|---|
| `Mid to Senior Engineer Roadmap.md` | Program overview — start here |
| `00 … 06 - Phase N - *.md` | Phase guides: goals, reading, deliverables |
| `Assignments/` | One card per assignment (`A<phase>.<n>`), with rubric and review prompts |
| `Senior Engineer Competency Matrix.md` | What "senior" means here; re-scored monthly |
| `Mentor Hub.md` | Mentor dashboard + how to run the program |
| `Templates/` | Assignment card, submission, 1:1 templates |
| `_scripts/new_engineer.py` | Enrolls an engineer: creates `Cohort/<Name>/` with dated submissions |
| `Assignments.base`, `Cohort.base` | Obsidian Bases views (catalog, review queue, overdue…) |

## Usage

Open this folder as an Obsidian vault, then:

```bash
cd _scripts
python3 new_engineer.py "Ana Souza" 2026-11-02 --peer "Bruno Lima"
```

`Cohort/` is git-ignored: it holds per-engineer notes and scores and is not meant to be public.
