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
