# LeetCode 113. Path Sum II
# Time: O(n)  Space: O(h)

from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        """DFS backtracking: collect root-to-leaf paths that sum to target."""
        result: List[List[int]] = []

        def dfs(node: Optional[TreeNode], remaining: int, path: List[int]):
            if not node:
                return
            path.append(node.val)
            # Check if leaf with correct sum
            if not node.left and not node.right and remaining == node.val:
                result.append(path[:])  # copy current path
            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)
            path.pop()  # backtrack

        dfs(root, targetSum, [])
        return result
