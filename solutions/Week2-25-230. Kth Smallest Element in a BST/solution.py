# LeetCode 230. Kth Smallest Element in a BST
# 時間複雜度: O(k) 或 O(n) 中序  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """BST 中序為遞增序，第 k 個即第 k 小。中序遍歷到第 k 個即回傳。"""
        self.k = k
        self.ans = None

        def inorder(node: Optional[TreeNode]) -> None:
            if not node or self.ans is not None:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.ans
