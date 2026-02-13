# LeetCode 104. Maximum Depth of Binary Tree
# 時間複雜度: O(n)  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """二元樹最大深度 = 1 + max(左深度, 右深度)，遞迴即可。"""
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
