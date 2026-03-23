# Minimum Height Trees

## Problem Description
Given a tree of `n` nodes labeled `0` to `n-1` and `n-1` edges, find all roots that minimize the tree's height (Minimum Height Trees). Return a list of their labels.


## Solution

```python
# LeetCode 310. Minimum Height Trees
# Time: O(n)  Space: O(n)

from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Repeatedly trim leaf nodes layer by layer.
        The last 1 or 2 remaining nodes are the MHT roots.
        """
        if n <= 2:
            return list(range(n))

        # Build adjacency list
        neighbors = [set() for _ in range(n)]
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)

        # Initialize leaves (degree 1)
        leaves = deque(i for i in range(n) if len(neighbors[i]) == 1)
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                # Each leaf has exactly one neighbor
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return list(leaves)
```

## Approach
Topological leaf trimming (like peeling an onion):

1. Build an adjacency list. Identify all leaf nodes (degree 1).
2. Repeatedly remove all current leaves and update neighbor degrees.
3. Nodes that become degree 1 after removal are the new leaves.
4. Continue until 1 or 2 nodes remain -- these are the MHT roots.

The intuition: the center of the longest path in a tree minimizes the maximum distance to any node. Trimming from the outside converges to this center.

## Complexity
- **Time:** O(n) -- each node and edge processed once.
- **Space:** O(n) -- adjacency list and queue.
