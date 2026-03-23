# LeetCode 102. Binary Tree Level Order Traversal
# 時間複雜度: O(n)  空間複雜度: O(w) 最寬層
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """層序遍歷：BFS，每層一列表。"""
        if not root:
            return []
        q = deque([root])
        out = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(level)
        return out
