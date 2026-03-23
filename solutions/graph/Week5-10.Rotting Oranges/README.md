# Rotting Oranges

- **LeetCode:** [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

## Problem Description

In a grid, `0` represents an empty cell, `1` a fresh orange, and `2` a rotten orange. Every minute, any fresh orange adjacent (4-directionally) to a rotten orange becomes rotten. Return the minimum number of minutes until no fresh orange remains, or `-1` if impossible.


## Solution

```python
# LeetCode 994. Rotting Oranges
# Time: O(m * n)  Space: O(m * n)
# Multi-source BFS

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        while q:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            if fresh == 0:
                return minutes

        return -1
```

## Approach

Multi-source BFS:

1. Enqueue all initially rotten oranges and count fresh oranges.
2. BFS level by level; each level represents one minute. For each rotten orange, rot its fresh neighbors and decrement the fresh count.
3. If fresh reaches 0, return the current minute count. If BFS ends with fresh > 0, return -1.

## Complexity

- **Time:** O(m * n) -- each cell processed at most once.
- **Space:** O(m * n) -- queue size in the worst case.
