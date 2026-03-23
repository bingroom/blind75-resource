# Pacific Atlantic Water Flow

**Topic:** Graph
- **LeetCode 連結:** [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- **難度:** Medium

## 題目描述

給定一個 m x n 的矩陣代表地形高度，左邊和上邊靠太平洋，右邊和下邊靠大西洋。水只能從高處流向等高或更低處。求哪些格子的水可以同時流到兩個大洋。

## 解題思路

1. 反向思考：從太平洋的邊界向內 DFS，標記所有能流到太平洋的格子。
2. 同樣從大西洋的邊界向內 DFS，標記所有能流到大西洋的格子。
3. DFS 時只走高度大於等於當前格子的鄰居（反向流動）。
4. 取兩個集合的交集，即為能同時流到兩個大洋的格子。

## 程式碼

```python
# LeetCode 417. Pacific Atlantic Water Flow
# 時間複雜度: O(m * n)  空間複雜度: O(m * n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        左與上為太平洋、右與下為大西洋，水從高往低流。求能同時流到兩洋的格子。從兩洋邊緣分別 DFS/BFS 標記可到達的格子，取交集。
        """
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r: int, c: int, seen: set) -> None:
            seen.add((r, c))
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, seen)

        for c in range(n):
            dfs(0, c, pac)
            dfs(m - 1, c, atl)
        for r in range(m):
            dfs(r, 0, pac)
            dfs(r, n - 1, atl)
        return [[r, c] for r in range(m) for c in range(n) if (r, c) in pac and (r, c) in atl]
```

## 複雜度分析

- **時間複雜度:** O(m×n)。
- **空間複雜度:** O(m×n)。
