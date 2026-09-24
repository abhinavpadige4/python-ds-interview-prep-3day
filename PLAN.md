# 3-Day Python Data Structures Interview Prep Plan

**Dates:** 2026-09-25 → 2026-09-27
**Notion tracker:** https://app.notion.com/p/Python-Data-Structures-Interview-Prep-3-Day-Plan-3e540c05b27981dd8649f4423ec67294

**Rules of engagement**
- 25 min per problem max. If stuck, read the solution, then re-implement from scratch.
- Every problem: write it, run it, then explain it out loud in 60 seconds (interview simulation).
- Take every break. Fatigue is the #1 reason people underperform in interviews.
- Sleep 7+ hours each night. No all-nighters.

---

## DAY 1 — 2026-09-25 — Arrays, Strings, Sets, Dicts (Hash Maps)

**Goal:** Master in-place array manipulation, sliding window, and hash-map lookups.

| Time | Activity | Resource / Notes |
|------|----------|------------------|
| 09:00–09:30 | Review Python lists, tuples, strings | https://docs.python.org/3/tutorial/datastructures.html |
| 09:30–09:45 | ☕ Break | Walk, hydrate |
| 09:45–11:15 | Practice: arrays & strings (5 problems) | 283, 26, 27, 977, 209 |
| 11:15–12:00 | Review solutions, note patterns | Two-pointer, sliding window |
| 12:00–13:00 | 🍽️ Lunch break | Step away from screen |
| 13:00–13:30 | Review sets and dicts | https://realpython.com/python-sets/ · https://realpython.com/python-dicts/ |
| 13:30–14:30 | Practice: sets & dicts (5 problems) | 349, 202, 1, 36, 380 |
| 14:30–14:45 | ☕ Break | |
| 14:45–16:00 | Continue practice, review hash-map patterns | Complement lookup, frequency counting |
| 16:00–16:30 | Flashcards: key methods & time complexities | https://apps.ankiweb.net/ |
| 16:30–17:00 | Wrap-up, note weak areas | Update Notion tracker |

**Day 1 problems (10):**
1. 283 — Move Zeroes
2. 26 — Remove Duplicates from Sorted Array
3. 27 — Remove Element
4. 977 — Squares of a Sorted Array
5. 209 — Minimum Size Subarray Sum
6. 349 — Intersection of Two Arrays
7. 202 — Happy Number
8. 1 — Two Sum
9. 36 — Valid Sudoku
10. 380 — Insert Delete GetRandom O(1)

**Patterns to internalize:**
- Two-pointer (in-place removal, sorted-array ops)
- Sliding window (min subarray sum)
- Hash-map complement lookup (Two Sum)
- Set-based deduplication (Intersection, Happy Number)
- Hybrid list+dict for O(1) insert/delete/getRandom

---

## DAY 2 — 2026-09-26 — Stacks, Queues, Heaps, Bisect

**Goal:** Master LIFO/FIFO structures, monotonic stacks, and heap-based top-K problems.

| Time | Activity | Resource / Notes |
|------|----------|------------------|
| 09:00–09:30 | Review collections.deque, Counter, defaultdict, namedtuple | https://docs.python.org/3/library/collections.html |
| 09:30–09:45 | ☕ Break | |
| 09:45–11:15 | Practice: stacks & queues (5 problems) | 232, 225, 933, 20, 155 |
| 11:15–12:00 | Review solutions, note patterns | Amortized O(1), monotonic stack |
| 12:00–13:00 | 🍽️ Lunch break | |
| 13:00–13:30 | Review heapq and bisect | https://docs.python.org/3/library/heapq.html · https://docs.python.org/3/library/bisect.html |
| 13:30–15:00 | Practice: heaps & bisect (4 problems) | 621, 215, 347, 480 |
| 15:00–15:15 | ☕ Break | |
| 15:15–16:30 | Continue practice, review heap patterns | Min-heap, max-heap via negation, two-heap median |
| 16:30–17:00 | Flashcards + wrap-up | Update Notion tracker |

**Day 2 problems (9):**
1. 232 — Implement Queue using Stacks
2. 225 — Implement Stack using Queues
3. 933 — Number of Recent Calls
4. 20 — Valid Parentheses
5. 155 — Min Stack
6. 621 — Task Scheduler
7. 215 — Kth Largest Element in an Array
8. 347 — Top K Frequent Elements
9. 480 — Sliding Window Median

**Patterns to internalize:**
- Amortized O(1) via dual-structure (queue↔stack)
- Monotonic stack for matching/parentheses
- Auxiliary stack for running min
- Heap for top-K and scheduling
- Two-heap trick for streaming median

---

## DAY 3 — 2026-09-27 — Linked Lists, Trees, Mock Interview

**Goal:** Master pointer manipulation, tree traversals, and simulate a real interview.

| Time | Activity | Resource / Notes |
|------|----------|------------------|
| 09:00–09:30 | Review linked list & tree node templates | See `mock_interview/templates.py` |
| 09:30–09:45 | ☕ Break | |
| 09:45–11:15 | Practice: linked lists (4 problems) | 21, 141, 142, 206 |
| 11:15–12:00 | Review solutions, note patterns | Fast/slow pointer, dummy node |
| 12:00–13:00 | 🍽️ Lunch break | |
| 13:00–14:30 | Practice: trees (4 problems) | 104, 226, 102, 94 |
| 14:30–14:45 | ☕ Break | |
| 14:45–15:15 | Review tree patterns | BFS vs DFS, recursion vs iteration |
| 15:15–16:45 | 🎯 **MOCK INTERVIEW (90 min)** | See `mock_interview/MOCK_INTERVIEW.md` |
| 16:45–17:15 | Debrief + score yourself | Use the rubric in `mock_interview/RUBRIC.md` |
| 17:15–17:30 | Final wrap-up, sleep early | |

**Day 3 problems (8):**
1. 21 — Merge Two Sorted Lists
2. 141 — Linked List Cycle
3. 142 — Linked List Cycle II
4. 206 — Reverse Linked List
5. 104 — Maximum Depth of Binary Tree
6. 226 — Invert Binary Tree
7. 102 — Binary Tree Level Order Traversal
8. 94 — Binary Tree Inorder Traversal

**Patterns to internalize:**
- Dummy head node for list surgery
- Fast/slow pointer (cycle detection, Floyd's tortoise & hare)
- Iterative + recursive reversal
- BFS with deque for level order
- DFS recursion for depth, inversion, inorder

---

## Mock interview (Day 3, 15:15–16:45)

Full script in `mock_interview/MOCK_INTERVIEW.md`. Structure:

- **0–5 min:** Warm-up, "tell me about yourself"
- **5–15 min:** Concept questions (hash maps, stacks, heaps, trees)
- **15–60 min:** Two medium problems (one from Day 1, one from Day 3)
- **60–75 min:** System-design-lite: design a URL shortener using dicts
- **75–90 min:** Reverse Q&A + debrief

---

## Success criteria

By end of Day 3 you should be able to:
- [ ] Explain time/space complexity of every core Python data structure
- [ ] Solve any medium problem in the 27 above from scratch in <25 min
- [ ] Recognize the pattern (two-pointer, sliding window, heap, monotonic stack, BFS/DFS) within 2 min of reading a problem
- [ ] Communicate a solution out loud clearly in 60 seconds
- [ ] Handle a mock interview without freezing
