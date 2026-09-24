"""
LeetCode 977 — Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order, return an
array of the squares of each number sorted in non-decreasing order.

Example:
    Input:  nums = [-4,-1,-1,0,1,3]
    Output: [0,1,1,9,16,9] -> sorted: [0,1,1,9,9,16]

Approach: Two-pointer from both ends. Largest square is at either end.
Time:  O(n)
Space: O(n) for output
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1  # fill from the end
        while left <= right:
            l_sq = nums[left] * nums[left]
            r_sq = nums[right] * nums[right]
            if l_sq > r_sq:
                result[pos] = l_sq
                left += 1
            else:
                result[pos] = r_sq
                right -= 1
            pos -= 1
        return result


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([-4, -1, -1, 0, 1, 3], [0, 1, 1, 9, 9, 16]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([], []),
        ([0], [0]),
        ([1, 2, 3], [1, 4, 9]),
    ]
    for nums, expected in tests:
        result = s.sortedSquares(nums)
        assert result == expected, f"{nums} -> {result}, expected {expected}"
        print(f"OK {nums} -> {result}")
