"""
LeetCode 1 — Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target. Each input has exactly
one solution. You may not use the same element twice.

Example:
    Input:  nums = [2,7,11,15], target = 9
    Output: [0,1]  (2 + 7 = 9)

Approach: Single-pass hash map. Store complement -> index.
Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]
    for nums, target, expected in tests:
        result = s.twoSum(nums, target)
        assert sorted(result) == sorted(expected), f"{nums} target={target} -> {result}, expected {expected}"
        print(f"OK {nums} target={target} -> {result}")
