# 01 Matrix

**Topic:** Graph

- **LeetCode:** [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)

## Problem Description

Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell. The distance between two adjacent cells is `1`.


## Solution

```python
# LeetCode 542. 01 Matrix
# Time: O(m * n)  Space: O(m * n)

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[0] * n for _ in range(m)]
        q = deque()

        # Start BFS from all 0-cells simultaneously
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    dist[r][c] = float("inf")

        while q:
            r, c = q.popleft()
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return dist
```

## Approach

Multi-source BFS starting from all `0` cells at once:

1. Initialize a distance matrix. Set distance to `0` for all `0`-cells and `inf` for all `1`-cells.
2. Enqueue all `0`-cells.
3. BFS outward: for each dequeued cell, check all four neighbors. If the neighbor's recorded distance is greater than current + 1, update it and enqueue.

This guarantees each cell is visited with its shortest distance first.

## Complexity

- **Time:** O(m * n) -- each cell enqueued at most once.
- **Space:** O(m * n) -- distance matrix and queue.
