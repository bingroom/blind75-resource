# Lowest Common Ancestor of a Binary Tree

## Problem Description
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q. The LCA is the lowest node that has both p and q as descendants (a node can be a descendant of itself).


## Solution

```python
# LeetCode 236. Lowest Common Ancestor of a Binary Tree
# Time: O(n)  Space: O(h)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        If current node is p or q, return it.
        Recurse left and right. If both return non-null, current node is LCA.
        Otherwise return whichever side is non-null.
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```

## Approach
Recursive post-order traversal:

1. If the current node is null, p, or q, return it.
2. Recurse into left and right subtrees.
3. If both sides return non-null, the current node is the LCA (p and q are in different subtrees).
4. If only one side returns non-null, propagate that result upward.

## Complexity
- **Time:** O(n) -- worst case visits all nodes.
- **Space:** O(h) -- recursion stack.
