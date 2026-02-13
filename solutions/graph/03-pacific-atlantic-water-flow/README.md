# Pacific Atlantic Water Flow

- **LeetCode:** [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return *a **2D list** of grid coordinates *`result`* where *`result[i] = [r_i, c_i]`* denotes that rain water can flow from cell *`(r_i, c_i)`* to **both** the Pacific and Atlantic oceans*.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)

```

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

```

**Example 2:**

```

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

```

 

**Constraints:**

	- `m == heights.length`

	- `n == heights[r].length`

	- `1 <= m, n <= 200`

	- `0 <= heights[r][c] <= 10^5`

## Solution

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

## 思路

- **反向思考：** 從太平洋邊（第一行、第一列）與大西洋邊（最後一行、最後一列）分別做 DFS/BFS，標記「能流到該洋」的格子（從邊緣往高處走）。兩邊都能到的格子即為答案。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(m×n)。

## 相關閱讀

- **演算法:** DFS/BFS、多源點遍歷
