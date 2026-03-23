# Symmetric Tree

## Problem Description
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


## Solution

```python
# LeetCode 101. Symmetric Tree
# Time: O(n)  Space: O(h)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Check if left and right subtrees are mirror images."""

        def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val
                and is_mirror(t1.left, t2.right)
                and is_mirror(t1.right, t2.left)
            )

        return is_mirror(root, root)
```

## Approach
Use a recursive helper that checks if two subtrees are mirror images:

1. If both nodes are null, they are mirrors.
2. If only one is null, not mirrors.
3. Otherwise, values must match, and `left.left` must mirror `right.right`, and `left.right` must mirror `right.left`.

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(h) -- recursion stack.
