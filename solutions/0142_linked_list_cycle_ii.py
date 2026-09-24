"""
LeetCode 142 — Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return None.

Example:
    Input:  head = [3,2,0,-4], pos = 1
    Output: returns the node at index 1

Approach: Floyd's algorithm. When slow and fast meet, reset one to head
and move both one step at a time. They meet at the cycle start.
Time:  O(n)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                # Find cycle start
                ptr = head
                while ptr is not slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None


if __name__ == "__main__":
    # 1 -> 2 -> 3 -> 4 -> 2 (cycle at node 2)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    s = Solution()
    result = s.detectCycle(n1)
    assert result is n2, f"expected node 2, got {result.val if result else None}"
    print("OK cycle start detected at node 2")

    # No cycle
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    assert s.detectCycle(n1) is None
    print("OK no cycle returns None")
