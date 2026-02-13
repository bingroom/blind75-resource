# Number of Islands

- **LeetCode:** [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

**Example 1:**

```

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

```

**Example 2:**

```

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 300`

	- `grid[i][j]` is `'0'` or `'1'`.

## Solution

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

## 思路

- **DFS/BFS：** 遍歷每個格子，遇到 '1' 就從該格做 DFS 把整座島標記成已訪（例如改為 '0'），島嶼數即發起 DFS 的次數。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(m×n)（遞迴棧最壞）。

## 相關閱讀

- **演算法:** DFS、BFS、Connected Components
