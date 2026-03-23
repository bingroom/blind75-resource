# Number of Connected Components in an Undirected Graph

- **LeetCode:** [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

## Problem Description

Given `n` nodes labeled `0` to `n - 1` and a list of undirected edges, return the number of connected components in the graph.


## Solution

```python
# LeetCode 323. Number of Connected Components in an Undirected Graph
# Time: O(n + E * alpha(n))  Space: O(n)
# Union-Find approach

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        components = n
        for a, b in edges:
            if union(a, b):
                components -= 1

        return components
```

## Approach

Union-Find with path compression and union by rank:

1. Initialize each node as its own component (count = n).
2. For each edge, union the two endpoints. If they were in different components, decrement the component count.
3. Return the final count.

## Complexity

- **Time:** O(n + E * alpha(n)) where E is the number of edges and alpha is the inverse Ackermann function.
- **Space:** O(n) -- parent and rank arrays.
