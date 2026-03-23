# Inorder Successor in BST

## Problem Description
Given the root of a BST and a node `p`, find the in-order successor of `p` (the node with the smallest key greater than `p.val`). Return null if no successor exists.


## Solution

```python
# LeetCode 285. Inorder Successor in BST
# Time: O(h)  Space: O(1)

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderSuccessor(
        self, root: Optional[TreeNode], p: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        BST property: successor is the smallest node larger than p.
        Go left when current val > p.val (potential successor),
        go right otherwise.
        """
        successor = None
        while root:
            if root.val > p.val:
                successor = root  # candidate; try to find a smaller one
                root = root.left
            else:
                root = root.right  # need a larger value
        return successor
```

## Approach
Leverage BST ordering -- no need for full inorder traversal:

1. If current node's value is greater than p's value, it is a potential successor. Record it and go left to find a smaller candidate.
2. If current node's value is less than or equal to p's value, the successor must be in the right subtree. Go right.
3. When traversal ends, the last recorded candidate is the answer.

## Complexity
- **Time:** O(h) -- single root-to-leaf traversal.
- **Space:** O(1) -- iterative, no extra space.
