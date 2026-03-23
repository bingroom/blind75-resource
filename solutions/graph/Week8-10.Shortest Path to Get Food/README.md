# Shortest Path to Get Food

- **LeetCode:** [1730. Shortest Path to Get Food](https://leetcode.com/problems/shortest-path-to-get-food/)

## Problem Description

Given an `m x n` grid where `'*'` is your starting position, `'#'` is food, `'O'` is free space, and `'X'` is an obstacle, return the length of the shortest path to reach any food cell. Return `-1` if no food is reachable.


## Solution

```python
# LeetCode 1730. Shortest Path to Get Food
# Time: O(m * n)  Space: O(m * n)
# BFS from starting position

from typing import List
from collections import deque


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        # Find starting position
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '*':
                    q.append((r, c, 0))
                    grid[r][c] = 'V'  # mark visited
                    break
            if q:
                break

        while q:
            r, c, dist = q.popleft()
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 'X' and grid[nr][nc] != 'V':
                    if grid[nr][nc] == '#':
                        return dist + 1
                    grid[nr][nc] = 'V'
                    q.append((nr, nc, dist + 1))

        return -1
```

## Approach

Standard BFS from the starting position:

1. Locate the `'*'` cell and enqueue it with distance 0.
2. BFS outward, skipping obstacles (`'X'`) and visited cells.
3. Return immediately when a food cell (`'#'`) is reached.
4. If the queue empties without finding food, return -1.

## Complexity

- **Time:** O(m * n) -- each cell visited at most once.
- **Space:** O(m * n) -- queue and visited markers.
