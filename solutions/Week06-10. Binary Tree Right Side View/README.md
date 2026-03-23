# Binary Tree Right Side View

**Topic:** Tree

## Problem Description
Given the root of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom.


## Solution

```python
# LeetCode 199. Binary Tree Right Side View
# Time: O(n)  Space: O(n)

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """BFS level order -- take the last node of each level."""
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
```

## Approach
Use BFS (level-order traversal). For each level, the last node in the queue is the rightmost node visible from the right side.

1. Initialize a queue with the root.
2. For each level, iterate through all nodes at that level.
3. The last node processed in each level is the right-side-visible node.
4. Add children (left then right) to the queue.

## Complexity
- **Time:** O(n) -- each node visited once.
- **Space:** O(n) -- queue can hold up to n/2 nodes at the widest level.
