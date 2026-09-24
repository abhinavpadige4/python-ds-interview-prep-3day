"""
LeetCode 206 — Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list and return it.

Example:
    Input:  head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Approach: Iterative with prev/curr pointers.
Time:  O(n)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


def build(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
    ]
    for vals, expected in tests:
        result = to_list(s.reverseList(build(vals)))
        assert result == expected, f"{vals} -> {result}, expected {expected}"
        result_rec = to_list(s.reverseListRecursive(build(vals)))
        assert result_rec == expected, f"recursive {vals} -> {result_rec}, expected {expected}"
        print(f"OK {vals} -> {result}")
