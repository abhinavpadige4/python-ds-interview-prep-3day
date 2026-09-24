"""
LeetCode 155 — Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

- push(x): Push element onto stack
- pop(): Remove the top element
- top(): Get the top element
- getMin(): Retrieve the minimum element

All operations must be O(1).

Approach: Auxiliary stack tracking running minimum.
Time:  O(1) per operation
Space: O(n)
"""
from typing import List, Tuple


class MinStack:
    def __init__(self):
        # Each entry: (value, current_min)
        self._stack: List[Tuple[int, int]] = []

    def push(self, val: int) -> None:
        current_min = val if not self._stack else min(val, self._stack[-1][1])
        self._stack.append((val, current_min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2
    ms.pop()
    assert ms.getMin() == -2
    ms.pop()
    print("OK all MinStack tests passed")
