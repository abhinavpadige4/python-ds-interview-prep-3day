"""
LeetCode 209 — Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is >= target.
Return 0 if no such subarray exists.

Example:
    Input:  target = 7, nums = [2,3,1,2,4,3]
    Output: 3  (subarray [4,3])

Approach: Sliding window. Expand right, shrink left while sum >= target.
Time:  O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        current_sum = 0
        left = 0
        for right, val in enumerate(nums):
            current_sum += val
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    s = Solution()
    tests = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
        (1, [1], 1),
    ]
    for target, nums, expected in tests:
        result = s.minSubArrayLen(target, nums)
        assert result == expected, f"target={target} nums={nums} -> {result}, expected {expected}"
        print(f"OK target={target} nums={nums} -> {result}")
