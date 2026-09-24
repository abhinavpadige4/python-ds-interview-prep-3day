"""
LeetCode 27 — Remove Element
https://leetcode.com/problems/remove-element/

Given an array nums and a value val, remove all instances of val in-place
and return the new length. Order of remaining elements doesn't matter.

Example:
    Input:  nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2]

Approach: Two-pointer. Overwrite with non-val elements.
Time:  O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2, 3, 0, 0, 4], 2, 6),
        ([], 1, 0),
        ([1, 2, 3], 4, 3),
    ]
    for nums, val, expected_len in tests:
        arr = nums[:]
        length = s.removeElement(arr, val)
        assert length == expected_len, f"{nums} val={val} -> {length}, expected {expected_len}"
        assert val not in arr[:length], f"val {val} still in {arr[:length]}"
        print(f"OK {nums} val={val} -> len {length}, arr {arr[:length]}")
