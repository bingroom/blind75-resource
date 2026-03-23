# Number of Islands

**Topic:** Graph
- **LeetCode 連結:** [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- **難度:** Medium

## 題目描述

給定一個由 '1'（陸地）和 '0'（水）組成的二維網格，計算島嶼的數量。島嶼由水平或垂直相鄰的陸地連接而成，且被水包圍。

## 解題思路

1. 遍歷整個網格，遇到 '1' 時島嶼計數加一。
2. 從該位置啟動 DFS，將所有相連的 '1' 標記為 '0'（已訪問）。
3. DFS 向上下左右四個方向遞迴擴展，直到邊界或遇到水。
4. 遍歷結束後，計數值即為島嶼總數。

## 程式碼

```python
# LeetCode 200. Number of Islands
# 時間複雜度: O(m * n)  空間複雜度: O(m * n) 遞迴
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        '1' 陸地、'0' 水，求島嶼數。對每個未訪的 '1' DFS/BFS 並標記為已訪，島嶼數即 DFS 次數。
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                dfs(r + dr, c + dc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count
```

## 複雜度分析

- **時間複雜度:** O(m×n)。
- **空間複雜度:** O(m×n)（遞迴棧最壞）。
