# LeetCode 662. Maximum Width of Binary Tree
# Time: O(n)  Space: O(n)

from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """BFS with position indices; width = rightmost - leftmost + 1."""
        if not root:
            return 0
        max_width = 0
        queue = deque([(root, 0)])  # (node, index)
        while queue:
            level_size = len(queue)
            _, first_idx = queue[0]
            for _ in range(level_size):
                node, idx = queue.popleft()
                # Normalize index to prevent overflow
                idx -= first_idx
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))
            # After processing level, last idx seen is the rightmost
            max_width = max(max_width, idx + 1)
        return max_width
