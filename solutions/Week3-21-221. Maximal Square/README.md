# Maximal Square

**Topic:** Dynamic Programming
- **LeetCode 連結:** [221. Maximal Square](https://leetcode.com/problems/maximal-square/)
- **難度:** Medium

## 題目描述

給定一個由 '0' 和 '1' 組成的二維矩陣，找出只包含 '1' 的最大正方形的面積。

## 解題思路

1. 建立 dp 陣列，dp[i][j] 表示以 (i,j) 為右下角的最大全 1 正方形邊長。
2. 若 matrix[i][j] 為 '1'，則 dp[i][j] = min(上、左、左上) + 1。
3. 追蹤最大邊長，最終回傳面積（邊長平方）。

## 程式碼

```python
# LeetCode 221. Maximal Square
# Time: O(m * n)  Space: O(m * n), can be optimized to O(n)

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        # dp[i][j] = side length of the largest square with bottom-right corner at (i, j)
        dp = [[0] * n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # Limited by the smallest of the three neighbors
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
```

## 複雜度分析

- **時間複雜度:** O(m * n)
- **空間複雜度:** O(m * n)
