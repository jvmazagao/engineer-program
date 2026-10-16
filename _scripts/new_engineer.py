#!/usr/bin/env python3
"""Enroll an engineer in the Mid -> Senior program.

Creates Cohort/<Name>/ with a Dashboard, a 1:1 log, and one Submission note per
assignment card, each with a real due date computed from the start date.

Usage:
    python3 new_engineer.py "Ana Souza" 2026-11-02 [--peer "Bruno Lima"]

The start date should be a Monday (week 1 starts that day). Due = Sunday of the
assignment's due_week. Safe to re-run: existing files are never overwritten, so
new assignment cards added later can be synced by running it again.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSIGNMENTS = ROOT / "Assignments"
COHORT = ROOT / "Cohort"
NOW = datetime.now().astimezone().replace(microsecond=0).isoformat()


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    return dict(re.findall(r"^(\w+): (.*)$", m.group(1), re.M))


def write_new(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def submission(card: Path, fm: dict[str, str], name: str, start: date, peer: str) -> str:
    due = start + timedelta(weeks=int(fm["due_week"]) - 1, days=6)
    title = fm["title"].strip('"')
    peer_line = peer if fm.get("review") == "peer+mentor" else ""
    return f"""---
type: Submission
title: "{title} — {name}"
description: Submission for {fm['id']} by {name}
tags: [career, senior, submission]
generated: {{ by: human:jvmazagao, at: {NOW} }}
status: draft
assignment: "[[{card.stem}]]"
assignment_id: "{fm['id']}"
engineer: {name}
phase: {fm['phase']}
format: {fm['format']}
review: {fm['review']}
due: {due.isoformat()}
state: not-started
submitted:
reviewed:
peer_reviewer: {peer_line}
score:
---

# {title}

Assignment: [[{card.stem}]] · Dashboard: [[{name} — Dashboard]]

> **Workflow:** `not-started` → `in-progress` → `submitted` → (`changes-requested` → `submitted`)* → `approved`
> When you hand in: set `state: submitted` and `submitted:` to today's date.

## Artifacts

- Repo / PR:
- Doc / dashboard / recording:

## What I did

## Answers to the brief

## Self-assessment

| Criterion | My score (1–4) | Why |
|---|---|---|
| | | |

## What was hard / questions for the mentor

---

## Peer review

*Reviewer:* {peer_line}
- 👍 One thing done well:
- 🔧 One thing to improve:
- ❓ One question:

## Mentor review

| Criterion | Score (1–4) | Comment |
|---|---|---|
| | | |

**Decision:** approved / changes requested
**Next step:**
"""


def dashboard(name: str, start: date, peer: str) -> str:
    return f"""---
type: Dashboard
title: {name} — Dashboard
description: Progress dashboard for {name} in the Mid → Senior program.
tags: [career, senior, cohort]
generated: {{ by: human:jvmazagao, at: {NOW} }}
status: draft
engineer: {name}
start_date: {start.isoformat()}
peer: {peer}
---

# {name} — Dashboard

Program: [[Mid to Senior Engineer Roadmap]] · Catalog: [[Assignments.base]] · Mentor view: [[Mentor Hub]]

**Start:** {start.isoformat()} · **Peer buddy:** {peer or "—"} · 1:1s: [[{name} — 1-1 Log]] · Self-assessment: [[Senior Engineer Competency Matrix]]

## How this works

1. Open the next assignment below, read the card, and do the work.
2. Fill in the submission note, set `state: submitted` and `submitted:` to today's date.
3. Your peer (for `peer+mentor` items) and your mentor review it in the same note.
4. Fix and resubmit on `changes-requested`, or move on when it's `approved`.

## My assignments

![[Cohort.base#My work]]

## Goals for this phase

-

## Brag highlights

- (copy the best items from your brag document here monthly)
"""


def one_on_one(name: str) -> str:
    return f"""---
type: 1-1 Log
title: {name} — 1-1 Log
description: Running log of mentor 1:1s with {name}.
tags: [career, senior, cohort, one-on-one]
generated: {{ by: human:jvmazagao, at: {NOW} }}
status: draft
engineer: {name}
---

# {name} — 1-1 Log

← [[{name} — Dashboard]] · Template: [[1-1 Template]]

Newest entry on top. Copy the [[1-1 Template]] for each session.
"""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("name")
    p.add_argument("start", help="Program start date, YYYY-MM-DD (a Monday)")
    p.add_argument("--peer", default="", help="Peer buddy's name")
    a = p.parse_args()

    start = date.fromisoformat(a.start)
    if start.weekday() != 0:
        print(f"warning: {start} is not a Monday", file=sys.stderr)

    base = COHORT / a.name
    created = 0
    created += write_new(base / f"{a.name} — Dashboard.md", dashboard(a.name, start, a.peer))
    created += write_new(base / f"{a.name} — 1-1 Log.md", one_on_one(a.name))

    for card in sorted(ASSIGNMENTS.glob("*.md")):
        fm = frontmatter(card.read_text(encoding="utf-8"))
        if fm.get("type") != "Assignment":
            continue
        out = base / "Submissions" / f"{fm['id']} — {a.name}.md"
        created += write_new(out, submission(card, fm, a.name, start, a.peer))

    print(f"{a.name}: {created} file(s) created in {base}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
