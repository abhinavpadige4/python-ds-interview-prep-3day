"""
LeetCode 20 — Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '['
and ']', determine if the input string is valid.

A string is valid if:
- Open brackets are closed by the same type of bracket
- Open brackets are closed in the correct order
- Every close bracket has a corresponding open bracket of the same type

Example:
    Input:  s = "()[]{}"
    Output: true

Approach: Stack. Push open brackets, pop and match on close.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    s = Solution()
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
    ]
    for inp, expected in tests:
        result = s.isValid(inp)
        assert result == expected, f"'{inp}' -> {result}, expected {expected}"
        print(f"OK '{inp}' -> {result}")
