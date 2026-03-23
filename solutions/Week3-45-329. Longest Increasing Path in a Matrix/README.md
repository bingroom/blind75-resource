# Longest Increasing Path in a Matrix

**Topic:** Graph
- **LeetCode 連結:** [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
- **難度:** Hard

## 題目描述

給定一個 m x n 的整數矩陣，找出最長嚴格遞增路徑的長度。可以往上下左右四個方向移動。

## 解題思路

1. 對每個格子進行 DFS，尋找以該格為起點的最長遞增路徑。
2. 只往值嚴格大於當前格的鄰居移動。
3. 使用記憶化（memoization）儲存每個格子的結果，避免重複計算。
4. 回傳所有格子中的最大值。

## 程式碼

```python
# LeetCode 329. Longest Increasing Path in a Matrix
# Time: O(m * n)  Space: O(m * n)

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            best = 1
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1 + dfs(ni, nj))

            memo[(i, j)] = best
            return best

        return max(dfs(i, j) for i in range(m) for j in range(n))
```

## 複雜度分析

- **時間複雜度:** O(m * n) -- each cell is visited and computed exactly once due to memoization
- **空間複雜度:** O(m * n) -- for the memo table and recursion stack
