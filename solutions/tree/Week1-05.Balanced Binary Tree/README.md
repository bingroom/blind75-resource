# Balanced Binary Tree

## Problem Description
Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is one in which the depth of the two subtrees of every node never differs by more than one.


## Solution

```python
# LeetCode 110. Balanced Binary Tree
# Time: O(n)  Space: O(h)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Bottom-up recursion: return height or -1 if unbalanced."""

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return height(root) != -1
```

## Approach
Use bottom-up recursion that returns the height of each subtree. If at any node the left and right heights differ by more than 1, return -1 to signal imbalance. This avoids redundant height calculations compared to a top-down approach.

1. Base case: null node has height 0.
2. Recursively get left and right subtree heights.
3. If either returns -1, propagate -1 (already unbalanced).
4. If `abs(left - right) > 1`, return -1.
5. Otherwise return `1 + max(left, right)`.

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(h) -- recursion stack, where h is tree height.
