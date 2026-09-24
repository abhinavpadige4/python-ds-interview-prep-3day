"""
LeetCode 104 — Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

Example:
    Input:  root = [3,9,20,null,null,15,7]
    Output: 3

Approach: DFS recursion.
Time:  O(n)
Space: O(h) where h is tree height
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    s = Solution()
    #       3
    #      / \
    #     9  20
    #        /  \
    #       15   7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert s.maxDepth(root) == 3
    print("OK depth 3")

    assert s.maxDepth(None) == 0
    print("OK empty tree")

    assert s.maxDepth(TreeNode(1)) == 1
    print("OK single node")

    # Skewed tree
    skewed = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert s.maxDepth(skewed) == 4
    print("OK skewed tree depth 4")
