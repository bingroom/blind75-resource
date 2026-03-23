# Rotting Oranges

**Topic:** Graph
- **LeetCode 連結:** [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- **難度:** Medium

## 題目描述

給定一個網格，其中 0 代表空格、1 代表新鮮橘子、2 代表腐爛橘子。每分鐘腐爛橘子會感染上下左右相鄰的新鮮橘子。回傳使所有橘子腐爛所需的最少分鐘數，若無法全部腐爛則回傳 -1。

## 解題思路

1. 遍歷網格，將所有腐爛橘子加入佇列，同時計算新鮮橘子數量。
2. 使用多源 BFS，每一輪處理佇列中所有腐爛橘子，將相鄰的新鮮橘子變為腐爛並加入佇列。
3. 每輪結束後分鐘數加一，直到沒有新鮮橘子或佇列為空。
4. 若仍有新鮮橘子剩餘，回傳 -1；否則回傳分鐘數。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(m * n) -- each cell processed at most once.
- **空間複雜度:** O(m * n) -- queue size in the worst case.
