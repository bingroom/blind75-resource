# Minimum Knight Moves

**Topic:** Graph
- **LeetCode 連結:** [1197. Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/)
- **難度:** Medium

## 題目描述

在無限大的棋盤上，騎士從 (0,0) 出發，求到達座標 (x,y) 的最少移動步數。

## 解題思路

1. 利用對稱性，將目標座標轉為第一象限。
2. 使用 BFS 從 (0,0) 開始，嘗試騎士的八個方向移動。
3. 用集合記錄已訪問的座標，避免重複。
4. 當到達目標座標時回傳步數。

## 程式碼

```python
# LeetCode 1197. Minimum Knight Moves
# Time: O(|x| * |y|)  Space: O(|x| * |y|)
# BFS in first quadrant using symmetry

from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # By symmetry we only need to consider the first quadrant
        x, y = abs(x), abs(y)

        q = deque([(0, 0, 0)])  # (row, col, steps)
        visited = {(0, 0)}
        moves = [(1, 2), (2, 1), (2, -1), (1, -2),
                 (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        while q:
            cx, cy, steps = q.popleft()
            if cx == x and cy == y:
                return steps
            for dx, dy in moves:
                nx, ny = cx + dx, cy + dy
                # Allow small negative coords (-1) to handle edge cases near origin
                if (nx, ny) not in visited and nx >= -1 and ny >= -1:
                    visited.add((nx, ny))
                    q.append((nx, ny, steps + 1))

        return -1
```

## 複雜度分析

- **時間複雜度:** O(|x| * |y|) -- the BFS explores a bounded region around the target.
- **空間複雜度:** O(|x| * |y|) -- visited set.
