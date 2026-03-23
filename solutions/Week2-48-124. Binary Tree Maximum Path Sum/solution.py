# LeetCode 124. Binary Tree Maximum Path Sum
# 時間複雜度: O(n)  空間複雜度: O(h)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        路徑為任意節點到任意節點（可經由根）。遞迴回傳「以該節點為端點」的最大單邊路徑和，並用「左+根+右」更新全域最大。
        """
        self.best = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = max(0, gain(node.left))
            right = max(0, gain(node.right))
            self.best = max(self.best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return self.best
