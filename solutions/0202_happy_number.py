"""
LeetCode 202 — Happy Number
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the
squares of its digits. Repeat until the number equals 1 (happy) or loops
eternally in a cycle (not happy).

Example:
    Input:  n = 19
    Output: true  (1^2 + 9^2 = 82, 8^2 + 2^2 = 68, ..., 1)

Approach: Floyd's tortoise & hare (cycle detection).
Time:  O(log n) — numbers eventually drop below 3-digit range
Space: O(1)
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_sq_sum(x: int) -> int:
            total = 0
            while x:
                d = x % 10
                total += d * d
                x //= 10
            return total

        slow = n
        fast = digit_sq_sum(n)
        while fast != 1 and slow != fast:
            slow = digit_sq_sum(slow)
            fast = digit_sq_sum(digit_sq_sum(fast))
        return fast == 1


if __name__ == "__main__":
    s = Solution()
    tests = [
        (19, True),
        (1, True),
        (2, False),
        (4, False),
        (7, True),
        (10000000, True),
    ]
    for n, expected in tests:
        result = s.isHappy(n)
        assert result == expected, f"n={n} -> {result}, expected {expected}"
        print(f"OK n={n} -> {result}")
