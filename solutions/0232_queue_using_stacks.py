"""
LeetCode 232 — Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

Implement a first in first out (FIFO) queue using only two stacks.
Supported operations: push, pop, peek, empty.

Approach: Two stacks. `in_stack` for pushes, `out_stack` for pops.
Transfer from in_stack to out_stack only when out_stack is empty.
Time:  Amortized O(1) per operation
Space: O(n)
"""
from typing import List


class MyQueue:
    def __init__(self):
        self._in: List[int] = []
        self._out: List[int] = []

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        self._transfer()
        return self._out.pop()

    def peek(self) -> int:
        self._transfer()
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out

    def _transfer(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False
    assert q.pop() == 2
    assert q.empty() is True
    print("OK all MyQueue tests passed")
