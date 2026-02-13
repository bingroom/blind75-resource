# LeetCode 235. Lowest Common Ancestor of a BST
# 時間複雜度: O(h)  空間複雜度: O(1) 迭代
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """
        BST 的 LCA：若 p、q 都小於根則在左子樹，都大於根則在右子樹，否則根即為 LCA。
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return root
