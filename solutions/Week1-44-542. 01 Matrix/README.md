# 01 Matrix

**Topic:** Graph
- **LeetCode 連結:** [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
- **難度:** Medium

## 題目描述

給定一個由 0 和 1 組成的二維矩陣，對每個格子求出其到最近的 0 的距離。相鄰格子指上下左右四個方向，距離以曼哈頓距離計算。

## 解題思路

1. 建立距離矩陣，將所有值為 0 的格子距離設為 0 並加入佇列，其餘設為無限大。
2. 從所有 0 格子同時開始 BFS（多源 BFS）。
3. 每次從佇列取出一個格子，檢查四個方向的鄰居：若經由當前格子能縮短距離，則更新並加入佇列。
4. BFS 結束後，距離矩陣即為答案。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(m * n) -- each cell enqueued at most once.
- **空間複雜度:** O(m * n) -- distance matrix and queue.
