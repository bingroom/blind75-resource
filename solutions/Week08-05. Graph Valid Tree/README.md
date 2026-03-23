# Graph Valid Tree

**Topic:** Graph

- **LeetCode:** [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

## Problem Description

Given `n` nodes labeled `0` to `n - 1` and a list of undirected edges, determine if these edges form a valid tree. A valid tree is a connected acyclic graph.


## Solution

```python
# LeetCode 261. Graph Valid Tree
# Time: O(n * alpha(n))  Space: O(n)
# Union-Find approach

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree has exactly n-1 edges and no cycles
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # cycle detected
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        for a, b in edges:
            if not union(a, b):
                return False

        return True
```

## Approach

Union-Find:

1. A tree with `n` nodes must have exactly `n - 1` edges. If not, return False immediately.
2. Process each edge with Union-Find. If both endpoints already share the same root, a cycle exists -- return False.
3. If all edges are processed without a cycle and the edge count is `n - 1`, the graph is a valid tree.

## Complexity

- **Time:** O(n * alpha(n)) where alpha is the inverse Ackermann function.
- **Space:** O(n) -- parent and rank arrays.
