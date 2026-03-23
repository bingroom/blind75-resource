# Maximal Square

- **LeetCode:** [221. Maximal Square](https://leetcode.com/problems/maximal-square/)

## Problem Description

Given an `m x n` binary matrix filled with `'0'`s and `'1'`s, find the largest square containing only `'1'`s and return its area.


## Solution

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

## Approach

Use a 2D DP table where `dp[i][j]` represents the side length of the largest square whose bottom-right corner is at `(i, j)`.

1. If `matrix[i][j] == '0'`, then `dp[i][j] = 0`.
2. If `matrix[i][j] == '1'` and it is on the first row or column, `dp[i][j] = 1`.
3. Otherwise, `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`. The square is limited by the smallest neighbor because all three must support the extension.
4. Track the maximum side length and return `max_side^2`.

## Complexity

- **Time:** O(m * n)
- **Space:** O(m * n)
