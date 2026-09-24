"""
LeetCode 283 — Move Zeroes
https://leetcode.com/problems/move-zeroes/

Given an array nums, move all 0's to the end of it while maintaining the
relative order of the non-zero elements. Must be done in-place.

Example:
    Input:  nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Approach: Two-pointer. `write` tracks the next non-zero slot.
Time:  O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
        # Everything from `write` onward is already 0.


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 0]),
    ]
    for nums, expected in tests:
        arr = nums[:]
        s.moveZeroes(arr)
        assert arr == expected, f"{nums} -> {arr}, expected {expected}"
        print(f"OK {nums} -> {arr}")
