"""
LeetCode 380 — Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Implement the RandomizedSet class:
- insert(val): Insert val if not present. Return true if inserted.
- remove(val): Remove val if present. Return true if removed.
- getRandom(): Return a random element from the current set.

All operations must be O(1) average time.

Approach: List + dict. Dict maps value -> index in list.
To delete in O(1), swap with last element then pop.
Time:  O(1) average for all operations
Space: O(n)
"""
import random
from typing import List


class RandomizedSet:
    def __init__(self):
        self._nums: List[int] = []
        self._index: dict = {}  # value -> index in _nums

    def insert(self, val: int) -> bool:
        if val in self._index:
            return False
        self._index[val] = len(self._nums)
        self._nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._index:
            return False
        idx = self._index[val]
        last = self._nums[-1]
        # Swap with last, then pop
        self._nums[idx] = last
        self._index[last] = idx
        self._nums.pop()
        del self._index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._nums)


if __name__ == "__main__":
    rs = RandomizedSet()
    assert rs.insert(1) is True
    assert rs.insert(2) is True
    assert rs.insert(1) is False  # duplicate
    assert rs.remove(1) is True
    assert rs.remove(3) is False  # not present
    assert rs.insert(2) is False  # still there
    assert rs.insert(3) is True
    # getRandom should return 2 or 3
    for _ in range(100):
        r = rs.getRandom()
        assert r in (2, 3), f"getRandom returned {r}"
    print("OK all RandomizedSet tests passed")
