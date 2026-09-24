"""
LeetCode 215 — Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest
element in the array. Not the kth distinct element.

Example:
    Input:  nums = [3,2,1,5,6,4], k = 2
    Output: 5

Approach: Min-heap of size k. Push all, pop until size k.
Time:  O(n log k)
Space: O(k)
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 10, 4, 3, 20, 15], 3, 10),
    ]
    for nums, k, expected in tests:
        result = s.findKthLargest(nums, k)
        assert result == expected, f"nums={nums} k={k} -> {result}, expected {expected}"
        print(f"OK nums={nums} k={k} -> {result}")
