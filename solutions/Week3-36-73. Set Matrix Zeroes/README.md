# Set Matrix Zeroes

**Topic:** Matrix
- **LeetCode 連結:** [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
- **難度:** Medium

## 題目描述

給定一個 m x n 矩陣，若某元素為 0，則將其所在行和列全部設為 0。要求原地操作，使用 O(1) 額外空間。

## 解題思路

1. 先記錄第一行和第一列是否原本含有 0。
2. 用第一行和第一列作為標記：遍歷矩陣，若 matrix[i][j] 為 0，則標記 matrix[i][0] 和 matrix[0][j] 為 0。
3. 根據標記將對應位置設為 0（跳過第一行列）。
4. 最後根據步驟 1 的記錄處理第一行和第一列。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(m×n)。
- **空間複雜度:** O(1)。
