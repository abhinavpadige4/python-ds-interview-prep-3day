"""
LeetCode 933 — Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/

Implement the RecentCounter class:
- ping(t): Adds a new request at time t and returns the number of
  requests that have happened in the past 3000 milliseconds (inclusive).

It is guaranteed that t is non-decreasing across calls.

Approach: Queue (deque). Pop from front while older than t-2999.
Time:  O(1) amortized per ping
Space: O(n)
"""
from collections import deque
from typing import Deque


class RecentCounter:
    def __init__(self):
        self._q: Deque[int] = deque()

    def ping(self, t: int) -> int:
        self._q.append(t)
        # Remove calls older than 3000ms window
        while self._q[0] < t - 2999:
            self._q.popleft()
        return len(self._q)


if __name__ == "__main__":
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(3002) == 3  # 1 is now out of window
    print("OK all RecentCounter tests passed")
