# Diameter of Binary Tree

## Problem Description
Given the root of a binary tree, return the length of the diameter of the tree. The diameter is the length of the longest path between any two nodes (measured in number of edges). This path may or may not pass through the root.


## Solution

```python
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
```

## Approach
Compute the height of each subtree bottom-up. At each node, the longest path passing through it equals `left_height + right_height`. Track the global maximum across all nodes.

1. Base case: null node has height 0.
2. Recursively compute left and right heights.
3. Update global max with `left + right`.
4. Return `1 + max(left, right)` as this node's height.

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(h) -- recursion stack.
