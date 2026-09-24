"""
LeetCode 225 — Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/

Implement a last in first out (LIFO) stack using only queues.
Supported operations: push, pop, top, empty.

Approach: Single queue. On push, rotate the queue so the new element
is at the front (simulating stack top).
Time:  O(n) for push, O(1) for pop/top/empty
Space: O(n)
"""
from collections import deque
from typing import Deque


class MyStack:
    def __init__(self):
        self._q: Deque[int] = deque()

    def push(self, x: int) -> None:
        self._q.append(x)
        # Rotate so x is at the front
        for _ in range(len(self._q) - 1):
            self._q.append(self._q.popleft())

    def pop(self) -> int:
        return self._q.popleft()

    def top(self) -> int:
        return self._q[0]

    def empty(self) -> bool:
        return not self._q


if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert s.empty() is False
    assert s.pop() == 1
    assert s.empty() is True
    print("OK all MyStack tests passed")
