"""
LeetCode 26 — Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once.
Return the length of the unique portion.

Example:
    Input:  nums = [1,1,2]
    Output: 2, nums = [1,2,_]

Approach: Two-pointer. `write` is the index of the last unique element.
Time:  O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write = 0
        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]
        return write + 1


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 4, 5], 5),
    ]
    for nums, expected_len in tests:
        arr = nums[:]
        length = s.removeDuplicates(arr)
        assert length == expected_len, f"{nums} -> len {length}, expected {expected_len}"
        print(f"OK {nums} -> len {length}, arr {arr}")
