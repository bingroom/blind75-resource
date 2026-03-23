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
