"""
LeetCode 347 — Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Example:
    Input:  nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Approach: Counter + heap. Or Counter.most_common(k).
Time:  O(n log k) with heap, O(n) with most_common
Space: O(n)
"""
import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        # Use heap to get top-k by frequency
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _, num in heap]


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
    ]
    for nums, k, expected in tests:
        result = s.topKFrequent(nums, k)
        assert sorted(result) == sorted(expected), f"nums={nums} k={k} -> {result}, expected {expected}"
        print(f"OK nums={nums} k={k} -> {result}")
