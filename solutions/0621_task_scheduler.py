"""
LeetCode 621 — Task Scheduler
https://leetcode.com/problems/task-scheduler/

Given a array of CPU tasks represented by letters A-Z and a cooling
interval n, return the minimum number of slots needed to finish all tasks.
Same task cannot run within n slots of each other.

Example:
    Input:  tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8  (A -> B -> idle -> A -> B -> idle -> A -> B)

Approach: Count frequencies. If max_freq * (n+1) < total tasks, answer
is total tasks (no idle needed). Otherwise, answer is
(max_freq - 1) * (n + 1) + count_of_max_freq_tasks.
Time:  O(n)
Space: O(1) — 26 letters
"""
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        # Number of tasks that share the max frequency
        num_max = sum(1 for c in counts.values() if c == max_freq)
        # Idle slots needed + tasks that fill them
        idle_based = (max_freq - 1) * (n + 1) + num_max
        return max(len(tasks), idle_based)


if __name__ == "__main__":
    s = Solution()
    tests = [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "C", "A", "B", "B", "B"], 1, 6),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A"], 1, 1),
    ]
    for tasks, n, expected in tests:
        result = s.leastInterval(tasks, n)
        assert result == expected, f"tasks={tasks} n={n} -> {result}, expected {expected}"
        print(f"OK tasks={tasks} n={n} -> {result}")
