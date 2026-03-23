# Set Matrix Zeroes

**Topic:** Array

- **LeetCode:** [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[0].length`

	- `1 <= m, n <= 200`

	- `-2^31 <= matrix[i][j] <= 2^31 - 1`

 

**Follow up:**

	- A straightforward solution using `O(mn)` space is probably a bad idea.

	- A simple improvement uses `O(m + n)` space, but still not the best solution.

	- Could you devise a constant space solution?

## Solution

```python
# LeetCode 73. Set Matrix Zeroes
# 時間複雜度: O(m * n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        若某格為 0，將該行該列全設為 0，要求 O(1) 空間。用第一行、第一列當標記，先記下第一行/列是否要變 0。
        """
        m, n = len(matrix), len(matrix[0])
        row0 = any(matrix[0][c] == 0 for c in range(n))
        col0 = any(matrix[r][0] == 0 for r in range(m))
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if row0:
            for c in range(n):
                matrix[0][c] = 0
        if col0:
            for r in range(m):
                matrix[r][0] = 0

```

## 思路

- **用第一行、第一列當標記：** 先記錄第一行/第一列是否原本就有 0。然後用 matrix[r][0] 與 matrix[0][c] 標記第 r 行、第 c 列是否要變 0，最後根據標記填 0，再根據一開始的記錄處理第一行/列。

## 時間 / 空間複雜度

- **時間:** O(m×n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** In-place 標記
