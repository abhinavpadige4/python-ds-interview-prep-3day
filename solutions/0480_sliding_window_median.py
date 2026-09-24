"""
LeetCode 480 — Sliding Window Median
https://leetcode.com/problems/sliding-window-median/

The median is the middle value in an ordered integer list. If the size
is even, median is the mean of the two middle values.

Given an array nums and a window size k, return the median for each
sliding window of size k moving from left to right.

Example:
    Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [-1, -1, 3, 5, 6, 7]

Approach: Two heaps (max-heap for lower half, min-heap for upper half)
with lazy deletion via a "to_remove" counter.
Time:  O(n log k)
Space: O(k)
"""
import heapq
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # lower: max-heap (negate values)
        # upper: min-heap
        lower = []
        upper = []
        to_remove = {}
        result = []

        def add_to_lower(x):
            heapq.heappush(lower, -x)

        def add_to_upper(x):
            heapq.heappush(upper, x)

        def rebalance():
            # lower should have ceil(k/2) elements, upper has floor(k/2)
            while len(lower) > (k + 1) // 2:
                add_to_upper(-heapq.heappop(lower))
            while len(lower) < (k + 1) // 2:
                add_to_lower(heapq.heappop(upper))

        def clean_top(heap, negate=False):
            while heap:
                val = -heap[0] if negate else heap[0]
                if to_remove.get(val, 0) > 0:
                    heapq.heappop(heap)
                    to_remove[val] -= 1
                else:
                    break

        def get_median():
            clean_top(lower, negate=True)
            clean_top(upper, negate=False)
            if k % 2 == 1:
                return -lower[0]
            else:
                return (-lower[0] + upper[0]) / 2.0

        for i, num in enumerate(nums):
            # Add to lower, then move max of lower to upper
            add_to_lower(num)
            add_to_upper(-heapq.heappop(lower))
            rebalance()

            if i >= k:
                outgoing = nums[i - k]
                to_remove[outgoing] = to_remove.get(outgoing, 0) + 1

            if i >= k - 1:
                result.append(get_median())

        return result


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [-1.0, -1.0, 3.0, 5.0, 6.0, 7.0]),
        ([1, 2, 3, 4, 5, 6, 7], 1, [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]),
        ([1, 2, 3], 3, [2.0]),
    ]
    for nums, k, expected in tests:
        result = s.medianSlidingWindow(nums, k)
        assert result == expected, f"nums={nums} k={k} -> {result}, expected {expected}"
        print(f"OK nums={nums} k={k} -> {result}")
