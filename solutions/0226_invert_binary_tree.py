"""
LeetCode 226 — Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree and return its root.
Swap every left and right child.

Example:
    Input:  root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Approach: DFS recursion.
Time:  O(n)
Space: O(h)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def to_list(node):
    """BFS serialize tree."""
    if not node:
        return []
    from collections import deque
    q = deque([node])
    out = []
    while q:
        n = q.popleft()
        if n:
            out.append(n.val)
            q.append(n.left)
            q.append(n.right)
        else:
            out.append(None)
    # Trim trailing Nones
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    s = Solution()
    #       4
    #      / \
    #     2   7
    #    / \ / \
    #   1  3 6  9
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                          TreeNode(7, TreeNode(6), TreeNode(9)))
    result = s.invertTree(root)
    assert to_list(result) == [4, 7, 2, 9, 6, 3, 1]
    print("OK inverted tree")

    assert s.invertTree(None) is None
    print("OK empty tree")

    single = TreeNode(1)
    assert to_list(s.invertTree(single)) == [1]
    print("OK single node")
