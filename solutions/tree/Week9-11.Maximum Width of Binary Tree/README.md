# Maximum Width of Binary Tree

## Problem Description
Given the root of a binary tree, return the maximum width of the tree. The width of one level is defined as the length between the leftmost and rightmost non-null nodes (including null nodes in between).


## Solution

```python
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
```

## Approach
BFS with index tracking. Assign each node a position index (root = 0). For a node at index `i`, its left child is at `2*i` and right child at `2*i + 1`.

1. Use a queue storing `(node, index)` pairs.
2. At each level, normalize indices by subtracting the first index (prevents integer overflow in deep/skewed trees).
3. Width of a level = last index - first index + 1.
4. Track the global maximum width.

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(n) -- queue can hold up to n/2 nodes.
