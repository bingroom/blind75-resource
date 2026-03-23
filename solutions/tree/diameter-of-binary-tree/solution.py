# LeetCode 543. Diameter of Binary Tree
# Time: O(n)  Space: O(h)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Track max diameter while computing heights bottom-up."""
        self.ans = 0

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            # Diameter through this node = left + right
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        height(root)
        return self.ans
