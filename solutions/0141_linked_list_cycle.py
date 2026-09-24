"""
LeetCode 141 — Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given the head of a linked list, determine if the linked list has a cycle
in it. If there is a cycle, return true; otherwise return false.

A cycle exists if some node in the list can be reached again by following
the next pointers continuously.

Example:
    Input:  head = [3,2,0,-4], pos = 1
    Output: true  (tail connects to index 1)

Approach: Floyd's tortoise & hare. Fast moves 2, slow moves 1.
If they meet, there's a cycle.
Time:  O(n)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    # Build list with cycle: 1 -> 2 -> 3 -> 4 -> 2
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # cycle
    s = Solution()
    assert s.hasCycle(n1) is True
    print("OK cycle detected")

    # No cycle
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    assert s.hasCycle(n1) is False
    print("OK no cycle")

    # Empty
    assert s.hasCycle(None) is False
    print("OK empty list")
