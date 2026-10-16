---
type: Roadmap
title: Phase 0 — CS Fundamentals (Algorithms and Data Structures)
description: Months 1–3. Computer science foundations for engineers without a CS degree: how computers work, complexity, data structures, and core algorithms.
tags: [career, senior, study, schedule, algorithms, data-structures, fundamentals]
generated: { by: human:jvmazagao, at: 2026-10-15T00:00:00-03:00 }
status: draft
---

# Phase 0 — CS Fundamentals (Months 1–3)

← [[Mid to Senior Engineer Roadmap]] · Next → [[01 - Phase 1 - Technical Depth]]

**Who this is for:** engineers who came from a bootcamp, self-taught, or another field. You can ship features, but Big-O, recursion, trees, or graphs feel shaky, and you've never looked at what the machine actually does.

**Why it matters for senior:** the goal is not passing LeetCode interviews. Every later phase builds on this:
- Indexes are B-trees ([[01 - Phase 1 - Technical Depth|Phase 1]])
- Caches are hash maps with an eviction policy ([[02 - Phase 2 - System Design|Phase 2]])
- Dependency resolution and workflow DAGs are graphs
- The "why is this slow?" answer is often an accidental O(n²)
- Seniors catch these in code review ([[04 - Phase 4 - Code Quality and Review|Phase 4]])

**Goal:** given a problem, pick the right data structure, estimate its cost, and implement a correct solution without looking it up.

**Deliverable:** a public `dsa-from-scratch` repo implementing every core structure with tests, plus ~80 solved problems with your own notes on the pattern each one uses.

## Assignments

Graded deliverables for this phase. Each engineer has a matching submission note in their `Cohort/<name>/Submissions/` folder. See [[Mentor Hub]].

| ID | Assignment | Due week | Format | Review |
|---|---|---|---|---|
| A0.1 | [[A0.1 - Big-O Lab]] | 2 | 🧪 code | mentor |
| A0.2 | [[A0.2 - Build a Hash Map]] | 3 | 🧪 code | mentor |
| A0.3 | [[A0.3 - Pattern Journal I]] | 4 | 🧪 code | peer+mentor |
| A0.4 | [[A0.4 - Linear Structures From Scratch]] | 5 | 🧪 code | mentor |
| A0.5 | [[A0.5 - Sorting Showdown]] | 7 | 🧪 code | mentor |
| A0.6 | [[A0.6 - Mock Whiteboard I]] | 8 | 🎤 live | live |
| A0.7 | [[A0.7 - Trees and Why Indexes Are Fast]] | 9 | 🧪 code | mentor |
| A0.8 | [[A0.8 - Build System Scheduler]] | 11 | 🧪 code | mentor |
| A0.9 | [[A0.9 - Phase 0 Exam]] | 12 | 🎤 live | live |

## Resources

