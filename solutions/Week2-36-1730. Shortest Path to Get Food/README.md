# Shortest Path to Get Food

**Topic:** Graph
- **LeetCode 連結:** [1730. Shortest Path to Get Food](https://leetcode.com/problems/shortest-path-to-get-food/)
- **難度:** Medium

## 題目描述

給定一個網格，'*' 為起始位置，'#' 為食物，'O' 為可通行空地，'X' 為障礙物。求從起點到最近食物的最短路徑長度，若無法到達則回傳 -1。

## 解題思路

1. 在網格中找到起始位置 '*'。
2. 從起點開始進行 BFS，將起點加入佇列並標記為已訪問。
3. 每次從佇列取出一個格子，向上下左右四個方向擴展。
4. 若鄰居為食物 '#'，回傳當前距離 + 1。
5. 若為可通行格子，標記已訪問後加入佇列繼續搜尋。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(m * n) -- each cell visited at most once.
- **空間複雜度:** O(m * n) -- queue and visited markers.
