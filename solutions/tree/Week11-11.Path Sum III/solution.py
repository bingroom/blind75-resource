# LeetCode 437. Path Sum III
# Time: O(n)  Space: O(n)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Prefix sum approach: at each node, check how many previous
        prefix sums equal (current_sum - targetSum).
        """
        prefix_counts = {0: 1}  # base case: empty prefix
        self.count = 0

        def dfs(node: Optional[TreeNode], curr_sum: int):
            if not node:
                return
            curr_sum += node.val
            # Number of valid paths ending here
            self.count += prefix_counts.get(curr_sum - targetSum, 0)
            # Record current prefix sum
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            # Backtrack: remove current prefix sum when leaving this node
            prefix_counts[curr_sum] -= 1

        dfs(root, 0)
        return self.count
