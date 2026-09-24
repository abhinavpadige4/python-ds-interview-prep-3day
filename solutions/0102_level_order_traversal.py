"""
LeetCode 102 — Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its
nodes' values (left-to-right, level-by-level).

Example:
    Input:  root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Approach: BFS with deque. Process level by level.
Time:  O(n)
Space: O(n)
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result


if __name__ == "__main__":
    s = Solution()
    #       3
    #      / \
    #     9  20
    #        /  \
    #       15   7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]
    print("OK level order")

    assert s.levelOrder(None) == []
    print("OK empty tree")

    assert s.levelOrder(TreeNode(1)) == [[1]]
    print("OK single node")
