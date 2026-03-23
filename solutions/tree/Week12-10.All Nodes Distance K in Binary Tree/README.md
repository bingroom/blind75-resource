# All Nodes Distance K in Binary Tree

## Problem Description
Given the root of a binary tree, a target node, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.


## Solution

```python
# LeetCode 863. All Nodes Distance K in Binary Tree
# Time: O(n)  Space: O(n)

from collections import deque
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(
        self, root: TreeNode, target: TreeNode, k: int
    ) -> List[int]:
        """
        Convert tree to undirected graph via parent pointers,
        then BFS from target to find all nodes at distance k.
        """
        # Step 1: Record parent of every node using DFS
        parent = {}

        def dfs(node, par=None):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)

        # Step 2: BFS from target node
        visited = {target}
        queue = deque([target])
        dist = 0

        while queue:
            if dist == k:
                return [node.val for node in queue]
            dist += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return []
```

## Approach
Convert the tree into an undirected graph, then BFS from the target:

1. **Build parent map:** DFS through the tree to record each node's parent, enabling upward traversal.
2. **BFS from target:** Treat the tree as an undirected graph (each node connects to left child, right child, and parent). BFS outward from target, tracking visited nodes.
3. When BFS reaches distance `k`, return all nodes in the current queue.

## Complexity
- **Time:** O(n) -- DFS to build parent map + BFS visits each node at most once.
- **Space:** O(n) -- parent map, visited set, and BFS queue.