| Type | Resource | Use |
|---|---|---|
| 📖 ⭐ | *Grokking Algorithms* 2e, Aditya Bhargava | Gentle, visual first pass |
| 📖 ⭐ | [Problem Solving with Algorithms and Data Structures using Python (free)](https://runestone.academy/ns/books/published/pythonds3/index.html) | Main textbook, interactive |
| 🧪 ⭐ | [NeetCode Roadmap / NeetCode 150](https://neetcode.io/roadmap) | Practice ordered by pattern |
| 📺 ⭐ | [NeetCode YouTube](https://www.youtube.com/@NeetCode) | Explanation after you attempt a problem |
| 🧪 | [VisuAlgo](https://visualgo.net/) | Watch structures and algorithms animate |
| 📺 | [CS50x — Harvard](https://cs50.harvard.edu/x/) weeks 0–5 | Memory, C, pointers, basics |
| 📺 | [Crash Course Computer Science](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo) eps 1–20 | How a computer works, in short episodes |
| 📖 🔸 | *Code*, Charles Petzold | From switches to CPUs, a great read |
| 📺 🔸 | [Algorithms I & II — Sedgewick (Coursera)](https://www.coursera.org/learn/algorithms-part1) | More rigor |
| 📖 🔸 | *The Algorithm Design Manual*, Skiena | Reference and "war stories" |
| 📖 🔸 | [Teach Yourself CS](https://teachyourselfcs.com/) | Long-term self-study path |

## Rules for practice

1. **Try for 25 minutes before looking at a solution.** If stuck, read only the hint or pattern, then try again.
2. **After solving:** write a 5-line note with the pattern, the key insight, the time and space complexity, and the mistake you made.
3. **Re-solve after 1 week and after 1 month** without notes. You've learned it when you can solve it cold.
4. **Easy → Medium.** Don't chase Hards. Seniors need fluency, not competitive programming.
5. **Implement structures from scratch** before using the library version, then use the library forever.

## Month 1 — How computers work + complexity + linear structures

### Week 1 — The machine
- [ ] Crash Course CS eps 1–10 (binary, logic gates, CPU, RAM, instructions)
- [ ] Binary/hex, bits and bytes, integers vs floats (why `0.1 + 0.2 != 0.3`)
- [ ] Memory: addresses, stack vs heap, what a pointer/reference is
- [ ] Processes vs threads, what the OS does (CS50 week 4 or Crash Course eps 18–20)
- 🧪 Create the `dsa-from-scratch` repo (tests + CI)

📝 Notes: `Binary and Hex`, `Stack vs Heap`, `Process vs Thread`

### Week 2 — Complexity (Big-O)
- [ ] Grokking ch. 1; Runestone ch. 3 (Analysis)
- [ ] O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ); best/average/worst; space complexity
- [ ] Amortized cost (why `list.append` is O(1))
- 🧪 Time the same task at n = 10³, 10⁴, 10⁵ with O(n) vs O(n²) code and plot it
- 📖 Revisit [[Time Complexity]]

📝 Notes: `Big-O`, `Amortized Analysis`

### Week 3 — Arrays, strings, hash maps
- [ ] Dynamic arrays (resize/copy), strings as arrays, immutability
- [ ] Hash maps and sets: hashing, collisions, load factor, why lookup is O(1) on average
- 🧪 Implement a dynamic array and a hash map (chaining)
- 🧪 NeetCode: Arrays & Hashing (8–10 problems: Two Sum, Contains Duplicate, Group Anagrams, Top K Frequent…)

📝 Notes: `Dynamic Array`, `Hash Map`, `Pattern - Frequency Count`

### Week 4 — Two pointers, sliding window, prefix sums
- 🧪 NeetCode: Two Pointers + Sliding Window (8–10 problems)
- [ ] Prefix sums for range queries
- 🔁 Re-solve week 3 problems cold

📝 Notes: `Pattern - Two Pointers`, `Pattern - Sliding Window`, `Prefix Sum`

**Month 1 self-check:** I can explain why a nested loop over two lists is slow and rewrite it with a hash set.

## Month 2 — Linked structures, recursion, sorting, searching

### Week 5 — Linked lists, stacks, queues
- [ ] Singly/doubly linked lists; stack (LIFO); queue/deque (FIFO)
- 🧪 Implement linked list, stack, queue from scratch
- 🧪 NeetCode: Stack + Linked List (8 problems), and revisit [[Valid Parentheses]]

📝 Notes: `Linked List`, `Stack`, `Queue`, `Pattern - Monotonic Stack`

### Week 6 — Recursion
- [ ] Grokking ch. 3; Runestone ch. 5: base case, recursive case, the call stack
- [ ] Recursion vs iteration; stack overflow; memoization intro
- 🧪 Factorial, Fibonacci (naive vs memoized), power set, permutations, flatten nested list
- 🧪 Draw the call tree for 3 of them by hand

📝 Notes: `Recursion`, `Call Stack`

### Week 7 — Sorting
- [ ] Runestone ch. 6: bubble/insertion (why O(n²)), merge sort, quicksort, why O(n log n) is the lower bound for comparison sorts
- [ ] Stability; counting/bucket sort; what your language's `sort` uses (Timsort/pdqsort)
- 🧪 Implement merge sort and quicksort with tests
- 📖 Revisit [[H-Index]]

📝 Notes: `Merge Sort`, `Quicksort`, `Divide and Conquer`

### Week 8 — Binary search
- [ ] Classic binary search; off-by-one discipline; searching on the answer space
- 🧪 NeetCode: Binary Search (7 problems)
- 🔁 Re-solve month 1 problems cold

📝 Notes: `Binary Search`, `Pattern - Binary Search on Answer`

**Month 2 self-check:** I can write binary search and merge sort from memory, bug-free, and trace a recursive call stack.

## Month 3 — Trees, heaps, graphs, DP

### Week 9 — Trees and BSTs
- [ ] Tree vocabulary, traversals (pre/in/post-order, level-order), BST insert/search/delete
- [ ] Balanced trees (concept only): AVL/red-black; **B-trees and why databases use them**
- 🧪 Implement BST + 4 traversals
- 🧪 NeetCode: Trees (10 problems)

📝 Notes: `Binary Tree Traversals`, `BST`, `B-Tree` (links forward to [[01 - Phase 1 - Technical Depth|Phase 1]] databases)

### Week 10 — Heaps and tries
- [ ] Heap / priority queue: push/pop O(log n), heapify O(n); top-K problems
- [ ] Trie for prefix search (autocomplete)
- 🧪 Implement a min-heap; NeetCode: Heap/Priority Queue (5) + Tries (3)

📝 Notes: `Heap`, `Pattern - Top K`, `Trie`

### Week 11 — Graphs
- [ ] Representations: adjacency list vs matrix. Revisit [[Algoritimos/Grafos/Teoria|Grafos — Teoria]]
- [ ] BFS (shortest path, unweighted), DFS, cycle detection, topological sort, Dijkstra (concept + implementation)
- [ ] Real-world mapping: dependency graphs, workflow DAGs, service call graphs
- 🧪 NeetCode: Graphs (8 problems); implement topological sort for a fake build system

📝 Notes: `BFS`, `DFS`, `Topological Sort`, `Dijkstra`

### Week 12 — Dynamic programming and greedy (intro)
- [ ] Grokking ch. 9–10: overlapping subproblems, memoization vs tabulation; when greedy works
- 🧪 NeetCode: 1-D DP (6 problems: Climbing Stairs, House Robber, Coin Change…)
- 🔁 Full review: re-solve 15 random problems from months 1–3 cold

📝 Notes: `Dynamic Programming`, `Greedy`, `Pattern - Memoization`

## Pattern cheat-sheet

| If the problem says… | Try… |
|---|---|
| "find pair/duplicate/count" | Hash map / set |
| "sorted array", "find in O(log n)" | Binary search |
| "contiguous subarray/substring" | Sliding window / prefix sum |
| "matching brackets", "next greater" | Stack / monotonic stack |
| "top K", "k-th largest", "merge K sorted" | Heap |
| "shortest path, unweighted" | BFS |
| "all combinations/permutations" | Backtracking (recursion) |
| "dependencies, ordering" | Topological sort |
| "count ways", "min/max cost", overlapping subproblems | Dynamic programming |
| "prefix lookup" | Trie |

## Keep it going after Phase 0

- **3 problems/week** (1 new, 2 re-solves) for the rest of the plan. Keep the pattern fluent.
- In code review ([[04 - Phase 4 - Code Quality and Review|Phase 4]]), check complexity: look for list lookups inside loops, repeated DB queries in loops (N+1), and unbounded recursion.

## Phase self-check

- [ ] I can state the time/space complexity of any code I write, and spot accidental O(n²)
- [ ] I can implement hash map, linked list, stack, queue, heap, BST, BFS, DFS from scratch
- [ ] Given a new Medium problem, I can name a likely pattern within 5 minutes
- [ ] I can explain why a database index makes a query fast
- [ ] ~80 problems solved, each with a pattern note, and 30+ re-solved cold
