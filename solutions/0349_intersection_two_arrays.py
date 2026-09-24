"""
LeetCode 349 — Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/

Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must be unique.

Example:
    Input:  nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Approach: Convert smaller array to set, filter the other.
Time:  O(m + n)
Space: O(min(m, n))
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use the smaller array for the set to save memory
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        set1 = set(nums1)
        return list(set1 & set(nums2))


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, 2, 2, 1], [2, 2], [2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([], [1, 2], []),
        ([1, 2, 3], [4, 5, 6], []),
    ]
    for nums1, nums2, expected in tests:
        result = s.intersection(nums1, nums2)
        assert sorted(result) == sorted(expected), f"{nums1} & {nums2} -> {result}, expected {expected}"
        print(f"OK {nums1} & {nums2} -> {result}")
