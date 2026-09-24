# Mock Interview — Day 3 (90 minutes)

**When:** 2026-09-27, 15:15–16:45
**Format:** Self-administered. Set a timer. Do not look at solutions until after each problem.

---

## Setup

- Close all tabs except a blank code editor and a timer.
- Grab a notebook for scratch work.
- Record yourself on video (optional but recommended).
- Use the rubric in `RUBRIC.md` to score yourself afterward.

---

## Agenda (90 min)

| Time | Segment | Notes |
|------|---------|-------|
| 0–5 min | Warm-up | "Tell me about yourself" |
| 5–15 min | Concept questions | 4 rapid-fire questions |
| 15–45 min | Problem 1 (medium) | 30 min |
| 45–50 min | Break | 5 min |
| 50–80 min | Problem 2 (medium) | 30 min |
| 80–90 min | System-design-lite + reverse Q&A | 10 min |

---

## Warm-up (5 min)

**Interviewer:** "Thanks for coming in. Before we dive in, can you give me a 60-second intro — background, what you're excited about, and why this role?"

**Your job:** Prepare a 60-second pitch. Structure:
1. Current role / education (15s)
2. What you've built (15s)
3. Why this company / role (15s)
4. What you're excited to learn (15s)

---

## Concept questions (10 min)

Answer each in 60–90 seconds out loud.

1. **Hash maps:** What's the average and worst-case time complexity of a Python `dict` lookup? When does it degrade?
2. **Stacks vs queues:** Give one real-world use case for each. Which would you use for undo/redo, and which for BFS?
3. **Heaps:** Python's `heapq` is a min-heap. How would you implement a max-heap? What's the time complexity of `heappush`?
4. **Trees:** What's the difference between BFS and DFS? Which one finds the shortest path in an unweighted graph?

---

## Problem 1 (30 min) — from Day 1

**Pick one:**
- **Two Sum (LC 1):** Given an array of integers and a target, return indices of the two numbers that add up to target.
- **Minimum Size Subarray Sum (LC 209):** Given positive integers and a target, find the minimal length subarray with sum ≥ target.

**Interviewer script:**
> "Let's start with a classic. You have an array of integers and a target sum. Find two numbers that add up to the target and return their indices. Each input has exactly one solution. You may not use the same element twice. Walk me through your approach before you code."

**What to do:**
1. Restate the problem (30s)
2. Ask clarifying questions (30s): duplicates? negative numbers? return first pair or any?
3. Propose brute force, then optimize (2 min)
4. State time/space complexity (30s)
5. Code it (15 min)
6. Walk through an example (5 min)
7. Edge cases (2 min)

---

## Problem 2 (30 min) — from Day 3

**Pick one:**
- **Reverse Linked List (LC 206):** Reverse a singly linked list.
- **Binary Tree Level Order Traversal (LC 102):** Return level-order traversal.

**Interviewer script (Reverse Linked List):**
> "Here's a singly linked list. Reverse it in-place and return the new head. Try to do it iteratively first, then tell me how you'd do it recursively."

**Interviewer script (Level Order):**
> "Given a binary tree, return its level-order traversal — a list of lists, one per level, left to right. What data structure would you reach for?"

---

## System-design-lite (10 min)

**Prompt:** "Design a URL shortener. Users submit a long URL and get back a short code. Given a short code, return the original URL. Assume 100M URLs and 1M lookups/day."

**What to cover:**
- Data model: `dict[str, str]` mapping short code → long URL
- Short code generation: base62 encoding of an auto-incrementing counter, or hash + collision check
- Reverse lookup (optional): second dict for long → short
- Storage: Redis for hot data, S3/DB for cold
- Scaling: consistent hashing, sharding by short-code prefix
- Trade-offs: hash collisions vs sequential IDs, cache invalidation

**Sample answer (60s):**
> "I'd use a dict mapping short codes to long URLs. For generation, I'd use a monotonic counter encoded in base62 — gives me 62^6 = 56 billion unique codes, plenty for 100M URLs. Lookups are O(1). For 1M lookups/day, a single Redis instance handles it easily. If we scale to billions, I'd shard by the first character of the short code. I'd also add a reverse dict for idempotent submissions."

---

## Reverse Q&A (10 min)

Prepare 3–5 questions for the interviewer:
1. What does the team's code review process look like?
2. What's the biggest technical challenge the team is facing right now?
3. How does the team balance shipping features vs technical debt?
4. What does success look like in the first 90 days?
5. What's the on-call / incident response culture like?

---

## After the mock

1. Stop recording.
2. Score yourself using `RUBRIC.md`.
3. Note 2 things you did well and 2 things to improve.
4. Update your Notion tracker.
5. Sleep early — interview day is tomorrow.
