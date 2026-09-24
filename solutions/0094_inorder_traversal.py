"""
LeetCode 94 — Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its
nodes' values. Inorder: left -> root -> right.

Example:
    Input:  root = [1,null,2,3]
    Output: [1,3,2]

Approach: Iterative with explicit stack (avoids recursion limit).
Time:  O(n)
Space: O(h)
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        while curr or stack:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result


if __name__ == "__main__":
    s = Solution()
    #       1
    #        \
    #         2
    #        /
    #       3
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert s.inorderTraversal(root) == [1, 3, 2]
    assert s.inorderTraversalRecursive(root) == [1, 3, 2]
    print("OK inorder [1,3,2]")

    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                          TreeNode(6, TreeNode(5), TreeNode(7)))
    assert s.inorderTraversal(root) == [1, 2, 3, 4, 5, 6, 7]
    print("OK inorder [1,2,3,4,5,6,7]")

    assert s.inorderTraversal(None) == []
    print("OK empty tree")
